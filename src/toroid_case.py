"""Caja de transporte de un toroide suelto; dimensiones del hueco en mm."""
import argparse
import math
from pathlib import Path

import manifold3d as mf
import numpy as np
import trimesh


ROOT = Path(__file__).resolve().parents[1]


def dimension(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("se requiere una dimension positiva y finita")
    return number


def cylinder(radius, height, z=0):
    return mf.Manifold.cylinder(height, radius, circular_segments=128).translate((0, 0, z))


def mesh(solid):
    data = solid.to_mesh()
    return trimesh.Trimesh(np.asarray(data.vert_properties[:, :3]), np.asarray(data.tri_verts))


def build(diameter, height):
    if diameter < 20 or height < 10:
        raise ValueError("hueco minimo: diametro 20 mm y altura 10 mm")
    radius = diameter / 2
    total = height + 4
    split = total / 2
    base = cylinder(radius + 4, split) - cylinder(radius, split + 1, 2)
    tongue = cylinder(radius + 2, 2, split) - cylinder(radius, 3, split)
    base += tongue
    lid = cylinder(radius + 4, total - split, split) - cylinder(radius, total - 2 - split, split)
    lid -= cylinder(radius + 2.3, 2, split)
    centers = ((radius + 8, 0), (-radius - 8, 0),
               (0, radius + 8), (0, -radius - 8))
    for x, y in centers:
        base += cylinder(5.5, split).translate((x, y, 0))
        lid += cylinder(5.5, total - split, split).translate((x, y, 0))
        hole = cylinder(1.7, total + 2, -1).translate((x, y, 0))
        base -= hole
        lid -= hole
    return base, lid, total


def validate(base, lid, diameter, height):
    for name, solid in (("base", base), ("tapa", lid)):
        model = mesh(solid)
        if (solid.status() != mf.Error.NoError or not model.is_watertight
                or not model.is_winding_consistent or model.volume <= 0
                or len(model.split()) != 1):
            raise RuntimeError(f"{name}: solido no valido")
    if (base ^ lid).volume() > 1e-4:
        raise RuntimeError("interferencia base/tapa")
    gauge = cylinder(diameter / 2 - 0.1, height - 0.2, 2.1)
    if (gauge ^ (base + lid)).volume() > 1e-4:
        raise RuntimeError("el hueco no cumple las dimensiones solicitadas")
    for lift in np.linspace(0, 10, 21):
        if (base ^ lid.translate((0, 0, float(lift)))).volume() > 1e-4:
            raise RuntimeError("interferencia al extraer la tapa")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diameter", type=dimension, required=True)
    parser.add_argument("--height", type=dimension, required=True)
    args = parser.parse_args()
    if args.diameter < 20 or args.height < 10:
        parser.error("hueco minimo: diametro 20 mm y altura 10 mm")
    base, lid, total = build(args.diameter, args.height)
    validate(base, lid, args.diameter, args.height)
    tag = f"{args.diameter:g}x{args.height:g}"
    output = ROOT / "stl"
    output.mkdir(exist_ok=True)
    for name, solid in (("base", base),
                        ("lid", lid.rotate((180, 0, 0)).translate((0, 0, total)))):
        model = mesh(solid)
        if abs(model.bounds[0, 2]) > 1e-5:
            raise RuntimeError("orientacion de impresion incorrecta")
        path = output / f"toroid-case-{name}_{tag}_P0_BricoHams.stl"
        model.export(path)
        loaded = trimesh.load_mesh(path)
        if not loaded.is_watertight or not loaded.is_winding_consistent:
            raise RuntimeError("exportacion STL no valida")
        print(f"{path.name}: {loaded.extents.round(2).tolist()} mm")
    print("OK: 2 solidos; hueco comprobado; cierre y 21 posiciones de extraccion sin choque.")
    print("Solo transporte; compatibilidad del toroide/PCB y pruebas fisicas pendientes.")


if __name__ == "__main__":
    main()
