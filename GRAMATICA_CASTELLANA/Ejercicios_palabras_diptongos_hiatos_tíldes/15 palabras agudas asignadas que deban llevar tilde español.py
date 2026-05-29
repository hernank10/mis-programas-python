def identificar_palabras_agudas(palabras_agudas):
    # Contador de palabras agudas sin tilde
    contador_palabras_sin_tilde = 0

    # Regla: Las palabras agudas terminadas en vocal, "n" o "s" deben llevar tilde.
    for palabra in palabras_agudas:
        if palabra[-1] in ['a', 'e', 'i', 'o', 'u', 'n', 's']:
            if palabra[-1] not in 'áéíóú':
                print(f"La palabra '{palabra}' debería llevar tilde.")
                contador_palabras_sin_tilde += 1

    return contador_palabras_sin_tilde

# Palabras agudas asignadas para evaluar
palabras_agudas_evaluar = ["cafes", "perdiz", "lapiz", "hospital", "ciudad", "atras", "camion", "domingos", "canal", "espanol", "papel", "cancion", "ruido", "sofa", "joven"]

# Solicitar al usuario que identifique palabras agudas que deberían llevar tilde
print("Identifica las palabras agudas que deberían llevar tilde:")
palabras_sin_tilde = identificar_palabras_agudas(palabras_agudas_evaluar)

if palabras_sin_tilde == 0:
    print("¡Excelente! Todas las palabras agudas están correctamente tildadas.")
elif palabras_sin_tilde <= 5:
    print(f"Has identificado {palabras_sin_tilde} palabras agudas sin tilde. Recuerda que deberían llevar tilde.")
else:
    print("Recuerda que solo debes permitir un máximo de cinco palabras agudas sin tilde.")
