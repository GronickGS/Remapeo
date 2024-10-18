from pynput import keyboard
import time

# Variables para almacenar la última tecla presionada y el tiempo
last_key = None
last_time = 0

# Definir el tiempo máximo entre pulsaciones para detectar doble clic
double_press_interval = 0.3  # En segundos

# Crear una instancia de Controller
controller = keyboard.Controller()

# Diccionario para mapeo de teclas
key_map = {
  'a': 'q', # Cambiar 'r' por 'y'
  's': 'w',  # Cambiar 'a' por 'b'
  'd': 'e',
  'f': 'r',
  'j': 'u',
  'k': 'i',
  'l': 'o',
  'ñ': 'p' 
  }

# Función que se ejecuta cuando se presiona una tecla
def on_press(key):
    global last_key, last_time

    try:
        current_time = time.time()

        # Verificar si se presionó la misma tecla dos veces rápidamente
        if key == last_key and (current_time - last_time) <= double_press_interval:
            # Verificar si la tecla está en el mapeo
            if key.char in key_map:
                # Borrar la primera letra presionada (simular backspace)
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)

                # Simular la tecla reemplazada
                replacement_key = key_map[key.char]
                controller.press(replacement_key)
                controller.release(replacement_key)
                
                # Resetear las variables para evitar duplicación
                last_key = None
                return  # No continuar procesando la segunda tecla

        else:
            # Actualizar la última tecla presionada y el tiempo
            last_key = key
            last_time = current_time

    except AttributeError:
        # Para las teclas especiales (Ctrl, Shift, etc.)
        pass

# Función que se ejecuta cuando se suelta una tecla (no se necesita implementar nada aquí)
def on_release(key):
    pass

# Iniciar la escucha de teclas
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
