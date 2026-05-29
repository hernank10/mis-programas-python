def identificar_palabras_agudas(fragmento_texto):
    # Dividir el fragmento de texto en palabras
    palabras = fragmento_texto.split()

    # Contador de palabras agudas sin tilde
    contador_palabras_sin_tilde = 0

    # Regla: Las palabras agudas terminadas en vocal, "n" o "s" deben llevar tilde.
    for palabra in palabras:
        if palabra[-1] in ['a', 'e', 'i', 'o', 'u', 'n', 's']:
            if palabra[-1] not in 'áéíóú':
                print(f"La palabra '{palabra}' debería llevar tilde.")
                contador_palabras_sin_tilde += 1

    return contador_palabras_sin_tilde

# Ejemplo de un artículo
articulo = """
En la actualidad, la tecnología juega un papel fundamental en nuestra vida diaria. 
La comunicación, la educación y el trabajo se han visto transformados por los avances tecnológicos.
Sin embargo, no todas las personas tienen acceso a estas herramientas. Es importante 
garantizar la igualdad de oportunidades en el uso de la tecnología.

El internet ha revolucionado la forma en que obtenemos información y nos comunicamos. 
Las redes sociales nos permiten conectar con personas de todo el mundo y compartir 
nuestras experiencias. No obstante, debemos ser conscientes de los riesgos asociados 
con la privacidad y la seguridad en línea.
"""

# Solicitar al usuario que identifique palabras agudas sin tilde
print("Identifique palabras agudas que deberían llevar tilde:")
palabras_sin_tilde = identificar_palabras_agudas(articulo)

if palabras_sin_tilde <= 5:
    print("¡Buen trabajo! Has identificado correctamente las palabras agudas sin tilde.")
else:
    print("Recuerda que solo debes permitir un máximo de cinco palabras agudas sin tilde.")
