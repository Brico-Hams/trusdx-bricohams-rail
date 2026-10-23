"""
BricoHams - (tr)uSDX modular rail system (v3): medidas compartidas.
Sin dependencias (solo math) para que lo usen tanto el script de Fusion 360 (fusion/) como la
verificación en Python (src/verify.py).

Medidas en mm. Ejes: X ancho (mirando el equipo de frente, izquierda -X), Y fondo (frente y=0,
trasera +Y), Z alto (mesa z=0).
"""
import math

# ---------------- Riel DL2MAN (medido de bottom_cover_battery.stl y battery-slider.stl) ------------
DT_NECK, DT_BASE, DT_DEPTH = 27.2, 29.2, 3.0   # ranura hembra: boca, fondo, profundidad
DT_EXTRA = 0.0                                 # holgura extra por lado (+0.1/+0.2 si aprieta)
# lengüeta macho (secciones del slider): cuello 25.0 hasta 0.5 mm, 28.0 a 2 mm, punta 27.7 a 3 mm
TG_NECK, TG_WIDE, TG_TIP, TG_DEPTH = 25.0, 28.0, 27.7, 3.0
BUMP_D, BUMP_H = 2.0, 0.5                      # resaltes de la lengüeta
DIMPLE_AT = (10.0, 50.0)                       # resaltes/cavidades desde el extremo del slider
DIMPLE_D, DIMPLE_DEPTH = 2.6, 0.6
SLIDE_LEN = 60.0                               # largo de la lengüeta (sentido de deslizamiento)
RAIL_Z0 = 3.0      # fondo ciego de cada ranura = tope; las lengüetas quedan en z 3..63
PLATE_T = 5.0      # grosor de la placa que lleva la ranura (igual que bottom_cover_battery)
CHAMFER = 0.8      # ensanche de la embocadura superior de la ranura (últimos 2 mm)

# ---------------- (tr)uSDX en la carcasa DL2MAN ---------------------------------------------------
R_L, R_W, R_T = 90.0, 60.0, 30.0   # largo (X) x ancho (sobre la pendiente) x grueso
TILT = 50.0                        # inclinación de la radio respecto a la mesa (grados)
LIP_T, LIP_H = 4.0, 8.0            # labio delantero que sujeta la pared inferior de la radio
R_Z0 = 16.0                        # altura del canto inferior-delantero de la radio

# ---------------- Soporte ------------------------------------------------------------------------
ST_W = 90.0        # ancho = largo de la radio: los extremos con conectores quedan libres
Y_BACK = 56.0      # cara trasera del soporte (deja 8 mm libres detrás de la pared superior)
WALL = 3.0         # pared del soporte hueco (se imprime con la boca abajo, sin soportes)

# ---------------- ATU-10 (N7DDC, caja de aluminio 100 x 71 x 25) ----------------------------------
ATU_L, ATU_H, ATU_T = 100.0, 71.0, 25.0
ATU_CLR = 0.4      # holgura por lado de la funda
ATU_WALL = 2.5     # paredes de la funda
ATU_END_T = 2.0    # marco del extremo de los BNC (tope)
ATU_TAB = 6.0      # catetos de las pestañas de esquina del marco

# ---------------- Marca de agua ------------------------------------------------------------------
WM_TEXT, WM_DEPTH = "BRICOHAMS", 0.6
CALL = None        # indicativo en la marca de agua, p.ej. "EA4XXX"

# ---------------- Derivadas ----------------------------------------------------------------------
_t = math.radians(TILT)
U = (math.cos(_t), math.sin(_t))     # (y,z) por la pendiente
N = (-math.sin(_t), math.cos(_t))    # (y,z) normal, hacia la pantalla
P0 = (LIP_T * U[0] - LIP_H * N[0], R_Z0)   # canto inferior-delantero de la radio: el labio queda en y=0
Z_BACK = P0[1] + (Y_BACK - P0[0]) * math.tan(_t)   # altura de la cara trasera del soporte

ATU_XI = ATU_L / 2 + ATU_CLR                     # media longitud interior de la funda
ATU_Y0 = Y_BACK                                  # cara delantera de la funda
ATU_YC0 = ATU_Y0 + ATU_WALL                      # hueco interior
ATU_YC1 = ATU_YC0 + ATU_T + 2 * ATU_CLR
ATU_Y1 = ATU_YC1 + PLATE_T                       # cara trasera (ranura)
ATU_ZC0, ATU_ZC1 = ATU_WALL, ATU_WALL + ATU_H + 2 * ATU_CLR
ATU_Z1 = ATU_ZC1 + ATU_WALL

def radio_pt(u, v):
    """Punto (y,z) de la radio: u por la pendiente desde el canto inferior, v hacia la cara superior."""
    return (P0[0] + u * U[0] + v * N[0], P0[1] + u * U[1] + v * N[1])

def stand_profile():
    """Perfil (y,z) del soporte: cuña bajo la radio + labio delantero + cara trasera vertical."""
    la = radio_pt(0, LIP_H)
    lb = (la[0] - LIP_T * U[0], la[1] - LIP_T * U[1])
    return [(lb[0], 0.0), (Y_BACK, 0.0), (Y_BACK, Z_BACK), P0, la, lb]

def slot_profile(yf, grow=0.0):
    """Trapecio (x,y) de la ranura hembra con la boca en y=yf; flancos prolongados 1 mm fuera."""
    n, b, d = DT_NECK/2 + DT_EXTRA + grow, DT_BASE/2 + DT_EXTRA + grow, DT_DEPTH + DT_EXTRA
    o = n - (b - n) / d
    return [(-o, yf + 1), (-b, yf - d), (b, yf - d), (o, yf + 1)]

def tongue_profile(yf):
    """Polígono (x,y) de la lengüeta macho que sale de la cara y=yf hacia -Y (0.2 mm dentro de la pared)."""
    n, w, t, d = TG_NECK / 2, TG_WIDE / 2, TG_TIP / 2, TG_DEPTH
    half = [(n, yf + 0.2), (n, yf - 0.5), (w, yf - 2.0), (t, yf - d)]
    return [(-x, y) for x, y in half] + [(x, y) for x, y in half[::-1]]

def atu_window():
    """Octógono (y,z) del marco de los BNC: el hueco de la funda menos las pestañas de esquina."""
    a, b, c, d, k = ATU_YC0, ATU_YC1, ATU_ZC0, ATU_ZC1, ATU_TAB
    return [(a + k, c), (b - k, c), (b, c + k), (b, d - k), (b - k, d), (a + k, d), (a, d - k), (a, c + k)]
