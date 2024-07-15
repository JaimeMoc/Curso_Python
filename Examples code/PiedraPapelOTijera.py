# Programa básico que simula el Juego: Piedra, papel o tijera.
# Día 1, practicando Python.
# Jaime Alberto Suarez Moctezuma.

# Importación de la líbreria Random.
import random

# Definición de las posibles opciones a seleccionar.
opciones = ["tijera", "papel", "piedra"]

# Lectura de la opci+on del usuario.
usuario = input("Elige una opción (piedra, papel, tijera): ").lower()
computadora = random.choice(opciones) # Se genera la opción de la computadora.

# Ciclo If que se anticipa ante una respuesta incorrecta.
if usuario not in opciones:
    print("Error.")
    quit()

# Ciclo If que define las reglas del juego.
if usuario == computadora:
    print(computadora)
    print("Ha sido un empate!!!")
elif usuario == "tijera" and computadora == "piedra" or usuario == "papel" and computadora == "tijera" and usuario == "piedra" and computadora =="papel":
    print(computadora)
    print("Haz perdido!!!")
else:
    print(computadora)
    print("Haz ganado!!!")