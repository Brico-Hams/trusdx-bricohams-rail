# 8 · Estado general y orden de fabricación

Actualizado el 2026-10-29. Las vistas se regeneran con `src/render_previews.py`.
Todos los accesorios son **P0**, sin ensayos físicos realizados. Una malla válida o un cálculo sin
interferencia no certifican resistencia, seguridad eléctrica, ajuste impreso ni rendimiento RF.

## Inventario y estado

| Elemento | Archivos / manual | Estado real |
|---|---|---|
| Atril del (tr)uSDX | [STL](../stl/trusdx-stand_rail_BricoHams.stl), [impresión](02_impresion.md) | Modelo existente; verificación digital, prueba física pendiente |
| Funda ATU-10 | [STL](../stl/atu10-sleeve_rail_BricoHams.stl), [montaje](03_montaje.md) | Modelo existente para caja nominal de 100 × 71 × 25 mm |
| Batería con riel | [STL](../stl/battery-3x18650_rail_BricoHams.stl), [P0](04_prototipo_test.md) | Solo prueba de riel liberada; portapilas real y electrónica aún sin adaptar |
| Portapilas elegido | [BOM](03_montaje.md#materiales) | Triple, 75,6 × 61,5 × 18,3 mm anunciados; confirmar medidas y conexión 3S |
| BMS y cargador | [Guía](03_montaje.md) | Candidatos identificados; cotas, equilibrado y validación eléctrica/térmica pendientes |
| Cable DC a radio | [BOM](03_montaje.md#materiales) | Referencia 3,5 × 1,3 mm, centro positivo; comprobar unidad real |
| Micrófono y altavoz | [Conexión](03_montaje.md) | Pinout de radio documentado; modelos de accesorios sin identificar |
| Llave recta portátil | [Manual, dos STL y BOM](05_llave_morse.md) | Geometría comprobada; hardware ajustable y prueba física pendientes |
| Antena U01 FT114-43 | [Manual y BOM](07_antena_u01.md) | Identificada en foto y esquema; aislador/devanador P0 nuevos |
| Cubierta FT114 sobre PCB | [Referencia original](07_antena_u01.md#referencias-e-identificación) | STL original consultado fuera del repo; ajuste físico pendiente |
| Caja cilíndrica genérica | [Manual y STL](06_protector_toroide.md) | Solo transporte de toroide suelto; **no usar para la U01 sobre PCB** |
| Bandeja de antena bajo atril | Concepto descrito abajo | **Sin CAD ni STL**: faltan dimensiones del conjunto recogido |

## Orden recomendado para una unidad de test

1. Imprimir el módulo de batería existente para probar el **riel**, no para dar por adaptado el portapilas.
2. Medir portapilas y placas reales. Resolver sujeción, aislamiento, cableado y acceso USB-C antes de un pack operativo.
3. Imprimir base/palanca Morse y montar según su manual; comprobar continuidad sin conectar a la radio.
4. Imprimir un aislador U01 de muestra y revisar acabado; producir el resto tras el ensayo mecánico.
   El devanador auxiliar es opcional: la PCB de la antena ya tiene función de recogida.
5. Ensayar la cubierta FT114 original con la revisión de PCB real, sin forzar ni pinzar bobinado o terminales.
6. Completar las listas de aceptación de cada manual antes de probar alimentación o RF.

No se han creado G-code ni perfiles de laminador específicos de una impresora no confirmada.
El material base de prueba es PETG; cada manual detalla orientación, paredes y relleno.

## Bandeja desmontable bajo el atril: concepto pendiente

La opción preferida es una **base de transporte independiente con tapa**, debajo del atril,
sin debilitar las paredes del soporte ni escalar el riel. Alojaría la PCB devanadera con su cubierta,
apoyos blandos que no presionen componentes, una correa de retención y separación de cuerda/conectores.
La antena debe retirarse y desplegarse antes de transmitir.

Antes de generar STL hacen falta:

- Largo, ancho y grosor máximos de la antena recogida, **incluidos hilo, cubierta y SMA/BNC**.
- Volumen de cuerda y conectores, y decisión de llevar el coaxial de al menos 5 m dentro o aparte.
- Masa real para revisar estabilidad al elevar la radio.
- Espacio de apertura, apoyo del atril y fijación desmontable que no obstruya rieles ni cables.

No se representa esta bandeja en las imágenes como si estuviera construida. Los renders actuales
mantienen las combinaciones reales de los STL existentes.

## Comprobaciones reproducibles

```bash
python -m unittest discover -s src -p "test_*.py"
python src/verify.py
python src/render_previews.py
```

La verificación del conjunto original está en [verificacion.md](verificacion.md).
Los generadores de accesorios comprueban sólidos y su geometría específica; no incluyen la tornillería,
muelles o cables en los cálculos de interferencia.
