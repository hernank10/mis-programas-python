def concordancia_adjetivo_sustantivo(oracion):
    adj = oracion.split(" ")[0]
    sust = oracion.split(" ")[1]

    if adj.endswith("o") and sust.endswith("o"):
        return True
    elif adj.endswith("a") and sust.endswith("a"):
        return True
    else:
        return False

oracion = input("Ingrese una oración: ")

if concordancia_adjetivo_sustantivo(oracion):
    print("La concordancia entre el adjetivo y el sustantivo es correcta.")
else:
    print("La concordancia entre el adjetivo y el sustantivo es incorrecta.")
