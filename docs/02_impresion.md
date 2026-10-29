# 2 · Impresión

## Ajustes recomendados (PETG)

| Ajuste | Soporte | Funda ATU-10 | Batería |
|---|---|---|---|
| Altura de capa | 0,2 mm | 0,2 mm | 0,15–0,2 mm |
| Paredes | 4 | 4 | 3 |
| Relleno | 15–20 % | 20 % | 25 % |
| Soportes | **No** | **No** | **No** |
| Orientación | Tal cual viene: boca abierta sobre la cama | Tal cual viene: de pie, ranura y lengüeta en vertical | Tal cual viene: de pie, con el hueco del BMS abierto hacia arriba |
| Brim | 3–5 mm si la cama no agarra bien | 3 mm (pieza alta y estrecha) | 3 mm |

Temperaturas orientativas de PETG: boquilla a 235–245 °C, cama a 75–80 °C y ventilador al 30–50 %.

## Notas

- Los ajustes de esta tabla corresponden a los tres módulos originales. Para accesorios nuevos,
  consultar [pala K6ARK](05_llave_morse.md), [llave recta DJ9FM](09_llave_recta_dj9fm.md),
  [aisladores y devanador U01](07_antena_u01.md)
  y [caja genérica de transporte](06_protector_toroide.md). La caja genérica no sirve para la PCB U01.
- La antigua llave recta BricoHams P0 queda obsoleta. Las dos referencias actuales no comparten
  receta: K6ARK exige PETG y bisagras de dos perímetros; DJ9FM requiere revisar orientación,
  soportes y ajuste de rodamientos. No escalar los STL para corregir encajes.
- El portapilas triple seleccionado mide 75,6 × 61,5 × 18,3 mm según anuncio:
  no se ha adaptado ni validado su retención en el STL actual; ver [estado P0](04_prototipo_test.md).

- Las ranuras y las lengüetas verticales salen como la tapa de DL2MAN. Los voladizos de la cola de milano son de 3 mm y
  salen bien sin soportes. La lengüeta de la pendiente del soporte tiene flancos a unos 30° de la vertical: tampoco
  necesita soportes.
- **Prueba de ajuste:** antes de imprimir las piezas grandes, imprime la batería (es la más pequeña) y pruébala en la
  tapa `bottom_cover_battery` de la radio.
  - Si entra dura en las ranuras del repo, sube `DT_EXTRA` (en `src/dims.py`) a 0,2 y vuelve a ejecutar el script de
    Fusion 360. Si entra dura en la tapa de la radio, estrecha `TG_SECTIONS`.
  - Si queda floja y el clic no se nota, sube `DIMPLE_DEPTH` a 0,8.
- **Funda del ATU-10:** mide tu ATU-10 antes de imprimir y ajusta `ATU_L`, `ATU_H` y `ATU_T`. Debe entrar a mano con un
  ligero roce. Si queda floja, pega una tira de fieltro en el fondo de la funda.
- **Batería:** mide tu portapilas (`BAT_HOLDER_L`, `BAT_HOLDER_H`) y el grosor de tus placas de BMS y cargador
  (`BAT_CAV_H`, 7 mm por defecto).
- La marca de agua está grabada a 0,6 mm. Si quieres resaltarla, rellena el grabado con pintura acrílica.
- Para la Anycubic Kobra S1 con PETG: limpia la cama con jabón, usa un brim de 3 mm y una primera capa lenta (20–30 mm/s).
