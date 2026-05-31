import pygame

# Inicializar el mixer de sonido
pygame.mixer.init()

# Cargar sonidos
sonido_correcto = pygame.mixer.Sound("correcto.wav")
sonido_error = pygame.mixer.Sound("error.wav")

# Función para respuesta correcta
def respuesta_correcta():
    print("✔️ ¡Correcto! 🎉")
    sonido_correcto.play()

# Función para respuesta incorrecta
def respuesta_incorrecta():
    print("❌ Incorrecto, intenta de nuevo.")
    sonido_error.play()

# Simulación de un programa interactivo
print("Ejercicio: ¿Cuál es la palabra aguda correcta?")
respuesta = input("Escribe tu respuesta: ")

if respuesta.lower() == "camión":
    respuesta_correcta()
else:
    respuesta_incorrecta()
