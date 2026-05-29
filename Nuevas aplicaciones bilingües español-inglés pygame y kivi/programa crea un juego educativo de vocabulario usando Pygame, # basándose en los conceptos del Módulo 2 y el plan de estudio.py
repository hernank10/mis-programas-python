# Este programa crea un juego educativo de vocabulario usando Pygame,
# basándose en los conceptos del Módulo 2 y el plan de estudio.
# Incorpora elementos visuales avanzados para una experiencia inmersiva.

import pygame
import random
import math

# --- Inicialización y configuración ---
pygame.init()

# Dimensiones de la pantalla
ANCHO, ALTO = 1000, 700
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Vocabulario Bilingüe")

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

# --- Contenido de la lección ---
# Diccionario para almacenar las palabras, ampliado para el juego.
vocabulario = {
    "perro": "dog",
    "gato": "cat",
    "pato": "duck",
    "casa": "house",
    "coche": "car",
    "sol": "sun",
    "luna": "moon",
    "agua": "water",
    "comida": "food",
    "árbol": "tree"
}
palabras_espanol = list(vocabulario.keys())

# --- Variables de estado del juego ---
estado_juego = "menu"  # Puede ser "menu", "jugando", "resultados"
puntaje = 0
palabras_jugadas = []
palabra_actual = ""
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
        self.color_actual = pygame.Color(0, 0, 0)
        self.color_animacion = 0
        self.hover = False

    def dibujar(self, superficie):
        self.color_animacion = (self.color_animacion + 1) % 360
        color_rgb = pygame.Color(0)
        color_rgb.hsva = (self.color_animacion, 100, 100, 100)
        
        # Efecto hover: agrandar el botón
        temp_rect = self.rect.copy()
        if self.hover:
            temp_rect.inflate_ip(10, 5)
        
        # Efecto de vidrio (glassmorphism)
        pygame.draw.rect(superficie, TRANSPARENTE_BLANCO, temp_rect, border_radius=15)
        pygame.draw.rect(superficie, color_rgb, temp_rect, 5, border_radius=15)
        
        # Texto del botón y emoticon
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
        self.emoticones_sintaxis = ['<', '>', '{', '}', '()', ';', '[]', '==', '!=', '->', '🇪🇸', '🇬🇧', '📚', '🚀']

    def emitir(self, x, y, emoticones):
        # Combina los emoticones de sintaxis con los específicos del evento
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
    
    # Gradiente dinámico de colores
    for y in range(ALTO):
        r = int(128 + 127 * math.sin(math.radians(tiempo_animacion + y / 2)))
        g = int(128 + 127 * math.sin(math.radians(tiempo_animacion + y / 2 + 120)))
        b = int(128 + 127 * math.sin(math.radians(tiempo_animacion + y / 2 + 240)))
        pygame.draw.line(PANTALLA, (r, g, b), (0, y), (ANCHO, y))

def iniciar_juego():
    """Resetea las variables del juego para empezar de nuevo."""
    global estado_juego, puntaje, palabras_jugadas, palabra_actual, respuesta_usuario
    estado_juego = "jugando"
    puntaje = 0
    palabras_jugadas.clear()
    obtener_nueva_palabra()
    respuesta_usuario = ""

def obtener_nueva_palabra():
    """Selecciona una nueva palabra que no se haya usado."""
    global palabra_actual
    palabras_disponibles = [p for p in palabras_espanol if p not in palabras_jugadas]
    if palabras_disponibles:
        palabra_actual = random.choice(palabras_disponibles)
        palabras_jugadas.append(palabra_actual)
    else:
        # Si no hay más palabras, ir a la pantalla de resultados.
        ir_a_resultados()

def ir_a_resultados():
    """Cambia el estado del juego a 'resultados'."""
    global estado_juego
    estado_juego = "resultados"

