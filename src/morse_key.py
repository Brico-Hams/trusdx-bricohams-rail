"""Genera y verifica una llave Morse recta P0 independiente (mm)."""
from pathlib import Path

import manifold3d as mf
import numpy as np
import trimesh


ROOT = Path(__file__).resolve().parents[1]
PIVOT_X, PIVOT_Z = 14.0, 14.0
HOLE_D = 3.4


def box(x0, x1, y0, y1, z0, z1):
    return mf.Manifold.cube((x1 - x0, y1 - y0, z1 - z0)).translate((x0, y0, z0))


def cylinder(x, y, z, diameter, height):
    return mf.Manifold.cylinder(height, diameter / 2, circular_segments=64).translate((x, y, z))


def axle(diameter):
    return mf.Manifold.cylinder(30, diameter / 2, circular_segments=64).rotate(
        (90, 0, 0)).translate((PIVOT_X, 15, PIVOT_Z))


def parts():
    base = box(0, 72, -18, 18, 0, 5)
    for y0, y1 in ((-10.5, -6.5), (6.5, 10.5)):
        base += box(8, 20, y0, y1, 4, 21)
    base -= axle(HOLE_D)
    for x in (4, 48):
        base -= cylinder(x, 0, -1, HOLE_D, 7)
    base -= cylinder(32, 0, 4, 6.6, 2)
    for y in (-14, 14):
        base -= box(26, 46, y - 1.5, y + 1.5, -1, 6)
    boss = mf.Manifold.cylinder(10, 5, circular_segments=64).rotate(
        (90, 0, 0)).translate((PIVOT_X, 5, PIVOT_Z))
    lever = box(2, 62, -5, 5, 12, 16) + boss + box(54, 68, -5, 5, 12, 20)
    lever -= axle(HOLE_D)
    lever -= cylinder(48, 0, 11, HOLE_D, 10)
    lever -= cylinder(32, 0, 11, 6.6, 2)
    return base, lever


def mesh(solid):
    data = solid.to_mesh()
    return trimesh.Trimesh(np.asarray(data.vert_properties[:, :3]),
                           np.asarray(data.tri_verts))


def validate(base, lever):
    for name, solid in (("base", base), ("palanca", lever)):
        model = mesh(solid)
        if (solid.status() != mf.Error.NoError or not model.is_watertight
                or not model.is_winding_consistent or model.volume <= 0
                or len(model.split()) != 1):
            raise RuntimeError(f"{name}: solido no valido")
    for angle in np.linspace(0, 2, 41):
        moving = lever.translate((-PIVOT_X, 0, -PIVOT_Z)).rotate(
            (0, float(angle), 0)).translate((PIVOT_X, 0, PIVOT_Z))
        if (moving ^ base).volume() > 1e-4:
            raise RuntimeError(f"interferencia plastica a {angle:.2f} grados")
    for name, solid in (("base", base), ("palanca", lever)):
        if (solid ^ axle(3)).volume() > 1e-4:
            raise RuntimeError(f"{name}: el eje M3 no pasa")
    print("OK: 2 solidos; eje M3 libre; 41 posiciones de palanca, 0..2 grados sin choque plastico.")


def main():
    base, lever = parts()
    validate(base, lever)
    output = ROOT / "stl"
    output.mkdir(exist_ok=True)
    printable = {
        "morse-key-base_P0_BricoHams.stl": base,
        "morse-key-lever_P0_BricoHams.stl": lever.rotate((90, 0, 0)).translate((0, 14, 5)),
    }
    for name, solid in printable.items():
        model = mesh(solid)
        if abs(model.bounds[0, 2]) > 1e-5:
            raise RuntimeError(f"{name}: no apoya en Z=0")
        model.export(output / name)
        loaded = trimesh.load_mesh(output / name)
        if not loaded.is_watertight or not loaded.is_winding_consistent:
            raise RuntimeError(f"{name}: exportacion STL no valida")
        print(f"{name}: {loaded.extents.round(2).tolist()} mm; {len(loaded.faces)} triangulos")


if __name__ == "__main__":
    main()
