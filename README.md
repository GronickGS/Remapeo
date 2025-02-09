# Detector de Doble Tecla

Este programa detecta cuando una tecla se presiona dos veces rápidamente y la reemplaza por otro carácter o palabra definida en los diccionarios de mapeo. Además, permite la ejecución de combinaciones de teclas como `Ctrl + C`, `Ctrl + V` y `Ctrl + Alt + →`.

## Características
- Detecta doble pulsación de teclas dentro de un intervalo de tiempo predefinido.
- Reemplaza caracteres individuales por otros definidos en el diccionario `mapa_teclas`.
- Reemplaza teclas por palabras completas usando `mapa_palabras`.
- Ejecuta combinaciones de teclas como copiar (`Ctrl + C`), pegar (`Ctrl + V`) y cambiar de ventana (`Ctrl + Alt + →`).
- Muestra un mensaje de estado cada minuto indicando que el programa sigue en ejecución.

## Requisitos
- Python 3.x
- Biblioteca `pynput`

Para instalar `pynput`, ejecuta:
```sh
pip install pynput
```

## Uso
Ejecuta el script y empieza a escribir. Si presionas dos veces una tecla dentro del tiempo establecido, se reemplazará según la configuración.

Ejemplo:
- Presionar `g` dos veces rápidamente la reemplaza por `@gmail.com`.
- Presionar `a` dos veces rápidamente la reemplaza por `q`.
- Presionar `m` dos veces rápidamente ejecuta `Ctrl + Alt + →`.

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

# EXE Windows

## Libreria usada
pip install pynput

## Crear instalable
pip install pyinstaller
pyinstaller --onefile --noconsole remapeo.py

## Opciones:
-- onefile: crea un solo archivo ejecutable.
-- noconsole: oculta la ventana de la consola cuando se ejecuta el programa.

¡Diviértete automatizando tu escritura! 🚀