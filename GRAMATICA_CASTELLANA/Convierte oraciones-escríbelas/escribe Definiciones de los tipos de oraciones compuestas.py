# Definiciones de los tipos de oraciones compuestas
tipos_oracion_compuesta = {
    "yuxtapuesta": "Son oraciones unidas sin nexos, separadas por comas, punto y coma, o dos puntos ('Llegué temprano estaba todo cerrado.'). Ejemplo: 'Llegué temprano, estaba todo cerrado.'",
    "coordinada_copulativa": "Las oraciones están unidas por nexos como 'y', 'e' o 'ni'(Juan estudia  Pedro trabaja.). Ejemplo: 'Juan estudia y Pedro trabaja.'",
    "coordinada_disyuntiva": "Las oraciones están unidas por nexos como 'o' u 'o bien'(Puedes venir _ quedarte en casa). Ejemplo: 'Puedes venir o quedarte en casa.'",
    "coordinada_adversativa": "Las oraciones expresan ideas opuestas, unidas por nexos como 'pero', 'sin embargo', 'aunque'(Estudió mucho, __ no aprobó.). Ejemplo: 'Estudió mucho, pero no aprobó.'",
    "coordinada_distributiva": "Las oraciones se alternan, unidas por nexos como 'ya... ya', 'bien... bien'(Bien estudia, __ trabaja, siempre está ocupado.). Ejemplo: 'Bien estudia, bien trabaja, siempre está ocupado.'",
    "subordinada_sustantiva": "La oración subordinada funciona como un sustantivo dentro de la principal(Dijo que vendría _ la fie _sta.). Ejemplo: 'Dijo que vendría a la fiesta.'",
    "subordinada_adjetiva": "La oración subordinada funciona como un adjetivo y complementa a un sustantivo de la oración principal (El coche que compré es rojo.). Ejemplo: 'El coche que compré es rojo.'",
    "subordinada_adverbial": "La oración subordinada funciona como un adverbio dentro de la oración principal (Cuando llegues avísame.). Ejemplo: 'Cuando llegues, avísame.'",
    "subordinada_causal": "Indica la causa o el motivo de la oración principal (No salió ____ estaba lloviendo.). Ejemplo: 'No salió porque estaba lloviendo.'",
    "subordinada_condicional": "Expresa una condición para que se realice la oración principal (Si estudias  aprobarás el examen.). Ejemplo: 'Si estudias, aprobarás el examen.'"
}

# Función para verificar la oración del usuario
def verificar_oracion(tipo, oracion_usuario):
    ejemplo_correcto = tipos_oracion_compuesta[tipo].split("Ejemplo: ")[1].strip()
    if oracion_usuario.strip().lower() == ejemplo_correcto.lower():
        return True
    return False

def menu():
    print("Bienvenido al programa de clasificación de oraciones compuestas.\n")
    
    # Presenta las opciones de clasificación de oraciones
    print("Selecciona el tipo de oración compuesta que deseas practicar:")
    for idx, tipo in enumerate(tipos_oracion_compuesta, 1):
        print(f"{idx}. {tipo.replace('_', ' ').capitalize()}")
    
    opcion = input("\nElige una opción (1-10): ")
    
    # Valida la opción seleccionada
    tipos_disponibles = list(tipos_oracion_compuesta.keys())
    if opcion.isdigit() and 1 <= int(opcion) <= len(tipos_disponibles):
        tipo_seleccionado = tipos_disponibles[int(opcion) - 1]
        definicion = tipos_oracion_compuesta[tipo_seleccionado]
        
        # Muestra la definición del tipo seleccionado
        print(f"\nHas seleccionado: {tipo_seleccionado.replace('_', ' ').capitalize()}")
        print(f"Definición: {definicion.split('Ejemplo: ')[0].strip()}")
        
        # Solicita al usuario que escriba su propia oración basada en la definición
        oracion_usuario = input("\nEscribe un ejemplo de este tipo de oración: ")
        
        # Verifica si la oración es correcta
        if verificar_oracion(tipo_seleccionado, oracion_usuario):
            print("¡Correcto! Has escrito la oración correctamente.")
        else:
            print(f"La oración no coincide con el ejemplo esperado. Aquí tienes un ejemplo correcto:\n{tipos_oracion_compuesta[tipo_seleccionado].split('Ejemplo: ')[1]}")
    
    else:
        print("Opción inválida. Inténtalo de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    while True:
        menu()
        continuar = input("\n¿Quieres practicar con otra oración? (s/n): ")
        if continuar.lower() != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
