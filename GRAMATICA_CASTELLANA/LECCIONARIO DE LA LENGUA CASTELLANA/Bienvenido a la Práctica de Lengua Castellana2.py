import random

# --- Datos de ejemplo para ejercicios ---
# Más adelante, estos datos vendrán de una base de datos o de archivos JSON
EJERCICIOS_DATA = {
    "Ortografía": {
        "Básico": {
            "Uso correcto de tildes": [
                {"pregunta": "¿Qué palabra necesita tilde: 'examen' o 'arbol'?", "tipo": "seleccion_multiple", "opciones": ["examen", "arbol"], "respuesta": "arbol", "explicacion": "Árbol lleva tilde porque es una palabra grave terminada en 'l'."},
                {"pregunta": "Completa con 'el' o 'él': '___ es mi amigo, y ___ perro es suyo.'", "tipo": "completar_oraciones", "respuesta": ["él", "el"], "explicacion": "'Él' es pronombre personal y 'el' es artículo."},
                {"pregunta": "Detecta el error: 'La cancion me gusto mucho.'", "tipo": "detectar_errores", "respuesta": {"palabra_erronea": "cancion", "correccion": "canción"}, "explicacion": "Canción lleva tilde por ser palabra aguda terminada en 'n'."},
            ],
            "Selección múltiple": [
                {"pregunta": "¿Cuál de las siguientes palabras está escrita correctamente?", "tipo": "seleccion_multiple", "opciones": ["vaca", "baca"], "respuesta": "vaca", "explicacion": "Vaca (animal) se escribe con 'v'."}
            ]
        },
        "Intermedio": {
            "Uso correcto de tildes": [
                {"pregunta": "¿Qué palabra necesita tilde: 'telefono' o 'mesa'?", "tipo": "seleccion_multiple", "opciones": ["telefono", "mesa"], "respuesta": "telefono", "explicacion": "Teléfono lleva tilde porque es una palabra esdrújula."},
                {"pregunta": "Completa con 'mas' o 'más': 'Quiero ___ tiempo para estudiar.'", "tipo": "completar_oraciones", "respuesta": ["más"], "explicacion": "'Más' lleva tilde cuando es adverbio de cantidad."},
            ]
        }
    },
    "Morfología": {
        "Básico": {
            "Clasificación de palabras": [
                {"pregunta": "Clasifica 'casa': ¿sustantivo, verbo o adjetivo?", "tipo": "seleccion_multiple", "opciones": ["sustantivo", "verbo", "adjetivo"], "respuesta": "sustantivo", "explicacion": "Casa es una palabra que nombra una cosa, por lo tanto es un sustantivo."},
            ],
            "Conjugación verbal": [
                {"pregunta": "Conjuga el verbo 'cantar' en presente, primera persona singular.", "tipo": "conjugacion_verbal", "respuesta": "canto", "explicacion": "Yo canto."},
            ]
        }
    },
    # ... Añadir más áreas, niveles y tipos de ejercicios
}

# --- Funciones Auxiliares ---

