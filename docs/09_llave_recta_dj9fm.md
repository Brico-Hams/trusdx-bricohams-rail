# 9 · Llave recta compacta con imanes DJ9FM

Segunda opción del kit, junto a la [pala doble K6ARK](05_llave_morse.md).
Autor: **Willie, DJ9FM / willie42**. Modelo original:
[Straight Morse Key - Compact With Magnets](https://www.thingiverse.com/thing:6940422),
licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
Se incorporan originales con atribución, no una copia presentada como creación BricoHams.

![Piezas DJ9FM, sin ensamblaje ni hardware](../images/dj9fm_key.png)

## Elegir una de las dos opciones

| | Pala K6ARK | Llave recta DJ9FM |
|---|---|---|
| Acción | Dos palas laterales, puntos/rayas del keyer | Una palanca vertical; duración manual de cada signo |
| Mecanismo | Flexión de PETG | Rodamientos y retorno magnético regulable |
| Radio | CW, modo pala doble/iámbico | CW, modo straight key |
| Contactos | DIT y DAH independientes a masa | Un contacto a masa |
| Uso | Manipulación electrónica portátil | Aprendizaje/manual y uso portátil |

No usar simultáneamente ambas en un divisor de MIC/KEY.
La antigua llave recta BricoHams P0 no es una tercera recomendación.

## Archivos de impresión

Se preparan los ocho STL del autor, incluidos los alternativos. **No imprimirlos todos como una única llave**.
La selección inicial para estudiar el montaje es base2, arm2, button2, distance y magnetmount.
La compatibilidad de la pareja de palanca/botón y el número de separadores deben confirmarse
con las fotos/CAD del autor y el hardware real antes de producir el juego final.

| Pieza | Archivo preparado | Envolvente (mm) |
|---|---|---|
| Base | [dj9fm-key-base.stl](../stl/dj9fm-key-base.stl) | 35 × 89 × 30,157 |
| Palanca 2 | [dj9fm-key-arm2.stl](../stl/dj9fm-key-arm2.stl) | 24,996 × 77,499 × 8 |
| Botón 2 | [dj9fm-key-button2.stl](../stl/dj9fm-key-button2.stl) | 28,126 × 28,126 × 17,794 |
| Separador | [dj9fm-key-distance.stl](../stl/dj9fm-key-distance.stl) | 6,4 × 9,999 × 9,998 |
| Soporte magnético | [dj9fm-key-magnetmount.stl](../stl/dj9fm-key-magnetmount.stl) | 14 × 14 × 18 |
| Palanca alternativa | [dj9fm-key-arm-alternative.stl](../stl/dj9fm-key-arm-alternative.stl) | 18 × 70 × 8 |
| Botón alternativo | [dj9fm-key-button-alternative.stl](../stl/dj9fm-key-button-alternative.stl) | 25,073 × 25,075 × 6,105 |
| Knopf2 alternativo | [dj9fm-key-knopf2-alternative.stl](../stl/dj9fm-key-knopf2-alternative.stl) | 28,126 × 28,126 × 17,794 |

Los [originales](../vendor/dj9fm-key/README.md) no se han modificado.
Las copias de impresión solo trasladan Z; **eso no garantiza la mejor orientación de laminado**.
Revisar cada pieza, especialmente separadores y botones, y orientarla para el alojamiento y acabado
requeridos sin escalarla. Punto de partida de ensayo BricoHams: PETG, capa 0,2 mm y 4 paredes;
no son ajustes publicados por el autor ni validados físicamente.
Revisar soportes locales y puentes en el laminador. No imprimir una base cuyo laminado deje
alojamientos críticos sin soporte adecuado.

## BOM publicado por el autor

| Elemento | Cantidad |
|---|---|
| Tornillo 3 × 10 mm | 2 |
| Tornillo 3 × 15 mm | 2 |
| Tornillo 3 × 20 mm | 1 |
| Rodamiento 698, 19 × 8 × 6 mm | 2 |
| Imán Ø10 × 3 mm | 2 |
| Cable fino, terminal de anillo y chincheta/contacto metálico | Según montaje |
| Jack de 3,5 mm | 1 |
| Goma esponjosa adhesiva para la base | Opcional |
| Cable a MIC/KEY | 1; según jack y adaptación elegidos |

La ficha dice «screw 3x…»: no se presupone una rosca, cabeza ni tuerca universal para
todos los alojamientos. Confirmar con el modelo y hardware real.
Mantener imanes pequeños fuera del alcance de niños y alejados de dispositivos médicos sensibles;
no soltarlos ni cerrar la pieza sin verificar su retención.

## Montaje y ajuste

Usar las fotografías y el [vídeo del autor](https://youtu.be/gBxgxKQY3Dw) para el orden
y orientación. La ficha explica que el tornillo trasero ajusta recorrido y el soporte
del imán superior ajusta fuerza de retorno.

1. Hacer una presentación en seco de base, rodamientos, palanca y separadores.
   No prensar los rodamientos a golpes ni usar tornillos para corregir interferencias.
2. Comprobar la pareja de botón y palanca. El autor indica instalar el tornillo del botón
   **antes** del contacto superior de chincheta.
3. Montar los contactos y cableado con holgura en la parte móvil. El autor utiliza la chincheta
   como contacto superior y un terminal de anillo en el montaje; no se confía en rodamientos
   o imanes como camino eléctrico.
4. Orientar los imanes para obtener el retorno previsto y asegurar su retención.
   Comprobar retorno abierto antes de conectar a una radio.
5. Ajustar fuerza y recorrido gradualmente; bloquear las fijaciones necesarias sin frenar la palanca.
   No se fija una distancia de contacto universal sin ensayar el hardware.

No se ha simulado un ensamblaje de hardware ni certificado la fuerza magnética, el juego del eje
o los encajes de las variantes. Las vistas muestran **piezas separadas**, no un ensamblaje validado.

## Conexionado al (tr)uSDX

Clavija TRS de 3,5 mm del lado de **MIC/KEY**:

```text
Punta (tip, PTT/DIT) ------- contacto fijo
                                  /
Cuerpo (sleeve, GND) ------ contacto movil
Anillo (ring, MIC/DAH) ---- sin conectar y aislado
```

Es un contacto seco normalmente abierto, sin alimentación. Identificar con multímetro las
patillas del jack y el cable; no basarse en su posición física o colores.
Configurar **CW / straight key**, no pala iámbica. Conectar con la radio apagada.
Referencia: [pinout oficial DL2MAN](https://dl2man.de/wp-content/uploads/2021/12/image-61-1024x447.png).

## Aceptación

- Medir abierto en reposo y continuidad al pulsar en el extremo del cable; anillo aislado.
- Ensayar 100 pulsaciones sin radio: retorno, rodamientos, contactos, cable y retención de imanes.
- Probar transmisión supervisada con carga ficticia de 50 ohmios de potencia adecuada.
  Detenerse si se mantiene el cierre al soltar.

Digitalmente se validan ocho mallas cerradas/orientadas/de un componente y geometría conservada
al preparar/exportar. El montaje y funcionamiento físico siguen pendientes.

```bash
python src/prepare_dj9fm.py
python -m unittest discover -s src -p "test_*.py"
python src/render_previews.py
```
