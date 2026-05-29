def identificar_palabras_esdrujulas_en_texto(fragmento_texto):
    # Dividir el fragmento de texto en palabras
    palabras = fragmento_texto.split()

    # Palabras esdrújulas asignadas para evaluar
    palabras_esdrujulas_evaluar = ["música", "cántaro", "médico", "héroe", "fácil", "rápido", "débil", "lápiz", "mágico", "móvil", "género", "fórceps", "público", "cóctel", "fútbol"]

    # Contador de palabras esdrújulas sin tilde
    contador_palabras_sin_tilde = 0

    # Regla: Todas las palabras esdrújulas deben llevar tilde.
    for palabra in palabras:
        # Limpiar la palabra de puntuación
        palabra = palabra.strip('.,!?()[]{}":;')

        if palabra.lower() in palabras_esdrujulas_evaluar:
            if palabra[-1] not in 'áéíóú':
                print(f"La palabra '{palabra}' debería llevar tilde.")
                contador_palabras_sin_tilde += 1

    return contador_palabras_sin_tilde

# Ejemplo de un artículo
articulo = """
La música es una expresión artística que ha existido a lo largo de la historia. 
El médico trató al paciente con cuidado y profesionalismo. 
La rapidez con la que resolvieron el problema fue sorprendente. 
La técnica utilizada en la construcción del edificio fue innovadora.
El público disfrutó del espectáculo de principio a fin.
"""

# Solicitar al usuario que identifique palabras esdrújulas en el fragmento de texto
print("Identifica las palabras esdrújulas que deberían llevar tilde:")
palabras_sin_tilde = identificar_palabras_esdrujulas_en_texto(articulo)

if palabras_sin_tilde == 0:
    print("¡Excelente! Todas las palabras esdrújulas están correctamente tildadas.")
elif palabras_sin_tilde <= 15:
    print(f"Has identificado {palabras_sin_tilde} palabras esdrújulas sin tilde. Recuerda que deberían llevar tilde.")
else:
    print("Recuerda que solo debes permitir un máximo de quince palabras esdrújulas sin tilde.")
