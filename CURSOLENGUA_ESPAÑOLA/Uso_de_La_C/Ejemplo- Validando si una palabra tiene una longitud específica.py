def termina_en_vocal(palabra):
  """Verifica si una palabra termina en vocal.

  Args:
    palabra: La palabra a evaluar.

  Returns:
    True si la palabra termina en vocal, False en caso contrario.
  """

  vocales = "aeiouáéíóú"
  return palabra[-1] in vocales
