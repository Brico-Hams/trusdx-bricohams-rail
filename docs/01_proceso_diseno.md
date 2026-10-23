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
| Batería 3×18650 | `vendor/battery-slider.stl` (DL2MAN) | Hueco del portapilas: 77 × 60 × 22 mm; lengüeta DL2MAN |
| Riel bajo la radio | `vendor/bottom_cover_battery.stl` (DL2MAN) | Perfil real de la ranura (tabla «Perfil del riel») |
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
   macho, en la cara delantera del módulo siguiente. La batería se engancha igual al soporte, a la funda del ATU-10 o a
   la tapa `bottom_cover_battery` de la radio, y el slider original de DL2MAN también sirve.
2. **Riel de la radio:** la pendiente del soporte lleva una lengüeta DL2MAN de 60 mm. La radio, con la tapa
   `bottom_cover_battery`, baja por ella hasta el labio (tope) y hace clic. Queda sujeta: no se cae al mover el soporte.
3. **Batería propia** con un hueco de 77 × 58 × 7 mm entre la lengüeta y el portapilas para el **BMS 3S** y el
   **cargador USB-C**. Está abierto por arriba, así que el USB-C queda accesible con la batería montada. Tiene dos pasos
   de cables al portapilas y una salida por la pared izquierda, hacia el jack DC de la radio.
4. **Cadena por detrás, nada a los lados.** Los dos extremos de la radio tienen conectores, así que los módulos van detrás:
   soporte → funda ATU-10 → batería. El soporte mide 90 mm de ancho, lo mismo que la radio.
5. **Encaje vertical desde arriba.** Cada ranura es ciega abajo (tope a 3 mm de la mesa) y abierta arriba, con la
   embocadura ensanchada 0,8 mm. Los módulos bajan hasta el tope y los detents (a 10 y 50 mm) hacen clic. La gravedad
   ayuda a la retención.
6. **Radio a 50°** sobre una pendiente con un labio de 4 × 8 mm que sujeta la pared inferior (la que no tiene
   aberturas). La pantalla mira hacia el operador sentado.
7. **Soporte hueco y abierto por abajo**, con paredes de 3 mm y 5 mm en la placa del riel. Se imprime sin soportes.
8. **Funda del ATU-10** abierta por el lado de la pantalla, el botón y el USB-C (izquierda). En el lado de los BNC
   (derecha) lleva un marco de 2 mm con pestañas de esquina que hacen de tope sin tapar los conectores. Los BNC quedan
   así cerca de la antena de la radio, para un latiguillo corto.
9. **8 mm libres** entre la pared superior de la radio y la cara trasera del soporte, para la abertura de 6 × 5 mm.

## Perfil del riel (estándar DL2MAN)

Ancho total (mm) a cada profundidad desde la cara, medido con rayos en los STL de DL2MAN:

| Profundidad | Ranura de `bottom_cover_battery` | Lengüeta del slider original | Lengüeta BricoHams | Ranura BricoHams |
|---|---|---|---|---|
| 0,1 mm | 26,6 | 25,0 | 25,0 | 26,7 |
| 0,7 mm (labio de la boca) | 25,9 | 25,4 | 25,0 | 26,1 |
| 1,5 mm | 26,9 | 27,0 | 26,4 | 27,4 |
| 2,3 mm | 28,5 | 28,0 | 28,0 | 28,7 |
| 2,9 mm | 29,1 | 27,3 | 27,6 | 29,3 |
| Detents (a 10 y 50 mm) | Cavidades | Resaltes Ø2 × 0,5 mm | Resaltes Ø2 × 0,5 mm | Cavidades Ø2,6 × 0,6 mm |

- Las **ranuras** BricoHams copian la de la tapa de DL2MAN, con `DT_EXTRA` = 0,1 mm de holgura por lado.
- La **lengüeta** BricoHams copia la del slider, algo más estrecha (0,15–0,45 mm por lado), para que entre con holgura
  también en la tapa original de la radio. El slider original de DL2MAN casi no tiene holgura en su tapa.

## Resultado

| Combinación | Huella (ancho × fondo) | Alto |
|---|---|---|
| (tr)uSDX solo | 90 × 74 mm (la radio sobresale 18 mm por delante) | 85 mm |
| (tr)uSDX + batería | 90 × 109 mm | 85 mm |
| (tr)uSDX + ATU-10 + batería | 103 × 142 mm | 85 mm |

La [verificación](verificacion.md) da **0 mm³ de choque** entre módulos, todas las zonas de acceso libres y los rieles
reteniendo en todas las uniones: radio en el soporte, batería y funda en las ranuras, batería bajo la radio y slider
original de DL2MAN en el soporte.

## Parámetros (`src/dims.py`)

Los usan el modelo de Fusion 360 (`fusion/trusdx_rail_fusion.py`) y la verificación (`src/verify.py`).

| Parámetro | Valor | Uso |
|---|---|---|
| `TILT` | 50° | Inclinación de la radio |
| `DT_EXTRA` | 0,1 | Holgura por lado de las ranuras sobre la tapa original. Súbela a 0,2 si entra duro |
| `TG_SECTIONS` | — | Perfil de la lengüeta (radio, funda y batería) |
| `BAT_HOLDER_L`, `BAT_HOLDER_H` | 77, 22 | Hueco del portapilas 3×18650. **Mide el tuyo** |
| `BAT_CAV_H` | 7 | Alto del hueco del BMS y del cargador USB-C. Súbelo si tus placas son más gruesas |
| `DIMPLE_DEPTH` | 0,6 | Profundidad de los detents. Súbela para un clic más fuerte |
| `RAIL_Z0` | 3 | Altura del tope de todas las ranuras |
| `ATU_L`, `ATU_H`, `ATU_T` | 100, 71, 25 | Caja del ATU-10. **Mide la tuya**: cambia según el vendedor |
| `ATU_CLR` | 0,4 | Holgura por lado de la funda |
| `CALL` | `None` | Indicativo en el lateral derecho del soporte y en la funda |

## Herramientas

- **Fusion 360** para el modelo: bocetos, extrusiones, vaciado, loft de la embocadura, revoluciones de los detents y
  texto grabado, con historial paramétrico. Exporta STL (impresión) y STEP (para editar en cualquier CAD).
- **Python 3** solo para medir y verificar: `trimesh` (lectura y medidas de los STL originales), `manifold3d`
  (booleanas de interferencia), `scipy` (estabilidad) y `pyvista` (imágenes).
