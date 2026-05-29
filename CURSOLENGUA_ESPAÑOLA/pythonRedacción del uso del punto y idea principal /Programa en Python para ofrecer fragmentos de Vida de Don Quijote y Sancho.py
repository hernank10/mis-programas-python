import random

def leer_fragmento(archivo, numero_fragmento):
  """
  Lee un fragmento aleatorio del archivo especificado.

  Args:
    archivo: El nombre del archivo a leer.
    numero_fragmento: El número del fragmento que se desea leer.

  Returns:
    El texto del fragmento especificado.
  """

  with open(archivo, "r") as f:
    lineas = f.readlines()

  fragmento = lineas[numero_fragmento - 1]

  return fragmento

def mostrar_fragmento(fragmento):
  """
  Muestra un fragmento de texto en la consola.

  Args:
    fragmento: El texto del fragmento que se desea mostrar.
  """

  print(fragmento)

def analizar_fragmento(fragmento):
  """
  Analiza un fragmento de texto y solicita al usuario que observe cómo la idea principal crece a lo largo de los párrafos y cómo cada uno de ellos contiene un abordaje o aspecto distinto.

  Args:
    fragmento: El texto del fragmento que se desea analizar.
  """

  print("**Análisis del fragmento**")

  # Solicitar al usuario que observe cómo la idea principal crece a lo largo de los párrafos.
  print("Observe cómo la idea principal crece a lo largo de los párrafos.")
  print("¿Cómo se desarrolla la idea principal en cada párrafo?")

  # Solicitar al usuario que observe cómo cada párrafo contiene un abordaje o aspecto distinto.
  print("Observe cómo cada párrafo contiene un abordaje o aspecto distinto.")
  print("¿Qué aspectos diferentes se abordan en cada párrafo?")

  # Solicitar al usuario que relea el fragmento y escriba la idea principal.
  print("Relea el fragmento y escriba la idea principal.")
  idea_principal = input("Idea principal: ")

  # Solicitar al usuario que reflexione acerca del uso del punto y seguido y del punto y aparte.
  print("Reflexione acerca del uso del punto y seguido y del punto y aparte.")
  print("¿Cómo contribuyen estos signos de puntuación a la organización y comprensión del texto?")

def main():
  """
  Función principal del programa.
  """

  # Leer el archivo de texto.
  archivo = "Vida_de_Don_Quijote_y_Sancho.txt"

  # Solicitar al usuario el número del fragmento que desea leer.
  numero_fragmento = int(input("Ingrese el número del fragmento que desea leer: "))

  # Leer el fragmento especificado.
  fragmento = leer_fragmento(archivo, numero_fragmento)

  # Mostrar el fragmento en la consola.
  mostrar_fragmento(fragmento)

  # Analizar el fragmento.
  analizar_fragmento(fragmento)

if __name__ == "__main__":
  main()
