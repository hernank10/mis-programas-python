import random

palabras_aa_fijas = ["Aaiún", "Isaac", "Aarón", "Caaguazú", "Caacupé", "Caazapá", "africaans"]
palabras_aa_variables = ["reactivar", "coactuar", "preanunciar", "autoaprendizaje", "aeroacústica"]
palabras_ee_variables = ["relegir", "remplazar", "restrenar", "preestreno", "sobresdrújulo", "rembolsar", "reencontrar", "reestructurar", "sobrentender", "teledocación"]

def generar_ejercicio():
  tipo_palabra = random.choice(["fija", "aa_variable", "ee_variable"])
  if tipo_palabra == "fija":
    palabra = random.choice(palabras_aa_fijas)
    respuesta_correcta = palabra + "aa"
  elif tipo_palabra == "aa_variable":
    palabra = random.choice(palabras_aa_variables)
    respuesta_correcta = palabra + "a"  # Ambas opciones son válidas
    print(f"Ambas opciones, '{palabra}aa' y '{palabra}a', son válidas.")
  else:
    palabra = random.choice(palabras_ee_variables)
    respuesta_correcta = palabra + "e"  # Ambas opciones son válidas
    print(f"Ambas opciones, '{palabra}ee' y '{palabra}e', son válidas.")

  respuesta = input(f"Escribe la palabra con doble 'aa', 'ee' o 'a', 'e': {palabra}")

  if respuesta == respuesta_correcta or respuesta in [palabra + "a", palabra + "e"]:
    print("¡Correcto!")
  else:
    print(f"Incorrecto. Las opciones correctas son: {respuesta_correcta}, {palabra}a o {palabra}e")

def main():
  print("¡Practica la escritura de palabras con doble 'aa', 'ee' o 'a', 'e'!")
  while True:
    generar_ejercicio()
    continuar = input("¿Quieres continuar? (s/n): ")
    if continuar.lower() != "s":
      break

if __name__ == "__main__":
  main()
