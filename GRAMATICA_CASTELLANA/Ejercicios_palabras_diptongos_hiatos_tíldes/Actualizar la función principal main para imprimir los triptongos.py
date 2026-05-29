def main():
  """
  Función principal que pide al usuario 5 oraciones en español y luego muestra los
  diptongos y triptongos encontrados en cada palabra de cada oración.
  """

  oraciones = []
  for i in range(5):
    oracion = input("Ingrese una oración en español: ")
    oraciones.append(oracion)

  for oracion in oraciones:
    palabras = oracion.split()
    for palabra in palabras:
      diptongos = identificar_diptongos(palabra)
      if diptongos:
        print(f"Los diptongos y triptongos en la palabra '{palabra}' son: {diptongos}")


if __name__ == "__main__":
  main()
