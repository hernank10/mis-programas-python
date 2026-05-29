def mostrar_reglas(reglas, idioma):
  """Muestra cada regla por separado y permite al usuario reescribirla."""
  for i, regla in enumerate(reglas):
    print(f"Regla {i+1} ({idioma}): {regla}")
    respuesta = input("Escribe la regla nuevamente (o presiona Enter para continuar): ")
    if respuesta:
      print("Tu respuesta:", respuesta)

# Diccionario con las reglas ortográficas en español e inglés
reglas_ortograficas = {
  "b": {
    "es": [
      "Después de m: Siempre se escribe 'b' después de la letra 'm'.",
      # ... (agrega aquí las demás reglas de la "b" en español)
    ],
    "en": [
      "After m: You always write 'b' after the letter 'm'.",
      # ... (agrega aquí las demás reglas de la "b" en inglés)
    ]
  },
  # ... (agrega los diccionarios para las letras "v" y "w")
}

def main():
  idioma = input("¿En qué idioma deseas practicar? (español/inglés): ")
  while idioma not in ['español', 'inglés']:
    idioma = input("Opción inválida. Ingresa 'español' o 'inglés': ")

  letra = input(f"¿Quieres practicar las reglas de la 'b', 'v' o 'w' en {idioma}? ")
  while letra not in ['b', 'v', 'w']:
    letra = input("Opción inválida. Ingresa 'b', 'v' o 'w': ")

  reglas = reglas_ortograficas[letra][idioma[:2]]  # Toma las dos primeras letras del idioma
  mostrar_reglas(reglas, idioma)

if __name__ == "__main__":
  main()
