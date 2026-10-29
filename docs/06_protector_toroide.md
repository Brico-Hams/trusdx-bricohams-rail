# 6 · Protector de transporte para toroide, P0

La [antena U01 de DL2MAN](https://dl2man.de/u01-emergency-communications-antenna/)
incluye variantes FT82-43, FT114-43 y FT140-43. Su página enlaza cubiertas específicas
para algunas PCB. La imagen corregida identifica **FT114-43 montado en PCB devanadera**:
esta caja de toroide suelto **no corresponde a ese montaje**. Ver el
[kit U01 y la cubierta específica de referencia](07_antena_u01.md).

Se entrega un diseño BricoHams nuevo e independiente para **transportar un toroide suelto**,
sin copiar las cubiertas originales. No es una carcasa para operar la antena, no fija una PCB
y no ofrece impermeabilidad ni una potencia RF admisible certificada.

![Caja genérica de transporte; no cubierta U01](../images/toroid_case.png)

## STL de referencia

Ejemplo **de hueco Ø50 × 26 mm**, no medida atribuida al toroide del usuario:

- [Base Ø50 × 26 P0](../stl/toroid-case-base_50x26_P0_BricoHams.stl).
- [Tapa Ø50 × 26 P0](../stl/toroid-case-lid_50x26_P0_BricoHams.stl).

La cavidad es cilíndrica. Mide el conjunto **con bobinado, protección de hilos y acolchado**
antes de elegir dimensiones. Los diámetros nominales de ferrita no equivalen a los del conjunto bobinado.
El ejemplo no confirma que quepa un FT140 ni ninguno de los conjuntos U01.
Si el toroide está soldado a PCB o conectado a terminales que no caben completamente dentro,
**no usar estos STL**: hace falta medir ese montaje y diseñar sus apoyos y salidas.

## Diseño y BOM

- Dos mitades con techo y suelo de 2 mm, paredes nominales de 4 mm.
- Labio de centrado de 2 mm de alto, con holgura radial de 0,3 mm respecto al alojamiento de la tapa.
- Cuatro orejetas con taladros de Ø3,4 mm. En el ejemplo, conjunto cerrado de 30 mm de alto,
  cuerpo de Ø58 mm y envolvente máxima de 77 × 77 mm, incluidas las orejetas.
- 4 tornillos **M3 × 40**, 8 arandelas y 4 tuercas como selección inicial del ejemplo.
  Comprobar longitud real y proteger los extremos para evitar enganches durante el transporte.
- Acolchado dieléctrico suave, no conductor: el espesor debe estar incluido al dimensionar el hueco.
  No apretar el bobinado con espuma forzada ni permitir movimiento que roce el esmalte.

Imprimir una base y una tapa en PETG, capa 0,2 mm, 4 paredes y 25–30 % de relleno,
en la orientación suministrada (caras cerradas sobre la cama). Revisar laminado antes de imprimir.
No se incluye G-code ni STEP. Este accesorio usa un generador Python separado de los módulos Fusion:

```bash
python src/toroid_case.py --diameter 50 --height 26
```

Los argumentos especifican **el hueco interior**, no la ferrita desnuda.
El [generador](../src/toroid_case.py) exige diámetro mínimo de 20 mm y altura de 10 mm.
Para otras alturas, elegir tornillos según el espesor cerrado (altura del hueco + 4 mm),
arandelas y tuerca. No escalar los STL completos: alteraría taladros y holguras.

## Montaje y aceptación

1. Probar primero el cierre vacío, sin forzar ni flexionar las orejetas.
2. Colocar el acolchado y el toroide desconectado. Todos los hilos y terminales deben quedar
   dentro del volumen libre, sin cruzar la unión de las mitades, el labio o los tornillos.
   No doblar ni desoldar un montaje U01 para hacerlo entrar.
3. Cerrar a mano alternando los cuatro tornillos. La tapa debe asentar sin comprimir el bobinado;
   no usar la tornillería para vencer una interferencia.
4. Comprobar que no hay movimiento que golpee la ferrita, roce de hilos, tensión en terminales
   ni grietas del plástico. Las pruebas físicas siguen pendientes.
5. Abrir la caja y retirar el conjunto **antes de conectar o transmitir**. No pasar RF con la
   tornillería y el toroide dentro de esta caja de transporte no caracterizada.

La validación digital comprueba mallas cerradas, una sola pieza por mitad, hueco interior,
ausencia de intersección al cerrar y 21 posiciones de extracción vertical de la tapa.
No prueba impactos, estanqueidad, temperatura, RF ni compatibilidad con una PCB concreta.

**Estado:** STL genérico de referencia, no seleccionado para el conjunto FT114-43 sobre PCB
que muestra la fotografía corregida. No se afirma que la antena U01 del usuario esté protegida por este ejemplo.
