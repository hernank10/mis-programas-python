# Este programa implementa un juego de aventura en Pygame para el Módulo 9,
# donde el jugador se mueve por un mapa y resuelve retos de sintaxis
# generados dinámicamente con IA.

import pygame
import sys
import json
import sqlite3
import random
import requests

# --- Configuración del juego ---
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Sintaxis: Aventura Gramatical")

# Colores (en formato RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (10, 25, 47)
VIBRANT_GREEN = (77, 248, 87)
VIBRANT_RED = (255, 80, 80)
INPUT_BOX_COLOR = (200, 200, 200)

# Fuentes
font_small = pygame.font.Font(None, 24)
font_medium = pygame.font.Font(None, 40)
font_large = pygame.font.Font(None, 60)

# Jugador y objetos del juego
PLAYER_SIZE = 30
PLAYER_SPEED = 5
PLAYER_COLOR = (248, 196, 42) # Amarillo
BOOK_COLOR = (50, 150, 255)
TEACHER_COLOR = (255, 100, 100)

# Estados del juego
STATE_EXPLORING = "exploring"
STATE_CHALLENGE = "challenge"
STATE_LOADING = "loading"
STATE_FINISHED = "finished"

# --- Configuración de la Base de Datos (para respaldo) ---
DB_NAME = "preguntas.db"

def inicializar_db():
    """Conecta a la base de datos y crea la tabla si no existe,
       insertando datos iniciales si la tabla está vacía."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS preguntas (
            id INTEGER PRIMARY KEY,
            oracion_original TEXT NOT NULL,
            oracion_transformada TEXT NOT NULL,
            tipo_transformacion TEXT NOT NULL,
            idioma TEXT NOT NULL,
            dificultad INTEGER NOT NULL
        )
    """)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM preguntas")
    if cursor.fetchone()[0] == 0:
        lecciones_iniciales = [
            ("The boy who is wearing a hat is my brother.", "El chico que lleva un sombrero es mi hermano.", "adjetiva", "inglés", 1),
            ("Es importante que estudies.", "That you study is important.", "sustantiva", "español", 1),
            ("I believe that she is right.", "Creo que ella tiene razón.", "sustantiva", "inglés", 1),
            ("The house where I was born is for sale.", "La casa donde nací está en venta.", "adjetiva", "español", 1),
            ("I know who stole the cookies.", "Sé quién robó las galletas.", "sustantiva", "inglés", 1),
            ("No sé si va a llover mañana.", "I don't know if it will rain tomorrow.", "sustantiva", "español", 1),
            ("Because it's raining, we can't go to the park.", "Como está lloviendo, no podemos ir al parque.", "causal", "inglés", 2),
            ("He was so tired that he fell asleep.", "Estaba tan cansado que se quedó dormido.", "consecutiva", "inglés", 2),
            ("Cuando llegué a casa, mi hermana ya se había ido.", "When I arrived home, my sister had already left.", "temporal", "español", 2),
            ("He works as if he were a machine.", "Trabaja como si fuera una máquina.", "comparativa", "inglés", 2),
            ("Debido a que tengo un examen, no puedo salir.", "Because I have an exam, I can't go out.", "causal", "español", 2),
            ("Tan pronto como vi el mensaje, te llamé.", "As soon as I saw the message, I called you.", "temporal", "español", 2),
            ("Although she was sick, she went to school.", "A pesar de que estaba enferma, fue a la escuela.", "concesiva", "inglés", 3),
            ("Para que apruebes el curso, tienes que estudiar más.", "In order for you to pass the course, you have to study more.", "final", "español", 3),
            ("I will help you, provided that you ask nicely.", "Te ayudaré, siempre y cuando pidas bien.", "condicional", "inglés", 3),
            ("Though it was cold, we went swimming.", "Aunque hacía frío, fuimos a nadar.", "concesiva", "inglés", 3),
            ("Por mucho que insistas, no cambiaré de opinión.", "However much you insist, I won't change my mind.", "concesiva", "español", 3),
            ("Para que lo entiendas, te lo explicaré de nuevo.", "So that you understand it, I will explain it again.", "final", "español", 3),
        ]
        cursor.executemany("INSERT INTO preguntas (oracion_original, oracion_transformada, tipo_transformacion, idioma, dificultad) VALUES (?, ?, ?, ?, ?)", lecciones_iniciales)
        conn.commit()
    conn.close()

