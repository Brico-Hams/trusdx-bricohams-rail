"""
BricoHams - (tr)uSDX modular rail system (v3): modelo en Fusion 360.

Crea un diseño nuevo con dos componentes (soporte del (tr)uSDX y funda del ATU-10), con su historial
de operaciones, y exporta cada pieza a stl/ (STL) y step/ (STEP) del repositorio.
Las medidas salen de src/dims.py (las mismas que usa src/verify.py).

Uso: Fusion 360 > Utilidades > Scripts y complementos > "+" > este fichero > Ejecutar.
Después: python src/verify.py && python src/render_previews.py
"""
import adsk.core, adsk.fusion, math, pathlib, sys, importlib

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
import dims as D
importlib.reload(D)

C = 0.1   # mm -> cm (unidades internas de la API)
VI = adsk.core.ValueInput.createByReal
OP = adsk.fusion.FeatureOperations

def P(x, y, z):
    return adsk.core.Point3D.create(x * C, y * C, z * C)

def plane_at(comp, base, offset_mm):
    if not offset_mm:
        return base
    pi = comp.constructionPlanes.createInput()
    pi.setByOffset(base, VI(offset_mm * C))
    return comp.constructionPlanes.add(pi)

def polygon(sk, pts3d):
    """Polígono cerrado en el boceto a partir de puntos del modelo (mm)."""
    lines = sk.sketchCurves.sketchLines
    sp = [sk.modelToSketchSpace(P(*p)) for p in pts3d]
    first = prev = lines.addByTwoPoints(sp[0], sp[1])
    for q in sp[2:]:
        prev = lines.addByTwoPoints(prev.endSketchPoint, q)
    lines.addByTwoPoints(prev.endSketchPoint, first.startSketchPoint)

def sketch_poly(comp, plane, pts3d):
    sk = comp.sketches.add(plane)
    polygon(sk, pts3d)
    return sk

def extrude(comp, prof, dist_mm, op, bodies=None, symmetric=False):
    ei = comp.features.extrudeFeatures.createInput(prof, op)
    if symmetric:
        ei.setSymmetricExtent(VI(dist_mm * C), True)
    else:
        d = adsk.fusion.ExtentDirections.PositiveExtentDirection if dist_mm > 0 \
            else adsk.fusion.ExtentDirections.NegativeExtentDirection
        ei.setOneSideExtent(adsk.fusion.DistanceExtentDefinition.create(VI(abs(dist_mm) * C)), d)
    if bodies:
        ei.participantBodies = bodies
    return comp.features.extrudeFeatures.add(ei)

def sphere(comp, center, r, op, bodies=None):
    """Esfera por revolución de un semicírculo en el plano YZ (los centros están en x=0)."""
    x, y, z = center
    sk = comp.sketches.add(comp.yZConstructionPlane)
    top, bot, c = (sk.modelToSketchSpace(P(x, y, z + r)), sk.modelToSketchSpace(P(x, y, z - r)),
                   sk.modelToSketchSpace(P(x, y, z)))
    sk.sketchCurves.sketchArcs.addByCenterStartSweep(c, top, math.pi)
    axis = sk.sketchCurves.sketchLines.addByTwoPoints(top, bot)
    ri = comp.features.revolveFeatures.createInput(sk.profiles.item(0), axis, op)
    ri.setAngleExtent(False, VI(2 * math.pi))
    if bodies:
        ri.participantBodies = bodies
    return comp.features.revolveFeatures.add(ri)

def rail_slot(comp, body, yf, z_top):
    """Ranura hembra DL2MAN vertical con la boca en y=yf, tope en RAIL_Z0, embocadura y detents."""
    z0 = D.RAIL_Z0
    sk = sketch_poly(comp, plane_at(comp, comp.xYConstructionPlane, z0),
                     [(x, y, z0) for x, y in D.slot_profile(yf)])
    extrude(comp, sk.profiles.item(0), z_top + 1 - z0, OP.CutFeatureOperation, [body])
    # embocadura: loft del perfil normal (2 mm por debajo) al ensanchado (en la cara superior)
    za, zb = z_top - 2, z_top + 0.01
    s1 = sketch_poly(comp, plane_at(comp, comp.xYConstructionPlane, za), [(x, y, za) for x, y in D.slot_profile(yf)])
    s2 = sketch_poly(comp, plane_at(comp, comp.xYConstructionPlane, zb),
                     [(x, y, zb) for x, y in D.slot_profile(yf, D.CHAMFER)])
    li = comp.features.loftFeatures.createInput(OP.CutFeatureOperation)
    li.loftSections.add(s1.profiles.item(0)); li.loftSections.add(s2.profiles.item(0))
    li.participantBodies = [body]
    comp.features.loftFeatures.add(li)
    r = D.DIMPLE_D / 2
    for z in D.DIMPLE_AT:
        sphere(comp, (0, yf - D.DT_DEPTH - D.DIMPLE_DEPTH + r, z0 + z), r, OP.CutFeatureOperation, [body])

