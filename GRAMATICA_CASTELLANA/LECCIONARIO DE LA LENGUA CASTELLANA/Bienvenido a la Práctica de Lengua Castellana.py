import random
import os

# --- Datos de ejemplo para ejercicios ---
# La estructura ha cambiado ligeramente para ser más flexible con las respuestas.
# Ahora la "respuesta" puede ser un string, una lista o un diccionario.
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
    "Sintaxis": {
        "Básico": {
            "Reorganizar oraciones": [
                {"pregunta": "Ordena las palabras: 'come / Manzanas / Juan'.", "tipo": "reorganizar_oraciones", "respuesta": "Juan come manzanas.", "explicacion": "El orden lógico es Sujeto + Verbo + Objeto."},
                {"pregunta": "Ordena las palabras: 'es / Mi / grande / casa'.", "tipo": "reorganizar_oraciones", "respuesta": "Mi casa es grande.", "explicacion": "El orden lógico es Posesivo + Sustantivo + Verbo + Adjetivo."},
            ]
        }
    }
}

# --- Funciones Auxiliares ---

def clear_screen():
    # Detecta el sistema operativo para usar el comando correcto
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_option(prompt, min_val, max_val):
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Opción inválida. Por favor, ingresa un número entre {min_val} y {max_val}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def normalize_text(text):
    return text.strip().lower()

# --- Lógica del Programa (Práctica) ---

def run_exercise(ejercicio, question_num, total_questions):
    clear_screen()
    print(f"\n--- Ejercicio {question_num}/{total_questions} ---")
    print(f"Pregunta: {ejercicio['pregunta']}")

    is_correct = False
    user_answer = None

    if ejercicio['tipo'] == 'seleccion_multiple':
        for i, opcion in enumerate(ejercicio['opciones']):
            print(f"{i + 1}. {opcion}")
        choice = get_valid_option("Tu respuesta (número): ", 1, len(ejercicio['opciones']))
        user_answer = normalize_text(ejercicio['opciones'][choice - 1])
        is_correct = (user_answer == normalize_text(ejercicio['respuesta']))

    elif ejercicio['tipo'] == 'completar_oraciones':
        num_espacios = ejercicio['pregunta'].count('___')
        user_answers = []
        for i in range(num_espacios):
            answer_part = input(f"Palabra {i + 1}: ").strip()
            user_answers.append(normalize_text(answer_part))
        user_answer = user_answers
        is_correct = (user_answer == [normalize_text(r) for r in ejercicio['respuesta']])

    elif ejercicio['tipo'] == 'detectar_errores':
        print(f"Oración: {ejercicio['pregunta']}")
        error_word = input("Palabra errónea: ").strip()
        correction = input("Corrección: ").strip()
        user_answer = {"palabra_erronea": normalize_text(error_word), "correccion": normalize_text(correction)}
        
        correct_error = normalize_text(ejercicio['respuesta']['palabra_erronea'])
        correct_correction = normalize_text(ejercicio['respuesta']['correccion'])
        is_correct = (user_answer['palabra_erronea'] == correct_error and
                      user_answer['correccion'] == correct_correction)

    elif ejercicio['tipo'] == 'reorganizar_oraciones':
        print(f"Ordena las palabras: {ejercicio['pregunta']}")
        user_answer = normalize_text(input("Tu oración reordenada: "))
        is_correct = (user_answer == normalize_text(ejercicio['respuesta']))

    elif ejercicio['tipo'] == 'clasificacion_de_palabras':
        print(f"Clasifica la palabra: {ejercicio['pregunta']}")
        user_answer = normalize_text(input("Tu clasificación: "))
        is_correct = (user_answer == normalize_text(ejercicio['respuesta']))

    elif ejercicio['tipo'] == 'conjugacion_verbal':
        print(f"Conjuga el verbo: {ejercicio['pregunta']}")
        user_answer = normalize_text(input("Tu conjugación: "))
        is_correct = (user_answer == normalize_text(ejercicio['respuesta']))

    else:
        print(f"Tipo de ejercicio '{ejercicio['tipo']}' no implementado para la práctica.")
        input("Presiona Enter para continuar...")
        return False # No sumamos puntos por tipos no implementados

    if is_correct:
        print("¡Correcto! ✅")
        return True
    else:
        print("Incorrecto. ❌")
        print(f"Explicación: {ejercicio['explicacion']}")
        return False

