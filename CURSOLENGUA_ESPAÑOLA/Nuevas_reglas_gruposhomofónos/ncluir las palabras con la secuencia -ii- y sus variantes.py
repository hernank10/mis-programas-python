import random

palabras_aa_fijas = ["Aaiún", "Isaac", "Aarón", "Caaguazú", "Caacupé", "Caazapá", "africaans"]
palabras_aa_variables = ["reactivar", "coactuar", "preanunciar", "autoaprendizaje", "aeroacústica"]
palabras_ee_variables = ["relegir", "remplazar", "restrenar", "preestreno", "sobresdrújulo", "rembolsar", "reencontrar", "reestructurar", "sobrentender", "teledocación"]
palabras_ii_fijas = ["chií", "chiísmo", "chiita", "priista", "Rociíto", "friísimo", "impiísima"]
palabras_ii_variables = ["antimperialismo", "antincendio", "antiinflacionario", "antiinflamatorio", "mininvestigación", "multinstitucional", "plurideológico", "seminconsciente"]

def generar_ejercicio():
  tipo_palabra = random.choice(["aa_fija", "aa_variable", "ee_variable", "ii_fija", "ii_variable"])
  if tipo_palabra == "aa_fija":
    # ... (código existente para palabras con -aa- fijas)
  elif tipo_palabra == "aa_variable":
    # ... (código existente para palabras con -aa- variables)
  elif tipo_palabra == "ee_variable":
    # ... (código existente para palabras con -ee- variables)
  elif tipo_palabra == "ii_fija":
    palabra = random.choice(palabras_ii_fijas)
    respuesta_correcta = palabra + "ii"
  else:  # ii_variable
    palabra = random.choice(palabras_ii_variables)
    respuesta_correcta = palabra + "i"  # Ambas opciones son válidas
    print(f"Ambas opciones, '{palabra}ii' y '{palabra}i', son válidas.")

  respuesta = input(f"Escribe la palabra con doble 'aa', 'ee', 'ii' o 'a', 'e', 'i': {palabra}")

  # ... (código existente para verificar la respuesta)

def main():
  # ... (código existente para la función principal)

if __name__ == "__main__":
  main()