def rail_tongue(comp, body, yf):
    """Lengüeta macho DL2MAN en la cara y=yf, hacia -Y, con los resaltes de los detents."""
    z0 = D.RAIL_Z0
    sk = sketch_poly(comp, plane_at(comp, comp.xYConstructionPlane, z0), [(x, y, z0) for x, y in D.tongue_profile(yf)])
    extrude(comp, sk.profiles.item(0), D.SLIDE_LEN, OP.JoinFeatureOperation, [body])
    r = D.BUMP_D / 2
    for z in D.DIMPLE_AT:
        sphere(comp, (0, yf - D.TG_DEPTH - D.BUMP_H + r, z0 + z), r, OP.JoinFeatureOperation, [body])

def planar_face(body, normal, coord_axis, coord):
    for f in body.faces:
        g = f.geometry
        if isinstance(g, adsk.core.Plane) and f.evaluator.getNormalAtPoint(f.pointOnFace)[1].isEqualTo(
                adsk.core.Vector3D.create(*normal)) and abs(getattr(f.pointOnFace, coord_axis) - coord * C) < 1e-4:
            return f
    raise RuntimeError(f"cara no encontrada: normal {normal}, {coord_axis}={coord}")

def engrave(comp, body, face, text, h, a, b, above=True, flip=False):
    """Graba `text` (altura h) sobre la cara plana `face`, centrado en la línea a-b (puntos del modelo, mm).
       Fusion orienta el texto según los ejes del boceto de cada cara: above/flip se eligieron
       comprobando en el STL que se lee bien desde fuera."""
    sk = comp.sketches.add(face)
    path = sk.sketchCurves.sketchLines.addByTwoPoints(sk.modelToSketchSpace(P(*a)), sk.modelToSketchSpace(P(*b)))
    path.isConstruction = True
    ti = sk.sketchTexts.createInput2(text, h * C)
    ti.setAsAlongPath(path, above, adsk.core.HorizontalAlignments.CenterHorizontalAlignment, 0)
    st = sk.sketchTexts.add(ti)
    st.isHorizontalFlip = st.isVerticalFlip = flip
    extrude(comp, st, -D.WM_DEPTH, OP.CutFeatureOperation, [body])

def new_component(root, name):
    occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    occ.component.name = name
    return occ.component

def stand(root):
    comp = new_component(root, "trusdx-stand_rail")
    sk = sketch_poly(comp, comp.yZConstructionPlane, [(0, y, z) for y, z in D.stand_profile()])
    body = extrude(comp, sk.profiles.item(0), D.ST_W, OP.NewBodyFeatureOperation, symmetric=True).bodies.item(0)
    body.name = "soporte"
    # hueco abierto por abajo (paredes WALL) y placa trasera de PLATE_T para la ranura
    faces = adsk.core.ObjectCollection.create()
    faces.add(planar_face(body, (0, 0, -1), "z", 0))
    si = comp.features.shellFeatures.createInput(faces, False)
    si.insideThickness = VI(D.WALL * C)
    comp.features.shellFeatures.add(si)
    yp = D.Y_BACK - D.PLATE_T
    zp = D.P0[1] + (yp - D.P0[0]) * math.tan(math.radians(D.TILT))
    sk = sketch_poly(comp, comp.yZConstructionPlane, [(0, yp, 0), (0, D.Y_BACK, 0), (0, D.Y_BACK, D.Z_BACK), (0, yp, zp)])
    extrude(comp, sk.profiles.item(0), D.ST_W, OP.JoinFeatureOperation, [body], symmetric=True)
    rail_slot(comp, body, D.Y_BACK, D.Z_BACK)
    # marcas de agua en los laterales, en la franja baja bajo la radio
    yc, z = D.Y_BACK / 2 + 2, 5.0
    engrave(comp, body, planar_face(body, (-1, 0, 0), "x", -D.ST_W / 2), D.WM_TEXT, 5.0,
            (-D.ST_W / 2, yc - 20, z), (-D.ST_W / 2, yc + 20, z), above=False, flip=True)
    engrave(comp, body, planar_face(body, (1, 0, 0), "x", D.ST_W / 2), D.CALL or "(tr)uSDX", 5.0,
            (D.ST_W / 2, yc - 20, z), (D.ST_W / 2, yc + 20, z))
    return comp, body

