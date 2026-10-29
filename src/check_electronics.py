"""Comprueba dos envolventes electronicas en la bateria BricoHams, sin modificarla."""
import argparse
from itertools import product
import math
from pathlib import Path

import geom as b


def positive_mm(value: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("se requiere una medida finita mayor que cero")
    return number


def layouts(bms: list[float], charger: list[float], clearance: float):
    """Envolventes X/Y/Z: placas paralelas al riel, sin apilarlas en profundidad."""
    wall = (b.BAT_L - b.BAT_HOLDER_L) / 2
    origin = (wall + clearance, b.BAT_PLATE + clearance, b.BAT_CAV_Z0 + clearance)
    available = (b.BAT_HOLDER_L - 2 * clearance,
                 b.BAT_CAV_H - 2 * clearance,
                 b.SLIDE_LEN - b.BAT_CAV_Z0 - 2 * clearance)
    for turn_bms, turn_charger, axis in product((False, True), (False, True), (0, 2)):
        sizes = []
        for board, turn in ((bms, turn_bms), (charger, turn_charger)):
            length, width, height = board
            sizes.append((width, height, length) if turn else (length, height, width))
        total = [max(a, c) for a, c in zip(*sizes)]
        total[axis] = sizes[0][axis] + clearance + sizes[1][axis]
        if any(size > limit + 1e-9 for size, limit in zip(total, available)):
            continue
        second = list(origin)
        second[axis] += sizes[0][axis] + clearance
        yield tuple(zip((origin, tuple(second)), sizes))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bms", nargs=3, type=positive_mm, required=True,
                        metavar=("L", "W", "H"), help="envolvente BMS, mm")
    parser.add_argument("--charger", nargs=3, type=positive_mm, required=True,
                        metavar=("L", "W", "H"), help="envolvente cargador, mm")
    parser.add_argument("--clearance", type=positive_mm, default=0.5,
                        help="margen a paredes y entre placas, mm (0.5)")
    parser.add_argument("--stl", type=Path,
                        default=b.OUT / "battery-3x18650_rail_BricoHams.stl")
    args = parser.parse_args()
    mesh = b.trimesh.load_mesh(args.stl)
    if not mesh.is_watertight or not mesh.is_winding_consistent or mesh.volume <= 0:
        parser.error("el STL debe ser una malla cerrada, orientada y de volumen positivo")
    plastic = b.to_mf(mesh)
    if plastic.status() != b.mf.Error.NoError:
        parser.error(f"STL no valido para booleanas: {plastic.status()}")
    found = False
    for layout in layouts(args.bms, args.charger, args.clearance):
        boxes = [b.box(x, x + dx, y, y + dy, z, z + dz)
                 for (x, y, z), (dx, dy, dz) in layout]
        if any((box ^ plastic).volume() > 1e-4 for box in boxes):
            continue
        found = True
        print("OK geometrico: envolventes dentro del hueco y sin choque con el STL.")
        for name, (origin, size) in zip(("BMS", "cargador"), layout):
            print(f"{name}: origen XYZ {origin}, dimensiones XYZ {size} mm")
        break
    if not found:
        print("NO CABE en las disposiciones probadas o hay interferencia con el STL.")
    print("Solo colocacion estatica; no valida USB-C, cables, fijacion, aislamiento, "
          "insercion ni funcionamiento electrico.")
    return 0 if found else 1


if __name__ == "__main__":
    raise SystemExit(main())
