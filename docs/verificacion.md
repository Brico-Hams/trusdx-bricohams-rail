# Verificación de choques y accesos

Generado por `python src/verify.py`. Radio y ATU-10 son modelos simplificados (cajas); la batería es `vendor/battery-slider.stl`.

### Piezas impresas

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | pieza soporte: sólido estanco y único | 60.3 cm³ |
| OK | pieza funda ATU-10: sólido estanco y único | 71.1 cm³ |

### 1 · (tr)uSDX solo en el soporte

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | choque soporte / radio | 0.00 mm³ |
| OK | acceso libre: radio: pantalla, mando y pulsadores | 0 mm³ |
| OK | acceso libre: radio: DC + USB (extremo izq.) | 0 mm³ |
| OK | acceso libre: radio: antena + MIC/KEY + auric. (extremo der.) | 0 mm³ |
| OK | acceso libre: radio: abertura pared superior | 0 mm³ |
| OK | estable: centro de masas dentro de la huella | margen 19 mm, CdM (0, 19, 47), 227 g (masas estimadas) |

### 2 · (tr)uSDX + batería

| Resultado | Comprobación | Valor |
|---|---|---|
| OK | choque soporte / radio | 0.00 mm³ |
| OK | choque soporte / batería | 0.29 mm³ |
| OK | choque radio / batería | 0.00 mm³ |
| OK | acceso libre: radio: pantalla, mando y pulsadores | 0 mm³ |
| OK | acceso libre: radio: DC + USB (extremo izq.) | 0 mm³ |
| OK | acceso libre: radio: antena + MIC/KEY + auric. (extremo der.) | 0 mm³ |
| OK | acceso libre: radio: abertura pared superior | 0 mm³ |
| OK | acceso libre: extraer batería hacia arriba | 0 mm³ |
| OK | estable: centro de masas dentro de la huella | margen 14 mm, CdM (0, 42, 40), 427 g (masas estimadas) |

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
| OK | choque funda ATU-10 / batería | 0.29 mm³ |
| OK | choque ATU-10 / batería | 0.00 mm³ |
| OK | acceso libre: radio: pantalla, mando y pulsadores | 0 mm³ |
| OK | acceso libre: radio: DC + USB (extremo izq.) | 0 mm³ |
| OK | acceso libre: radio: antena + MIC/KEY + auric. (extremo der.) | 0 mm³ |
| OK | acceso libre: radio: abertura pared superior | 0 mm³ |
| OK | acceso libre: ATU-10: OLED, botón y USB-C (-X) | 0 mm³ |
| OK | acceso libre: ATU-10: BNC TX/ANT (+X) | 0 mm³ |
| OK | acceso libre: extraer batería hacia arriba | 0 mm³ |
| OK | acceso libre: extraer funda ATU-10 (con batería) hacia arriba | 0 mm³ |
| OK | estable: centro de masas dentro de la huella | margen 28 mm, CdM (0, 61, 40), 578 g (masas estimadas) |

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
| OK | soporte -> batería: asentado sin choque | 0.29 mm³ |
| OK | soporte -> batería: retiene al tirar hacia atrás 1,5 mm (cola de milano) | 13 mm³ |
| OK | soporte -> batería: tope al empujar 1 mm hacia abajo | 35 mm³ |
| OK | soporte -> batería: clic de los detents al subir 5 mm | 2.54 mm³ |
| OK | soporte -> batería: camino de inserción libre desde arriba (solo roce de detents) | máx 2.54 mm³ |
| OK | soporte -> funda ATU-10: asentado sin choque | 0.00 mm³ |
| OK | soporte -> funda ATU-10: retiene al tirar hacia atrás 1,5 mm (cola de milano) | 12 mm³ |
| OK | soporte -> funda ATU-10: tope al empujar 1 mm hacia abajo | 81 mm³ |
| OK | soporte -> funda ATU-10: clic de los detents al subir 5 mm | 1.26 mm³ |
| OK | soporte -> funda ATU-10: camino de inserción libre desde arriba (solo roce de detents) | máx 1.26 mm³ |
| OK | funda ATU-10 -> batería: asentado sin choque | 0.29 mm³ |
| OK | funda ATU-10 -> batería: retiene al tirar hacia atrás 1,5 mm (cola de milano) | 13 mm³ |
| OK | funda ATU-10 -> batería: tope al empujar 1 mm hacia abajo | 35 mm³ |
| OK | funda ATU-10 -> batería: clic de los detents al subir 5 mm | 2.54 mm³ |
| OK | funda ATU-10 -> batería: camino de inserción libre desde arriba (solo roce de detents) | máx 2.54 mm³ |

**Resultado global: TODO OK**