# --- Clases del juego ---
class Player(pygame.sprite.Sprite):
    """Representa al jugador que se mueve por el mapa."""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PLAYER_SIZE, PLAYER_SIZE])
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel = [0, 0]

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

class GameObject(pygame.sprite.Sprite):
    """Representa objetos interactivos como libros y profesores."""
    def __init__(self, x, y, size, color, object_type):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.object_type = object_type

# --- Funciones para la IA y la base de datos ---
def obtener_pregunta_ia(dificultad):
    """Llama a la API de Gemini para obtener una pregunta.
       Nota: En una aplicación real, esto debería ejecutarse en un hilo
       separado para no bloquear el juego."""
    try:
        prompt_ia = f"Generate a bilingual syntax question in JSON format. The question should include 'oracion_original' (a sentence in English), 'oracion_transformada' (the equivalent Spanish translation), 'tipo_transformacion' (the syntactic transformation, one of 'adjetiva', 'sustantiva', 'causal', 'consecutiva', 'temporal', 'comparativa', 'concesiva', 'final', or 'condicional'), and 'idioma' ('inglés' or 'español'). The difficulty should correspond to 'dificultad' {dificultad}. The generated sentence should be based on this difficulty level. For instance, for difficulty 1, use simple sentences. For difficulty 3, use more complex sentence structures. The output must be in JSON format."

        payload = {
            "contents": [{"parts": [{"text": prompt_ia}]}],
            "generationConfig": {
                "responseMimeType": "application/json",
                "responseSchema": {
                    "type": "OBJECT",
                    "properties": {
                        "oracion_original": {"type": "STRING"},
                        "oracion_transformada": {"type": "STRING"},
                        "tipo_transformacion": {"type": "STRING"},
                        "idioma": {"type": "STRING"},
                    },
                    "propertyOrdering": ["oracion_original", "oracion_transformada", "tipo_transformacion", "idioma"]
                }
            }
        }
        
        # URL de la API de Gemini. Reemplazar si se usa otro endpoint.
        api_key = ""
        api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=" + api_key
        
        response = requests.post(api_url, json=payload)
        response.raise_for_status() # Lanza una excepción si la respuesta no es 200 OK
        
        result = response.json()
        json_str = result['candidates'][0]['content']['parts'][0]['text']
        ia_data = json.loads(json_str)

        return (
            ia_data['oracion_original'],
            ia_data['oracion_transformada'],
            ia_data['tipo_transformacion'],
        )

    except (requests.RequestException, KeyError, json.JSONDecodeError) as e:
        print(f"Error al obtener pregunta de la IA: {e}")
        return None

