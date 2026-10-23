# 3 · Montaje, cableado y materiales

## Piezas a imprimir

| STL | Autor / licencia | Cant. | Para qué combinación |
|---|---|---|---|
| `stl/trusdx-stand_rail_BricoHams.stl` | BricoHams · CC BY-NC-SA 4.0 | 1 | Todas |
| `stl/battery-3x18650_rail_BricoHams.stl` | BricoHams · CC BY-NC-SA 4.0 | 1 | Con batería |
| `stl/atu10-sleeve_rail_BricoHams.stl` | BricoHams · CC BY-NC-SA 4.0 | 1 | Solo con ATU-10 |
| Carcasa completa del (tr)uSDX con **`bottom_cover_battery.stl`** ([Printables 103619](https://www.printables.com/model/103619)) | DL2MAN · CC BY-SA 4.0 | 1 | Todas: la tapa con ranura es la que engancha la radio al soporte |
| Opcional: `battery-slider.stl` (DL2MAN) o la variante de DL1MAD ([Printables 1339609](https://www.printables.com/model/1339609)) | DL2MAN / DL1MAD · CC BY-SA 4.0 | (1) | Si ya los tienes: también encajan en el soporte |

Las piezas BricoHams también están en STEP (`step/`) para modificarlas en cualquier CAD; el modelo de origen es
`fusion/trusdx_rail_fusion.py` (Fusion 360).

## Materiales

| Material | Cant. | Notas |
|---|---|---|
| Portapilas 3×18650 (77 × 60 × 22 mm) | 1 | El mismo que usa el slider de DL2MAN |
| Celdas 18650 **protegidas** | 3 | |
| Placa **BMS 3S** | 1 | Debe caber en el hueco de 77 × 58 × 7 mm junto con el cargador |
| Placa de **carga USB-C para 3S** (12,6 V) | 1 | Con el USB-C hacia arriba, en el borde abierto del hueco |
| Fusible en línea y portafusible | 1 | En el positivo de salida |
| Cable de 22 AWG y clavija DC del (tr)uSDX | — | Salida de la batería, por la pared izquierda |
| Latiguillo coaxial corto, SMA (o BNC con el adaptador de la radio) a BNC | 1 | Radio → ATU-10 (TX), por el lado derecho |
| Cianoacrilato o cinta de doble cara | — | Para fijar las placas en el hueco |
| Fieltro adhesivo o patas de goma | Opcional | Bajo el soporte y la funda; o en la funda si el ATU-10 queda flojo |

> ⚠️ Un pack 3S de iones de litio llega a **12,6 V** con carga completa. Comprueba que esa tensión está dentro de lo que
> admite tu (tr)uSDX. Pon un fusible en serie, respeta la polaridad y aísla las placas (cinta Kapton) dentro del hueco.

## Pasos

1. **Batería:**
   1. Mete el BMS y el cargador en el hueco por arriba, con el USB-C del cargador en el borde superior para poder
      cargar con la batería montada. Fíjalos con cinta de doble cara.
   2. Pasa los cables del portapilas al hueco por los dos pasos que hay junto a cada extremo.
   3. Saca el cable de salida (con el fusible) por la abertura de la pared izquierda.
   4. Desliza el portapilas bajo los labios y pon las celdas.
2. **Radio en el soporte:** la radio debe llevar la tapa `bottom_cover_battery`. Con la pantalla hacia ti y la pared larga
   **sin aberturas** abajo, mete la ranura de la tapa en la lengüeta de la pendiente por arriba y deslízala hacia abajo
   hasta el labio. Notarás el clic. Los conectores quedan en los extremos libres: antena, MIC/KEY y auriculares a la
   derecha; DC y USB a la izquierda.
3. **(tr)uSDX + batería:** mira el soporte desde atrás. Mete la lengüeta de la batería en la ranura **por arriba**, con
   el portapilas mirando hacia atrás, y empújala hacia abajo hasta el tope. Notarás el clic de los detents.
4. **(tr)uSDX + ATU-10 + batería:**
   1. Mete el ATU-10 en la funda por el lado izquierdo, con los BNC por delante, hasta que toque las pestañas del marco
      derecho. La pantalla, el botón y el USB-C quedan a la izquierda.
   2. Baja la funda por la trasera del soporte, con la lengüeta en la ranura, hasta el tope.
   3. Baja la batería por la ranura trasera de la funda, igual que en el paso 3.
5. **Cableado:**
   - **Alimentación:** el cable sale de la batería por la izquierda y va al jack DC de la radio, en su extremo izquierdo.
   - **RF:** une la antena de la radio (extremo derecho) con el BNC **TX** del ATU-10 mediante el latiguillo. La antena
     va al BNC **ANT**.
   - **USB** de la radio (CAT/audio): por el extremo izquierdo.
   - **Carga:** el USB-C del cargador queda arriba, en el borde de la batería.
6. **Para desmontar,** saca primero los módulos de atrás hacia arriba (batería y funda). Después desliza la radio hacia
   arriba por la pendiente. Con la funda del ATU-10 puesta, la radio no puede salir.
7. **Uso portátil:** la batería se engancha también bajo la radio, en su tapa `bottom_cover_battery`: es el mismo riel.
   Con la batería bajo la radio, la radio no se puede poner en el soporte.

## Módulos sueltos

- **Soporte:** sujeta la radio por su riel sin nada más. La ranura trasera queda vacía.
- **Funda del ATU-10:** se tiene de pie sola, con el ATU-10 dentro, y deja libres los dos paneles.
- **Batería:** pack independiente con su cargador USB-C, o bajo la radio para uso portátil.
