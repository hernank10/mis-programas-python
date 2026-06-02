import sys
import random
import difflib

# Intentar importar colorama para colores en la terminal (opcional)
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False

# Lista de 100 consejos para crear juegos de texto en Python con sus traducciones al inglés
consejos = [
    {"español": "Define el concepto del juego.", "inglés": "Define the game's concept."},
    {"español": "Crea una historia atractiva.", "inglés": "Create an engaging story."},
    {"español": "Establece objetivos claros.", "inglés": "Set clear objectives."},
    {"español": "Diseña el mundo del juego.", "inglés": "Design the game's world."},
    {"español": "Desarrolla personajes profundos.", "inglés": "Develop deep characters."},
    {"español": "Planea los puzzles y desafíos.", "inglés": "Plan the puzzles and challenges."},
    {"español": "Establece reglas claras.", "inglés": "Establish clear rules."},
    {"español": "Documenta tu diseño.", "inglés": "Document your design."},
    {"español": "Define el flujo del juego.", "inglés": "Define the game's flow."},
    {"español": "Identifica los objetos clave.", "inglés": "Identify key objects."},
    {"español": "Usa clases y objetos.", "inglés": "Use classes and objects."},
    {"español": "Modulariza el código.", "inglés": "Modularize the code."},
    {"español": "Implementa funciones reutilizables.", "inglés": "Implement reusable functions."},
    {"español": "Mantén una estructura de directorios clara.", "inglés": "Maintain a clear directory structure."},
    {"español": "Usa diccionarios para datos.", "inglés": "Use dictionaries for data."},
    {"español": "Implementa herencia para clases.", "inglés": "Implement inheritance for classes."},
    {"español": "Separa la lógica de presentación.", "inglés": "Separate logic from presentation."},
    {"español": "Usa comentarios y docstrings.", "inglés": "Use comments and docstrings."},
    {"español": "Implementa un sistema de comandos modular.", "inglés": "Implement a modular command system."},
    {"español": "Mantén consistencia en la nomenclatura.", "inglés": "Maintain consistency in naming."},
    {"español": "Implementa un sistema de comandos flexible.", "inglés": "Implement a flexible command system."},
    {"español": "Usa input() eficazmente.", "inglés": "Use input() effectively."},
    {"español": "Proporciona feedback inmediato.", "inglés": "Provide immediate feedback."},
    {"español": "Implementa autocompletado de comandos.", "inglés": "Implement command autocomplete."},
    {"español": "Usa colores para mejorar la lectura.", "inglés": "Use colors to enhance readability."},
    {"español": "Maneja comandos no reconocidos.", "inglés": "Handle unrecognized commands."},
    {"español": "Incluye un comando de ayuda detallado.", "inglés": "Include a detailed help command."},
    {"español": "Permite a los jugadores ver el inventario.", "inglés": "Allow players to view their inventory."},
    {"español": "Facilita la navegación.", "inglés": "Facilitate navigation."},
    {"español": "Implementa comandos de acción directa.", "inglés": "Implement direct action commands."},
    {"español": "Crea una clase de inventario.", "inglés": "Create an inventory class."},
    {"español": "Permite añadir y remover objetos.", "inglés": "Allow adding and removing objects."},
    {"español": "Limita el tamaño del inventario.", "inglés": "Limit inventory size."},
    {"español": "Categoriza los objetos.", "inglés": "Categorize objects."},
    {"español": "Implementa funciones de equipamiento.", "inglés": "Implement equipping functions."},
    {"español": "Añade funcionalidad de combinación de objetos.", "inglés": "Add object combination functionality."},
    {"español": "Usa íconos o descripciones detalladas.", "inglés": "Use icons or detailed descriptions."},
    {"español": "Implementa un sistema de peso o volumen.", "inglés": "Implement a weight or volume system."},
    {"español": "Permite organizar el inventario.", "inglés": "Allow inventory organization."},
    {"español": "Añade objetos especiales con funciones únicas.", "inglés": "Add special objects with unique functions."},
    {"español": "Crea diálogos interactivos.", "inglés": "Create interactive dialogues."},
    {"español": "Desarrolla una trama secundaria.", "inglés": "Develop a secondary plot."},
    {"español": "Usa descripciones vivas y detalladas.", "inglés": "Use vivid and detailed descriptions."},
    {"español": "Incorpora decisiones que afecten la historia.", "inglés": "Incorporate decisions that affect the story."},
    {"español": "Mantén un ritmo adecuado.", "inglés": "Maintain an appropriate pace."},
    {"español": "Introduce misterios y revelaciones graduales.", "inglés": "Introduce mysteries and gradual revelations."},
    {"español": "Crea conflictos y obstáculos.", "inglés": "Create conflicts and obstacles."},
    {"español": "Usa flashbacks o vistazos al pasado.", "inglés": "Use flashbacks or glimpses into the past."},
    {"español": "Mantén la coherencia narrativa.", "inglés": "Maintain narrative consistency."},
    {"español": "Implementa narración ambiental.", "inglés": "Implement environmental storytelling."},
    {"español": "Crea protagonistas relatables.", "inglés": "Create relatable protagonists."},
    {"español": "Desarrolla antagonistas complejos.", "inglés": "Develop complex antagonists."},
    {"español": "Añade personajes secundarios con propósitos claros.", "inglés": "Add secondary characters with clear purposes."},
    {"español": "Permite el desarrollo de personajes.", "inglés": "Allow character development."},
    {"español": "Implementa relaciones entre personajes.", "inglés": "Implement relationships between characters."},
    {"español": "Usa diálogos dinámicos.", "inglés": "Use dynamic dialogues."},
    {"español": "Incluye personalidades diversas.", "inglés": "Include diverse personalities."},
    {"español": "Dale a cada personaje un propósito.", "inglés": "Give each character a purpose."},
    {"español": "Implementa misterios personales.", "inglés": "Implement personal mysteries."},
    {"español": "Permite la evolución de las relaciones.", "inglés": "Allow relationships to evolve."},
    {"español": "Implementa manejo de excepciones.", "inglés": "Implement exception handling."},
    {"español": "Usa mensajes de error claros.", "inglés": "Use clear error messages."},
    {"español": "Depura paso a paso.", "inglés": "Debug step by step."},
    {"español": "Valida la entrada del usuario.", "inglés": "Validate user input."},
    {"español": "Prueba todos los comandos.", "inglés": "Test all commands."},
    {"español": "Usa logs para monitorear el juego.", "inglés": "Use logs to monitor the game."},
    {"español": "Revisa regularmente el código.", "inglés": "Regularly review the code."},
    {"español": "Implementa pruebas unitarias.", "inglés": "Implement unit tests."},
    {"español": "Documenta errores comunes.", "inglés": "Document common errors."},
    {"español": "Solicita feedback de usuarios.", "inglés": "Request user feedback."},
    {"español": "Añade música y sonidos (opcional).", "inglés": "Add music and sounds (optional)."},
    {"español": "Implementa guardados automáticos.", "inglés": "Implement autosaves."},
    {"español": "Incluye descripciones dinámicas.", "inglés": "Include dynamic descriptions."},
    {"español": "Usa variables para el estado del juego.", "inglés": "Use variables for the game's state."},
    {"español": "Proporciona opciones de personalización.", "inglés": "Provide customization options."},
    {"español": "Implementa un sistema de puntuación.", "inglés": "Implement a scoring system."},
    {"español": "Añade logros y recompensas.", "inglés": "Add achievements and rewards."},
    {"español": "Facilita la navegación a través de ayudas contextuales.", "inglés": "Facilitate navigation through contextual aids."},
    {"español": "Implementa consecuencias para las decisiones del jugador.", "inglés": "Implement consequences for player decisions."},
    {"español": "Optimiza la velocidad del juego.", "inglés": "Optimize the game's speed."},
    {"español": "Aprovecha bibliotecas estándar de Python.", "inglés": "Leverage Python's standard libraries."},
    {"español": "Incorpora colorama para colores.", "inglés": "Incorporate colorama for colors."},
    {"español": "Usa textwrap para formatear textos.", "inglés": "Use textwrap to format texts."},
    {"español": "Explora pygame para funcionalidades avanzadas.", "inglés": "Explore pygame for advanced functionalities."},
    {"español": "Implementa json para guardar datos.", "inglés": "Implement json to save data."},
    {"español": "Usa pickle para serializar objetos (con precaución).", "inglés": "Use pickle to serialize objects (with caution)."},
    {"español": "Incorpora re para manejar expresiones regulares.", "inglés": "Incorporate re to handle regular expressions."},
    {"español": "Aprovecha argparse para configuraciones.", "inglés": "Leverage argparse for configurations."},
    {"español": "Usa logging para monitorear el juego.", "inglés": "Use logging to monitor the game."},
    {"español": "Explora recursos en línea y tutoriales.", "inglés": "Explore online resources and tutorials."},
    {"español": "Optimiza el uso de memoria.", "inglés": "Optimize memory usage."},
    {"español": "Minimiza las operaciones costosas.", "inglés": "Minimize costly operations."},
    {"español": "Implementa caching para datos recurrentes.", "inglés": "Implement caching for recurring data."},
    {"español": "Usa generadores para grandes cantidades de datos.", "inglés": "Use generators for large amounts of data."},
    {"español": "Profiling del código.", "inglés": "Profile the code."},
    {"español": "Evita la duplicación de código.", "inglés": "Avoid code duplication."},
    {"español": "Usa listas y diccionarios de forma eficiente.", "inglés": "Use lists and dictionaries efficiently."},
    {"español": "Implementa lazy loading para recursos.", "inglés": "Implement lazy loading for resources."},
    {"español": "Evita variables globales innecesarias.", "inglés": "Avoid unnecessary global variables."},
    {"español": "Mantén el código limpio y legible.", "inglés": "Keep the code clean and readable."},
    {"español": "Define estructuras de datos claras.", "inglés": "Define clear data structures."},
    {"español": "Usa patrones de diseño apropiados.", "inglés": "Use appropriate design patterns."},
    {"español": "Implementa un sistema de eventos.", "inglés": "Implement an event system."},
    {"español": "Usa flags para estados específicos.", "inglés": "Use flags for specific states."},
    {"español": "Permite la extensión del juego fácilmente.", "inglés": "Allow the game to be easily extended."},
    {"español": "Implementa una interfaz de usuario intuitiva.", "inglés": "Implement an intuitive user interface."},
    {"español": "Usa funciones de ayuda para nuevas funcionalidades.", "inglés": "Use help functions for new features."},
    {"español": "Mantén la consistencia en el estilo de código.", "inglés": "Maintain consistency in code style."},
    {"español": "Usa herramientas de control de versiones.", "inglés": "Use version control tools."},
    {"español": "Implementa backups automáticos del juego.", "inglés": "Implement automatic game backups."},
    {"español": "Usa comentarios para explicar bloques complejos.", "inglés": "Use comments to explain complex blocks."},
    {"español": "Implementa un sistema de niveles o etapas.", "inglés": "Implement a system of levels or stages."},
    {"español": "Usa recursos externos como imágenes ASCII (opcional).", "inglés": "Use external resources like ASCII art (optional)."},
    {"español": "Implementa un sistema de registros detallados.", "inglés": "Implement a detailed logging system."},
    {"español": "Usa estructuras de datos adecuadas para cada necesidad.", "inglés": "Use appropriate data structures for each need."},
    {"español": "Implementa ciclos de juego eficientes.", "inglés": "Implement efficient game loops."},
    {"español": "Usa funciones recursivas con cuidado.", "inglés": "Use recursive functions carefully."},
    {"español": "Evita dependencias innecesarias.", "inglés": "Avoid unnecessary dependencies."},
    {"español": "Usa herramientas de linting para mantener el código limpio.", "inglés": "Use linting tools to keep the code clean."},
    {"español": "Implementa una documentación clara y completa.", "inglés": "Implement clear and complete documentation."},
    {"español": "Usa módulos personalizados para organizar el código.", "inglés": "Use custom modules to organize the code."},
    {"español": "Implementa una lógica de juego clara y bien definida.", "inglés": "Implement clear and well-defined game logic."},
    {"español": "Usa variables descriptivas para facilitar la lectura.", "inglés": "Use descriptive variables to facilitate reading."},
    {"español": "Implementa una arquitectura escalable.", "inglés": "Implement a scalable architecture."},
    {"español": "Usa listas de comprobación para asegurar características.", "inglés": "Use checklists to ensure features."},
    {"español": "Implementa pruebas de rendimiento.", "inglés": "Implement performance tests."},
    {"español": "Usa herramientas de depuración para identificar errores.", "inglés": "Use debugging tools to identify errors."},
    {"español": "Implementa manejadores de eventos para interacciones.", "inglés": "Implement event handlers for interactions."},
    {"español": "Usa comentarios para explicar decisiones de diseño.", "inglés": "Use comments to explain design decisions."},
    {"español": "Mantén la simplicidad en la implementación inicial.", "inglés": "Keep simplicity in the initial implementation."},
    {"español": "Escala la complejidad del juego gradualmente.", "inglés": "Scale the game's complexity gradually."},
    {"español": "Usa feedback de jugadores para mejorar el juego.", "inglés": "Use player feedback to improve the game."},
    {"español": "Mantén una copia de seguridad regular del código.", "inglés": "Maintain regular backups of the code."},
    {"español": "Implementa una interfaz amigable para el usuario.", "inglés": "Implement a user-friendly interface."},
    {"español": "Usa técnicas de programación defensiva para evitar errores.", "inglés": "Use defensive programming techniques to avoid errors."}
]

