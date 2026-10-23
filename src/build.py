#!/usr/bin/env python3
"""
BricoHams - (tr)uSDX modular rail system (v3)
Genera las piezas imprimibles: soporte del (tr)uSDX y funda del ATU-10, unidos por el riel de
cola de milano DL2MAN (el mismo de bottom_cover_battery / battery-slider).

    python src/build.py                      # sin indicativo
    python src/build.py --call EA4XXX        # con indicativo en la marca de agua

Cadena de módulos (de delante a atrás): soporte -> [funda ATU-10] -> batería.
Cada pieza lleva una ranura hembra DL2MAN vertical en su cara trasera; la funda del ATU-10 lleva
además la lengüeta macho en su cara delantera. Todo se encaja desde arriba y baja hasta el tope.

Medidas en mm. Ejes: X ancho (mirando el equipo de frente, izquierda -X), Y fondo (frente y=0,
trasera +Y), Z alto (mesa z=0).
"""
import argparse, math, pathlib, numpy as np, trimesh, manifold3d as mf
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties

ROOT = pathlib.Path(__file__).resolve().parents[1]
VENDOR, OUT = ROOT / "vendor", ROOT / "stl"

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

# ------------------------------------------------------------------------------------------------
U = np.array([math.cos(math.radians(TILT)), math.sin(math.radians(TILT))])    # (y,z) por la pendiente
N = np.array([-math.sin(math.radians(TILT)), math.cos(math.radians(TILT))])   # (y,z) normal, hacia la pantalla
P0 = np.array([LIP_T * U[0] - LIP_H * N[0], R_Z0])   # canto inferior-delantero: el labio queda en y=0

# funda del ATU-10 (coordenadas absolutas, detrás del soporte)
ATU_XI = ATU_L / 2 + ATU_CLR                     # media longitud interior
ATU_Y0 = Y_BACK                                  # cara delantera de la funda
ATU_YC0 = ATU_Y0 + ATU_WALL                      # hueco interior
ATU_YC1 = ATU_YC0 + ATU_T + 2 * ATU_CLR
ATU_Y1 = ATU_YC1 + PLATE_T                       # cara trasera (ranura)
ATU_ZC0, ATU_ZC1 = ATU_WALL, ATU_WALL + ATU_H + 2 * ATU_CLR
ATU_Z1 = ATU_ZC1 + ATU_WALL

def radio_pt(u, v):
    """Punto (y,z) de la radio: u por la pendiente desde el canto inferior, v hacia la cara superior."""
    return P0 + u * U + v * N

def to_mf(tm):
    return mf.Manifold(mf.Mesh(vert_properties=np.asarray(tm.vertices, np.float32),
                               tri_verts=np.asarray(tm.faces, np.uint32)))

def to_tm(m):
    g = m.to_mesh(); return trimesh.Trimesh(g.vert_properties[:, :3], g.tri_verts)

def box(x0, x1, y0, y1, z0, z1):
    return mf.Manifold.cube([x1-x0, y1-y0, z1-z0]).translate([x0, y0, z0])

def _xs(pts):
    """CrossSection con el sentido de giro correcto (antihorario)."""
    a = sum(x0*y1 - x1*y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))
    return mf.CrossSection([pts if a > 0 else pts[::-1]])

def _along_x(cs, x0, x1):
    """Extruye un perfil del plano (y,z) a lo largo de X entre x0 y x1."""
    return mf.Manifold.extrude(cs, x1 - x0).transform([[0, 0, 1, x0], [1, 0, 0, 0], [0, 1, 0, 0]])

def text2d(txt, h):
    """Texto -> CrossSection centrado en el origen (altura de mayúsculas ~h)."""
    tp = TextPath((0, 0), txt, size=h*1.38, prop=FontProperties(family="DejaVu Sans", weight="bold"))
    cs = mf.CrossSection([p for p in tp.to_polygons() if len(p) > 2], mf.FillRule.EvenOdd)
    b = cs.bounds()
    return cs.translate([-(b[0]+b[2])/2, -(b[1]+b[3])/2])

def engrave_text(txt, h, depth):
    return mf.Manifold.extrude(text2d(txt, h), depth)

# ---------------- Riel ---------------------------------------------------------------------------
def rail_slot(yf, z_top):
    """Cortador de la ranura hembra vertical, centrada en x=0, con la boca en la cara y=yf (material
       en y<yf). Fondo ciego (tope) en z=RAIL_Z0, abierta por arriba, cavidades de los detents."""
    def prof(grow):
        n, b, d = DT_NECK/2 + DT_EXTRA + grow, DT_BASE/2 + DT_EXTRA + grow, DT_DEPTH + DT_EXTRA
        o = n - (b - n) / d    # flancos prolongados 1 mm fuera de la cara (sin vértices sobre ella)
        return _xs([(-o, yf + 1), (-b, yf - d), (b, yf - d), (o, yf + 1)])
    cut = mf.Manifold.extrude(prof(0), z_top + 1 - RAIL_Z0).translate([0, 0, RAIL_Z0])
    flare = mf.Manifold.hull(mf.Manifold.batch_boolean([
        mf.Manifold.extrude(prof(0), 0.01).translate([0, 0, z_top - 2]),
        mf.Manifold.extrude(prof(CHAMFER), 0.01).translate([0, 0, z_top + 0.01])], mf.OpType.Add))
    r = DIMPLE_D / 2
    dimples = [mf.Manifold.sphere(r, 32).translate([0, yf - DT_DEPTH - DIMPLE_DEPTH + r, RAIL_Z0 + z])
               for z in DIMPLE_AT]
    return mf.Manifold.batch_boolean([cut, flare] + dimples, mf.OpType.Add)

