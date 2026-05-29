import re

def contiene_vocal(palabra):
  """Verifica si una palabra contiene al menos una vocal.

  Args:
    palabra: La palabra a evaluar.

  Returns:
    True si la palabra contiene al menos una vocal, False en caso contrario.
  """

  return bool(re.search('[aeiouáéíóú]', palabra))
