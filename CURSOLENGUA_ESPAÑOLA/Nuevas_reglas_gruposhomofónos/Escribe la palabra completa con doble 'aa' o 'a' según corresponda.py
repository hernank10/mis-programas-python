import random

palabras_aa_fijas = ["Aaiún", "Isaac", "Aarón", "Caaguazú", "Caacupé", "Caazapá", "africaans"]
palabras_aa_variables = ["reactivar", "coactuar", "preanunciar", "autoaprendizaje", "aeroacústica"]  # Ejemplos de palabras con -aa- o -a-

def generar_ejercicio():
  tipo_palabra = random.choice(["fija", "variable"])
  if tipo_palabra == "fija":
    palabra = random.choice(palabras_aa_fijas)
    respuesta_correcta = palabra + "aa"
  else:
    palabra = random.choice(palabras_aa_variables)
    respuesta_correcta = palabra + "a"  # Ambas opciones son válidas en este caso
    print(f"Ambas opciones, '{palabra}aa' y '{palabra}a', son válidas.")

  respuesta = input(f"Escribe la palabra con doble 'aa' o 'a': {palabra}")

  if respuesta == respuesta_correcta or respuesta == palabra + "a":
    print("¡Correcto!")
  else:
    print(f"Incorrecto. Las opciones correctas son: {respuesta_correcta} o {palabra}a")

def main():
  print("¡Practica la escritura de palabras con doble 'aa' o 'a'!")
  while True:
    generar_ejercicio()
    continuar = input("¿Quieres continuar? (s/n): ")
    if continuar.lower() != "s":
      break

if __name__ == "__main__":
  main()