def select_and_run_exercises(area, level, exercise_type):
    if area in EJERCICIOS_DATA and level in EJERCICIOS_DATA[area] and exercise_type in EJERCICIOS_DATA[area][level]:
        exercises = list(EJERCICIOS_DATA[area][level][exercise_type]) # Copia de la lista
        if not exercises:
            print("No hay ejercicios en esta categoría para practicar. Presiona Enter para volver.")
            input()
            return

        random.shuffle(exercises)
        
        score = 0
        total_questions_for_session = min(len(exercises), 3) # Limitar a 3 ejercicios por sesión

        print(f"\nIniciando sesión de práctica para {exercise_type} ({area} - {level})...")
        input("Presiona Enter para comenzar.")

        for i in range(total_questions_for_session):
            if run_exercise(exercises[i], i + 1, total_questions_for_session):
                score += 1
            print("-" * 50)
            if i < total_questions_for_session -1: # No pedir enter después del último ejercicio
                input("Presiona Enter para el siguiente ejercicio...")
        
        clear_screen()
        print("\n--- ¡Sesión de Práctica Terminada! ---")
        print(f"Obtuviste {score} de {total_questions_for_session} preguntas correctas.")
        print("¡Sigue practicando para mejorar! 💪")
    else:
        print("No hay ejercicios disponibles para esa selección.")
    
    input("Presiona Enter para regresar al menú principal...")

# --- Menús de Navegación (Práctica) ---

def show_exercise_type_selection(area, level):
    clear_screen()
    print(f"\n🧪 Tipos de Ejercicio para {area} - {level}:")
    if area not in EJERCICIOS_DATA or level not in EJERCICIOS_DATA[area]:
        print("Nivel o área no encontrados. Volviendo al menú principal.")
        input("Presiona Enter para continuar...")
        return
    
    types = list(EJERCICIOS_DATA[area][level].keys())
    for i, tipo in enumerate(types):
        print(f"{i + 1}. {tipo}")
    print(f"{len(types) + 1}. Volver a Niveles")
    print("-" * 50)

    choice = get_valid_option("Selecciona un número de tipo de ejercicio: ", 1, len(types) + 1)
    if choice <= len(types):
        selected_type = types[choice - 1]
        select_and_run_exercises(area, level, selected_type)
    # Si elige volver, simplemente la función termina y el bucle principal lo lleva al menú anterior

def show_level_selection(area):
    clear_screen()
    print(f"\n🎯 Nivel para {area}:")
    if area not in EJERCICIOS_DATA:
        print("Área no encontrada. Volviendo al menú principal.")
        input("Presiona Enter para continuar...")
        return

    levels = list(EJERCICIOS_DATA[area].keys())
    for i, nivel in enumerate(levels):
        print(f"{i + 1}. {nivel}")
    print(f"{len(levels) + 1}. Volver a Áreas")
    print("-" * 50)

    choice = get_valid_option("Selecciona un número de nivel: ", 1, len(levels) + 1)
    if choice <= len(levels):
        selected_level = levels[choice - 1]
        show_exercise_type_selection(area, selected_level)

def show_area_selection():
    clear_screen()
    print("\n📚 Selecciona un Área del Lenguaje:")
    areas = list(EJERCICIOS_DATA.keys())
    for i, area in enumerate(areas):
        print(f"{i + 1}. {area}")
    print(f"{len(areas) + 1}. Volver al Menú Principal")
    print("-" * 50)

    choice = get_valid_option("Selecciona un número de área: ", 1, len(areas) + 1)
    if choice <= len(areas):
        selected_area = areas[choice - 1]
        show_level_selection(selected_area)

