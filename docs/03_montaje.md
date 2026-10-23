# 3 · Montaje, cableado y materiales

## Piezas a imprimir

| STL | Autor / licencia | Cant. | Para qué combinación |
|---|---|---|---|
| `stl/trusdx-stand_rail_BricoHams.stl` | BricoHams · CC BY-NC-SA 4.0 | 1 | Todas |
| `stl/atu10-sleeve_rail_BricoHams.stl` | BricoHams · CC BY-NC-SA 4.0 | 1 | Solo con ATU-10 |
| `battery-slider.stl` ([Printables 103619](https://www.printables.com/model/103619)) o `battery-slider-with-usb-charger` de DL1MAD ([Printables 1339609](https://www.printables.com/model/1339609)) | DL2MAN / DL1MAD · CC BY-SA 4.0 | 1 | Con batería |
| `trusdx-battery-lead-shroud.stl` ([Printables 1097625](https://www.printables.com/model/1097625)) | KD9WNR · CC BY-NC 4.0 | 1 | Con batería (opcional) |
| Carcasa completa del (tr)uSDX, con `bottom_cover.stl` o `bottom_cover_battery.stl` | DL2MAN · CC BY-SA 4.0 | 1 | Todas |

Las piezas BricoHams también están en STEP (`step/`) para modificarlas en cualquier CAD; el modelo de origen es
`fusion/trusdx_rail_fusion.py` (Fusion 360).

## Materiales

| Material | Cant. | Notas |
|---|---|---|
| Portapilas 3×18650 | 1 | El modelo para el que DL2MAN diseñó el slider (ver su ficha) |
| Celdas 18650 **protegidas**, o una BMS 3S | 3 | |
| Fusible en línea y portafusible | 1 | Cerca del portapilas, en el positivo |
| Cable de 22 AWG y clavija DC del (tr)uSDX | — | Para la batería |
| Latiguillo coaxial corto, SMA (o BNC con el adaptador de la radio) a BNC | 1 | Radio → ATU-10 (TX), por el lado derecho |
| Cianoacrilato | — | Para el protector de cables del portapilas |
| Fieltro adhesivo o patas de goma | Opcional | Bajo el soporte y la funda; o en la funda si el ATU-10 queda flojo |
| Opcional: placa de carga USB-C para 3S | 1 | Con la variante de DL1MAD |

> ⚠️ Un pack 3S de iones de litio llega a **12,6 V** con carga completa. Comprueba que esa tensión está dentro de lo que
> admite tu (tr)uSDX. Pon un fusible en serie y respeta la polaridad.

## Pasos

1. **Portapilas:** encájalo en el slider DL2MAN. Si usas el protector de KD9WNR, fíjalo con una gota de CA y haz los
   empalmes dentro.
2. **Radio en el soporte:** apoya la tapa inferior de la radio en la pendiente, con la pared larga **sin aberturas** abajo,
   contra el labio. La pantalla queda arriba y los conectores, en los extremos libres: antena, MIC/KEY y auriculares a la
   derecha; DC y USB a la izquierda.
3. **(tr)uSDX + batería:** mira el soporte desde atrás. Mete la lengüeta del slider en la ranura **por arriba**, con el
   portapilas mirando hacia atrás, y empújalo hacia abajo hasta el tope. Notarás el clic de los detents.
4. **(tr)uSDX + ATU-10 + batería:**
   1. Mete el ATU-10 en la funda por el lado izquierdo, con los BNC por delante, hasta que toque las pestañas del marco
      derecho. La pantalla, el botón y el USB-C quedan a la izquierda.
   2. Baja la funda por la trasera del soporte, con la lengüeta en la ranura, hasta el tope.
   3. Baja la batería por la ranura trasera de la funda, igual que en el paso 3.
5. **Cableado:**
   - **Alimentación:** lleva el cable de la batería por el lado izquierdo hasta el jack DC de la radio.
   - **RF:** une la antena de la radio (extremo derecho) con el BNC **TX** del ATU-10 mediante el latiguillo. La antena
     va al BNC **ANT**.
   - **USB** de la radio (CAT/audio): por el extremo izquierdo.
6. **Para desmontar,** saca primero los módulos de atrás hacia arriba: batería, funda y, por último, la radio.
7. **Uso portátil:** la batería también se engancha a la radio con `bottom_cover_battery.stl` de DL2MAN; es el mismo
   riel. Con la batería bajo la radio, la radio ya no apoya en el soporte.

## Módulos sueltos

- **Soporte:** sujeta la radio sin nada más. La ranura trasera queda vacía.
- **Funda del ATU-10:** se tiene de pie sola, con el ATU-10 dentro, y deja libres los dos paneles.
- **Batería:** es el slider original de DL2MAN; funciona como pack independiente o bajo la radio.
