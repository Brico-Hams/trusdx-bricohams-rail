#!/usr/bin/env python3
"""
Comprobación de choques y accesos para cada combinación de módulos.

    (modela las piezas en Fusion 360 con fusion/trusdx_rail_fusion.py)
    python src/verify.py

Usa las piezas generadas en stl/, vendor/battery-slider.stl (DL2MAN) y modelos simplificados
(cajas) de la radio y del ATU-10. Para cada combinación comprueba:
  - que ninguna pieza se mete en otra (volumen de intersección),
  - que las zonas de acceso de conectores y mandos (cajas delante de cada cara) están libres,
  - el encaje de cada riel: asentado, retención lateral, tope, clic y camino de inserción,
  - la estabilidad: centro de masas dentro de la huella de apoyo (masas estimadas).
Sale con código 1 si algo falla.
"""
import sys, pathlib, numpy as np, trimesh
from scipy.spatial import ConvexHull
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import geom as b

S = b.OUT
ENV = 40.0        # largo de las zonas de acceso de los conectores (clavija + curva del cable)
ENV_TOP = 30.0    # altura libre sobre la cara superior de la radio (mando de 20 mm + dedos)
ENV_BACK = 8.0    # hueco libre detrás de la pared superior de la radio (abertura de 6 x 5)
LIFT = 70.0       # recorrido de extracción hacia arriba
# masas estimadas (kg): radio en carcasa, 3x18650 + portapilas + slider, ATU-10 en su caja
MASS = {"radio": 0.20, "batería": 0.20, "ATU-10": 0.12}
PETG = 1.27e-6 * 0.35     # kg/mm3 con ~35 % de material efectivo (paredes + relleno)

def tilted(u0, u1, v0, v1, x0, x1):
    """Caja en el sistema de la radio (u por la pendiente, v normal) extruida en X."""
    pts = [tuple(b.radio_pt(u, v)) for u, v in ((u0, v0), (u1, v0), (u1, v1), (u0, v1))]
    return b._along_x(b._xs(pts), x0, x1)

def load(name):
    return b.to_mf(trimesh.load(S / name))

def parts():
    p = {"soporte": load("trusdx-stand_rail_BricoHams.stl"),
         "funda ATU-10": load("atu10-sleeve_rail_BricoHams.stl"),
         "radio": tilted(0, b.R_W, 0, b.R_T, -b.R_L/2, b.R_L/2)}
    ax1 = b.ATU_XI; ax0 = ax1 - b.ATU_L
    ay0, az0 = b.ATU_YC0 + b.ATU_CLR, b.ATU_ZC0 + b.ATU_CLR
    p["ATU-10"] = b.box(ax0, ax1, ay0, ay0 + b.ATU_T, az0, az0 + b.ATU_H)
    sl = b.VENDOR / "battery-slider.stl"
    p["_slider"] = trimesh.load(sl) if sl.exists() else None
    i = 3.5   # las zonas de los paneles del ATU-10 dejan fuera las pestañas de esquina del marco
    env = {
        "radio: pantalla, mando y pulsadores": ("radio", tilted(0, b.R_W, b.R_T, b.R_T + ENV_TOP, -b.R_L/2, b.R_L/2)),
        "radio: DC + USB (extremo izq.)": ("radio", tilted(0, b.R_W, 0, b.R_T, -b.R_L/2 - ENV, -b.R_L/2)),
        "radio: antena + MIC/KEY + auric. (extremo der.)": ("radio", tilted(0, b.R_W, 0, b.R_T, b.R_L/2, b.R_L/2 + ENV)),
        "radio: abertura pared superior": ("radio", tilted(b.R_W, b.R_W + ENV_BACK, 0, b.R_T, -b.R_L/2, b.R_L/2)),
        "ATU-10: OLED, botón y USB-C (-X)": ("ATU-10", b.box(ax0 - ENV, ax0, ay0 + i, ay0 + b.ATU_T - i, az0 + i, az0 + b.ATU_H - i)),
        "ATU-10: BNC TX/ANT (+X)": ("ATU-10", b.box(ax1, ax1 + ENV, ay0 + i, ay0 + b.ATU_T - i, az0 + i, az0 + b.ATU_H - i)),
    }
    return p, env