# --- Funciones del Editor de Ejercicios ---

def select_category_for_editor():
    """Permite al usuario seleccionar Área > Nivel > Tipo para editar."""
    clear_screen()
    print("--- Seleccionar Categoría para Edición ---")

    # Selección de Área
    areas = list(EJERCICIOS_DATA.keys())
    if not areas:
        print("No hay áreas disponibles. Por favor, añade una primero.")
        input("Presiona Enter para volver...")
        return None, None, None

    for i, area_name in enumerate(areas):
        print(f"{i + 1}. {area_name}")
    print(f"{len(areas) + 1}. Añadir nueva Área")
    print(f"0. Cancelar")
    area_choice = get_valid_option("Selecciona un número de área: ", 0, len(areas) + 1)

    if area_choice == 0:
        return None, None, None
    elif area_choice == len(areas) + 1:
        new_area = input("Introduce el nombre de la nueva Área: ").strip()
        if new_area:
            EJERCICIOS_DATA[new_area] = {}
            print(f"Área '{new_area}' creada.")
            return new_area, None, None # Forzamos a que vuelva a seleccionar el nivel
        else:
            print("Nombre de área no válido.")
            input("Presiona Enter para continuar...")
            return None, None, None
    else:
        selected_area = areas[area_choice - 1]

    # Selección de Nivel
    levels = list(EJERCICIOS_DATA[selected_area].keys())
    print("\n--- Seleccionar Nivel para Edición ---")
    if not levels:
        print(f"No hay niveles disponibles para '{selected_area}'. Por favor, añade uno primero.")
        input("Presiona Enter para volver...")
        return selected_area, None, None

    for i, level_name in enumerate(levels):
        print(f"{i + 1}. {level_name}")
    print(f"{len(levels) + 1}. Añadir nuevo Nivel")
    print(f"0. Cancelar")
    level_choice = get_valid_option("Selecciona un número de nivel: ", 0, len(levels) + 1)

    if level_choice == 0:
        return None, None, None
    elif level_choice == len(levels) + 1:
        new_level = input("Introduce el nombre del nuevo Nivel: ").strip()
        if new_level:
            EJERCICIOS_DATA[selected_area][new_level] = {}
            print(f"Nivel '{new_level}' creado en '{selected_area}'.")
            return selected_area, new_level, None # Forzamos a que vuelva a seleccionar el tipo
        else:
            print("Nombre de nivel no válido.")
            input("Presiona Enter para continuar...")
            return None, None, None
    else:
        selected_level = levels[level_choice - 1]

    # Selección de Tipo de Ejercicio
    exercise_types = list(EJERCICIOS_DATA[selected_area][selected_level].keys())
    print("\n--- Seleccionar Tipo de Ejercicio para Edición ---")
    if not exercise_types:
        print(f"No hay tipos de ejercicio disponibles para '{selected_area}' - '{selected_level}'. Por favor, añade uno primero.")
        input("Presiona Enter para volver...")
        return selected_area, selected_level, None

    for i, type_name in enumerate(exercise_types):
        print(f"{i + 1}. {type_name}")
    print(f"{len(exercise_types) + 1}. Añadir nuevo Tipo de Ejercicio")
    print(f"0. Cancelar")
    type_choice = get_valid_option("Selecciona un número de tipo: ", 0, len(exercise_types) + 1)

    if type_choice == 0:
        return None, None, None
    elif type_choice == len(exercise_types) + 1:
        new_type = input("Introduce el nombre del nuevo Tipo de Ejercicio: ").strip()
        if new_type:
            EJERCICIOS_DATA[selected_area][selected_level][new_type] = []
            print(f"Tipo de ejercicio '{new_type}' creado en '{selected_area}' - '{selected_level}'.")
            return selected_area, selected_level, new_type
        else:
            print("Nombre de tipo de ejercicio no válido.")
            input("Presiona Enter para continuar...")
            return None, None, None
    else:
        selected_type = exercise_types[type_choice - 1]

    return selected_area, selected_level, selected_type

