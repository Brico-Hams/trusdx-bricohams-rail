# 5 · Llave Morse recta portátil P0

Se interpreta «moser key» como **llave recta manual**, no pala iámbica.
Accesorio independiente de diseño BricoHams: no modifica la radio ni ocupa el riel de la batería.
Es un prototipo para pruebas supervisadas, no un manipulador mecánico ya ensayado.

![Geometría de la llave P0, sin hardware](../images/morse_key.png)

## Archivos y fabricación

Imprimir una unidad de cada pieza, a escala 100 %, en la orientación suministrada:

- [Base P0](../stl/morse-key-base_P0_BricoHams.stl): 72 × 36 × 21 mm.
- [Palanca P0](../stl/morse-key-lever_P0_BricoHams.stl): se entrega tumbada sobre un lateral para imprimir.

PETG, capa 0,2 mm, 4 paredes, 35 % de relleno; comprobar el laminado de los puentes de los taladros
de los soportes del eje. Usar soportes locales si el perfil de la impresora los requiere.
Eliminar rebabas sin agrandar indiscriminadamente los alojamientos.

Para este accesorio se usa un generador independiente,
[src/morse_key.py](../src/morse_key.py), con `manifold3d` y `trimesh` de las dependencias del proyecto:

```bash
python src/morse_key.py
```

Es una excepción al modelado en Fusion 360 de los módulos originales: no cambia su generador,
STL ni STEP, y no produce un STEP de esta llave. Las dos piezas son geometría nueva, no un remix
de los modelos de terceros. Se aplica la licencia de las piezas BricoHams.

## BOM adicional

| Material | Cantidad | Selección y uso |
|---|---|---|
| Base y palanca impresas | 1 + 1 | Archivos anteriores |
| Tornillo o eje M3, longitud útil suficiente para atravesar 21 mm | 1 | Un M3 × 30 es candidato; preferible tramo liso en la articulación |
| Tuerca autoblocante M3 y arandelas para el eje | 1 juego | No apretar las orejetas hasta pinzar la palanca |
| Tornillos M3 de contacto y tope, tuercas y contratuercas | 3 juegos | Dos contactos en X=48 mm y un tope trasero en X=4 mm; longitudes a ajustar físicamente, surtido M3 × 10/12/16/20 como punto de partida |
| Terminales de anillo M3 y cable flexible de dos conductores | 2 + 1 tramo | Un terminal por contacto; dejar bucle flexible en el contacto móvil |
| Muelle de compresión suave | 1 | Diámetro exterior máximo 6 mm, longitud libre inicial 10–12 mm; verificar esfuerzo y que no llegue a espiras juntas |
| Patas aislantes antideslizantes | 4 | Altura mínima inicial 6 mm; aumentarla si sobresalen tornillos o tuercas por debajo |
| Correa de velcro de hasta 18 mm de ancho | 1 | Ranuras laterales de 20 × 3 mm; usar sobre una tabla o soporte rígido, no sobre la radio |
| Clavija TRS de audio de 3,5 mm | 1 | Para MIC/KEY; no confundir con el conector DC |

Las longitudes de tornillo y el muelle son componentes de ajuste del prototipo, no cotas de hardware
validadas. No usar la correa como sustituto de fijaciones en la radio ni rodear conectores o ventilación.

## Montaje mecánico

Las coordenadas siguientes corresponden al montaje, no al STL de la palanca tumbada.
X avanza desde la parte trasera hacia el pulsador; Z es altura desde el suelo de la base.

1. Colocar la palanca entre las dos orejetas. Alinear el eje en **X=14, Z=14 mm**.
   Los taladros son de Ø3,4 mm para un eje M3; quedan 1,5 mm nominales por lado entre palanca y orejetas.
   Colocar arandelas donde proceda y asegurar el eje sin bloquear el giro.
2. Introducir el muelle en los dos asientos de **Ø6,6 × 1 mm**, centrados en **X=32, Y=0**.
   En la postura horizontal hay 9 mm entre fondos de asientos. Comprobar que queda retenido,
   vuelve a reposo y no se comprime hasta espiras juntas durante todo el movimiento.
3. Montar el tope trasero ajustable en **X=4, Y=0**. Debe sostener la parte trasera de la palanca
   y limitar su retorno. Bloquear con contratuerca; no dejar que el muelle expulse la palanca.
4. Montar los contactos metálicos enfrentados en **X=48, Y=0**, usando los taladros pasantes
   de la base y palanca. El plástico no conduce: la continuidad debe producirse entre las caras
   de los dos tornillos. Sujetar cada terminal con su tuerca y ajustar sin que el cable impida el giro.
   No se confía en la conducción a través del eje ni del muelle.
5. Ajustar el tope para que la palanca quede aproximadamente horizontal en reposo y los contactos
   tengan **0,3–0,5 mm de separación inicial**. Asegurar cada ajuste con contratuerca.
   El recorrido validado digitalmente es de 0 a 2° hacia abajo desde esa posición; no es un tope físico.
   Los contactos deben cerrar antes de alcanzar ese límite, sin forzar ni flexionar la palanca.
6. Añadir patas aislantes con espacio suficiente bajo toda la tornillería. Sujetar la base a una
   tabla mediante velcro o usarla sobre una superficie firme y antideslizante.

No usar contactos oxidados o con bordes que dañen el cable. Si hay rebote excesivo, atasco,
rotura, retorno débil o salida del muelle, detener la prueba y corregir el montaje.

## Conexión al (tr)uSDX: llave recta

Según el [pinout oficial de DL2MAN](https://dl2man.de/wp-content/uploads/2021/12/image-61-1024x447.png):
punta = PTT/DIT, anillo = MIC/DAH y cuerpo = masa.
Para esta llave recta usar una clavija TRS con **anillo sin conectar y aislado**:

```text
MIC/KEY, punta (tip) ------- contacto fijo
                                  /
MIC/KEY, cuerpo (sleeve) --- contacto móvil
MIC/KEY, anillo (ring) ----- sin conectar, aislado
```

Es un **contacto seco normalmente abierto**. No requiere alimentación, electrónica de conmutación
ni conexión a la batería. No aplicar tensión a MIC/KEY.
No usar un divisor pasivo para compartir simultáneamente este conector con el micrófono/PTT.

Conectar con la radio apagada. Elegir modo **CW** y configuración de **llave recta (straight key)**,
no pala iámbica; consultar el [manual](https://dl2man.de/4-trusdx-manual/) de la versión de firmware
para el nombre y valor del ajuste. La llave no genera automáticamente puntos/rayas: los forma el operador.

## Aceptación antes de transmitir

1. Desconectada de la radio, comprobar con multímetro circuito abierto en reposo entre punta y cuerpo,
   continuidad al pulsar y anillo aislado en ambos estados.
2. Realizar 100 pulsaciones sin alimentación: retorno completo, ausencia de cortocircuitos permanentes,
   cable sin pinzamiento, muelle retenido y tuercas firmes. Es una prueba pendiente, no un resultado medido.
3. Confirmar que ninguna parte metálica inferior toca la mesa o el soporte y que la base no se desplaza.
4. Probar CW con una carga ficticia de 50 ohmios de potencia adecuada y transmisión supervisada.
   Si queda transmitiendo al soltar, apagar/desconectar y revisar contactos y configuración antes de continuar.

La verificación del generador comprueba sólidos, paso del eje y 41 posiciones de giro sin choque
entre plásticos. No certifica tolerancias de impresión, desgaste, resistencia, muelle,
contactos, cableado ni compatibilidad de una configuración de firmware no comprobada.