def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Ver todos los consejos")
    print("2. Practicar la ortografía de los consejos")
    print("3. Practicar la traducción de los consejos del español al inglés")
    print("4. Practicar la traducción de los consejos del inglés al español")
    print("5. Salir")

def ver_consejos():
    print("\n=== Lista de 100 Consejos ===\n")
    for idx, consejo in enumerate(consejos, 1):
        print(f"{idx}. Español: {consejo['español']}")
        print(f"   Inglés: {consejo['inglés']}\n")
    input("Presiona Enter para volver al menú principal...")

def practicar_ortografia():
    print("\n=== Práctica de Ortografía ===\n")
    consejo = random.choice(consejos)
    print("Escribe el siguiente consejo correctamente:")
    print(f"\n\"{consejo['español']}\"\n")
    entrada_usuario = input("Tu versión: ").strip()

    # Comparar la entrada del usuario con el consejo original
    if comparar_texto(consejo['español'], entrada_usuario):
        print("\n¡Correcto! Excelente trabajo.")
    else:
        print("\nHay algunos errores en tu escritura.")
        print(f"Versión correcta: \"{consejo['español']}\"")
        diffs = difflib.ndiff([consejo['español']], [entrada_usuario])
        diferencias = ''.join(diffs)
        print("Diferencias:")
        print(diferencias)
    input("\nPresiona Enter para continuar...")

