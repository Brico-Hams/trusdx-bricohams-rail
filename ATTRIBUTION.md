# Atribución y licencias

Este proyecto se apoya en trabajos de la comunidad. Todos los créditos van a sus autores.

| Obra | Autor | Enlace | Licencia | Uso en este repo |
|---|---|---|---|---|
| Housing for (tr)uSDX QRP Transceiver | **DL2MAN** | https://www.printables.com/model/103619 | CC BY-SA 4.0 | **Perfil de cola de milano** medido de `bottom_cover_battery.stl` y `battery-slider.stl`, para ser compatible. Medidas de la carcasa y sus aberturas, y del hueco del portapilas del slider. `vendor/bottom_cover_battery.stl` y `vendor/battery-slider.stl` se incluyen sin modificar para la verificación |
| (tr)uSDX Battery Lead Cover | **Jim, KD9WNR** | https://www.printables.com/model/1097625 | CC BY-NC 4.0 | Usado en v1/v2; la batería v3 lleva su propia salida de cables |
| (tr)uSDX Stand with ATU-10 Enclosure | **Jim, KD9WNR** (inspirado en W5AUG) | https://www.printables.com/model/737296 | CC BY-NC 4.0 | Base de las versiones v1 y v2 de este repo. La v3 no usa su geometría; de su funda se tomó la referencia del hueco del ATU-10 |
| Battery slider with USB-C charger | **DL1MAD** (remix de DL2MAN) | https://www.printables.com/model/1339609 | CC BY-SA 4.0 | Compatible sin cambios |
| 3S Battery Case | **Richard Sisol** | https://makerworld.com/es/models/1583590-3s-battery-case#profileId-1666971 | Standard Digital File License (según la ficha de MakerWorld) | Referencia propuesta para el portabaterías 3×18650; integración pendiente. No se incluyen ni modifican sus archivos; cualquier modificación o redistribución requiere revisar los permisos de su licencia |
| ATU-10 | **N7DDC** (David Fainitski) | https://github.com/Dfinitski/ATU-10-10W-QRP-antenna-tuner | — | Medidas de la caja (100 × 71 × 25 mm) y disposición de los paneles |
| Morse Code Paddle / CW Key | **Adam Kimmerly / K6ARK** | https://www.printables.com/model/332611-morse-code-paddle-cw-key | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) | Cuatro originales sin modificar en `vendor/k6ark-paddle/`; copias en `stl/k6ark-*` trasladadas solo en Z; vista `images/morse_key.png` |
| Straight Morse Key - Compact With Magnets | **Willie DJ9FM / willie42** | https://www.thingiverse.com/thing:6940422 | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | Ocho originales y variantes en `vendor/dj9fm-key/`; copias en `stl/dj9fm-*` trasladadas solo en Z; vista `images/dj9fm_key.png` |

PCB, esquemas y firmware del (tr)uSDX son de DL2MAN y PE1NNZ, bajo sus propias licencias (CC BY-ND según DL2MAN). Este proyecto **no** los toca.

## Licencia de las piezas nuevas

`stl/*_BricoHams.stl`, `step/*_BricoHams.step`, `fusion/`, `src/`, `images/` y `docs/`: **CC BY-NC-SA 4.0**, © BricoHams.

**Excepciones:** las piezas K6ARK y su vista mantienen CC BY-NC-SA 4.0, © Adam Kimmerly / K6ARK.
Las piezas DJ9FM y su vista mantienen **CC BY-NC 4.0**, © Willie DJ9FM / willie42,
sin imponerles SA ni atribuir su diseño a BricoHams. Los manuales de integración son de BricoHams
y enlazan las instrucciones y créditos originales.

Se mantiene NC (no comercial) y SA, como en las versiones anteriores, para seguir el espíritu abierto del ecosistema
DL2MAN y KD9WNR.

Al redistribuir, cita a los autores de las piezas incluidas (también K6ARK o DJ9FM si corresponde)
y BricoHams, enlaza sus licencias e indica las transformaciones y este repositorio.
