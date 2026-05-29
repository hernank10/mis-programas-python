import random
import os
import time

# Dictionary of error types and their descriptions
ERROR_TIPOS = {
    1: "Concordancia de Sujeto-Verbo",
    2: "Uso incorrecto de Pronombres",
    3: "Uso incorrecto de Conectores",
    4: "Error de Puntuación",
    5: "Error de Ortografía",
}

# Exercise data with sentences, their errors, and correct versions.
# The 'error_type' key corresponds to the number in ERROR_TIPOS.
EJERCICIOS = {
    "es": [
        {"oracion": "El niño corren en el parque.", "error_type": 1, "correcta": "El niño corre en el parque."},
        {"oracion": "Ellas y yo va al cine.", "error_type": 1, "correcta": "Ellas y yo vamos al cine."},
        {"oracion": "El libro, cual me diste, es genial.", "error_type": 2, "correcta": "El libro que me diste es genial."},
        {"oracion": "Ellos tiene hambre.", "error_type": 1, "correcta": "Ellos tienen hambre."},
        {"oracion": "Fui a la tienda, pero no tenía dinero.", "error_type": 3, "correcta": "Fui a la tienda, pero no tenía dinero."},
        {"oracion": "El perro y los gatos es amigables.", "error_type": 1, "correcta": "El perro y los gatos son amigables."},
        {"oracion": "Tengo sueño. Y quiero dormir.", "error_type": 4, "correcta": "Tengo sueño y quiero dormir."},
        {"oracion": "La casa es muy grandes.", "error_type": 1, "correcta": "La casa es muy grande."},
        {"oracion": "El hombre que trabaja conmigo es el, que te dije.", "error_type": 4, "correcta": "El hombre que trabaja conmigo es el que te dije."},
        {"oracion": "Ella es intelijente y el es amable.", "error_type": 5, "correcta": "Ella es inteligente y él es amable."},
        {"oracion": "No puedo ir porque, estoy enfermo.", "error_type": 4, "correcta": "No puedo ir porque estoy enfermo."},
        {"oracion": "Los estudiantes es muy inteligentes.", "error_type": 1, "correcta": "Los estudiantes son muy inteligentes."},
        {"oracion": "Los carros nuevos, son rápidos.", "error_type": 4, "correcta": "Los carros nuevos son rápidos."},
        {"oracion": "Me gusta leer y escuchar música, sin embargo no me gusta bailar.", "error_type": 3, "correcta": "Me gusta leer y escuchar música, sin embargo, no me gusta bailar."},
        {"oracion": "La mesa y la silla están roto.", "error_type": 1, "correcta": "La mesa y la silla están rotas."},
        {"oracion": "El perro, cual es negro, es mio.", "error_type": 2, "correcta": "El perro que es negro es mío."},
        {"oracion": "El doctor y la enfermera está ocupados.", "error_type": 1, "correcta": "El doctor y la enfermera están ocupados."},
        {"oracion": "La comida es buena, y el servicio es excelente.", "error_type": 4, "correcta": "La comida es buena, y el servicio es excelente."},
        {"oracion": "Nosotros vamos a el cine.", "error_type": 5, "correcta": "Nosotros vamos al cine."},
        {"oracion": "Si tu estudias, tu aprobaras.", "error_type": 4, "correcta": "Si tú estudias, tú aprobarás."},
    ],
    "en": [
        {"oracion": "The dog runs fast.", "error_type": 1, "correcta": "The dog runs fast."},
        {"oracion": "The students is here.", "error_type": 1, "correcta": "The students are here."},
        {"oracion": "She sing a song.", "error_type": 1, "correcta": "She sings a song."},
        {"oracion": "Him and me went to the store.", "error_type": 2, "correcta": "He and I went to the store."},
        {"oracion": "The cat and dogs is friendly.", "error_type": 1, "correcta": "The cat and dogs are friendly."},
        {"oracion": "I like him, but he doesn't like I.", "error_type": 2, "correcta": "I like him, but he doesn't like me."},
        {"oracion": "The car is old, than it still works.", "error_type": 3, "correcta": "The car is old, but it still works."},
        {"oracion": "They go to the movies.", "error_type": 1, "correcta": "They go to the movies."},
        {"oracion": "I went to school, then I was sick.", "error_type": 3, "correcta": "I went to school, because I was sick."},
        {"oracion": "The girls is smart.", "error_type": 1, "correcta": "The girls are smart."},
        {"oracion": "He bought a new phone, than he lost it.", "error_type": 3, "correcta": "He bought a new phone, but he lost it."},
        {"oracion": "The books and the pens is on the table.", "error_type": 1, "correcta": "The books and the pens are on the table."},
        {"oracion": "I want to go, however I can't.", "error_type": 4, "correcta": "I want to go; however, I can't."},
        {"oracion": "The red car its fast.", "error_type": 5, "correcta": "The red car is fast."},
        {"oracion": "This is the man whom helped me.", "error_type": 2, "correcta": "This is the man who helped me."},
        {"oracion": "The boy and girl goes to school.", "error_type": 1, "correcta": "The boy and girl go to school."},
        {"oracion": "I have ate dinner.", "error_type": 5, "correcta": "I have eaten dinner."},
        {"oracion": "She went to the store. and bought milk.", "error_type": 4, "correcta": "She went to the store and bought milk."},
        {"oracion": "The cat sat on it's mat.", "error_type": 5, "correcta": "The cat sat on its mat."},
        {"oracion": "I did not know nobody.", "error_type": 2, "correcta": "I did not know anybody."}
    ]
}

