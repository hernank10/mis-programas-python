def identificar_diptongos(palabra):
  """
  Función que identifica los diptongos en una palabra en español.

  Args:
    palabra: La palabra en español a analizar.

  Returns:
    Una lista con los diptongos encontrados en la palabra.
  """

  diptongos = []
  for i in range(len(palabra) - 1):
    # Si la vocal actual es fuerte y la siguiente es débil, se forma un diptongo.
    if palabra[i] in "aeiou" and palabra[i + 1] in "iuy":
      diptongos.append(palabra[i] + palabra[i + 1])

    # Si la vocal actual es débil y la siguiente es fuerte, también se forma un diptongo.
    elif palabra[i] in "iuy" and palabra[i + 1] in "aeiou":
      diptongos.append(palabra[i] + palabra[i + 1])

  return diptongos


def main():
  """
  Función principal que pide al usuario 5 oraciones en español y luego muestra los
  diptongos encontrados en cada palabra de cada oración.
  """

  oraciones = []
  for i in range(5):
    oracion = input("Ingrese una oración en español: ")
    oraciones.append(oracion)

  for oracion in oraciones:
    palabras = oracion.split()
    for palabra in palabras:
      diptongos = identificar_diptongos(palabra)
      print(f"Los diptongos en la palabra '{palabra}' son: {diptongos}")


if __name__ == "__main__":
  main()
