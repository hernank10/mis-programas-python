# Este programa crea un juego educativo sobre sintaxis y transformaciones
# de oraciones usando Pygame.
# Incluye botones arcoíris, sistema de partículas y un diseño inmersivo.

import pygame
import random
import math

# --- Inicialización y configuración ---
pygame.init()

# Dimensiones de la pantalla
ANCHO, ALTO = 1000, 700
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Sintaxis de Oraciones")

# Colores y fuentes
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_OSCURO = (50, 50, 50)
TRANSPARENTE_BLANCO = (255, 255, 255, 150)
FUENTE_TITULO = pygame.font.Font(None, 80)
FUENTE_NORMAL = pygame.font.Font(None, 40)
FUENTE_PEQUENA = pygame.font.Font(None, 30)

# El reloj del juego
reloj = pygame.time.Clock()

# --- Contenido de la lección (oraciones y transformaciones) ---
# Cada tupla contiene: (oración_original, oración_transformada, tipo_transformación, idioma)
lecciones_oraciones = [
    ("The cat is big.", "El gato es grande.", "traducción", "inglés"),
    ("I am happy.", "I am not happy.", "negación", "inglés"),
    ("She reads a book.", "Does she read a book?", "interrogación", "inglés"),
    ("They are teachers.", "Are they teachers?", "interrogación", "inglés"),
    ("Yo como una manzana.", "I eat an apple.", "traducción", "español"),
    ("Ellos corren rápido.", "Ellos no corren rápido.", "negación", "español"),
    ("Él es mi amigo.", "¿Es él mi amigo?", "interrogación", "español"),
    ("They played football.", "Did they play football?", "pasado", "inglés"),
    ("She writes a letter.", "She wrote a letter.", "pasado", "inglés"),
    ("Nosotros leemos el libro.", "Nosotros no leemos el libro.", "negación", "español")
]

# --- Variables de estado del juego ---
estado_juego = "menu"  # Puede ser "menu", "jugando", "resultados"
puntaje = 0
preguntas_jugadas = []
pregunta_actual = None
respuesta_usuario = ""
mensaje_feedback = ""
tiempo_mensaje = 0
tiempo_respuesta = 0

