# Verificación de choques y accesos

Generado por `python src/verify.py`. Piezas exportadas desde Fusion 360. La radio es la tapa `vendor/bottom_cover_battery.stl` (DL2MAN) más una caja de 90 × 60 × 30 mm; el ATU-10 es una caja de 100 × 71 × 25 mm.

### Piezas impresas

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | pieza soporte: sólido estanco y único | 65.2 cm³ |
| OK | pieza funda ATU-10: sólido estanco y único | 71.2 cm³ |
| OK | pieza batería: sólido estanco y único | 49.5 cm³ |

### 1 · (tr)uSDX solo en el soporte

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | choque soporte / radio | 0.00 mm³ |
| OK | acceso libre: radio: pantalla, mando y pulsadores | 0 mm³ |
| OK | acceso libre: radio: DC + USB (extremo izq.) | 0 mm³ |
| OK | acceso libre: radio: antena + MIC/KEY + auric. (extremo der.) | 0 mm³ |
| OK | acceso libre: radio: abertura pared superior | 0 mm³ |
| OK | estable: centro de masas dentro de la huella | margen 17 mm, CdM (0, 17, 48), 229 g (masas estimadas) |

### 2 · (tr)uSDX + batería

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | choque soporte / radio | 0.00 mm³ |
| OK | choque soporte / batería | 0.00 mm³ |
| OK | choque radio / batería | 0.00 mm³ |
| OK | acceso libre: radio: pantalla, mando y pulsadores | 0 mm³ |
| OK | acceso libre: radio: DC + USB (extremo izq.) | 0 mm³ |
| OK | acceso libre: radio: antena + MIC/KEY + auric. (extremo der.) | 0 mm³ |
| OK | acceso libre: radio: abertura pared superior | 0 mm³ |
| OK | acceso libre: extraer batería hacia arriba | 0 mm³ |
| OK | estable: centro de masas dentro de la huella | margen 13 mm, CdM (0, 43, 41), 429 g (masas estimadas) |

### 3 · (tr)uSDX + ATU-10 + batería

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | choque soporte / radio | 0.00 mm³ |
| OK | choque soporte / funda ATU-10 | 0.00 mm³ |
| OK | choque soporte / ATU-10 | 0.00 mm³ |
| OK | choque soporte / batería | 0.00 mm³ |
| OK | choque radio / funda ATU-10 | 0.00 mm³ |
| OK | choque radio / ATU-10 | 0.00 mm³ |
| OK | choque radio / batería | 0.00 mm³ |
| OK | choque funda ATU-10 / ATU-10 | 0.00 mm³ |
| OK | choque funda ATU-10 / batería | -0.00 mm³ |
| OK | choque ATU-10 / batería | 0.00 mm³ |
| OK | acceso libre: radio: pantalla, mando y pulsadores | 0 mm³ |
| OK | acceso libre: radio: DC + USB (extremo izq.) | 0 mm³ |
| OK | acceso libre: radio: antena + MIC/KEY + auric. (extremo der.) | 0 mm³ |
| OK | acceso libre: radio: abertura pared superior | 0 mm³ |
| OK | acceso libre: ATU-10: OLED, botón y USB-C (-X) | 0 mm³ |
| OK | acceso libre: ATU-10: BNC TX/ANT (+X) | 0 mm³ |
| OK | acceso libre: extraer batería hacia arriba | 0 mm³ |
| OK | acceso libre: extraer funda ATU-10 (con batería) hacia arriba | 0 mm³ |
| OK | estable: centro de masas dentro de la huella | margen 28 mm, CdM (0, 62, 40), 581 g (masas estimadas) |

### Funda ATU-10 sola, con el ATU-10 dentro

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | choque funda ATU-10 / ATU-10 | 0.00 mm³ |
| OK | acceso libre: ATU-10: OLED, botón y USB-C (-X) | 0 mm³ |
| OK | acceso libre: ATU-10: BNC TX/ANT (+X) | 0 mm³ |
| OK | estable: centro de masas dentro de la huella | margen 16 mm, CdM (1, 72, 38), 152 g (masas estimadas) |

### Encaje de los rieles

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | soporte -> radio (bottom_cover_battery, por la pendiente): asentado sin choque | 0.00 mm³ |
| OK | soporte -> radio (bottom_cover_battery, por la pendiente): la cola de milano retiene al tirar 1,5 mm | 122 mm³ |
| OK | soporte -> radio (bottom_cover_battery, por la pendiente): tope al empujar 1 mm más allá | 373 mm³ |
| OK | soporte -> radio (bottom_cover_battery, por la pendiente): clic de los detents al sacar 5 mm | 1.06 mm³ |
| OK | soporte -> radio (bottom_cover_battery, por la pendiente): camino de inserción libre (solo roce de detents) | máx 1.06 mm³ |
| OK | soporte -> batería: asentado sin choque | 0.00 mm³ |
| OK | soporte -> batería: la cola de milano retiene al tirar 1,5 mm | 86 mm³ |
| OK | soporte -> batería: tope al empujar 1 mm más allá | 80 mm³ |
| OK | soporte -> batería: clic de los detents al sacar 5 mm | 1.28 mm³ |
| OK | soporte -> batería: camino de inserción libre (solo roce de detents) | máx 1.28 mm³ |
| OK | soporte -> funda ATU-10: asentado sin choque | 0.00 mm³ |
| OK | soporte -> funda ATU-10: la cola de milano retiene al tirar 1,5 mm | 86 mm³ |
| OK | soporte -> funda ATU-10: tope al empujar 1 mm más allá | 80 mm³ |
| OK | soporte -> funda ATU-10: clic de los detents al sacar 5 mm | 1.28 mm³ |
| OK | soporte -> funda ATU-10: camino de inserción libre (solo roce de detents) | máx 1.28 mm³ |
| OK | funda ATU-10 -> batería: asentado sin choque | -0.00 mm³ |
| OK | funda ATU-10 -> batería: la cola de milano retiene al tirar 1,5 mm | 86 mm³ |
| OK | funda ATU-10 -> batería: tope al empujar 1 mm más allá | 80 mm³ |
| OK | funda ATU-10 -> batería: clic de los detents al sacar 5 mm | 1.28 mm³ |
| OK | funda ATU-10 -> batería: camino de inserción libre (solo roce de detents) | máx 1.28 mm³ |
| OK | radio (bottom_cover_battery) -> batería, uso portátil: asentado sin choque | 0.00 mm³ |
| OK | radio (bottom_cover_battery) -> batería, uso portátil: la cola de milano retiene al tirar 1,5 mm | 122 mm³ |
| OK | radio (bottom_cover_battery) -> batería, uso portátil: clic de los detents al sacar 5 mm | 1.06 mm³ |
| OK | radio (bottom_cover_battery) -> batería, uso portátil: camino de inserción libre (solo roce de detents) | máx 1.06 mm³ |
| OK | soporte -> slider original DL2MAN: asentado sin choque | 0.26 mm³ |
| OK | soporte -> slider original DL2MAN: la cola de milano retiene al tirar 1,5 mm | 94 mm³ |
| OK | soporte -> slider original DL2MAN: tope al empujar 1 mm más allá | 35 mm³ |
| OK | soporte -> slider original DL2MAN: clic de los detents al sacar 5 mm | 2.54 mm³ |
| OK | soporte -> slider original DL2MAN: camino de inserción libre (solo roce de detents) | máx 2.54 mm³ |

**Resultado global: TODO OK**
