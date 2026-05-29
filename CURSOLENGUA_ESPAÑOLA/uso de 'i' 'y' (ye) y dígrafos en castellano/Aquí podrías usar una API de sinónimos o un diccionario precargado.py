import random

def crear_frases(palabras):
  """Pide al usuario que cree frases con las palabras dadas."""
  print("¡A crear frases divertidas! Utiliza las siguientes palabras:")
  print(palabras)
  while True:
    frase = input("Escribe tu frase: ")
    if frase.lower() == "salir":
      break
    print("¡Muy bien! Tu frase es:", frase)

def buscar_sinonimos(palabra):
  """Simula la búsqueda de sinónimos (puedes usar una API real)."""
  print(f"Buscando sinónimos de '{palabra}'...")
  # Aquí podrías usar una API de sinónimos o un diccionario precargado
  sinonimos = ["otro", "diferente", "distinto", "semejante"]  # Ejemplo básico
  print("Algunos sinónimos podrían ser:", ", ".join(sinonimos))

def jugar_con_palabras():
  """Ofrece opciones para jugar con las palabras."""
  print("¡Vamos a jugar con las palabras!")
  while True:
    opcion = input("Elige una opción:\n1. Crear un trabalenguas\n2. Crear una rima\n3. Crear una adivinanza\n4. Salir\n")
    if opcion == "1":
      print("¡Intenta crear un trabalenguas! Por ejemplo: 'Tres tristes tigres tragaban trigo en un trigal.'")
    elif opcion == "2":
      print("¡Intenta rimar! Por ejemplo: 'El perro corre, el gato maúlla.'")
    elif opcion == "3":
      print("¡Inventa una adivinanza! Por ejemplo: 'Tiene cuello pero no cabeza, tiene cuerpo pero no pies. ¿Qué es?'")
    elif opcion == "4":
      break
    else:
      print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
  palabras_iniciales = ["gato", "perro", "casa", "sol", "luna"]
  crear_frases(palabras_iniciales)
  palabra_a_buscar = input("¿De qué palabra te gustaría buscar sinónimos? ")
  buscar_sinonimos(palabra_a_buscar)
  jugar_con_palabras()
