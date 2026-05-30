import random

def crear_frases(palabras, reglas):
  """Pide al usuario que cree frases con las palabras dadas, enfatizando las reglas ortográficas."""
  print("¡A crear frases divertidas! Utiliza las siguientes palabras y recuerda las reglas:")
  for palabra, regla in reglas.items():
    print(f"- {palabra}: {regla}")
  while True:
    frase = input("Escribe tu frase: ")
    if frase.lower() == "salir":
      break
    # Aquí puedes agregar una función para verificar si la frase cumple con las reglas
    print("¡Muy bien! Tu frase es:", frase)

def buscar_sinonimos(palabra, diccionario_sinonimos):
  """Busca sinónimos de una palabra en un diccionario predefinido."""
  if palabra in diccionario_sinonimos:
    print(f"Algunos sinónimos de '{palabra}' podrían ser:", ", ".join(diccionario_sinonimos[palabra]))
  else:
    print(f"No se encontraron sinónimos para '{palabra}' en la base de datos.")

def jugar_con_palabras(opcion):
  """Ofrece opciones para jugar con las palabras, enfocándose en las reglas ortográficas."""
  if opcion == "1":
    print("¡Intenta crear un trabalenguas usando palabras con 'll', 'y' o dígrafos!")
  elif opcion == "2":
    print("¡Intenta rimar palabras que contengan 'i' o 'y'!")
  elif opcion == "3":
    print("¡Inventa una adivinanza usando palabras con dígrafos!")
  # ... otras opciones

if __name__ == "__main__":
  palabras_iniciales = ["calle", "hoy", "miel", "rey", "muchacho"]
  reglas = {
      "calle": "La 'll' se usa al inicio de sílaba.",
      "hoy": "La 'y' se usa al final de sílaba.",
      # ... agregar más reglas
  }
  diccionario_sinonimos = {
      "calle": ["avenida", "vía"],
      "hoy": "ahora",
      # ... agregar más sinónimos
  }

  crear_frases(palabras_iniciales, reglas)
  palabra_a_buscar = input("¿De qué palabra te gustaría buscar sinónimos? ")
  buscar_sinonimos(palabra_a_buscar, diccionario_sinonimos)
  opcion = input("¿Qué quieres hacer? (1: trabalenguas, 2: rimas, 3: adivinanzas, 4: salir) ")
  jugar_con_palabras(opcion)