def list_exercises():
    clear_screen()
    area, level, exercise_type = select_category_for_editor()
    if not (area and level and exercise_type):
        return

    print(f"\nEjercicios en {area} > {level} > {exercise_type}:")
    exercises = EJERCICIOS_DATA[area][level][exercise_type]

    if not exercises:
        print("No hay ejercicios en esta categoría.")
    else:
        for i, ejer in enumerate(exercises):
            print(f"  {i + 1}. Pregunta: {ejer['pregunta']}")
            print(f"     Tipo: {ejer['tipo']}")
            print(f"     Explicación: {ejer.get('explicacion', 'N/A')}")
            # Opcional: imprimir la respuesta para depuración
            # print(f"     Respuesta Correcta: {ejer['respuesta']}")
            print("     " + "-" * 20)
    input("Presiona Enter para volver al menú de edición...")

def add_exercise():
    clear_screen()
    print("--- Añadir Nuevo Ejercicio ---")
    area, level, exercise_type = select_category_for_editor()
    if not (area and level and exercise_type):
        return

    question = input("Introduce la pregunta: ").strip()
    if not question:
        print("La pregunta no puede estar vacía. Operación cancelada.")
        input("Presiona Enter para continuar...")
        return

    print("\nTipos de ejercicio disponibles:")
    tipos_validos = ["seleccion_multiple", "completar_oraciones", "detectar_errores",
                     "reorganizar_oraciones", "clasificacion_de_palabras", "conjugacion_verbal"]
    for i, tipo in enumerate(tipos_validos):
        print(f"{i + 1}. {tipo}")
    
    tipo_choice = get_valid_option("Selecciona el tipo de ejercicio: ", 1, len(tipos_validos))
    tipo = tipos_validos[tipo_choice - 1]

    respuesta = None
    opciones = []

    if tipo == "seleccion_multiple":
        print("Introduce las opciones (deja vacío para terminar):")
        while True:
            opcion = input("Opción: ").strip()
            if not opcion:
                break
            opciones.append(opcion)
        if not opciones:
            print("Debes introducir al menos una opción. Operación cancelada.")
            input("Presiona Enter para continuar...")
            return
        respuesta = input("Introduce la respuesta correcta (una de las opciones): ").strip()
        if respuesta not in opciones:
            print("La respuesta correcta debe ser una de las opciones proporcionadas. Operación cancelada.")
            input("Presiona Enter para continuar...")
            return
    elif tipo == "completar_oraciones":
        print("Introduce las palabras de respuesta para cada espacio (deja vacío para terminar):")
        respuestas_list = []
        while True:
            palabra = input("Palabra: ").strip()
            if not palabra:
                break
            respuestas_list.append(palabra)
        if not respuestas_list:
            print("Debes introducir al menos una palabra de respuesta. Operación cancelada.")
            input("Presiona Enter para continuar...")
            return
        respuesta = respuestas_list
    elif tipo == "detectar_errores":
        palabra_erronea = input("Introduce la palabra errónea: ").strip()
        correccion = input("Introduce la corrección: ").strip()
        if not palabra_erronea or not correccion:
            print("Ambos campos de error y corrección deben ser llenados. Operación cancelada.")
            input("Presiona Enter para continuar...")
            return
        respuesta = {"palabra_erronea": palabra_erronea, "correccion": correccion}
    else: # reorganizar_oraciones, clasificacion_de_palabras, conjugacion_verbal
        respuesta = input("Introduce la respuesta correcta: ").strip()
        if not respuesta:
            print("La respuesta no puede estar vacía. Operación cancelada.")
            input("Presiona Enter para continuar...")
            return
    
    explicacion = input("Introduce la explicación del ejercicio: ").strip()
    if not explicacion:
        print("La explicación no puede estar vacía. Operación cancelada.")
        input("Presiona Enter para continuar...")
        return

    new_exercise = {
        "pregunta": question,
        "tipo": tipo,
        "respuesta": respuesta,
        "explicacion": explicacion
    }
    if opciones: # Solo añadir si hay opciones (para seleccion_multiple)
        new_exercise["opciones"] = opciones

    EJERCICIOS_DATA[area][level][exercise_type].append(new_exercise)
    print("¡Ejercicio añadido exitosamente!")
    input("Presiona Enter para volver al menú de edición...")

