# (tr)uSDX · Sistema modular de riel — BricoHams

Soporte de mesa para el transceptor QRP **(tr)uSDX** con módulos que se enganchan entre sí sin herramientas:

| Módulo | Pieza | Se usa solo | Se engancha |
|---|---|---|---|
| **Soporte del (tr)uSDX** | `stl/trusdx-stand_rail_BricoHams.stl` (nuevo) | Sí: la radio a 50°, enganchada por su riel | Lengüeta en la pendiente (radio) + ranura en la trasera |
| **ATU-10** (N7DDC) | `stl/atu10-sleeve_rail_BricoHams.stl` (nuevo) | Sí: funda de mesa | Lengüeta delante + ranura detrás |
| **Batería 3×18650** | `stl/battery-3x18650_rail_BricoHams.stl` (nuevo) | Sí, o bajo la radio | Lengüeta DL2MAN; hueco para BMS 3S + cargador USB-C |

Como candidato para el portabaterías se propone el [3S Battery Case de Richard Sisol (MakerWorld, perfil 1666971)](https://makerworld.com/es/models/1583590-3s-battery-case#profileId-1666971).
Su adaptación al riel está **pendiente**: no sustituye todavía a la pieza de batería de esta tabla.
Ver [referencia y comprobaciones pendientes](docs/01_proceso_diseno.md#portabaterías-propuesto-makerworld).

Todas las uniones usan **el mismo riel de cola de milano que DL2MAN** usa para llevar la batería bajo la radio,
con sus detents de clic. La radio (con la tapa `bottom_cover_battery.stl` de DL2MAN) se desliza por la lengüeta de la
pendiente hasta el labio. Los demás módulos se encadenan por detrás y se encajan **desde arriba**, hasta un tope:

| Combinación | Orden (de delante a atrás) |
|---|---|
| (tr)uSDX solo | soporte |
| (tr)uSDX + batería | soporte → batería |
| (tr)uSDX + ATU-10 + batería | soporte → funda ATU-10 → batería |

![truSDX + ATU-10 + batería](images/combo3_trusdx_atu_bateria.png)

Nada se pone a los lados de la radio: sus dos extremos (antena, MIC/KEY y auriculares a la derecha; DC y USB a la izquierda)
y la cara superior (pantalla, mando y pulsadores) quedan libres en las tres combinaciones. El ATU-10 queda con sus BNC a la
derecha, junto a la antena de la radio, y su pantalla, botón y USB-C a la izquierda.
Ver la [comprobación de choques y accesos](docs/verificacion.md).

| (tr)uSDX solo | (tr)uSDX + batería | Zonas de acceso comprobadas |
|---|---|---|
| ![](images/combo1_trusdx.png) | ![](images/combo2_trusdx_bateria.png) | ![](images/accesos.png) |

| Soporte | Batería con hueco para BMS y cargador | Funda ATU-10 |
|---|---|---|
| ![](images/soporte.png) | ![](images/bateria.png) | ![](images/funda_atu10.png) |

## Documentación

1. [Proceso de diseño y medidas](docs/01_proceso_diseno.md)
2. [Impresión](docs/02_impresion.md)
3. [Montaje, cableado y materiales](docs/03_montaje.md)
4. [Verificación de choques y accesos](docs/verificacion.md)
5. [Atribución y licencias](ATTRIBUTION.md)

Para preparar la electrónica en la batería BricoHams actual, ver la
[comprobación de envolventes de BMS y cargador](docs/03_montaje.md#preparar-la-electrónica-para-la-batería-bricohams-actual).

## Regenerar las piezas

Las piezas se modelan en **Fusion 360**:

1. Ajusta las medidas en `src/dims.py` (inclinación, holguras del riel, medidas del ATU-10, `CALL` = tu indicativo
   para la marca de agua).
2. En Fusion 360: *Utilidades > Scripts y complementos > +* y elige `fusion/trusdx_rail_fusion.py`. Crea un diseño nuevo
   con los dos componentes y su historial, y exporta `stl/*.stl` y `step/*.step`.
3. Verifica y regenera las imágenes (Python solo comprueba; no modela):

```bash
pip install -r requirements.txt
python src/verify.py                  # choques, accesos, rieles y estabilidad -> docs/verificacion.md
python src/render_previews.py         # imágenes de images/
```

> **Versiones anteriores:** la v1 (riel en la trasera del soporte KD9WNR) y la v2 (riel en el lateral izquierdo) dejaban
> la batería tapando los conectores DC/USB de la radio o el sitio del ATU-10. Esta v3 lo resuelve con la cadena por detrás.

## Licencia

Las piezas nuevas: **CC BY-NC-SA 4.0** — ver [LICENSE.md](LICENSE.md).
Las piezas originales mantienen la licencia de sus autores — ver [ATTRIBUTION.md](ATTRIBUTION.md).

---
**BricoHams** · hecho por radioaficionados, para radioaficionados.
