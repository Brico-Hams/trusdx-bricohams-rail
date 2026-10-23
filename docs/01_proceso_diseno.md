# 1 · Proceso de diseño (v3)

## Objetivo

Tres módulos —soporte del (tr)uSDX, batería y ATU-10— que se usan **solos o unidos** sin herramientas, en tres
combinaciones: (tr)uSDX solo, (tr)uSDX + batería y (tr)uSDX + ATU-10 + batería. Los conectores y mandos de la radio y
del ATU-10 tienen que quedar accesibles, y ningún módulo puede chocar con otro.

## Qué fallaba en la v1 y la v2

Ambas versiones eran un remix del soporte de KD9WNR con un riel para la batería:

- **v1** — batería en la trasera del soporte: ocupaba justo el sitio donde KD9WNR pone la funda del ATU-10.
- **v2** — batería en el lateral izquierdo, de 90 mm de alto: tapaba el extremo izquierdo de la radio, donde están el
  **jack DC** y el **micro-USB** (CAT/audio). Además, el slider se metía por detrás, donde va la funda del ATU-10.

## Referencias y medidas

| Equipo | Fuente | Datos usados |
|---|---|---|
| (tr)uSDX en carcasa DL2MAN | STL de la carcasa ([Printables 103619](https://www.printables.com/model/103619)), secciones con `trimesh` | Caja de 90 × 60 × 30 mm. Conectores medidos en las paredes, ver tabla siguiente |
| Batería 3×18650 | `vendor/battery-slider.stl` (DL2MAN) | Slider de 90 × 29,5 × 60 mm; lengüeta DL2MAN |
| ATU-10 (N7DDC) | [Repositorio de N7DDC](https://github.com/Dfinitski/ATU-10-10W-QRP-antenna-tuner) y la funda de KD9WNR (hueco interior 71,6 × 27,5 mm) | Caja de aluminio de **100 × 71 × 25 mm**. Panel frontal: OLED de 0,91", botón y USB-C. Panel trasero: BNC TX y ANT |

Aberturas de la carcasa DL2MAN (medidas en los STL):

| Cara de la radio | Aberturas | Uso |
|---|---|---|
| Extremo derecho (`right_wall`) | 7 × 7,5 mm + 2 × Ø6,5 mm | Antena (SMA, con adaptador a BNC), MIC/KEY y auriculares/altavoz |
| Extremo izquierdo (`left_wall`) | Ø6,5 mm + 9 × 4 mm | Alimentación DC y micro-USB (CAT/audio) |
| Pared larga superior (`upper_wall`) | 6 × 5 mm | Abertura auxiliar: se deja libre |
| Pared larga inferior (`lower_wall`) | ninguna | Apoya en el labio del soporte |
| Tapa superior | Ventana OLED 24 × 12,5, encoder Ø8, 3 pulsadores Ø4,5, rejilla | Mandos y pantalla |
| Tapa inferior | Solo tornillos | Apoya en la pendiente |

> No he podido descargar las fotos de Printables (página protegida contra bots). La posición exacta de cada clavija dentro
> de los extremos no hace falta: la verificación reserva **el extremo entero** de la radio.

## Decisiones

1. **Un solo estándar de unión: el riel DL2MAN.** La ranura hembra va siempre en una cara trasera vertical; la lengüeta
   macho, en la cara delantera del módulo siguiente. Como el slider de batería ya lleva esa lengüeta, la batería se
   engancha igual al soporte, a la funda del ATU-10 o a la tapa `bottom_cover_battery` de la radio.
2. **Cadena por detrás, nada a los lados.** Los dos extremos de la radio tienen conectores, así que los módulos van detrás:
   soporte → funda ATU-10 → batería. El soporte mide 90 mm de ancho, lo mismo que la radio.
3. **Encaje vertical desde arriba.** Cada ranura es ciega abajo (tope a 3 mm de la mesa) y abierta arriba, con la
   embocadura ensanchada 0,8 mm. Los módulos bajan hasta el tope y los detents (a 10 y 50 mm) hacen clic. La gravedad
   ayuda a la retención.
4. **Radio a 50°** sobre una pendiente con un labio de 4 × 8 mm que sujeta la pared inferior (la que no tiene
   aberturas). La pantalla mira hacia el operador sentado.
5. **Soporte hueco y abierto por abajo**, con paredes de 3 mm y 5 mm en la placa del riel. Se imprime sin soportes.
6. **Funda del ATU-10** abierta por el lado de la pantalla, el botón y el USB-C (izquierda). En el lado de los BNC
   (derecha) lleva un marco de 2 mm con pestañas de esquina que hacen de tope sin tapar los conectores. Los BNC quedan
   así cerca de la antena de la radio, para un latiguillo corto.
7. **8 mm libres** entre la pared superior de la radio y la cara trasera del soporte, para la abertura de 6 × 5 mm.

## Perfil del riel (estándar DL2MAN)

| Elemento | Ranura hembra | Lengüeta macho (medida en el slider y copiada en la funda) |
|---|---|---|
| Ancho en la boca / cuello | 27,2 mm | 25,0 mm |
| Ancho máximo | 29,2 mm en el fondo | 28,0 mm a 2 mm de altura (27,7 en la punta) |
| Profundidad / alto | 3,0 mm | 3,0 mm |
| Detents | Cavidades Ø2,6 × 0,6 mm a 10 y 50 mm | Resaltes Ø2 × 0,5 mm a 10 y 50 mm |

## Resultado

| Combinación | Huella (ancho × fondo) | Alto |
|---|---|---|
| (tr)uSDX solo | 90 × 70 mm (la radio sobresale 14 mm por delante) | 81 mm |
| (tr)uSDX + batería | 90 × 96 mm | 81 mm |
| (tr)uSDX + ATU-10 + batería | 103 × 130 mm | 81 mm |

La [verificación](verificacion.md) da **0 mm³ de choque** entre módulos, todas las zonas de acceso libres y los rieles
reteniendo en las tres uniones.

## Parámetros (`src/build.py`)

| Parámetro | Valor | Uso |
|---|---|---|
| `TILT` | 50° | Inclinación de la radio |
| `DT_EXTRA` | 0,0 | Holgura extra por lado de la ranura. Súbela a +0,1/+0,2 si entra duro |
| `DIMPLE_DEPTH` | 0,6 | Profundidad de los detents. Súbela para un clic más fuerte |
| `RAIL_Z0` | 3 | Altura del tope de todas las ranuras |
| `ATU_L`, `ATU_H`, `ATU_T` | 100, 71, 25 | Caja del ATU-10. **Mide la tuya**: cambia según el vendedor |
| `ATU_CLR` | 0,4 | Holgura por lado de la funda |
| `--call` | — | Indicativo en el lateral derecho del soporte y en la funda |

## Herramientas

Python 3 con `manifold3d` (booleanas), `trimesh` (lectura y medidas), `scipy` (estabilidad), `matplotlib` (texto) y
`pyvista` (imágenes).
