"""Prepara STL K6ARK, CC BY-NC-SA 4.0; solo traslada Z, sin redisenar el mecanismo."""
from pathlib import Path

import numpy as np
import trimesh


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "vendor" / "k6ark-paddle"
FILES = {
    "paddles-standard.stl": "k6ark-paddle-standard.stl",
    "press-on-bottom-enclosed-sides.stl": "k6ark-paddle-base-enclosed.stl",
    "press-top-rounded.stl": "k6ark-paddle-top.stl",
    "cover.stl": "k6ark-paddle-cover.stl",
}


def load_original(name, source=SOURCE):
    model = trimesh.load_mesh(source / name)
    if (not model.is_watertight or not model.is_winding_consistent
            or model.volume <= 0 or len(model.split(only_watertight=False)) != 1):
        raise RuntimeError(f"{name}: malla original no valida")
    return model


def prepare(name, source=SOURCE):
    original = load_original(name, source)
    printable = original.copy()
    printable.apply_translation((0, 0, -original.bounds[0, 2]))
    if (not np.allclose(printable.extents, original.extents)
            or not np.isclose(printable.volume, original.volume)
            or abs(printable.bounds[0, 2]) > 1e-6):
        raise RuntimeError(f"{name}: se ha alterado la geometria")
    return printable


def export_parts(source, files):
    output = ROOT / "stl"
    output.mkdir(exist_ok=True)
    for name, target in files.items():
        printable = prepare(name, source)
        printable.export(output / target)
        check = trimesh.load_mesh(output / target)
        if (not check.is_watertight or not check.is_winding_consistent
                or check.volume <= 0 or len(check.split(only_watertight=False)) != 1
                or abs(check.bounds[0, 2]) > 1e-6
                or not np.allclose(check.extents, printable.extents, atol=1e-4)
                or not np.isclose(check.volume, printable.volume, rtol=1e-5)):
            raise RuntimeError(f"{target}: exportacion no valida")
        print(f"OK {target}: {check.extents.round(3).tolist()} mm")


def main():
    export_parts(SOURCE, FILES)
    print("Adam Kimmerly / K6ARK; CC BY-NC-SA 4.0. Encajes y tacto pendientes de ensayo fisico.")


if __name__ == "__main__":
    main()