def slider_at(p, y_rail):
    t = p["_slider"]
    if t is None:   # sin el STL original: lengüeta DL2MAN + caja del cuerpo
        return b.rail_tongue(y_rail) + b.box(-45, 45, y_rail, y_rail + 26, b.RAIL_Z0, b.RAIL_Z0 + 60)
    t = t.copy(); t.apply_transform(b.slider_pose(y_rail)); return b.to_mf(t)

def lift_env(m, owner, name, y0=None):
    """Zona libre encima de la pieza para sacarla hacia arriba (y0: desde la boca del riel; la
       lengüeta sube por dentro de la ranura y la comprueba check_joint)."""
    lo, hi = np.array(m.bounding_box()[:3]), np.array(m.bounding_box()[3:])
    return name, (owner, b.box(lo[0], hi[0], lo[1] if y0 is None else y0, hi[1], hi[2], hi[2] + LIFT))

class Report:
    def __init__(self): self.ok, self.lines = True, []
    def check(self, name, cond, val=""):
        self.ok &= bool(cond); self.lines.append(f"| {'OK' if cond else '**FALLO**'} | {name} | {val} |")
    def head(self, t): self.lines.append(f"\n### {t}\n\n| Resultado | Comprobación | Valor |\n|---|---|---|")

def vol(a, c): return (a ^ c).volume()

def check_combo(r, title, solids, envs, masses):
    r.head(title)
    names = list(solids)
    for i, a in enumerate(names):
        for c in names[i+1:]:
            v = vol(solids[a], solids[c])
            r.check(f"choque {a} / {c}", v < 0.5, f"{v:.2f} mm³")
    for en, (owner, e) in envs.items():
        hit = {s: vol(e, m) for s, m in solids.items() if s != owner}
        bad = {s: v for s, v in hit.items() if v > 0.01}
        r.check(f"acceso libre: {en}", not bad, ", ".join(f"{s} {v:.0f} mm³" for s, v in bad.items()) or "0 mm³")
    en = [k for k in envs if not k.startswith("extraer")]   # los caminos de extracción no llevan clavijas
    for i, a in enumerate(en):
        for c in en[i+1:]:
            if envs[a][0] != envs[c][0]:
                v = vol(envs[a][1], envs[c][1])
                if v > 0.01: r.check(f"zonas de acceso que se solapan: {a} / {c}", False, f"{v:.0f} mm³")
    # estabilidad
    com, tot = np.zeros(3), 0.0
    for s, m in solids.items():
        kg = masses.get(s, m.volume() * PETG)
        lo, hi = np.array(m.bounding_box()[:3]), np.array(m.bounding_box()[3:])
        c = (lo + hi) / 2 if s in masses else np.asarray(b.to_tm(m).center_mass)
        com += kg * c; tot += kg
    com /= tot
    feet = np.vstack([b.to_tm(m).vertices for m in solids.values()])
    feet = feet[feet[:, 2] < 0.2][:, :2]             # lo que toca la mesa
    eq = ConvexHull(feet).equations                  # a*x + b*y + c <= 0 dentro
    margin = -(eq[:, :2] @ com[:2] + eq[:, 2]).max()
    r.check("estable: centro de masas dentro de la huella", margin > 5,
            f"margen {margin:.0f} mm, CdM ({com[0]:.0f}, {com[1]:.0f}, {com[2]:.0f}), {tot*1000:.0f} g (masas estimadas)")