def limpiar_pantalla():
    """Limpia la consola."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_opcion_valida(prompt, opciones_validas):
    """
    Pide al usuario una opción y la valida contra una lista de opciones.
    Devuelve la opción seleccionada.
    """
    while True:
        try:
            seleccion = input(prompt).strip()
            if seleccion.isdigit():
                seleccion = int(seleccion)
                if seleccion in opciones_validas:
                    return seleccion
                else:
                    print("Opción inválida. Por favor, selecciona un número de la lista.")
            elif isinstance(opciones_validas[0], str) and seleccion.lower() in [op.lower() for op in opciones_validas]:
                return seleccion.capitalize() # Normalizar si son strings (ej. "Ortografía")
            else:
                print("Opción inválida. Por favor, ingresa una de las opciones mostradas.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

# --- Funciones de Tipos de Ejercicios ---

def ejecutar_seleccion_multiple(ejercicio):
    print(f"\nPregunta: {ejercicio['pregunta']}")
    for i, opcion in enumerate(ejercicio['opciones']):
        print(f"{i + 1}. {opcion}")
    
    opciones_num = list(range(1, len(ejercicio['opciones']) + 1))
    respuesta_usuario_idx = obtener_opcion_valida("Tu respuesta (número): ", opciones_num) - 1
    
    if ejercicio['opciones'][respuesta_usuario_idx].lower() == ejercicio['respuesta'].lower():
        print("¡Correcto! ✅")
        print(f"Explicación: {ejercicio['explicacion']}")
        return True
    else:
        print(f"Incorrecto. La respuesta correcta era: '{ejercicio['respuesta']}' ❌")
        print(f"Explicación: {ejercicio['explicacion']}")
        return False

def ejecutar_completar_oraciones(ejercicio):
    # Asume que las preguntas tienen ___ para el espacio en blanco
    # Y que las respuestas son una lista de strings en orden
    print(f"\nPregunta: {ejercicio['pregunta']}")
    user_inputs = []
    # Contar cuántos ___ hay en la pregunta para saber cuántas entradas pedir
    num_espacios = ejercicio['pregunta'].count('___')
    for i in range(num_espacios):
        user_input = input(f"Ingresa la palabra {i+1}: ").strip()
        user_inputs.append(user_input.lower())
    
    respuestas_correctas_normalizadas = [r.lower() for r in ejercicio['respuesta']]

    if user_inputs == respuestas_correctas_normalizadas:
        print("¡Correcto! ✅")
        print(f"Explicación: {ejercicio['explicacion']}")
        return True
    else:
        print(f"Incorrecto. La respuesta(s) correcta(s) era(n): '{' '.join(ejercicio['respuesta'])}' ❌")
        print(f"Explicación: {ejercicio['explicacion']}")
        return False

def ejecutar_detectar_errores(ejercicio):
    print(f"\nOración: {ejercicio['pregunta']}")
    palabra_detectada = input(f"¿Qué palabra está mal escrita? (Escribe la palabra): ").strip()
    correccion_sugerida = input(f"¿Cómo la corregirías? (Escribe la corrección): ").strip()

    if (palabra_detectada.lower() == ejercicio['respuesta']['palabra_erronea'].lower() and
        correccion_sugerida.lower() == ejercicio['respuesta']['correccion'].lower()):
        print("¡Correcto! ✅ Has detectado y corregido el error.")
        print(f"Explicación: {ejercicio['explicacion']}")
        return True
    else:
        print(f"Incorrecto. La palabra a corregir era '{ejercicio['respuesta']['palabra_erronea']}' y la corrección es '{ejercicio['respuesta']['correccion']}' ❌")
        print(f"Explicación: {ejercicio['explicacion']}")
        return False

def ejecutar_clasificacion_palabras(ejercicio):
    print(f"\nPregunta: {ejercicio['pregunta']}")
    user_input = input("Tu clasificación: ").strip()
    
    if user_input.lower() == ejercicio['respuesta'].lower():
        print("¡Correcto! ✅")
        print(f"Explicación: {ejercicio['explicacion']}")
        return True
    else:
        print(f"Incorrecto. La respuesta correcta era: '{ejercicio['respuesta']}' ❌")
        print(f"Explicación: {ejercicio['explicacion']}")
        return False

def ejecutar_conjugacion_verbal(ejercicio):
    print(f"\nPregunta: {ejercicio['pregunta']}")
    user_input = input("Tu conjugación: ").strip()

    if user_input.lower() == ejercicio['respuesta'].lower():
        print("¡Correcto! ✅")
        print(f"Explicación: {ejercicio['explicacion']}")
        return True
    else:
        print(f"Incorrecto. La conjugación correcta era: '{ejercicio['respuesta']}' ❌")
        print(f"Explicación: {ejercicio['explicacion']}")
        return False

# Diccionario para mapear tipos de ejercicio a sus funciones de ejecución
TIPOS_EJERCICIO_MAP = {
    "seleccion_multiple": ejecutar_seleccion_multiple,
    "completar_oraciones": ejecutar_completar_oraciones,
    "detectar_errores": ejecutar_detectar_errores,
    "clasificacion_de_palabras": ejecutar_clasificacion_palabras, # Asegurar que el nombre de la clave coincida con el tipo en EJERCICIOS_DATA
    "conjugacion_verbal": ejecutar_conjugacion_verbal,
    # TODO: Añadir funciones para: reescribir_frases, ordenar_oraciones, uso_correcto_de_tildes (si es distinto a selección/completar), identificacion_funciones_sintacticas, transformacion_oraciones
}

# --- Funciones del Menú Principal ---

def mostrar_menu_principal():
    """Muestra el menú principal y maneja la navegación."""
    limpiar_pantalla()
    print("✨ ¡Bienvenido a la Práctica de Lengua Castellana! ✨")
    print("--------------------------------------------------")
    print("1. Empezar a practicar")
    print("2. Salir")
    print("--------------------------------------------------")

    opcion = obtener_opcion_valida("Selecciona una opción: ", [1, 2])
    if opcion == 1:
        seleccionar_area()
    elif opcion == 2:
        print("¡Gracias por practicar! ¡Hasta pronto! 👋")
        exit()

def seleccionar_area():
    """Permite al usuario seleccionar un área del lenguaje."""
    limpiar_pantalla()
    print("\n📚 Selecciona un Área del Lenguaje:")
    areas = list(EJERCICIOS_DATA.keys())
    for i, area in enumerate(areas):
        print(f"{i + 1}. {area}")
    print("--------------------------------------------------")

    opcion_idx = obtener_opcion_valida("Selecciona un número de área: ", list(range(1, len(areas) + 1))) - 1
    area_seleccionada = areas[opcion_idx]
    seleccionar_nivel(area_seleccionada)

def seleccionar_nivel(area):
    """Permite al usuario seleccionar un nivel dentro del área."""
    limpiar_pantalla()
    print(f"\n🎯 Nivel para {area}:")
    niveles = list(EJERCICIOS_DATA[area].keys())
    for i, nivel in enumerate(niveles):
        print(f"{i + 1}. {nivel}")
    print("--------------------------------------------------")

    opcion_idx = obtener_opcion_valida("Selecciona un número de nivel: ", list(range(1, len(niveles) + 1))) - 1
    nivel_seleccionado = niveles[opcion_idx]
    seleccionar_tipo_ejercicio(area, nivel_seleccionado)

def seleccionar_tipo_ejercicio(area, nivel):
    """Permite al usuario seleccionar un tipo de ejercicio."""
    limpiar_pantalla()
    print(f"\n🧪 Tipos de Ejercicio para {area} - {nivel}:")
    tipos_ejercicios = list(EJERCICIOS_DATA[area][nivel].keys())
    for i, tipo in enumerate(tipos_ejercicios):
        print(f"{i + 1}. {tipo}")
    print("--------------------------------------------------")

    opcion_idx = obtener_opcion_valida("Selecciona un número de tipo de ejercicio: ", list(range(1, len(tipos_ejercicios) + 1))) - 1
    tipo_seleccionado = tipos_ejercicios[opcion_idx]
    ejecutar_ejercicios(area, nivel, tipo_seleccionado)

def ejecutar_ejercicios(area, nivel, tipo_ejercicio):
    """Ejecuta una serie de ejercicios del tipo seleccionado."""
    limpiar_pantalla()
    print(f"\n--- Iniciando Ejercicios de {tipo_ejercicio} ({area} - {nivel}) ---")
    ejercicios_disponibles = EJERCICIOS_DATA[area][nivel][tipo_ejercicio]
    
    if not ejercicios_disponibles:
        print("Lo siento, no hay ejercicios disponibles para esta selección. Regresando al menú principal.")
        input("Presiona Enter para continuar...")
        mostrar_menu_principal()
        return

    random.shuffle(ejercicios_disponibles) # Mezclar los ejercicios
    
    puntaje = 0
    total_preguntas = min(len(ejercicios_disponibles), 3) # Limitar a 3 preguntas por sesión para prueba

    for i in range(total_preguntas):
        ejercicio = ejercicios_disponibles[i]
        
        # Obtener la función de ejecución correcta
        ejecutor_funcion = TIPOS_EJERCICIO_MAP.get(ejercicio['tipo']) # 'tipo' es la clave interna del ejercicio

        if ejecutor_funcion:
            es_correcto = ejecutor_funcion(ejercicio)
            if es_correcto:
                puntaje += 1
            print("\n--------------------------------------------------")
            input("Presiona Enter para continuar con el siguiente ejercicio...")
            limpiar_pantalla()
        else:
            print(f"Error: Tipo de ejercicio '{ejercicio['tipo']}' no implementado aún.")
            print("\n--------------------------------------------------")
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
            
    print("\n--- ¡Sesión de Práctica Terminada! ---")
    print(f"Obtuviste {puntaje} de {total_preguntas} preguntas correctas.")
    print("¡Sigue practicando para mejorar! 💪")
    input("Presiona Enter para regresar al menú principal...")
    mostrar_menu_principal()

# --- Punto de entrada del programa ---
if __name__ == "__main__":
    mostrar_menu_principal()
