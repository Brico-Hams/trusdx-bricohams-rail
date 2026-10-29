# 4 · Prototipo de prueba P0: batería del (tr)uSDX

## Decisión de diseño

Se fija **P0 como prototipo de ajuste mecánico**, basado en la batería BricoHams v3 existente:
riel DL2MAN, portapilas triple para pack 3S1P y hueco separado para electrónica.
No se declara terminado el diseño eléctrico ni se autoriza una prueba con celdas instaladas.
No se usa la caja MakerWorld ni se amplía la pieza para cuatro celdas.

Esta decisión permite imprimir una pieza de test sin inventar cotas de placas, modificar el riel
ni cambiar a una tensión de batería no validada para la radio.

## Portapilas de la imagen aportada

El usuario corrige la imagen anterior: el portapilas utilizado dice **«3 × 18650 Battery Holder»**,
con medidas anunciadas de **75,6 × 61,5 × 18,3 mm**. La referencia de cuatro ranuras queda descartada.
«3 Pcs» significa tres unidades del portapilas. Las cotas son del anuncio, no una medición de la pieza recibida.

Comparación con el alojamiento nominal actual de **77 × 60 × 22 mm**, orientando
75,6 mm en X, 61,5 mm en Z y 18,3 mm en profundidad Y:

- X: quedan **1,4 mm totales**, antes de tolerancias de fabricación.
- Z: el portapilas supera la longitud actual en **1,5 mm**. Al ser un alojamiento abierto,
  esto no prueba por sí solo un choque: hay que comprobar posición, sobresaliente y retención.
- Y: quedan **3,7 mm totales** respecto a los 22 mm previstos; los labios pueden no sujetarlo.
  No se da por válido un montaje suelto ni se fijan espesores de calce sin medir la pieza real.
- Se selecciona este portapilas triple como referencia para la siguiente adaptación, pero el STL
  actual solo queda liberado para comprobar el riel, no como alojamiento validado de este modelo.
- La imagen no acredita la conexión eléctrica interna: confirmar serie 3S antes del montaje.
  Si es 3S, el pack alcanza 12,6 V con carga completa; no se aplica la advertencia de 4S de la foto anterior.
- La imagen tampoco identifica modelo, capacidad, dimensiones reales ni corriente de carga admisible de las celdas.

## Archivo para producir una unidad

Para probar **solo el riel**, imprimir **1 × [battery-3x18650_rail_BricoHams.stl](../stl/battery-3x18650_rail_BricoHams.stl)**,
sin escalar ni modificar. No es todavía la adaptación final al portapilas seleccionado. Modelo editable:
[battery-3x18650_rail_BricoHams.step](../step/battery-3x18650_rail_BricoHams.step).

| Característica | Valor |
|---|---|
| Envolvente del STL, X × Y × Z | 90 × 38,10 × 60 mm, incluidos riel y resaltes |
| Límites XYZ del STL | (0; −3,5; 0) a (90; 34,6; 60) mm |
| Alojamiento nominal del portapilas | 77 × 60 × 22 mm; comprobar también labios y recorrido de inserción |
| Hueco electrónico, plano XZ / profundidad Y | 77 × 58 mm / 7 mm |
| Espacio electrónico con márgenes de 0,5 mm | 76 × 57 mm / 6 mm |
| Carga USB-C prevista | Por el borde superior abierto; acceso pendiente de la placa real |
| Salida de alimentación | Abertura lateral izquierda existente |

Identificación SHA-256 del STL:

```text
6f168b16cf351dc8cf5c84f7b1a14093409731d7a1db3be76ef8777a75f09135
```

### Impresión

- PETG, capa de **0,2 mm**, **3 paredes**, **25 % de relleno**, brim de **3 mm**.
- Escala **100 %**, orientación original: Z = 0 sobre la cama, hueco abierto hacia arriba.
- Sin soportes como punto de partida; revisar la previsualización del laminador y los puentes.
- Usar el perfil PETG calibrado para la impresora. No se entrega G-code genérico.
- Si no está disponible un soporte BricoHams, probar el riel en la tapa original
  `bottom_cover_battery` del (tr)uSDX, sin alimentación.

