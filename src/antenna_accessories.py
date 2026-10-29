"""Accesorios mecanicos P0 para hilo de antena U01; sin certificacion de carga."""
import manifold3d as mf
import numpy as np
import trimesh

from geom import ROOT, box


def hole(x, y, diameter):
    return mf.Manifold.cylinder(8, diameter / 2, circular_segments=64).translate((x, y, -1))


def parts():
    insulator = box(0, 40, 0, 16, 0, 5)
    for x in (8, 32):
        insulator -= hole(x, 8, 5)
    winder = box(0, 120, 0, 55, 0, 5)
    for x in (-1, 100):
        for y in (10, 35):
            winder -= box(x, x + 21, y, y + 10, -1, 6)
    for x in (30, 90):
        winder -= hole(x, 27.5, 5)
    return {"u01-insulator_P0_BricoHams.stl": insulator,
            "u01-wire-winder_P0_BricoHams.stl": winder}


def validate(solid):
    if solid.status() != mf.Error.NoError:
        raise RuntimeError(f"solido no valido: {solid.status()}")
    data = solid.to_mesh()
    model = trimesh.Trimesh(np.asarray(data.vert_properties[:, :3]), np.asarray(data.tri_verts))
    if (not model.is_watertight or not model.is_winding_consistent
            or model.volume <= 0 or len(model.split()) != 1):
        raise RuntimeError("malla no valida")
    return model


def main():
    for name, solid in parts().items():
        model = validate(solid)
        path = ROOT / "stl" / name
        model.export(path)
        loaded = trimesh.load_mesh(path)
        if not loaded.is_watertight or not loaded.is_winding_consistent:
            raise RuntimeError(f"{name}: fallo de exportacion")
        print(f"OK {name}: {loaded.extents.tolist()} mm")


if __name__ == "__main__":
    main()