def edit_exercise():
    clear_screen()
    print("--- Editar Ejercicio ---")
    area, level, exercise_type = select_category_for_editor()
    if not (area and level and exercise_type):
        return

    exercises = EJERCICIOS_DATA[area][level][exercise_type]
    if not exercises:
        print("No hay ejercicios en esta categoría para editar.")
        input("Presiona Enter para volver...")
        return

    print("\nEjercicios disponibles para editar:")
    for i, ejer in enumerate(exercises):
        print(f"  {i + 1}. Pregunta: {ejer['pregunta']} (Tipo: {ejer['tipo']})")

    index = get_valid_option("Selecciona el número del ejercicio a editar (0 para cancelar): ", 0, len(exercises))
    if index == 0:
        print("Operación cancelada.")
        input("Presiona Enter para continuar...")
        return
    
    ejercicio_a_editar = exercises[index - 1]

    print(f"\nEditando ejercicio: {ejercicio_a_editar['pregunta']}")
    print("Deja vacío para mantener el valor actual.")

    new_question = input(f"Nueva pregunta ({ejercicio_a_editar['pregunta']}): ").strip()
    if new_question:
        ejercicio_a_editar['pregunta'] = new_question

    # Edición de tipo no permitida directamente para evitar inconsistencias complejas
    print(f"Tipo actual: {ejercicio_a_editar['tipo']} (no se puede cambiar directamente)")

    if ejercicio_a_editar['tipo'] == "seleccion_multiple":
        print(f"Opciones actuales: {ejercicio_a_editar.get('opciones', 'N/A')}")
        edit_options = input("¿Deseas editar las opciones? (s/n): ").strip().lower()
        if edit_options == 's':
            new_opciones = []
            print("Introduce las nuevas opciones (deja vacío para terminar):")
            while True:
                opcion = input("Nueva opción: ").strip()
                if not opcion:
                    break
                new_opciones.append(opcion)
            if new_opciones:
                ejercicio_a_editar['opciones'] = new_opciones
                print("Opciones actualizadas.")
            else:
                print("No se introdujeron nuevas opciones, se mantienen las anteriores.")

        new_respuesta = input(f"Nueva respuesta correcta ({ejercicio_a_editar['respuesta']}): ").strip()
        if new_respuesta:
            if new_respuesta not in ejercicio_a_editar.get('opciones', []):
                print("¡Advertencia! La nueva respuesta no está entre las opciones actuales. Considera editar las opciones.")
            ejercicio_a_editar['respuesta'] = new_respuesta

    elif ejercicio_a_editar['tipo'] == "completar_oraciones":
        print(f"Palabras de respuesta actuales: {ejercicio_a_editar['respuesta']}")
        edit_resp = input("¿Deseas editar las palabras de respuesta? (s/n): ").strip().lower()
        if edit_resp == 's':
            new_respuestas_list = []
            print("Introduce las nuevas palabras (deja vacío para terminar):")
            while True:
                palabra = input("Nueva palabra: ").strip()
                if not palabra:
                    break
                new_respuestas_list.append(palabra)
            if new_respuestas_list:
                ejercicio_a_editar['respuesta'] = new_respuestas_list
                print("Respuestas actualizadas.")
            else:
                print("No se introdujeron nuevas respuestas, se mantienen las anteriores.")

    elif ejercicio_a_editar['tipo'] == "detectar_errores":
        current_error_word = ejercicio_a_editar['respuesta']['palabra_erronea']
        current_correction = ejercicio_a_editar['respuesta']['correccion']
        
        new_error_word = input(f"Nueva palabra errónea ({current_error_word}): ").strip()
        if new_error_word:
            ejercicio_a_editar['respuesta']['palabra_erronea'] = new_error_word

        new_correction = input(f"Nueva corrección ({current_correction}): ").strip()
        if new_correction:
            ejercicio_a_editar['respuesta']['correccion'] = new_correction

    else: # reorganizar_oraciones, clasificacion_de_palabras, conjugacion_verbal
        new_respuesta = input(f"Nueva respuesta correcta ({ejercicio_a_editar['respuesta']}): ").strip()
        if new_respuesta:
            ejercicio_a_editar['respuesta'] = new_respuesta
    
    new_explicacion = input(f"Nueva explicación ({ejercicio_a_editar.get('explicacion', 'N/A')}): ").strip()
    if new_explicacion:
        ejercicio_a_editar['explicacion'] = new_explicacion

    print("¡Ejercicio editado exitosamente!")
    input("Presiona Enter para volver al menú de edición...")