def clear_screen():
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    """Muestra el menú principal y maneja la selección del usuario."""
    while True:
        clear_screen()
        print("--- 🏰 Defiende la Gramática 🏰 ---")
        print("1. Jugar")
        print("2. Salir")
        
        opcion = input("\nSelecciona una opción (1-2): ")
        
        if opcion == "1":
            jugar_defensa()
        elif opcion == "2":
            print("¡Gracias por jugar! 👋")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            input("Presiona Enter para continuar...")

def jugar_defensa():
    """Ejecuta una ronda del juego de defensa gramatical."""
    clear_screen()
    idioma = input("Selecciona un idioma (es/en): ").lower()
    
    if idioma not in ["es", "en"]:
        print("Idioma no válido.")
        input("Presiona Enter para volver al menú...")
        return
    
    ejercicios_disponibles = EJERCICIOS[idioma].copy()
    random.shuffle(ejercicios_disponibles)
    
    puntaje = 0
    vidas = 3 # 3 incorrect answers and the game is over
    
    print("¡Prepara tus torres gramaticales! 🧱")
    input("Presiona Enter para comenzar la primera oleada...")

    for i, ejercicio in enumerate(ejercicios_disponibles):
        if vidas <= 0:
            break
            
        clear_screen()
        print(f"--- Oleada {i+1} de {len(ejercicios_disponibles)} ---")
        print(f"Puntaje: {puntaje} | Vidas: {'❤️' * vidas}")
        
        print("\nOración incorrecta: ")
        print(f"  > {ejercicio['oracion']}\n")
        
        print("Elige el tipo de error para corregir la oración:")
        for key, value in ERROR_TIPOS.items():
            print(f"  {key}. {value}")
            
        try:
            respuesta_str = input("Tu elección: ")
            respuesta = int(respuesta_str)
            
            if respuesta == ejercicio["error_type"]:
                print(f"¡CORRECTO! ✅ La torre de '{ERROR_TIPOS[respuesta]}' dispara. Enemigo eliminado.")
                print(f"Versión correcta: '{ejercicio['correcta']}'")
                puntaje += 1
            else:
                print(f"INCORRECTO ❌. Esa torre no es la correcta. Enemigo avanza.")
                print(f"El error real era: '{ERROR_TIPOS[ejercicio['error_type']]}'.")
                vidas -= 1
        except (ValueError, KeyError):
            print("Entrada no válida. El enemigo avanza.")
            vidas -= 1
        
        input("\nPresiona Enter para continuar...")
        
    clear_screen()
    print("--- Fin del Juego ---")
    if vidas > 0:
        print("¡Victoria! 🎉 Has defendido la gramática exitosamente.")
        print(f"Puntaje final: {puntaje} de {len(ejercicios_disponibles)}")
    else:
        print("¡Derrota! 💀 Los enemigos gramaticales han sobrepasado tus defensas.")
        print(f"Tu puntaje fue: {puntaje} de {len(ejercicios_disponibles)}")
    
    input("Presiona Enter para volver al menú principal...")

if __name__ == "__main__":
    main_menu()