def rail_tongue(yf):
    """Lengüeta macho DL2MAN que sale de la cara y=yf hacia -Y, en z RAIL_Z0..RAIL_Z0+SLIDE_LEN."""
    n, w, t, d = TG_NECK / 2, TG_WIDE / 2, TG_TIP / 2, TG_DEPTH
    half = [(n, yf + 0.2), (n, yf - 0.5), (w, yf - 2.0), (t, yf - d)]   # empieza 0.2 mm dentro de la pared
    tg = mf.Manifold.extrude(_xs([(-x, y) for x, y in half] + [(x, y) for x, y in half[::-1]]),
                             SLIDE_LEN).translate([0, 0, RAIL_Z0])
    r = BUMP_D / 2
    bumps = [mf.Manifold.sphere(r, 32).translate([0, yf - TG_DEPTH - BUMP_H + r, RAIL_Z0 + z])
             for z in DIMPLE_AT]
    return mf.Manifold.batch_boolean([tg] + bumps, mf.OpType.Add)

# ---------------- Soporte ------------------------------------------------------------------------
def stand_profile():
    """Perfil (y,z) del soporte: cuña bajo la radio + labio delantero + cara trasera vertical."""
    la = radio_pt(0, LIP_H); lb = la - LIP_T * U
    z_back = P0[1] + (Y_BACK - P0[0]) * math.tan(math.radians(TILT))
    return _xs([(lb[0], 0), (Y_BACK, 0), (Y_BACK, z_back), tuple(P0), tuple(la), tuple(lb)]), z_back

def stand(call=None):
    prof, z_back = stand_profile()
    body = _along_x(prof, -ST_W/2, ST_W/2)
    inner = prof.offset(-WALL, mf.JoinType.Miter) ^ _xs([(-1, -1), (Y_BACK - PLATE_T, -1), (Y_BACK - PLATE_T, 200), (-1, 200)])
    inner = inner + _xs([(WALL, -1), (Y_BACK - PLATE_T, -1), (Y_BACK - PLATE_T, WALL + 0.5), (WALL, WALL + 0.5)])
    body -= _along_x(inner, -ST_W/2 + WALL, ST_W/2 - WALL)
    body -= rail_slot(Y_BACK, z_back)
    # marca de agua en los dos laterales (zona baja, bajo la radio)
    for x, t, sgn in ((-ST_W/2, WM_TEXT, -1), (ST_W/2, call or "(tr)uSDX", 1)):
        txt = engrave_text(t, 5.0, WM_DEPTH + 0.02)
        txt = txt.transform([[0, 0, sgn, 0], [sgn, 0, 0, 0], [0, 1, 0, 0]])   # plano YZ, legible desde fuera
        body -= txt.translate([x - sgn * WM_DEPTH, Y_BACK / 2 + 2, 7.5])
    return body

# ---------------- Funda del ATU-10 ---------------------------------------------------------------
def atu_sleeve(call=None):
    """Funda abierta por -X (pantalla, botón y USB-C del ATU-10) con marco-tope en +X (BNC)."""
    x1 = ATU_XI + ATU_END_T
    body = box(-ATU_XI, x1, ATU_Y0, ATU_Y1, 0, ATU_Z1)
    body -= box(-ATU_XI - 1, ATU_XI, ATU_YC0, ATU_YC1, ATU_ZC0, ATU_ZC1)
    a, b, c, d, k = ATU_YC0, ATU_YC1, ATU_ZC0, ATU_ZC1, ATU_TAB
    window = _xs([(a + k, c), (b - k, c), (b, c + k), (b, d - k), (b - k, d), (a + k, d), (a, d - k), (a, c + k)])
    body -= _along_x(window, ATU_XI - 0.1, x1 + 1)
    body += rail_tongue(ATU_Y0)
    body -= rail_slot(ATU_Y1, ATU_Z1)
    txt = engrave_text(WM_TEXT + (f"  {call}" if call else "") + "  ATU-10", 4.5, WM_DEPTH + 0.02)
    body -= txt.translate([0, (ATU_Y0 + ATU_Y1) / 2, ATU_Z1 - WM_DEPTH])
    return body

# ---------------- Posiciones de montaje (para verificación y renders) ----------------------------
def slider_pose(y_rail):
    """Matriz 4x4 que coloca battery-slider.stl (DL2MAN) en una ranura trasera con la boca en y_rail.
       slider: x (0..90, largo) -> X, y (lengüeta en y<0) -> +Y, z (0..60, deslizamiento) -> Z."""
    return np.array([[1, 0, 0, -R_L/2], [0, 1, 0, y_rail], [0, 0, 1, RAIL_Z0], [0, 0, 0, 1]], float)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--call", default=None, help="indicativo, p.ej. EA4XXX")
    a = ap.parse_args(); call = a.call.upper() if a.call else None
    OUT.mkdir(exist_ok=True)
    for f in OUT.glob("*.stl"): f.unlink()
    to_tm(stand(call)).export(OUT / "trusdx-stand_rail_BricoHams.stl")
    to_tm(atu_sleeve(call)).export(OUT / "atu10-sleeve_rail_BricoHams.stl")
    for f in sorted(OUT.glob("*.stl")):
        t = trimesh.load(f)
        print(f"{f.name:40s} {t.extents.round(1)}  min={t.bounds[0].round(1)}  estanca={t.is_watertight}")

if __name__ == "__main__":
    main()
