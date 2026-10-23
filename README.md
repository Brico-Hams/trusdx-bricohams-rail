# (tr)uSDX · Sistema modular de riel — BricoHams

Soporte de mesa para el transceptor QRP **(tr)uSDX** con módulos que se enganchan entre sí sin herramientas:

| Módulo | Pieza | Se usa solo | Se engancha |
|---|---|---|---|
| **Soporte del (tr)uSDX** | `stl/trusdx-stand_rail_BricoHams.stl` (nuevo) | Sí: la radio apoyada a 50° | Ranura DL2MAN en la trasera |
| **ATU-10** (N7DDC) | `stl/atu10-sleeve_rail_BricoHams.stl` (nuevo) | Sí: funda de mesa | Lengüeta delante + ranura detrás |
| **Batería 3×18650** | `battery-slider.stl` de DL2MAN (original) | Sí, o en la radio con `bottom_cover_battery.stl` | Su lengüeta DL2MAN |

Todas las uniones usan **el mismo riel de cola de milano que DL2MAN** usa para llevar la batería bajo la radio,
con sus detents de clic. Los módulos se encadenan por detrás y se encajan **desde arriba**, hasta un tope:

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

## Documentación

1. [Proceso de diseño y medidas](docs/01_proceso_diseno.md)
2. [Impresión](docs/02_impresion.md)
3. [Montaje, cableado y materiales](docs/03_montaje.md)
4. [Verificación de choques y accesos](docs/verificacion.md)
5. [Atribución y licencias](ATTRIBUTION.md)

## Regenerar las piezas

```bash
pip install -r requirements.txt
python src/build.py --call EA4XXX     # tu indicativo en la marca de agua (opcional)
python src/verify.py                  # choques, accesos, rieles y estabilidad -> docs/verificacion.md
python src/render_previews.py         # imágenes de images/
```

Los parámetros (inclinación, holguras del riel, medidas del ATU-10…) están al principio de `src/build.py`.

> **Versiones anteriores:** la v1 (riel en la trasera del soporte KD9WNR) y la v2 (riel en el lateral izquierdo) dejaban
> la batería tapando los conectores DC/USB de la radio o el sitio del ATU-10. Esta v3 lo resuelve con la cadena por detrás.

## Licencia

Las piezas nuevas: **CC BY-NC-SA 4.0** — ver [LICENSE.md](LICENSE.md).
Las piezas originales mantienen la licencia de sus autores — ver [ATTRIBUTION.md](ATTRIBUTION.md).

---
**BricoHams** · hecho por radioaficionados, para radioaficionados.