# --- Clases para efectos visuales ---
class BotonRainbow:
    """Un botón con efectos de pulsación y hover, y colores de arcoíris."""
    def __init__(self, x, y, ancho, alto, texto, accion, emoticon):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.accion = accion
        self.emoticon = emoticon
        self.color_animacion = 0
        self.hover = False

    def dibujar(self, superficie):
        self.color_animacion = (self.color_animacion + 1) % 360
        color_rgb = pygame.Color(0)
        color_rgb.hsva = (self.color_animacion, 100, 100, 100)
        
        temp_rect = self.rect.copy()
        if self.hover:
            temp_rect.inflate_ip(10, 5)
        
        glass_surface = pygame.Surface(temp_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(glass_surface, TRANSPARENTE_BLANCO, glass_surface.get_rect(), border_radius=15)
        superficie.blit(glass_surface, temp_rect.topleft)
        
        pygame.draw.rect(superficie, color_rgb, temp_rect, 5, border_radius=15)
        
        texto_renderizado = FUENTE_NORMAL.render(f"{self.emoticon} {self.texto}", True, BLANCO)
        texto_rect = texto_renderizado.get_rect(center=self.rect.center)
        superficie.blit(texto_renderizado, texto_rect)

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(evento.pos)
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(evento.pos):
                self.accion()

class ParticulaEmoticon:
    """Una partícula que se mueve, rota y se desvanece."""
    def __init__(self, x, y, emoticon):
        self.x = x
        self.y = y
        self.emoticon = emoticon
        self.velocidad_x = random.uniform(-1.5, 1.5)
        self.velocidad_y = random.uniform(-4, -1)
        self.alfa = 255
        self.rotacion = 0
        self.velocidad_rotacion = random.uniform(-5, 5)

    def actualizar(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        self.velocidad_y += 0.1  # Gravedad
        self.alfa -= 3
        self.rotacion += self.velocidad_rotacion

    def dibujar(self, superficie):
        if self.alfa > 0:
            emoticon_renderizado = FUENTE_NORMAL.render(self.emoticon, True, (255, 255, 255, self.alfa))
            emoticon_renderizado = pygame.transform.rotate(emoticon_renderizado, self.rotacion)
            rect = emoticon_renderizado.get_rect(center=(self.x, self.y))
            superficie.blit(emoticon_renderizado, rect)

class SistemaParticulas:
    """Gestiona el conjunto de partículas."""
    def __init__(self):
        self.particulas = []
        # Emoticones de sintaxis bilingüe para estudiantes preuniversitarios
        self.emoticones_sintaxis = ['()', ':', '[]', '==', '!=', '?', '¿', '!', '¡', '.', '🇪🇸', '🇬🇧', '📚', '🧠', '✍️', '💯']

    def emitir(self, x, y, emoticones):
        emoticones_totales = emoticones + random.sample(self.emoticones_sintaxis, k=3)
        for _ in range(10):
            emoticon = random.choice(emoticones_totales)
            self.particulas.append(ParticulaEmoticon(x, y, emoticon))

    def actualizar(self):
        self.particulas = [p for p in self.particulas if p.alfa > 0]
        for p in self.particulas:
            p.actualizar()

    def dibujar(self, superficie):
        for p in self.particulas:
            p.dibujar(superficie)

# --- Funciones de estado del juego ---
def dibujar_fondo_animado():
    """Dibuja un fondo de gradiente animado y con glassmorphism."""
    global tiempo_animacion
    tiempo_animacion = (tiempo_animacion + 0.5) % 360
    
    for y in range(ALTO):
        r = int(128 + 127 * math.sin(math.radians(tiempo_animacion + y / 2)))
        g = int(128 + 127 * math.sin(math.radians(tiempo_animacion + y / 2 + 120)))
        b = int(128 + 127 * math.sin(math.radians(tiempo_animacion + y / 2 + 240)))
        pygame.draw.line(PANTALLA, (r, g, b), (0, y), (ANCHO, y))

def iniciar_juego():
    """Resetea las variables del juego para empezar de nuevo."""
    global estado_juego, puntaje, preguntas_jugadas, pregunta_actual, respuesta_usuario
    estado_juego = "jugando"
    puntaje = 0
    preguntas_jugadas.clear()
    obtener_nueva_pregunta()
    respuesta_usuario = ""

def obtener_nueva_pregunta():
    """Selecciona una nueva oración que no se haya usado."""
    global pregunta_actual
    preguntas_disponibles = [p for p in lecciones_oraciones if p not in preguntas_jugadas]
    if preguntas_disponibles:
        pregunta_actual = random.choice(preguntas_disponibles)
        preguntas_jugadas.append(pregunta_actual)
    else:
        ir_a_resultados()

def ir_a_resultados():
    """Cambia el estado del juego a 'resultados'."""
    global estado_juego
    estado_juego = "resultados"

def verificar_respuesta():
    """Verifica si la respuesta del usuario es correcta y actualiza el puntaje."""
    global puntaje, respuesta_usuario, mensaje_feedback, tiempo_mensaje
    respuesta_correcta = pregunta_actual[1]
    
    if respuesta_usuario.lower().strip() == respuesta_correcta.lower().strip():
        mensaje_feedback = f"¡Correcto! Es una transformación de {pregunta_actual[2]} ✅✨"
        sistema_particulas.emitir(ANCHO // 2, ALTO // 2, ['✅', '🎉', '✨', '⭐', '🧠'])
        puntaje += 1
    else:
        mensaje_feedback = f"Incorrecto. La respuesta es '{respuesta_correcta}'. ❌💔"
        sistema_particulas.emitir(ANCHO // 2, ALTO // 2, ['❌', '💔', '😔', '😭', '🤯'])
        
    tiempo_mensaje = pygame.time.get_ticks()
    respuesta_usuario = ""

# --- Bucle principal del juego ---
sistema_particulas = SistemaParticulas()
tiempo_animacion = 0
input_rect = pygame.Rect(ANCHO // 2 - 250, ALTO - 150, 500, 50)
boton_iniciar = BotonRainbow(ANCHO // 2 - 100, ALTO // 2 + 50, 200, 60, "¡Empezar!", iniciar_juego, '🚀')
boton_reintentar = BotonRainbow(ANCHO // 2 - 120, ALTO - 150, 240, 60, "Jugar de Nuevo", iniciar_juego, '🎮')

en_ejecucion = True
while en_ejecucion:
    reloj.tick(60)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            en_ejecucion = False
        
        if estado_juego == "menu":
            boton_iniciar.manejar_evento(evento)
        elif estado_juego == "resultados":
            boton_reintentar.manejar_evento(evento)
        
        if estado_juego == "jugando":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    verificar_respuesta()
                    obtener_nueva_pregunta()
                elif evento.key == pygame.K_BACKSPACE:
                    respuesta_usuario = respuesta_usuario[:-1]
                else:
                    respuesta_usuario += evento.unicode
    
    # --- Actualización del juego ---
    sistema_particulas.actualizar()

    # --- Dibujar la pantalla ---
    dibujar_fondo_animado()

    if estado_juego == "menu":
        titulo_render = FUENTE_TITULO.render("Aprende Sintaxis de Oraciones", True, BLANCO)
        titulo_rect = titulo_render.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        PANTALLA.blit(titulo_render, titulo_rect)
        
        boton_iniciar.dibujar(PANTALLA)

    elif estado_juego == "jugando":
        # Indicadores de idioma y sintaxis
        idioma_lang_render = FUENTE_PEQUENA.render(f"Idioma: {pregunta_actual[3].capitalize()} {'🇪🇸' if pregunta_actual[3] == 'español' else '🇬🇧'}", True, BLANCO)
        PANTALLA.blit(idioma_lang_render, (20, 20))
        
        # Tipo de transformación
        tipo_render = FUENTE_NORMAL.render(f"Transforma a: {pregunta_actual[2].capitalize()}", True, BLANCO)
        tipo_rect = tipo_render.get_rect(center=(ANCHO // 2, ALTO // 2 - 150))
        PANTALLA.blit(tipo_render, tipo_rect)
        
        # Oración a transformar
        pregunta_render = FUENTE_NORMAL.render(pregunta_actual[0], True, BLANCO)
        pregunta_rect = pregunta_render.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        PANTALLA.blit(pregunta_render, pregunta_rect)

        # Caja de entrada (simulada) con glassmorphism
        input_glass_surface = pygame.Surface(input_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(input_glass_surface, (255, 255, 255, 100), input_glass_surface.get_rect(), border_radius=10)
        PANTALLA.blit(input_glass_surface, input_rect.topleft)
        pygame.draw.rect(PANTALLA, BLANCO, input_rect, 2, border_radius=10)
        
        respuesta_render = FUENTE_NORMAL.render(respuesta_usuario, True, BLANCO)
        PANTALLA.blit(respuesta_render, (input_rect.x + 10, input_rect.y + 10))
        
        puntaje_render = FUENTE_NORMAL.render(f"Puntaje: {puntaje}", True, BLANCO)
        PANTALLA.blit(puntaje_render, (ANCHO // 2 - 80, 20))
        
        if mensaje_feedback and pygame.time.get_ticks() - tiempo_mensaje < 2000:
            feedback_render = FUENTE_NORMAL.render(mensaje_feedback, True, BLANCO)
            feedback_rect = feedback_render.get_rect(center=(ANCHO // 2, ALTO // 2 + 50))
            PANTALLA.blit(feedback_render, feedback_rect)

    elif estado_juego == "resultados":
        titulo_render = FUENTE_TITULO.render("Resultados", True, BLANCO)
        titulo_rect = titulo_render.get_rect(center=(ANCHO // 2, ALTO // 2 - 100))
        PANTALLA.blit(titulo_render, titulo_rect)
        
        final_render = FUENTE_NORMAL.render(f"Puntaje final: {puntaje} de {len(lecciones_oraciones)}", True, BLANCO)
        final_rect = final_render.get_rect(center=(ANCHO // 2, ALTO // 2))
        PANTALLA.blit(final_render, final_rect)
        
        boton_reintentar.dibujar(PANTALLA)
    
    sistema_particulas.dibujar(PANTALLA)

    pygame.display.flip()

pygame.quit()
