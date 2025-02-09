# Detector de Doble Tecla
Algunas veces sucede que en nuestro teclado hay fallos en ciertas teclas, dejando de funcionar correctamente. Reemplazar un teclado completo puede ser costoso si solo una tecla presenta problemas. Este programa ofrece una solución permitiendo reasignar teclas defectuosas a otras teclas funcionales, evitando la necesidad de un reemplazo inmediato del hardware.

Este programa detecta cuando una tecla se presiona dos veces rápidamente y la reemplaza por otro carácter o palabra definida en los diccionarios de mapeo. Además, permite la ejecución de combinaciones de teclas como `Ctrl + C`, `Ctrl + V` y `Ctrl + Alt + →`.

## Características
- Detecta doble pulsación de teclas dentro de un intervalo de tiempo predefinido.
- Reemplaza caracteres individuales por otros definidos en el diccionario `mapa_teclas`.
- Reemplaza teclas por palabras completas usando `mapa_palabras`.
- Ejecuta combinaciones de teclas como copiar (`Ctrl + C`), pegar (`Ctrl + V`) y cambiar de ventana (`Ctrl + Alt + →`).
- Muestra un mensaje de estado cada minuto indicando que el programa sigue en ejecución.

## Requisitos
### Biblioteca
- Python 3.x
- `pynput`:
La biblioteca pynput se necesita en el script para escuchar las pulsaciones de teclas y controlar el teclado.

Para instalar `pynput`, ejecuta:
```sh
pip install pynput

```
Ejemplo:
- Presionar `g` dos veces rápidamente la reemplaza por `@gmail.com`.
- Presionar `a` dos veces rápidamente la reemplaza por `q`.
- Presionar `m` dos veces rápidamente ejecuta `Ctrl + Alt + →`.
- Presionar `c` dos veces rápidamente ejecuta `Ctrl + c`.

- `time`: 
La librería time se usa en el código para medir el tiempo entre pulsaciones de teclas y mostrar el estado cada minuto.

Para instalar `time`, ejecuta:
```sh
pip install time
```
- `threading`: 
El módulo `threading` se usa para ejecutar la función imprimir_estado en segundo plano, de modo que el programa pueda seguir escuchando las teclas presionadas sin bloquearse. No es necesario instalarlo, ya que es parte de la biblioteca estándar de Python.

## Personalización
Puedes modificar los diccionarios `mapa_teclas` y `mapa_palabras` para cambiar las teclas y palabras de reemplazo.

```python
mapa_teclas = {
    'a': 'q',
    'ñ': '?',
    's': 'Q'
}

mapa_palabras = {
    'g': "@gmail.com",
    'x': 'cap'
}
```

También puedes ajustar el tiempo de detección de doble pulsación modificando `intervalo_doble_pulsacion`.

```python
intervalo_doble_pulsacion = 0.3  # En segundos
```

## Ejecución
Para ejecutar el script:
```sh
python nombre_del_script.py
```

Presiona `Ctrl + C` en la terminal para detener la ejecución.

## Notas
- Este programa se ejecuta en segundo plano y captura todas las pulsaciones de teclado.
- No funciona en entornos donde `pynput` no tenga permisos suficientes.
- Puede interferir con otras aplicaciones si no se configura adecuadamente.

# Ejecutable para Windows

## Crear instalable
- pip install pyinstaller
- pyinstaller --onefile --noconsole remapeo.py

## Opciones:
-- onefile: crea un solo archivo ejecutable.
-- noconsole: oculta la ventana de la consola cuando se ejecuta el programa.

¡Diviértete automatizando tu escritura! 🚀