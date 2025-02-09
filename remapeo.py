from pynput import keyboard
import time
import threading

# Variables para almacenar la última tecla presionada y el tiempo
ultima_tecla = None  # Última tecla presionada
ultimo_tiempo = 0  # Momento en que se presionó la última tecla

# Definir el tiempo máximo entre pulsaciones para detectar doble pulsación
intervalo_doble_pulsacion = 0.3  # En segundos

# Crear una instancia de Controller para simular eventos de teclado
controlador = keyboard.Controller()

# Diccionario para mapeo de teclas individuales
# Si una tecla se presiona dos veces rápidamente, será reemplazada
mapa_teclas = {
    'a': 'q',  # 'a' -> 'q'
    'ñ': '?',  # 'ñ' -> '?'
    's': 'Q'   # 's' -> 'Q'
}

# Diccionario para teclas que deben reemplazarse por palabras completas
mapa_palabras = {
    'g': "@gmail.com",  # 'g' -> "@gmail.com"
    'x': 'cap'  # 'x' -> "cap"
}

# Función que se ejecuta cuando se presiona una tecla
def al_presionar(tecla):
    """
    Captura la tecla presionada y detecta si se presiona dos veces en un intervalo corto.
    Si la tecla está en los diccionarios de mapeo, la reemplaza por el valor asignado.
    """
    global ultima_tecla, ultimo_tiempo

    try:
        tiempo_actual = time.time()

        # Verificar si se presionó la misma tecla dos veces rápidamente
        if tecla == ultima_tecla and (tiempo_actual - ultimo_tiempo) <= intervalo_doble_pulsacion:
            if tecla.char in mapa_teclas:
                # Borrar la primera letra presionada (simular backspace x2)
                controlador.press(keyboard.Key.backspace)
                controlador.release(keyboard.Key.backspace)
                controlador.press(keyboard.Key.backspace)
                controlador.release(keyboard.Key.backspace)

                # Simular la tecla reemplazada
                tecla_reemplazo = mapa_teclas[tecla.char]
                controlador.press(tecla_reemplazo)
                controlador.release(tecla_reemplazo)

                print(f"Cambiando {tecla.char} por {tecla_reemplazo}")

            elif tecla.char in mapa_palabras:
                # Borrar la primera letra presionada (simular backspace x2)
                controlador.press(keyboard.Key.backspace)
                controlador.release(keyboard.Key.backspace)
                controlador.press(keyboard.Key.backspace)
                controlador.release(keyboard.Key.backspace)

                # Escribir la palabra completa
                palabra_reemplazo = mapa_palabras[tecla.char]
                controlador.type(palabra_reemplazo)

                print(f"Cambiando {tecla.char} por '{palabra_reemplazo}'")

            elif tecla.char == 'c':
                # Simular Ctrl + C (copiar)
                with controlador.pressed(keyboard.Key.ctrl):
                    controlador.press('c')
                    controlador.release('c')
                print("Ejecutando Ctrl+C")

            elif tecla.char == 'v':
                # Borrar la primera 'v' escrita antes de pegar
                controlador.press(keyboard.Key.backspace)
                controlador.release(keyboard.Key.backspace)
                controlador.press(keyboard.Key.backspace)
                controlador.release(keyboard.Key.backspace)
                controlador.press(keyboard.Key.backspace)
                controlador.release(keyboard.Key.backspace)

                # Simular Ctrl + V (pegar)
                with controlador.pressed(keyboard.Key.ctrl):
                    controlador.press('v')
                    controlador.release('v')
                print("Ejecutando Ctrl+V")

            elif tecla.char == 'm':
                # Simular Ctrl + Alt + Flecha Derecha
                with controlador.pressed(keyboard.Key.ctrl_l):
                    with controlador.pressed(keyboard.Key.alt):
                        controlador.press(keyboard.Key.right)
                        controlador.release(keyboard.Key.right)
                print("Ejecutando Ctrl+Alt+→")

            # Resetear las variables para evitar duplicación
            ultima_tecla = None
            return  # No continuar procesando la segunda tecla
        else:
            # Actualizar la última tecla presionada y el tiempo
            ultima_tecla = tecla
            ultimo_tiempo = tiempo_actual

    except AttributeError:
        # Para las teclas especiales (Ctrl, Shift, etc.), no hacer nada
        pass

# Función que imprime "En ejecución" cada minuto
conteo_ejecucion = 0

def imprimir_estado():
    """
    Imprime un mensaje cada minuto indicando que el programa sigue en ejecución.
    """
    global conteo_ejecucion
    while True:
        conteo_ejecucion += 1
        print("En ejecución...", conteo_ejecucion, "min")
        time.sleep(60)

# Crear un hilo para la función imprimir_estado, de modo que se ejecute en segundo plano
hilo_estado = threading.Thread(target=imprimir_estado, daemon=True)
hilo_estado.start()

# Iniciar la escucha de teclas
with keyboard.Listener(on_press=al_presionar) as oyente:
    oyente.join()
