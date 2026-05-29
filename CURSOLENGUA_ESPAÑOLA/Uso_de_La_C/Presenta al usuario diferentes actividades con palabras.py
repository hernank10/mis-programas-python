import random

def actividades_con_palabras():
  """Presenta al usuario diferentes actividades con palabras."""

  print("¡Vamos a jugar con las palabras! Elige una opción:")
  print("1. Inventa frases divertidas")
  print("2. Busca sinónimos")
  print("3. Crea trabalenguas, rimas o adivinanzas")

  opcion = input("Selecciona una opción (1, 2 o 3): ")

  if opcion == '1':
    lista_palabras = ["gato", "perro", "casa", "sol", "luna"]
    print("Utiliza estas palabras:", lista_palabras)
    print("¡Inventa una frase divertida usando al menos una de ellas!")
  elif opcion == '2':
    palabra = input("Escribe una palabra: ")
    print("Busca sinónimos de", palabra, ". ¡Puedes usar un diccionario o tu imaginación!")
  elif opcion == '3':
    print("¡Pon a prueba tu creatividad! Crea un trabalenguas, una rima o una adivinanza.")
  else:
    print("Opción inválida. Por favor, elige 1, 2 o 3.")

actividades_con_palabras()
