def cumple_reglas(palabra, reglas):
  """Verifica si una palabra cumple con todas las reglas.

  Args:
    palabra: La palabra a evaluar.
    reglas: Una lista de funciones de validación.

  Returns:
    True si la palabra cumple con todas las reglas, False en caso contrario.
  """

  for regla in reglas:
    if not regla(palabra):
      return False
  return True

# Ejemplo de uso:
reglas_a_aplicar = [comienza_con_c, termina_en_vocal]
palabra = "casa"
if cumple_reglas(palabra, reglas_a_aplicar):
  print("La palabra cumple todas las reglas.")
