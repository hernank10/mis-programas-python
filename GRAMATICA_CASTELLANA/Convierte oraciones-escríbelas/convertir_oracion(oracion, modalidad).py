def convertir_oracion(oracion, modalidad):
    if modalidad == 'interrogativa':
        return convertir_a_interrogativa(oracion)
    elif modalidad == 'imperativa':
        return convertir_a_imperativa(oracion)
    elif modalidad == 'exclamativa':
        return convertir_a_exclamativa(oracion)
    elif modalidad == 'desiderativa':
        return convertir_a_desiderativa(oracion)
    elif modalidad == 'dubitativa':
        return convertir_a_dubitativa(oracion)
    else:
        return oracion  # Por defecto, se devuelve la oración sin cambios

def convertir_a_interrogativa(oracion):
    if oracion.endswith('.'):
        return oracion[:-1] + '?'
    else:
        return oracion + '?'

def convertir_a_imperativa(oracion):
    # Un simple cambio a imperativa: comienza con un verbo
    palabras = oracion.split()
    if palabras[0].lower() in ["puede", "debes", "haz", "deberías"]:
        return oracion
    return "Haz " + " ".join(palabras).lower()

def convertir_a_exclamativa(oracion):
    return f"¡{oracion}!"

def convertir_a_desiderativa(oracion):
    return f"Ojalá {oracion}"

def convertir_a_dubitativa(oracion):
    return f"Tal vez {oracion}"

def menu():
    oracion = input("Escribe la oración: ")
    print("Selecciona la modalidad a la que deseas convertir la oración:")
    print("1. Interrogativa")
    print("2. Imperativa")
    print("3. Exclamativa")
    print("4. Desiderativa")
    print("5. Dubitativa")
    
    opcion = input("Opción: ")
    
    modalidades = {
        "1": "interrogativa",
        "2": "imperativa",
        "3": "exclamativa",
        "4": "desiderativa",
        "5": "dubitativa"
    }
    
    modalidad = modalidades.get(opcion, None)
    
    if modalidad:
        oracion_convertida = convertir_oracion(oracion, modalidad)
        print(f"Oración convertida: {oracion_convertida}")
    else:
        print("Opción inválida. Inténtalo de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    while True:
        menu()
        continuar = input("¿Quieres convertir otra oración? (s/n): ")
        if continuar.lower() != 's':
            break
