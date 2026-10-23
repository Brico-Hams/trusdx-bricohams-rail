#!/usr/bin/env python3
"""Genera las imágenes de images/ con pyvista (sin ventana).

    python src/build.py && python src/render_previews.py
"""
import sys, pathlib, numpy as np, pyvista as pv
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build as b, verify as vf

pv.OFF_SCREEN = True
I = b.ROOT / "images"
COL = {"soporte": "#9aa0a6", "funda ATU-10": "#5b9bd5", "radio": "#3a3f47", "ATU-10": "#c0c4c8", "batería": "#f0a020"}
FRONT_LEFT, BACK_RIGHT = (-1.0, -1.3, 0.9), (1.2, 1.4, 0.8)

def mesh(m): return pv.wrap(b.to_tm(m))

def shot(out, solids, views, titles, extra=(), size=(1600, 760)):
    pl = pv.Plotter(off_screen=True, shape=(1, len(views)), window_size=size)
    allb = np.array([m.bounding_box() for m in solids.values()])
    c = (allb[:, :3].min(0) + allb[:, 3:].max(0)) / 2
    for i, (v, t) in enumerate(zip(views, titles)):
        pl.subplot(0, i); pl.set_background("white")
        for n, m in solids.items():
            pl.add_mesh(mesh(m), color=COL.get(n, "#9aa0a6"), smooth_shading=False)
        for m, col, op in extra:
            pl.add_mesh(mesh(m), color=col, opacity=op)
        pl.camera_position = [tuple(c + np.array(v) * 210), tuple(c), (0, 0, 1)]
        pl.add_text(t, font_size=10, color="black", position="upper_left")
        pl.add_text("BricoHams", font_size=12, color="#bbbbbb", position="lower_right")
    pl.screenshot(I / out); pl.close()

def main():
    p, env = vf.parts()
    st, sv, radio, atu = p["soporte"], p["funda ATU-10"], p["radio"], p["ATU-10"]
    bat2, bat3 = vf.slider_at(p, b.Y_BACK), vf.slider_at(p, b.ATU_Y1)
    for f in I.glob("*.png"): f.unlink()
    shot("combo1_trusdx.png", {"soporte": st, "radio": radio}, [FRONT_LEFT, BACK_RIGHT],
         ["1 · (tr)uSDX solo: extremos con conectores libres", "Vista trasera: ranura DL2MAN vacía"])
    shot("combo2_trusdx_bateria.png", {"soporte": st, "radio": radio, "batería": bat2}, [FRONT_LEFT, BACK_RIGHT],
         ["2 · (tr)uSDX + batería", "La batería entra desde arriba en la trasera"])
    s3 = {"soporte": st, "radio": radio, "funda ATU-10": sv, "ATU-10": atu, "batería": bat3}
    shot("combo3_trusdx_atu_bateria.png", s3, [FRONT_LEFT, BACK_RIGHT],
         ["3 · (tr)uSDX + ATU-10 + batería", "Soporte -> funda ATU-10 -> batería"])
    zones = [(e, "#2ecc71" if not k.startswith("extraer") else "#3498db", 0.25) for k, (_, e) in env.items()]
    shot("accesos.png", s3, [FRONT_LEFT, BACK_RIGHT],
         ["Zonas de acceso que deben quedar libres (verde)", "Verde: conectores y mandos"], zones)
    shot("soporte.png", {"soporte": st}, [(-1.0, -1.2, 0.7), (0.9, 1.5, 0.6)],
         ["Soporte: labio y pendiente de 50°", "Ranura DL2MAN con tope abajo"], size=(1400, 700))
    shot("funda_atu10.png", {"funda ATU-10": sv}, [(-1.2, -1.0, 0.6), (1.3, 1.1, 0.6)],
         ["Funda ATU-10: lengüeta delante, abierta por -X", "Ranura detrás y marco-tope en +X (BNC)"], size=(1400, 700))
    for f in sorted(I.glob("*.png")): print(f.name)

if __name__ == "__main__":
    main()
