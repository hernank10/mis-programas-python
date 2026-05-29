def mostrar_reglas(reglas):
  """Muestra cada regla por separado y permite al usuario reescribirla."""
  for i, regla in enumerate(reglas):
    print(f"Regla {i+1}: {regla}")
    respuesta = input("Escribe la regla nuevamente (o presiona Enter para continuar): ")
    if respuesta:
      print("Tu respuesta:", respuesta)

# Diccionario con las reglas ortográficas
reglas_ortograficas = {
  "b": [
    "Después de m: Siempre se escribe 'b' después de la letra 'm'.",
    # ... (agrega aquí las demás reglas de la "b")
  ],
  "v": [
    "Después de n: Generalmente, después de la letra 'n' se escribe 'v'.",
    # ... (agrega aquí las demás reglas de la "v")
  ],
  "w": [
    "La letra 'w' es de origen extranjero y su uso en español es limitado.",
    # ... (agrega aquí las demás reglas de la "w")
  ]
}

# Función principal para iniciar el programa
def main():
  letra = input("¿Quieres practicar las reglas de la 'b', 'v' o 'w'? ")
  while letra not in ['b', 'v', 'w']:
    letra = input("Opción inválida. Ingresa 'b', 'v' o 'w': ")

  reglas = reglas_ortograficas[letra]
  mostrar_reglas(reglas)

if __name__ == "__main__":
  main()
