import random

# ... (listas existentes para vocales)

palabras_cc_variables = ["euroccidental", "microorganismo", "sicorgánico", "inocuo"]

def generar_ejercicio():
  tipo_palabra = random.choice(["aa_fija", "aa_variable", "ee_variable", "ii_fija", "ii_variable", "oo_fija", "oo_variable", "cc_variable"])
  # ... (código existente para seleccionar palabras y generar respuestas)

  if tipo_palabra == "cc_variable":
    palabra = random.choice(palabras_cc_variables)
    respuesta_correcta = palabra.replace("cc", "c")  # Ambas opciones son válidas
    print(f"Ambas opciones, '{palabra}' y '{respuesta_correcta}', son válidas.")

  # ... (resto del código)

def main():
  # ... (código existente para la función principal)

if __name__ == "__main__":
  main()
