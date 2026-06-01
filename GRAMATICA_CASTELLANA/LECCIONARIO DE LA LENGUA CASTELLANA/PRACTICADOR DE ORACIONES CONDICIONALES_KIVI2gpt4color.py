import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Juegos de Oraciones Condicionales 🎯")

# Fuente
font = pygame.font.SysFont(None, 32)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
YELLOW = (255, 255, 100)

# Puntos
puntos = 0

# Datos de ejemplo
oraciones_condicionales = {
    "Reales": [
        {"oracion": "Si estudias, aprobarás el examen.", "explicacion": "Condición real. SI + Presente + Futuro."},
        {"oracion": "Si llueve, nos quedamos en casa.", "explicacion": "Condición presente real. SI + Presente + Presente."}
    ],
    "Potenciales": [
        {"oracion": "Si estudiaras más, aprobarías fácilmente.", "explicacion": "Condición hipotética. SI + Pret. Imperfecto Subj. + Condicional simple."},
        {"oracion": "Si vinieras mañana, podrías ayudarme.", "explicacion": "Condición futura dudosa. SI + Pret. Imperfecto Subj. + Condicional simple."}
    ],
    "Irreales": [
        {"oracion": "Si hubieras estudiado, habrías aprobado.", "explicacion": "Condición no cumplida en el pasado. SI + Pret. Pluscuamperfecto Subj. + Condicional compuesto."},
        {"oracion": "Si me lo hubieras dicho, no habría venido.", "explicacion": "Condición pasada no cumplida. SI + Pluscuamperfecto Subj. + Condicional compuesto."}
    ]
}

# Juego 1: Clasificación
def juego_clasificacion():
    global puntos
    categoria = random.choice(list(oraciones_condicionales.keys()))
    oracion = random.choice(oraciones_condicionales[categoria])
    opciones = list(oraciones_condicionales.keys())
    random.shuffle(opciones)

    respuesta = None
    while True:
        screen.fill(WHITE)
        screen.blit(font.render(f"🎯 Puntos: {puntos}", True, BLACK), (700, 20))
        pregunta = font.render(f"🧠 ¿Qué tipo de oración es?: {oracion['oracion']}", True, BLACK)
        screen.blit(pregunta, (50, 50))

        for i, opcion in enumerate(opciones):
            pygame.draw.rect(screen, YELLOW, (50, 150 + i * 60, 400, 50), border_radius=10)
            texto_opcion = font.render(opcion, True, BLACK)
            screen.blit(texto_opcion, (60, 160 + i * 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(len(opciones)):
                    if 50 <= x <= 450 and 150 + i * 60 <= y <= 200 + i * 60:
                        respuesta = opciones[i]
                        break
        if respuesta:
            screen.fill(WHITE)
            if respuesta == categoria:
                resultado = font.render("✅ ¡Correcto! 🎉", True, GREEN)
                puntos += 1
            else:
                resultado = font.render(f"❌ Incorrecto. Era: {categoria}", True, RED)
            screen.blit(resultado, (50, 300))
            explicacion = font.render(f"📘 {oracion['explicacion']}", True, BLACK)
            screen.blit(explicacion, (50, 350))
            pygame.display.flip()
            pygame.time.wait(3000)
            break
        pygame.display.flip()

# Juego 2: Ordenar palabras
def juego_ordenar():
    global puntos
    categoria = random.choice(list(oraciones_condicionales.keys()))
    oracion = random.choice(oraciones_condicionales[categoria])
    palabras = oracion['oracion'].split()
    random.shuffle(palabras)
    respuesta_usuario = []

    while True:
        screen.fill(WHITE)
        screen.blit(font.render(f"🎯 Puntos: {puntos}", True, BLACK), (700, 20))
        texto_instruccion = font.render("🔤 Haz clic en las palabras en orden para formar la oración:", True, BLACK)
        screen.blit(texto_instruccion, (50, 50))

        for i, palabra in enumerate(palabras):
            if palabra != "":
                pygame.draw.rect(screen, GRAY, (50 + i * 120, 150, 100, 40), border_radius=10)
                screen.blit(font.render(palabra, True, BLACK), (60 + i * 120, 160))

        for i, palabra in enumerate(respuesta_usuario):
            screen.blit(font.render(palabra, True, BLUE), (50 + i * 120, 250))

        pygame.draw.rect(screen, RED, (700, 600, 150, 50), border_radius=8)
        screen.blit(font.render("🔁 Reiniciar", True, WHITE), (710, 610))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 700 <= x <= 850 and 600 <= y <= 650:
                    palabras = oracion['oracion'].split()
                    random.shuffle(palabras)
                    respuesta_usuario = []
                    continue
                for i, palabra in enumerate(palabras):
                    rect = pygame.Rect(50 + i * 120, 150, 100, 40)
                    if rect.collidepoint(x, y):
                        if palabra != "":
                            respuesta_usuario.append(palabra)
                            palabras[i] = ""
                        break
        if all(p == "" for p in palabras) and respuesta_usuario:
            screen.fill(WHITE)
            resultado = " ".join(respuesta_usuario)
            if resultado.strip() == oracion['oracion']:
                mensaje = font.render("✅ ¡Correcto! 🎊", True, GREEN)
                puntos += 1
            else:
                mensaje = font.render(f"❌ Incorrecto. Era: {oracion['oracion']}", True, RED)
            screen.blit(mensaje, (50, 300))
            explicacion = font.render(f"📘 {oracion['explicacion']}", True, BLACK)
            screen.blit(explicacion, (50, 350))
            pygame.display.flip()
            pygame.time.wait(4000)
            break
        pygame.display.flip()

# Juegos de marcador "próximamente"
def juego_placeholder(nombre):
    while True:
        screen.fill(WHITE)
        mensaje = font.render(f"🔧 {nombre} aún está en desarrollo...", True, BLACK)
        screen.blit(mensaje, (50, 300))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

# Juego principal con menú
def menu():
    while True:
        screen.fill(WHITE)
        screen.blit(font.render(f"🎯 Puntos: {puntos}", True, BLACK), (700, 20))
        titulo = font.render("🎮 Selecciona un juego condicional:", True, BLACK)
        screen.blit(titulo, (50, 50))

        opciones = [
            "Juego 1: Clasificación 📚", 
            "Juego 2: Ordenar palabras 🧩",
            "Juego 3: Completar espacios ✏️",
            "Juego 4: Memoria 🧠",
            "Juego 5: Construcción de oración 🧱",
            "Juego 6: Selección múltiple ✅",
            "Juego 7: Aventura textual 🗺️",
            "Juego 8: Carrera de condicionales 🚗",
            "Juego 9: Rompecabezas lógico 🧠",
            "Juego 10: Quiz visual 🖼️"
        ]

        for i, opcion in enumerate(opciones):
            pygame.draw.rect(screen, GRAY, (50, 100 + i * 50, 700, 40), border_radius=8)
            screen.blit(font.render(opcion, True, BLACK), (60, 110 + i * 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(len(opciones)):
                    if 50 <= x <= 750 and 100 + i * 50 <= y <= 140 + i * 50:
                        if i == 0:
                            juego_clasificacion()
                        elif i == 1:
                            juego_ordenar()
                        else:
                            juego_placeholder(opciones[i])
        pygame.display.flip()

menu()