def delete_exercise():
    clear_screen()
    print("--- Eliminar Ejercicio ---")
    area, level, exercise_type = select_category_for_editor()
    if not (area and level and exercise_type):
        return

    exercises = EJERCICIOS_DATA[area][level][exercise_type]
    if not exercises:
        print("No hay ejercicios en esta categoría para eliminar.")
        input("Presiona Enter para volver...")
        return

    print("\nEjercicios disponibles para eliminar:")
    for i, ejer in enumerate(exercises):
        print(f"  {i + 1}. Pregunta: {ejer['pregunta']} (Tipo: {ejer['tipo']})")

    index = get_valid_option("Selecciona el número del ejercicio a eliminar (0 para cancelar): ", 0, len(exercises))
    if index == 0:
        print("Operación cancelada.")
        input("Presiona Enter para continuar...")
        return
    
    ejercicio_a_eliminar = exercises[index - 1]

    confirm = input(f"¿Estás seguro de que quieres eliminar '{ejercicio_a_eliminar['pregunta']}'? (s/n): ").strip().lower()
    if confirm == 's':
        del exercises[index - 1]
        print("¡Ejercicio eliminado exitosamente!")
    else:
        print("Operación de eliminación cancelada.")
    
    input("Presiona Enter para volver al menú de edición...")

def show_editor_menu():
    while True:
        clear_screen()
        print("--- Editor de Ejercicios ---")
        print("1. Listar ejercicios")
        print("2. Añadir nuevo ejercicio")
        print("3. Editar ejercicio existente")
        print("4. Eliminar ejercicio")
        print("5. Volver al menú principal")
        print("-" * 50)

        choice = get_valid_option("Selecciona una opción: ", 1, 5)

        if choice == 1:
            list_exercises()
        elif choice == 2:
            add_exercise()
        elif choice == 3:
            edit_exercise()
        elif choice == 4:
            delete_exercise()
        elif choice == 5:
            break # Salir del bucle y volver al menú principal

# --- Menú Principal ---
def main_menu():
    while True:
        clear_screen()
        print("✨ ¡Bienvenido a la Práctica de Lengua Castellana! ✨")
        print("-" * 50)
        print("1. Empezar a practicar")
        print("2. Editar ejercicios") # Nueva opción para el editor
        print("3. Salir")
        print("-" * 50)

        choice = get_valid_option("Selecciona una opción: ", 1, 3)

        if choice == 1:
            show_area_selection()
        elif choice == 2:
            show_editor_menu() # Llama al menú del editor
        elif choice == 3:
            print("¡Gracias por practicar! ¡Hasta pronto! 👋")
            break

if __name__ == "__main__":
    main_menu()