def atu_sleeve(root):
    comp = new_component(root, "atu10-sleeve_rail")
    x1 = D.ATU_XI + D.ATU_END_T
    sk = sketch_poly(comp, comp.xYConstructionPlane,
                     [(-D.ATU_XI, D.ATU_Y0, 0), (x1, D.ATU_Y0, 0), (x1, D.ATU_Y1, 0), (-D.ATU_XI, D.ATU_Y1, 0)])
    body = extrude(comp, sk.profiles.item(0), D.ATU_Z1, OP.NewBodyFeatureOperation).bodies.item(0)
    body.name = "funda ATU-10"
    # hueco del ATU-10, abierto por -X
    xa = -D.ATU_XI
    sk = sketch_poly(comp, plane_at(comp, comp.yZConstructionPlane, xa),
                     [(xa, D.ATU_YC0, D.ATU_ZC0), (xa, D.ATU_YC1, D.ATU_ZC0), (xa, D.ATU_YC1, D.ATU_ZC1), (xa, D.ATU_YC0, D.ATU_ZC1)])
    extrude(comp, sk.profiles.item(0), D.ATU_L + 2 * D.ATU_CLR, OP.CutFeatureOperation, [body])
    # ventana del marco de los BNC (+X), con pestañas de esquina como tope
    sk = sketch_poly(comp, plane_at(comp, comp.yZConstructionPlane, D.ATU_XI), [(D.ATU_XI, y, z) for y, z in D.atu_window()])
    extrude(comp, sk.profiles.item(0), D.ATU_END_T + 1, OP.CutFeatureOperation, [body])
    rail_tongue(comp, body, D.ATU_Y0)
    rail_slot(comp, body, D.ATU_Y1, D.ATU_Z1)
    yc = (D.ATU_Y0 + D.ATU_Y1) / 2 - 2
    engrave(comp, body, planar_face(body, (0, 0, 1), "z", D.ATU_Z1),
            D.WM_TEXT + (f"  {D.CALL}" if D.CALL else "") + "  ATU-10", 4.5,
            (-40, yc, D.ATU_Z1), (40, yc, D.ATU_Z1))
    return comp, body

def export(design, comp, body, name):
    em = design.exportManager
    (REPO / "stl").mkdir(exist_ok=True); (REPO / "step").mkdir(exist_ok=True)
    so = em.createSTLExportOptions(body, str(REPO / "stl" / f"{name}_BricoHams.stl"))
    so.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    so.isBinaryFormat = True
    em.execute(so)
    em.execute(em.createSTEPExportOptions(str(REPO / "step" / f"{name}_BricoHams.step"), comp))

def run(_context: str):
    app = adsk.core.Application.get()
    app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    design = adsk.fusion.Design.cast(app.activeProduct)
    design.designType = adsk.fusion.DesignTypes.ParametricDesignType
    design.fusionUnitsManager.distanceDisplayUnits = adsk.fusion.DistanceUnits.MillimeterDistanceUnits
    root = design.rootComponent
    for build, name in ((stand, "trusdx-stand_rail"), (atu_sleeve, "atu10-sleeve_rail")):
        comp, body = build(root)
        export(design, comp, body, name)
        bb = body.boundingBox
        print(f"{name}: {body.volume:.1f} cm3, "
              f"min {[round(v * 10, 1) for v in (bb.minPoint.x, bb.minPoint.y, bb.minPoint.z)]}, "
              f"max {[round(v * 10, 1) for v in (bb.maxPoint.x, bb.maxPoint.y, bb.maxPoint.z)]}")