def practicar_traduccion_es_en():
    print("\n=== Práctica de Traducción: Español a Inglés ===\n")
    consejo = random.choice(consejos)
    print("Traduce el siguiente consejo al inglés:")
    print(f"\n\"{consejo['español']}\"\n")
    entrada_usuario = input("Tu traducción: ").strip()

    # Comparar la entrada del usuario con la traducción correcta
    if comparar_texto(consejo['inglés'], entrada_usuario):
        print("\n¡Traducción correcta! Excelente trabajo.")
    else:
        print("\nTraducción incorrecta.")
        print(f"Traducción correcta: \"{consejo['inglés']}\"")
        diffs = difflib.ndiff([consejo['inglés']], [entrada_usuario])
        diferencias = ''.join(diffs)
        print("Diferencias:")
        print(diferencias)
    input("\nPresiona Enter para continuar...")

def practicar_traduccion_en_es():
    print("\n=== Práctica de Traducción: Inglés a Español ===\n")
    consejo = random.choice(consejos)
    print("Traduce el siguiente consejo al español:")
    print(f"\n\"{consejo['inglés']}\"\n")
    entrada_usuario = input("Tu traducción: ").strip()

    # Comparar la entrada del usuario con el consejo original
    if comparar_texto(consejo['español'], entrada_usuario):
        print("\n¡Traducción correcta! Excelente trabajo.")
    else:
        print("\nTraducción incorrecta.")
        print(f"Traducción correcta: \"{consejo['español']}\"")
        diffs = difflib.ndiff([consejo['español']], [entrada_usuario])
        diferencias = ''.join(diffs)
        print("Diferencias:")
        print(diferencias)
    input("\nPresiona Enter para continuar...")

def comparar_texto(texto_original, texto_usuario):
    # Normalizar textos
    texto_original = texto_original.lower().strip()
    texto_usuario = texto_usuario.lower().strip()

    # Calcular similaridad
    similitud = difflib.SequenceMatcher(None, texto_original, texto_usuario).ratio()

    # Considerar correcto si la similitud es mayor al 90%
    return similitud > 0.9

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == '1':
            ver_consejos()
        elif opcion == '2':
            practicar_ortografia()
        elif opcion == '3':
            practicar_traduccion_es_en()
        elif opcion == '4':
            practicar_traduccion_en_es()
        elif opcion == '5':
            print("\nGracias por usar el programa. ¡Hasta luego!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    main()
