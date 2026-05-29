def identificar_diptongos(palabra):
  """
  Función que identifica los diptongos y triptongos en una palabra en español.

  Args:
    palabra: La palabra en español a analizar.

  Returns:
    Una lista con los diptongos y triptongos encontrados en la palabra.
  """

  diptongos = []
  for i in range(len(palabra) - 2):
    # Si la vocal actual es débil y la siguiente es fuerte, y la siguiente a esa también es fuerte, se forma un triptongo.
    if palabra[i] in "iuy" and palabra[i + 1] in "aeiou" and palabra[i + 2] in "aeiou":
      diptongos.append(palabra[i] + palabra[i + 1] + palabra[i + 2])

    # Se mantienen las condiciones originales para identificar diptongos.
    if palabra[i] in "aeiou" and palabra[i + 1] in "iuy":
      diptongos.append(palabra[i] + palabra[i + 1])

    elif palabra[i] in "iuy" and palabra[i + 1] in "aeiou":
      diptongos.append(palabra[i] + palabra[i + 1])

  return diptongos