def verificar_respuesta():
    """Verifica si la respuesta del usuario es correcta y actualiza el puntaje."""
    global puntaje, respuesta_usuario, mensaje_feedback, tiempo_mensaje
    respuesta_correcta = vocabulario[palabra_actual]
    
    if respuesta_usuario.lower().strip() == respuesta_correcta:
        mensaje_feedback = "¡Correcto! ✅✨"
        sistema_particulas.emitir(ANCHO // 2, ALTO // 2, ['✅', '🎉', '✨', '⭐'])
        puntaje += 1
    else:
        mensaje_feedback = f"Incorrecto. La respuesta es '{respuesta_correcta}'. ❌💔"
        sistema_particulas.emitir(ANCHO // 2, ALTO // 2, ['❌', '💔', '😔', '😭'])
        
    tiempo_mensaje = pygame.time.get_ticks()
    respuesta_usuario = "" # Borra la respuesta para el siguiente intento.

# --- Bucle principal del juego ---
sistema_particulas = SistemaParticulas()
tiempo_animacion = 0
input_rect = pygame.Rect(ANCHO // 2 - 200, ALTO - 150, 400, 50)
boton_iniciar = BotonRainbow(ANCHO // 2 - 100, ALTO // 2 + 50, 200, 60, "¡Empezar!", iniciar_juego, '🚀')
boton_reintentar = BotonRainbow(ANCHO // 2 - 120, ALTO - 150, 240, 60, "Jugar de Nuevo", iniciar_juego, '🎮')

en_ejecucion = True
while en_ejecucion:
    reloj.tick(60)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            en_ejecucion = False
        
        # Manejo de eventos de botones
        if estado_juego == "menu":
            boton_iniciar.manejar_evento(evento)
        elif estado_juego == "resultados":
            boton_reintentar.manejar_evento(evento)
        
        # Manejo de entrada de teclado
        if estado_juego == "jugando":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    verificar_respuesta()
                    obtener_nueva_palabra()
                elif evento.key == pygame.K_BACKSPACE:
                    respuesta_usuario = respuesta_usuario[:-1]
                else:
                    respuesta_usuario += evento.unicode
    
    # --- Actualización del juego ---
    sistema_particulas.actualizar()

    # --- Dibujar la pantalla ---
    dibujar_fondo_animado()

    if estado_juego == "menu":
        titulo_render = FUENTE_TITULO.render("¡Aprende Vocabulario!", True, BLANCO)
        titulo_rect = titulo_render.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        PANTALLA.blit(titulo_render, titulo_rect)
        
        boton_iniciar.dibujar(PANTALLA)

    elif estado_juego == "jugando":
        # Indicadores de idioma
        idioma_es_render = FUENTE_PEQUENA.render("Español 🇪🇸", True, BLANCO)
        PANTALLA.blit(idioma_es_render, (20, 20))
        
        idioma_en_render = FUENTE_PEQUENA.render("Inglés 🇬🇧", True, BLANCO)
        PANTALLA.blit(idioma_en_render, (ANCHO - idioma_en_render.get_width() - 20, 20))
        
        # Palabra a traducir
        palabra_render = FUENTE_NORMAL.render(palabra_actual, True, BLANCO)
        palabra_rect = palabra_render.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        PANTALLA.blit(palabra_render, palabra_rect)

        # Caja de entrada (simulada)
        pygame.draw.rect(PANTALLA, GRIS_OSCURO, input_rect, border_radius=10)
        pygame.draw.rect(PANTALLA, BLANCO, input_rect, 2, border_radius=10)
        
        # Dibujar la respuesta del usuario
        respuesta_render = FUENTE_NORMAL.render(respuesta_usuario, True, BLANCO)
        PANTALLA.blit(respuesta_render, (input_rect.x + 10, input_rect.y + 10))
        
        # Puntaje
        puntaje_render = FUENTE_NORMAL.render(f"Puntaje: {puntaje}", True, BLANCO)
        PANTALLA.blit(puntaje_render, (ANCHO // 2 - 80, 20))
        
        # Mensaje de feedback
        if mensaje_feedback and pygame.time.get_ticks() - tiempo_mensaje < 2000:
            feedback_render = FUENTE_NORMAL.render(mensaje_feedback, True, BLANCO)
            feedback_rect = feedback_render.get_rect(center=(ANCHO // 2, ALTO // 2 + 50))
            PANTALLA.blit(feedback_render, feedback_rect)

    elif estado_juego == "resultados":
        titulo_render = FUENTE_TITULO.render("Resultados", True, BLANCO)
        titulo_rect = titulo_render.get_rect(center=(ANCHO // 2, ALTO // 2 - 100))
        PANTALLA.blit(titulo_render, titulo_rect)
        
        final_render = FUENTE_NORMAL.render(f"Puntaje final: {puntaje} de {len(vocabulario)}", True, BLANCO)
        final_rect = final_render.get_rect(center=(ANCHO // 2, ALTO // 2))
        PANTALLA.blit(final_render, final_rect)
        
        boton_reintentar.dibujar(PANTALLA)
    
    # Dibujar las partículas siempre, sin importar el estado del juego
    sistema_particulas.dibujar(PANTALLA)

    pygame.display.flip()

pygame.quit()
