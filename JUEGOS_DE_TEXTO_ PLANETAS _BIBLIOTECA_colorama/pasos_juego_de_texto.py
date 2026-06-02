import time
import os

# Definir los 20 pasos en una lista
pasos = [
    "1. Planificación y Diseño del Juego: Define claramente la historia, los personajes principales y secundarios, así como los objetivos del juego.",
    "2. Estructura Básica del Juego: Crea las clases fundamentales (Room, Character, Item, Event, Game) que formarán la base del juego.",
    "3. Implementación de Habitaciones: Define todas las habitaciones necesarias, sus descripciones y las conexiones entre ellas mediante salidas (norte, sur, este, oeste).",
    "4. Sistema de Inventario Mejorado: Amplía la clase Game para manejar múltiples objetos y permite combinaciones de objetos para resolver desafíos.",
    "5. Interacción Avanzada con Personajes: Desarrolla diálogos dinámicos basados en el estado del juego, permitiendo que los personajes ofrezcan misiones secundarias y pistas clave.",
    "6. Sistema de Eventos Dinámicos: Implementa una clase Event que permita desencadenar eventos basados en condiciones específicas del juego.",
    "7. Manejo de Comandos Mejorado: Amplía el sistema de comandos para reconocer entradas más naturales y flexibles, mejorando la experiencia del usuario.",
    "8. Funciones de Guardar y Cargar Partidas: Añade funcionalidad para guardar el estado actual del juego en un archivo JSON y permitir la carga de partidas guardadas.",
    "9. Integración de Diálogos Basados en Estado: Modifica los diálogos de los personajes para que respondan de manera diferente según el progreso del juego.",
    "10. Implementación de Eventos Condicionales: Define eventos que se activen solo cuando se cumplan ciertas condiciones, enriqueciendo la narrativa.",
    "11. Mejora de la Gestión de Objetos: Permite al jugador usar y combinar objetos de manera más compleja para superar obstáculos.",
    "12. Optimización del Flujo del Juego: Asegura que el flujo del juego sea lógico y que las acciones del jugador tengan consecuencias claras.",
    "13. Creación de Funciones de Ayuda: Desarrolla una función de ayuda que liste todos los comandos disponibles y cómo utilizarlos.",
    "14. Implementación de Mensajes de Feedback: Proporciona mensajes claros y útiles en respuesta a las acciones del jugador, mejorando la interacción.",
    "15. Manejo de Errores y Validaciones: Añade validaciones para manejar entradas incorrectas y evita que el juego se detenga por errores inesperados.",
    "16. Desarrollo de un Sistema de Pistas: Introduce un sistema que ofrezca pistas al jugador cuando se encuentre bloqueado, facilitando la progresión.",
    "17. Añadir Características de Personalización: Permite al jugador personalizar ciertos aspectos del juego, como el nombre del personaje o la apariencia.",
    "18. Pruebas y Depuración: Realiza pruebas exhaustivas para identificar y corregir errores, asegurando una experiencia de juego fluida.",
    "19. Documentación del Código: Comenta y documenta el código de manera clara para facilitar futuras modificaciones y el entendimiento del proyecto.",
    "20. Mejoras de la Interfaz de Usuario: Refina la presentación del texto, utiliza formatos claros y considera la posibilidad de integrar colores o estilos para mejorar la legibilidad."
]

def clear_screen():
    # Limpiar la pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_paso(paso):
    clear_screen()
    print("--------------------------------------------------")
    print("             Paso para Implementar Mejora           ")
    print("--------------------------------------------------\n")
    print(paso)
    print("\nPresiona Enter para continuar al siguiente paso...")
    input()

def repetir_pasos():
    for paso in pasos:
        mostrar_paso(paso)
    print("Has revisado todos los pasos. ¡Bien hecho!")

if __name__ == "__main__":
    repetir_pasos()