def check_joint(r, name, female, male, solids_around=()):
    """Mueve la pieza macho respecto a la hembra y mide la interferencia."""
    t = lambda d: male.translate(d)
    s = vol(female, male)
    r.check(f"{name}: asentado sin choque", s < 0.5, f"{s:.2f} mm³")
    v = vol(female, t([0, 1.5, 0]))
    r.check(f"{name}: retiene al tirar hacia atrás 1,5 mm (cola de milano)", v > 1, f"{v:.0f} mm³")
    v = vol(female, t([0, 0, -1.0]))
    r.check(f"{name}: tope al empujar 1 mm hacia abajo", v > 1, f"{v:.0f} mm³")
    v = vol(female, t([0, 0, 5.0]))
    r.check(f"{name}: clic de los detents al subir 5 mm", 0.05 < v < 5, f"{v:.2f} mm³")
    path = max(vol(female, t([0, 0, dz])) + sum(vol(o, t([0, 0, dz])) for o in solids_around)
               for dz in np.arange(2, LIFT, 4.0))
    r.check(f"{name}: camino de inserción libre desde arriba (solo roce de detents)", path < 3, f"máx {path:.2f} mm³")

def main():
    p, env = parts()
    r = Report()
    st, sv, radio, atu = p["soporte"], p["funda ATU-10"], p["radio"], p["ATU-10"]
    r.head("Piezas impresas")
    for n, m in (("soporte", st), ("funda ATU-10", sv)):
        r.check(f"pieza {n}: sólido estanco y único", m.status().name == "NoError" and len(m.decompose()) == 1,
                f"{m.volume()/1000:.1f} cm³")
    radio_env = {k: v for k, v in env.items() if v[0] == "radio"}
    atu_env = {k: v for k, v in env.items() if v[0] == "ATU-10"}

    # 1) truSDX solo
    check_combo(r, "1 · (tr)uSDX solo en el soporte", {"soporte": st, "radio": radio}, radio_env, MASS)
    # 2) truSDX + batería (batería en la ranura trasera del soporte)
    bat2 = slider_at(p, b.Y_BACK)
    e2 = dict(radio_env); e2.update([lift_env(bat2, "batería", "extraer batería hacia arriba", b.Y_BACK)])
    check_combo(r, "2 · (tr)uSDX + batería", {"soporte": st, "radio": radio, "batería": bat2}, e2, MASS)
    # 3) truSDX + ATU-10 + batería (soporte -> funda ATU-10 -> batería)
    bat3 = slider_at(p, b.ATU_Y1)
    e3 = dict(radio_env); e3.update(atu_env)
    e3.update([lift_env(bat3, "batería", "extraer batería hacia arriba", b.ATU_Y1),
               lift_env(sv + atu + bat3, "funda ATU-10", "extraer funda ATU-10 (con batería) hacia arriba", b.ATU_Y0)])
    s3 = {"soporte": st, "radio": radio, "funda ATU-10": sv, "ATU-10": atu, "batería": bat3}
    check_combo(r, "3 · (tr)uSDX + ATU-10 + batería", s3, e3, MASS)
    # módulos sueltos
    check_combo(r, "Funda ATU-10 sola, con el ATU-10 dentro", {"funda ATU-10": sv, "ATU-10": atu}, atu_env, MASS)

    r.head("Encaje de los rieles")
    check_joint(r, "soporte -> batería", st, bat2, (radio,))
    check_joint(r, "soporte -> funda ATU-10", st, sv, (radio,))
    check_joint(r, "funda ATU-10 -> batería", sv, bat3, (st, radio))
    if p["_slider"] is None:
        r.lines.append("\n> Aviso: falta vendor/battery-slider.stl; la batería se ha modelado como una caja.")

    out = "\n".join(r.lines)
    print(out)
    (b.ROOT / "docs" / "verificacion.md").write_text(
        "# Verificación de choques y accesos\n\nGenerado por `python src/verify.py`. "
        "Radio y ATU-10 son modelos simplificados (cajas); la batería es `vendor/battery-slider.stl`.\n"
        + out + f"\n\n**Resultado global: {'TODO OK' if r.ok else 'HAY FALLOS'}**\n", encoding="utf-8")
    print("\nTODO OK" if r.ok else "\nHAY FALLOS")
    return r.ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
