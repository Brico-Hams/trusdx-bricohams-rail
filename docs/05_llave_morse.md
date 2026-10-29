# 5 · Pala CW portátil K6ARK: referencia seleccionada

Opción de pala doble. Para manipulación manual vertical, elegir la
[llave recta magnética DJ9FM](09_llave_recta_dj9fm.md); ambos modelos se ofrecen como alternativas.

**Sustituye a la llave recta BricoHams P0 anterior**, que no debe imprimirse para este kit.
El usuario ha seleccionado como referencia el diseño de **Adam Kimmerly, K6ARK**:
[Morse Code Paddle / CW Key](https://www.printables.com/model/332611-morse-code-paddle-cw-key),
bajo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
Se adopta el mecanismo original, no un rediseño presentado como equivalente.

![Pala K6ARK: mecanismo de referencia y piezas](../images/morse_key.png)

## Qué cambia

La referencia es una **pala doble para manipulador electrónico**, no una llave recta.
Usa bisagras y resortes flexibles de PETG, dos contactos y ajustes independientes de
recorrido y tensión. No lleva el eje ni el muelle de compresión de la propuesta anterior.
Las mallas y el generador anteriores se han retirado por estar **obsoletos para el kit portátil**.
La versión anterior sigue disponible en el historial Git.

Se seleccionan palas estándar para jack hembra, base cerrada, tapa redondeada y protector.
No mezclar la variante para conector macho con el jack hembra de este BOM.

## Imprimir una unidad de cada pieza

| Pieza | STL preparado | Envolvente (mm) |
|---|---|---|
| Palas estándar | [k6ark-paddle-standard.stl](../stl/k6ark-paddle-standard.stl) | 48 × 24 × 13,9 |
| Base cerrada | [k6ark-paddle-base-enclosed.stl](../stl/k6ark-paddle-base-enclosed.stl) | 31 × 24 × 15,2 |
| Tapa | [k6ark-paddle-top.stl](../stl/k6ark-paddle-top.stl) | 31 × 24 × 5,5 |
| Protector de transporte | [k6ark-paddle-cover.stl](../stl/k6ark-paddle-cover.stl) | 29,109 × 27,001 × 20,7 |

Estos tamaños son de piezas individuales; no se suman para calcular el conjunto.
Los [originales](../vendor/k6ark-paddle/README.md) se mantienen sin modificar.
Las copias de impresión solo trasladan Z hasta la cama; no se escala ni cambia el mecanismo.

**PETG obligatorio según el autor; no usar PLA para las palas.** Escala 100 %, boquilla de 0,4 mm,
capa de 0,3 mm como perfil de referencia del autor, sin soportes según su documentación.
Revisar el laminado de cada pieza: la bisagra debe tener **dos perímetros**, sin una única línea
con costura que la debilite. El autor limita el ancho de perímetro al 225 % de la boquilla.
No aplicar el relleno/paredes de la antigua llave recta como receta para esta bisagra.
Comprobar puentes, primera capa y orientación antes de imprimir.

## BOM del autor para la variante elegida

| Elemento | Cantidad | Notas |
|---|---|---|
| Cuatro piezas impresas anteriores | 1 de cada | Protector incluido para transporte |
| Jack hembra TRS de 3,5 mm para panel con tuerca | 1 | Comprobar cuerpo, rosca y patillas con el alojamiento; no cualquier jack de panel encaja |
| Prisionero M3 × 4 mm | 4 | Dos de recorrido/contacto y dos de tensión |
| Tornillo M3 × 4 mm | 1 | Poste/contacto común y fijación de la patilla de masa |
| Hilo fino AWG 34 o 36 | 2 tramos de unos 25 mm | El autor prefiere hilo resistente como nicromo; comprobar soldabilidad y fijación del material elegido |
| Cable TRS macho–macho de 3,5 mm | 1 | Continuidad punta–punta, anillo–anillo, cuerpo–cuerpo; no TRRS ni cable mono |
| Imán Ø10 × 2 mm | 3, opcionales | Accesorio del autor; no se han generado alojamientos nuevos ni base magnética |

La tabla de materiales del PDF indica 30 mm de hilo, pero los pasos describen aproximadamente
una pulgada por patilla lateral: preparar dos tramos de unos 25 mm y recortar tras el montaje.
El material fino no es el cable de alimentación 22 AWG; uno grueso puede limitar las palas.

## Montaje y ajuste

Seguir el manual original de la descarga facilitada por el usuario; este resumen no sustituye
sus imágenes ni permite identificar las patillas de cualquier jack:

1. Retirar rebabas de los encajes y verificar que las lengüetas elásticas no quedan unidas por hilos de impresión.
2. Identificar con multímetro las patillas del jack desconectado. Fijar un hilo fino a punta y otro a anillo;
   la masa común se fija al poste central mediante su tornillo, según la disposición original.
3. Montar el jack y su tuerca en las palas sin precargar las bisagras. Colocar las palas sobre la base
   y asegurar el contacto común; no forzar encajes si hay resistencia.
4. Llevar cada hilo al alojamiento de su prisionero de contacto, dejando holgura para el movimiento.
   Asegurar el hilo sin cortarlo y comprobar continuidad. Los prisioneros delanteros/superiores ajustan
   el recorrido; los traseros/inferiores, la tensión.
5. Encajar la tapa en su orientación correcta. Ajustar gradualmente hasta obtener dos contactos
   independientes, abiertos en reposo y con retorno completo. No flexionar arriba/abajo los extremos.
6. Usar el protector al transportar, sin aplastar las palas. La deformación lateral de acondicionamiento
   descrita por el autor no demuestra vida a fatiga: detenerse si aparecen marcas, grietas o retorno deficiente.

No se prescribe un modelo exacto de jack sin comprobar sus dimensiones; es el principal punto
de compatibilidad pendiente junto con las tolerancias de impresión.

## Conexión al (tr)uSDX

En **MIC/KEY**, según el
[pinout oficial](https://dl2man.de/wp-content/uploads/2021/12/image-61-1024x447.png):

```text
TRS punta (tip) ------- contacto DIT -----+
                                         +----- TRS cuerpo (sleeve, GND)
TRS anillo (ring) ----- contacto DAH -----+
```

Cada pala cierra un contacto seco a masa. **Aquí el anillo sí se utiliza**: no seguir la
instrucción de dejarlo aislado de la antigua llave recta. No alimentar el manipulador ni
conectarlo a DC o Audio OUT. No compartir MIC/KEY con micrófono/PTT mediante un divisor pasivo.

Conectar con la radio apagada. Elegir CW y un modo de manipulador para **pala doble/iámbico**,
no straight key. Consultar el [manual de la versión de firmware](https://dl2man.de/4-trusdx-manual/)
para ajustes, inversión de palas y velocidad; no se presupone un número de menú universal.

## Verificación y aceptación

Se comprueban cuatro mallas cerradas, orientadas y de un componente, volumen positivo,
preservación de geometría y apoyo en Z=0 tras exportar.
**No se afirma que los encajes a presión estén libres de interferencia**: forman parte del
diseño original, y el ajuste del jack, la flexión, el tacto y los contactos requieren pruebas físicas.

Antes de transmitir:

1. Comprobar en el extremo del cable abierto en reposo para punta–masa y anillo–masa.
2. Cada pala debe cerrar solo su línea; ambas pulsadas deben poder cerrar las dos.
   Confirmar retorno abierto y ausencia de puentes punta–anillo en reposo.
3. Ensayar 100 pulsaciones por lado sin radio; observar grietas, aflojamiento y cable pinzado.
4. Probar CW supervisado con carga ficticia de 50 ohmios de potencia adecuada.
   Detener la transmisión si queda una línea cerrada al soltar.

Regeneración reproducible:

```bash
python src/prepare_k6ark.py
python -m unittest discover -s src -p "test_*.py"
python src/render_previews.py
```

Estado: mecanismo de referencia seleccionado y archivos preparados digitalmente.
No se ha fabricado ni validado físicamente este ejemplar.
