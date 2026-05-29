import random

# ... (listas existentes para -aa-, -ee-, -ii-)

palabras_oo_fijas = ["zoo", "zoófago", "zoología", "zooplancton", "azoospermia", "epizootia", "espermatozoo", "protozoo", "bioxidación", "biooceánico"]
palabras_oo_variables = ["autobservación", "macroperación", "proccidental"]

def generar_ejercicio():
  tipo_palabra = random.choice(["aa_fija", "aa_variable", "ee_variable", "ii_fija", "ii_variable", "oo_fija", "oo_variable"])
  # ... (código existente para seleccionar palabras y generar respuestas)

  if tipo_palabra == "oo_fija":
    palabra = random.choice(palabras_oo_fijas)
    respuesta_correcta = palabra + "oo"
  elif tipo_palabra == "oo_variable":
    palabra = random.choice(palabras_oo_variables)
    respuesta_correcta = palabra + "o"  # Ambas opciones son válidas
    print(f"Ambas opciones, '{palabra}oo' y '{palabra}o', son válidas.")

  # ... (resto del código)

def main():
  # ... (código existente para la función principal)

if __name__ == "__main__":
  main()
