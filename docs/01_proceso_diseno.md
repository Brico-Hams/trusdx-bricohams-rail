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

### Portabaterías propuesto (MakerWorld)

Referencia propuesta: [3S Battery Case](https://makerworld.com/es/models/1583590-3s-battery-case#profileId-1666971),
de **Richard Sisol**, modelo 1583590, perfil 1666971. Según la ficha del autor, aloja tres celdas 18650,
tiene soportes interiores para un balanceador 3S, aberturas de ventilación y un sistema propio de muesca y gancho.
La lista del autor incluye ocho tornillos M2,5 × 12 mm.

Su integración en este proyecto está **pendiente**, no verificada:

- Medir la caja y su enganche; no asumir que coinciden con el hueco actual de 77 × 60 × 22 mm ni con el riel DL2MAN.
- Evaluar un soporte o adaptador independiente al riel, conservando el acceso a la tapa, ventilación y salida de cables.
- Comprobar el espacio para la electrónica elegida: el soporte para un balanceador no confirma espacio para el BMS
  y el cargador USB-C del diseño actual, ni sus funciones de protección y carga.
- Repetir las comprobaciones de choques, accesos, retención y estabilidad con las medidas reales antes de darlo por compatible.
- Revisar los permisos antes de modificar o redistribuir archivos: la ficha indica **Standard Digital File License**,
  no CC BY-NC-SA 4.0. Ver [atribución](../ATTRIBUTION.md).

Por ahora solo se enlaza la referencia; no se incorpora su geometría ni se cambian los parámetros, STL, STEP o resultados
de verificación del módulo de batería actual.

#### Comprobación geométrica de los STL aportados (2026-10-29)

Se han examinado los cuatro originales facilitados por el usuario en `3S+Battery+Case/`, sin modificarlos.
Esto resuelve el bloqueo de descarga anterior. Las coordenadas se interpretan en **mm** (STL no declara unidades);
se conserva la posición relativa original, sin recentrar cada pieza.

| Pieza | Dimensiones X × Y × Z (mm) | Volumen de material (mm³) | Triángulos |
|---|---|---|---|
| `3S_BOTTOM.stl` | 67,20 × 48,00 × 11,00 | 8 906,71 | 1 376 |
| `3S_TOP.stl` | 67,20 × 48,00 × 11,00 | 8 840,34 | 1 432 |
| `3S_BOTTOM_CASE.stl` | 85,17 × 85,74 × 15,30 | 18 817,44 | 4 584 |
| `3S_TOP_CASE.stl` | 84,34 × 85,74 × 14,50 | 17 742,17 | 4 768 |

Las cuatro mallas son cerradas (`is_watertight`), tienen orientación de caras consistente, volumen positivo,
un solo componente conectado y se convierten en sólidos válidos de Manifold.
El conjunto ocupa **85,17 × 85,74 × 29,00 mm**:
X = −39,9716…45,2000; Y = −42,8716…42,8716; Z = −14,5…14,5.
Las dos cunas interiores juntas ocupan 67,20 × 48,00 × 22,40 mm; esta envolvente no es un hueco libre.

**Método:** lectura con `trimesh` 5.2.0 y booleanas con `manifold3d` 3.5.4. Las intersecciones se calculan
sobre las mallas trianguladas, no sobre cajas envolventes. Las celdas son cilindros de 256 lados, con eje Y,
centro Z = 0 y centros X = −18,4 / 0 / 18,4 mm. No se simulan contactos, cables, tornillos ni placas.

| Comprobación | Resultado |
|---|---|
| Intersección entre las seis parejas de piezas, en posición original | **0,000000 mm³** en todas |
| Separación entre extremos Z de las cunas inferior y superior | 0,40 mm de separación entre sus envolventes; no es una holgura uniforme entre todas las superficies |
| Cierre vertical: ambas piezas superiores frente a ambas inferiores | Sin choque en los desplazamientos Z = 0 / 0,2 / 0,5 / 1 / 2 / 5 / 10 / 20 / 30 mm; muestreo, no barrido continuo |
| Tres celdas simuladas Ø18 × 65 mm | **0 mm³** de choque con las cuatro piezas, para cada celda |
| Celdas simuladas Ø18 × 70 mm | También sin choque con el plástico; no confirma espacio para contactos ni compatibilidad eléctrica |
| Celdas simuladas Ø18,4 × 65 mm | Interferencia de 8,43…10,03 mm³ por media cuna y celda: no queda holgura utilizable |
| Celdas simuladas Ø18,6 × 65 mm | Interferencia de 118,57…132,92 mm³ por media cuna y celda: **no encajan sin interferencia** |

Los perfiles de las cunas corresponden aproximadamente a radio **9,2 mm**, con paso entre ejes de **18,4 mm**.
El espesor radial en el fondo central de las cunas es **2,0 mm** (Z = ±9,2…±11,2); no es un mínimo global
de pared: hay ventanas y otras zonas con geometría distinta. En la sección Z = −5 mm, los cuatro taladros de
la cuna inferior tienen Ø2,3 mm; los de la superior en Z = +5 mm tienen Ø3,1 mm.
La triangulación explica que un cilindro de Ø18,4 mm ya roce aunque el radio nominal sea 9,2 mm.
Hay que medir las celdas reales, especialmente las protegidas; la denominación «18650» por sí sola no garantiza el ajuste.

**Consecuencia para BricoHams:** la caja completa no cabe en el alojamiento de **77 × 60 × 22 mm** del módulo
actual, ni permutando sus ejes. Las cunas interiores tampoco son un sustituto directo del portapilas:
su espesor conjunto es 22,4 mm y necesitan resolver contactos y sujeción.
El enganche propio de MakerWorld no queda validado como riel DL2MAN por estas pruebas.
Para usar la caja completa en la cadena modular hay que diseñar y verificar una interfaz de soporte adecuada;
no basta con cambiar `BAT_HOLDER_L` y `BAT_HOLDER_H`.

**Pendiente:** cotas funcionales del gancho/muesca para esa interfaz, retención y recorrido de inserción,
espacio real del BMS/cargador, conectores, ventilación con el adaptador y estabilidad del conjunto con radio/ATU-10.
No se han cambiado los STL/STEP BricoHams ni se atribuyen a esta caja los resultados de `verificacion.md`.
No se han añadido los originales de MakerWorld al control de versiones ni concedido permisos de redistribución.

Identificación de las mallas analizadas (SHA-256):

```text
3S_BOTTOM.stl       30b337e780c27f3d00a72055544bf648c09c71ef9c8de36196fe6e05c0e6b6fb
3S_BOTTOM_CASE.stl  e54ee46bd367b79585d9800bdf3029fdcc5ef8f73bba3a2c4308cc08ef927a60
3S_TOP.stl          6d8f3e4572680b4ba674cfab952b9bf84545a474c14082d266e8013460b731aa
3S_TOP_CASE.stl     850bb2f59d40b31d42d483723d6bb805e41bc90024babdac3244907d20efebdd
```

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

## Alcance actual y accesorios

Las decisiones y dimensiones de este documento describen los **módulos v3 originales**, no una
adaptación ya terminada al portapilas adquirido. La referencia real de tres ranuras mide
75,6 × 61,5 × 18,3 mm según anuncio; su retención y alojamiento siguen pendientes.
El hueco nominal y los resultados de interferencia no prueban que ese portapilas quede sujeto.
Consultar el [estado general actualizado](08_estado_general.md) y el [prototipo P0](04_prototipo_test.md).

La llave Morse, los aisladores/devanador U01 y la caja genérica de toroide son accesorios separados,
con generadores Python y manuales propios. No forman parte de la cadena de rieles ni de las pruebas
de estabilidad del conjunto original. La bandeja bajo el atril todavía es un concepto, sin STL.

## Herramientas

- **Fusion 360** para el modelo: bocetos, extrusiones, vaciado, loft de la embocadura, revoluciones de los detents y
  texto grabado, con historial paramétrico. Exporta STL (impresión) y STEP (para editar en cualquier CAD).
- **Python 3** para medir y verificar los módulos originales, y generar los accesorios P0 independientes:
  `trimesh` (lectura y medidas de los STL originales), `manifold3d`
  (booleanas de interferencia), `scipy` (estabilidad) y `pyvista` (imágenes).