def obtener_pregunta_db(dificultad):
    """Obtiene una pregunta aleatoria de la base de datos local."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT oracion_original, oracion_transformada, tipo_transformacion FROM preguntas WHERE dificultad = ? ORDER BY RANDOM() LIMIT 1", (dificultad,))
    pregunta = cursor.fetchone()
    conn.close()
    return pregunta

# --- Clase principal del juego ---
class Game:
    def __init__(self):
        self.state = STATE_EXPLORING
        self.player = Player(100, 100)
        self.all_sprites = pygame.sprite.Group()
        self.interactive_objects = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.dificultad_actual = 1
        self.puntaje = 0
        self.pregunta_actual = None
        self.user_answer = ""
        self.feedback = ""
        self.show_feedback_time = 0

        # Crear los objetos interactivos
        self.interactive_objects.add(GameObject(400, 300, 40, BOOK_COLOR, "libro"))
        self.interactive_objects.add(GameObject(700, 500, 40, TEACHER_COLOR, "profesor"))
        self.all_sprites.add(self.interactive_objects)

    def handle_input(self):
        """Maneja las entradas del usuario (teclado)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.state == STATE_EXPLORING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.vel[1] = -PLAYER_SPEED
                    elif event.key == pygame.K_DOWN:
                        self.player.vel[1] = PLAYER_SPEED
                    elif event.key == pygame.K_LEFT:
                        self.player.vel[0] = -PLAYER_SPEED
                    elif event.key == pygame.K_RIGHT:
                        self.player.vel[0] = PLAYER_SPEED
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_UP, pygame.K_DOWN]:
                        self.player.vel[1] = 0
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        self.player.vel[0] = 0
            
            elif self.state == STATE_CHALLENGE:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_answer = self.user_answer[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.check_answer()
                    else:
                        self.user_answer += event.unicode

    def check_collisions(self):
        """Verifica si el jugador colisiona con un objeto interactivo."""
        collided_objects = pygame.sprite.spritecollide(self.player, self.interactive_objects, False)
        if collided_objects:
            self.start_challenge()

    def start_challenge(self):
        """Inicia el modo de desafío, obteniendo una nueva pregunta."""
        self.state = STATE_LOADING
        self.user_answer = ""
        self.feedback = ""
        # Simula la obtención de la pregunta. En un juego real,
        # la llamada a la IA se haría de forma asíncrona.
        pregunta = obtener_pregunta_ia(self.dificultad_actual)
        if not pregunta:
            pregunta = obtener_pregunta_db(self.dificultad_actual)
            
        if pregunta:
            self.pregunta_actual = {
                "oracion_original": pregunta[0],
                "oracion_transformada": pregunta[1],
                "tipo_transformacion": pregunta[2]
            }
            self.state = STATE_CHALLENGE
        else:
            self.state = STATE_EXPLORING # No hay preguntas, vuelve a explorar

    def check_answer(self):
        """Verifica la respuesta del usuario."""
        if self.pregunta_actual:
            correct_answer = self.pregunta_actual['oracion_transformada'].lower().strip()
            if self.user_answer.lower().strip() == correct_answer:
                self.feedback = "¡Correcto! ✅"
                self.puntaje += 10
                # Desbloquear el siguiente nivel, si aplica
                self.interactive_objects.empty()
                if self.dificultad_actual < 3:
                    self.dificultad_actual += 1
                    self.interactive_objects.add(GameObject(700, 300, 40, BOOK_COLOR, "libro"))
                    self.all_sprites.add(self.interactive_objects)
            else:
                self.feedback = "Incorrecto. ❌"
            
            self.show_feedback_time = pygame.time.get_ticks()
            
            # Pausa breve para mostrar el feedback y luego regresa al juego
            pygame.time.wait(2000)
            self.state = STATE_EXPLORING
            self.user_answer = ""
            self.feedback = ""

    def run(self):
        """Bucle principal del juego."""
        clock = pygame.time.Clock()

        while True:
            self.handle_input()
            
            SCREEN.fill(DARK_BLUE)
            
            if self.state == STATE_EXPLORING:
                self.player.update()
                self.check_collisions()
                self.all_sprites.draw(SCREEN)

                # Dibuja la puntuación
                score_text = font_medium.render(f"Puntaje: {self.puntaje}", True, WHITE)
                SCREEN.blit(score_text, (10, 10))
                
            elif self.state == STATE_LOADING:
                loading_text = font_large.render("Cargando pregunta...", True, WHITE)
                text_rect = loading_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                SCREEN.blit(loading_text, text_rect)
            
            elif self.state == STATE_CHALLENGE:
                # Dibuja la pantalla de desafío
                pygame.draw.rect(SCREEN, BLACK, (50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100))
                pygame.draw.rect(SCREEN, WHITE, (50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100), 2)
                
                # Pregunta
                question_text = font_medium.render("Transforma la oración:", True, WHITE)
                SCREEN.blit(question_text, (70, 70))
                
                original_sentence = font_small.render(self.pregunta_actual['oracion_original'], True, WHITE)
                SCREEN.blit(original_sentence, (70, 120))
                
                transformation_text = font_small.render(f"Tipo de transformación: {self.pregunta_actual['tipo_transformacion']}", True, WHITE)
                SCREEN.blit(transformation_text, (70, 160))

                # Caja de texto para la respuesta
                input_box_rect = pygame.Rect(70, 220, SCREEN_WIDTH - 140, 50)
                pygame.draw.rect(SCREEN, INPUT_BOX_COLOR, input_box_rect)
                text_surface = font_medium.render(self.user_answer, True, BLACK)
                SCREEN.blit(text_surface, (input_box_rect.x + 5, input_box_rect.y + 5))

                # Botón de enviar (solo visual, se usa Enter)
                submit_button_text = font_medium.render("Enter para Enviar", True, WHITE)
                submit_button_rect = submit_button_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
                SCREEN.blit(submit_button_text, submit_button_rect)

                # Feedback
                feedback_text = font_medium.render(self.feedback, True, VIBRANT_GREEN if "Correcto" in self.feedback else VIBRANT_RED)
                feedback_rect = feedback_text.get_rect(center=(SCREEN_WIDTH // 2, 450))
                SCREEN.blit(feedback_text, feedback_rect)

            pygame.display.flip()
            clock.tick(60)

if __name__ == '__main__':
    inicializar_db()
    game = Game()
    game.run()
