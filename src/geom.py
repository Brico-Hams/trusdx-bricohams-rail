"""
Ayudas de geometría para la verificación y las imágenes (manifold3d + trimesh).
Las piezas imprimibles se modelan en Fusion 360 con fusion/trusdx_rail_fusion.py; aquí solo se
construyen los modelos simplificados (radio, ATU-10, lengüeta de batería) y las colocaciones.
"""
import pathlib, numpy as np, trimesh, manifold3d as mf
from dims import *

ROOT = pathlib.Path(__file__).resolve().parents[1]
VENDOR, OUT = ROOT / "vendor", ROOT / "stl"

def to_mf(tm):
    return mf.Manifold(mf.Mesh(vert_properties=np.asarray(tm.vertices, np.float32),
                               tri_verts=np.asarray(tm.faces, np.uint32)))

def to_tm(m):
    g = m.to_mesh(); return trimesh.Trimesh(g.vert_properties[:, :3], g.tri_verts)

def box(x0, x1, y0, y1, z0, z1):
    return mf.Manifold.cube([x1-x0, y1-y0, z1-z0]).translate([x0, y0, z0])

def _xs(pts):
    """CrossSection con el sentido de giro correcto (antihorario)."""
    pts = [tuple(p) for p in pts]
    a = sum(x0*y1 - x1*y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))
    return mf.CrossSection([pts if a > 0 else pts[::-1]])

def _along_x(cs, x0, x1):
    """Extruye un perfil del plano (y,z) a lo largo de X entre x0 y x1."""
    return mf.Manifold.extrude(cs, x1 - x0).transform([[0, 0, 1, x0], [1, 0, 0, 0], [0, 1, 0, 0]])

def rail_tongue(yf):
    """Lengüeta macho DL2MAN con resaltes (para la batería simplificada si falta el STL original)."""
    tg = mf.Manifold.extrude(_xs(tongue_profile(yf)), SLIDE_LEN).translate([0, 0, RAIL_Z0])
    r = BUMP_D / 2
    bumps = [mf.Manifold.sphere(r, 32).translate([0, yf - TG_DEPTH - BUMP_H + r, RAIL_Z0 + z])
             for z in DIMPLE_AT]
    return mf.Manifold.batch_boolean([tg] + bumps, mf.OpType.Add)

def slider_pose(y_rail):
    """Matriz 4x4 que coloca battery-slider.stl (DL2MAN) en una ranura trasera con la boca en y_rail.
       slider: x (0..90, largo) -> X, y (lengüeta en y<0) -> +Y, z (0..60, deslizamiento) -> Z."""
    return np.array([[1, 0, 0, -R_L/2], [0, 1, 0, y_rail], [0, 0, 1, RAIL_Z0], [0, 0, 0, 1]], float)
