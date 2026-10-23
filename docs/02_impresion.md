# 2 · Impresión

## Ajustes recomendados (PETG)

| Ajuste | Soporte | Funda ATU-10 | Slider DL2MAN |
|---|---|---|---|
| Altura de capa | 0,2 mm | 0,2 mm | 0,15 mm (recomendación de DL2MAN) |
| Paredes | 4 | 4 | 3 |
| Relleno | 15–20 % | 20 % | 20–25 % |
| Soportes | **No** | **No** | Según el original |
| Orientación | Tal cual viene: boca abierta sobre la cama | Tal cual viene: de pie, ranura y lengüeta en vertical | Según el original |
| Brim | 3–5 mm si la cama no agarra bien | 3 mm (pieza alta y estrecha) | No |

Temperaturas orientativas de PETG: boquilla a 235–245 °C, cama a 75–80 °C y ventilador al 30–50 %.

## Notas

- Las ranuras y la lengüeta quedan **en vertical**, como en la impresión de la tapa de DL2MAN. Los voladizos de la cola de
  milano son de 3 mm y salen bien sin soportes.
- **Prueba de ajuste:** antes de imprimir las piezas grandes, imprime solo la parte baja del soporte (en el laminador,
  corta a 25 mm de altura) y prueba el slider en los primeros 20 mm de la ranura.
  - Si entra duro, sube `DT_EXTRA` a 0,1–0,2 y regenera.
  - Si queda flojo y el clic no se nota, sube `DIMPLE_DEPTH` a 0,8.
- **Funda del ATU-10:** mide tu ATU-10 antes de imprimir y ajusta `ATU_L`, `ATU_H` y `ATU_T`. Debe entrar a mano con un
  ligero roce. Si queda floja, pega una tira de fieltro en el fondo de la funda.
- La marca de agua está grabada a 0,6 mm. Si quieres resaltarla, rellena el grabado con pintura acrílica.
- Para la Anycubic Kobra S1 con PETG: limpia la cama con jabón, usa un brim de 3 mm y una primera capa lenta (20–30 mm/s).
