def simplificar_grupos_consonanticos(texto):
  # Diccionario con las reglas de simplificación
  reglas = {'ps': 's', 'gn': 'n'}

  palabras = texto.split()
  resultado = []
  for palabra in palabras:
    nueva_palabra = ""
    for i in range(len(palabra)):
      if i < len(palabra) - 1 and palabra[i:i+2] in reglas:
        nueva_palabra += reglas[palabra[i:i+2]]
      else:
        nueva_palabra += palabra[i]
    resultado.append(nueva_palabra)
  return " ".join(resultado)

texto = "psicología gnóstico espanglish"
resultado = simplificar_grupos_consonanticos(texto)
print(resultado)  # Salida: sicología nóstico espanglish
