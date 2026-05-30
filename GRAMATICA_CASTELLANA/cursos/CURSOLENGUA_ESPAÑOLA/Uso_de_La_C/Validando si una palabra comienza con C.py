def comienza_con_c(palabra):
  """Verifica si una palabra comienza con la letra 'C'.

  Args:
    palabra: La palabra a evaluar.

  Returns:
    True si la palabra comienza con 'C', False en caso contrario.
  """

  return palabra[0] == 'C'

# Ejemplo de uso:
palabra = "casa"
if comienza_con_c(palabra):
  print("La palabra comienza con C.")
else:
  print("La palabra no comienza con C.")