## Electrónica candidata, no liberada para montaje

Los dos enlaces aportados corresponden a funciones complementarias, no a alternativas equivalentes:

| Elemento | Decisión para continuar |
|---|---|
| [Protección BMS 3S anunciada como 20 A](https://es.aliexpress.com/item/32809110553.html) | Candidata; falta confirmar equilibrado, cotas y especificaciones de la variante recibida |
| [Cargador USB-C con variantes 2S/3S/4S](https://es.aliexpress.com/item/1005008685119012.html) | Candidata **3S / 12,6 V / 1 A**, solo si las celdas admiten esa corriente y se valida su funcionamiento y temperatura |
| Portapilas | Triple de la imagen corregida: 75,6 × 61,5 × 18,3 mm anunciados; conexión 3S, medidas reales y retención pendientes de confirmar |
| Celdas | Tres iguales y compatibles con el portapilas y la carga; modelo todavía no identificado |
| Conector del pack a la radio | 1 clavija DC macho **3,5 × 1,3 mm**, centro positivo y exterior a masa, con cable bipolar; referencia y comprobaciones en el [BOM](03_montaje.md#materiales) |

No usar las cotas del resumen generado por IA del anuncio como medidas de fabricación.
No añadir soportes o taladros específicos hasta medir la placa completa, aislante, fijación,
soldaduras, conector y espacio necesario para el cable USB-C.
El BMS no sustituye al cargador y no se supone equilibrado por tener conexiones a las tres celdas.

## Prueba de aceptación P0, sin energía

1. Comprobar escala y medir el hueco impreso. Anotar material, perfil y medidas reales.
2. Ensayar **10 ciclos manuales** de inserción/extracción del riel en el soporte o tapa compatible.
   Aceptar si llega a su posición, se retiene lateralmente y no aparecen grietas, deformación
   permanente ni necesidad de herramientas. Es un criterio de test, no una prueba ya realizada.
3. Probar un portapilas triple vacío: debe insertarse, quedar sujeto y poder retirarse sin forzar.
   Si no está disponible, marcar esta comprobación como pendiente, no como aprobada.
4. Medir ambas placas y ejecutar
   [check_electronics.py](../src/check_electronics.py) con sus envolventes reales, según la
   [guía de montaje](03_montaje.md#preparar-la-electrónica-para-la-batería-bricohams-actual).
5. Ensayar las placas desconectadas o con galgas aislantes de sus dimensiones: aislamiento,
   fijación, entrada/salida, cable USB-C y salida de cables no deben quedar pinzados ni forzados.
6. Registrar cada fallo antes de modificar el CAD. Si hay que ampliar el hueco, regenerar STL y STEP
   en Fusion 360 y repetir la verificación; no escalar la pieza completa.

**No instalar celdas ni cargar el pack en esta fase.** La liberación del prototipo eléctrico requiere
confirmar las celdas, el portapilas triple, las funciones del BMS, el cargador y las polaridades;
después, una comprobación eléctrica y térmica supervisada. No se garantiza recepción sin ruido
ni carga simultánea durante el uso de la radio.

## Validación digital realizada

El 2026-10-29 se ejecutó `python src/verify.py` sobre los STL existentes: **TODO OK**.
Incluye interferencias, accesos, rieles y estabilidad con masas estimadas, ver
[informe generado](verificacion.md). No valida la electrónica real, las tolerancias de impresión,
la resistencia mecánica ni el encaje y retención del portapilas triple de la imagen corregida.

**Estado final:** archivo de impresión P0 seleccionado para prueba del riel y comprobado digitalmente.
Adaptación del alojamiento al portapilas triple, pruebas físicas y montaje eléctrico pendientes;
no es una liberación para producción o carga.
