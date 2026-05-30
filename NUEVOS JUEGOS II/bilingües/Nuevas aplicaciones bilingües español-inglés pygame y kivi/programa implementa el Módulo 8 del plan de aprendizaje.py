# Este programa implementa el Módulo 8 del plan de aprendizaje,
# enfocándose en el diseño de una interfaz de usuario completa y robusta.
# Se utiliza Pygame para la visualización y SQLite para la gestión de datos.

import pygame
import sqlite3
import random
import os

# Initialize Pygame
pygame.init()

# --- Screen and Clock Settings ---
ANCHO, ALTO = 1000, 700
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Sintaxis - Módulo 8")
RELOJ = pygame.time.Clock()
FPS = 60

# --- Colors and Fonts ---
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_OSCURO = (30, 30, 40)
GRIS_MEDIO = (50, 50, 60)
VERDE_CLARO = (124, 252, 0)
ROJO_CLARO = (255, 99, 71)

FONT_TITULO = pygame.font.Font(None, 60)
FONT_NORMAL = pygame.font.Font(None, 35)
FONT_PREGUNTA = pygame.font.Font(None, 28)
FONT_FEEDBACK = pygame.font.Font(None, 30)

# --- Database Configuration ---
DB_NAME = "preguntas.db"

def inicializar_db():
    """Connects to the database and creates the table if it does not exist,
       inserting initial data if the table is empty."""
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

# --- Game Classes ---

class Boton:
    """Class to create simple buttons."""
    def __init__(self, x, y, ancho, alto, texto, color_base, color_hover, comando):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color_base = color_base
        self.color_hover = color_hover
        self.comando = comando
        self.texto_renderizado = FONT_NORMAL.render(self.texto, True, BLANCO)
        self.texto_rect = self.texto_renderizado.get_rect(center=self.rect.center)

    def dibujar(self, pantalla):
        mouse_pos = pygame.mouse.get_pos()
        color_actual = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_base
        pygame.draw.rect(pantalla, color_actual, self.rect, border_radius=10)
        pantalla.blit(self.texto_renderizado, self.texto_rect)

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(evento.pos):
                self.comando()

class ParticulaAnimada:
    """Class to create particles with advanced animation."""
    def __init__(self, x, y, emoticon, color):
        self.x, self.y = x, y
        self.emoticon = emoticon
        self.color = color
        self.velocidad_x = random.uniform(-1, 1)
        self.velocidad_y = random.uniform(-3, -1)
        self.vida = 100
        self.font = pygame.font.Font(None, 20)

    def actualizar(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        self.velocidad_y += 0.05
        self.vida -= 1

    def dibujar(self, pantalla):
        superficie_texto = self.font.render(self.emoticon, True, self.color)
        pantalla.blit(superficie_texto, (self.x, self.y))

class JuegoSintaxis:
    def __init__(self):
        self.estado_juego = "menu_principal"
        self.puntaje = 0
        self.preguntas_jugadas_ids = []
        self.pregunta_actual = None
        self.preguntas_correctas_nivel = 0
        self.correctas_para_subir = 3
        self.dificultad_actual = 1
        self.mensaje_feedback = ""
        self.particulas = []
        self.input_box_rect = pygame.Rect(ANCHO // 2 - 250, ALTO // 2 + 100, 500, 50)
        self.input_text = ""
        self.input_activo = False
        self.reloj_feedback = 0

        self.botones_menu_principal = [
            Boton(ANCHO // 2 - 100, ALTO // 2 - 50, 200, 60, "Jugar", GRIS_MEDIO, BLANCO, lambda: self.cambiar_estado("jugando")),
            Boton(ANCHO // 2 - 100, ALTO // 2 + 30, 200, 60, "Estadísticas", GRIS_MEDIO, BLANCO, lambda: self.cambiar_estado("estadisticas")),
            Boton(ANCHO // 2 - 100, ALTO // 2 + 110, 200, 60, "Ayuda", GRIS_MEDIO, BLANCO, lambda: self.cambiar_estado("ayuda")),
            Boton(ANCHO // 2 - 100, ALTO // 2 + 190, 200, 60, "Salir", GRIS_MEDIO, BLANCO, lambda: self.cambiar_estado("salir"))
        ]
        
        self.botones_estadisticas = [
            Boton(ANCHO // 2 - 100, ALTO - 100, 200, 60, "Volver", GRIS_MEDIO, BLANCO, lambda: self.cambiar_estado("menu_principal"))
        ]
        
        self.botones_ayuda = [
            Boton(ANCHO // 2 - 100, ALTO - 100, 200, 60, "Volver", GRIS_MEDIO, BLANCO, lambda: self.cambiar_estado("menu_principal"))
        ]
        
        self.botones_juego = [
            Boton(ANCHO - 150, 50, 100, 40, "Menú", GRIS_MEDIO, BLANCO, lambda: self.cambiar_estado("menu_principal"))
        ]
        
        self.botones_resultados = [
            Boton(ANCHO // 2 - 100, ALTO // 2 + 100, 200, 60, "Jugar de Nuevo", GRIS_MEDIO, BLANCO, lambda: self.iniciar_juego())
        ]

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado == "jugando":
            self.iniciar_juego()
        elif nuevo_estado == "salir":
            pygame.quit()
            exit()
        self.estado_juego = nuevo_estado

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if self.estado_juego == "menu_principal":
                for boton in self.botones_menu_principal:
                    boton.manejar_evento(evento)
            elif self.estado_juego == "jugando":
                for boton in self.botones_juego:
                    boton.manejar_evento(evento)
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box_rect.collidepoint(evento.pos):
                        self.input_activo = True
                    else:
                        self.input_activo = False
                
                if evento.type == pygame.KEYDOWN:
                    if self.input_activo:
                        if evento.key == pygame.K_RETURN:
                            self.verificar_respuesta()
                        elif evento.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            self.input_text += evento.unicode
            elif self.estado_juego == "estadisticas":
                for boton in self.botones_estadisticas:
                    boton.manejar_evento(evento)
            elif self.estado_juego == "ayuda":
                for boton in self.botones_ayuda:
                    boton.manejar_evento(evento)
            elif self.estado_juego == "resultados":
                for boton in self.botones_resultados:
                    boton.manejar_evento(evento)

    def iniciar_juego(self):
        self.estado_juego = "jugando"
        self.puntaje = 0
        self.preguntas_jugadas_ids.clear()
        self.dificultad_actual = 1
        self.preguntas_correctas_nivel = 0
        self.obtener_nueva_pregunta()

    def obtener_nueva_pregunta(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM preguntas WHERE dificultad = ?", (self.dificultad_actual,))
        preguntas_disponibles_db = cursor.fetchall()
        
        preguntas_no_jugadas = [p for p in preguntas_disponibles_db if p[0] not in self.preguntas_jugadas_ids]
        
        if preguntas_no_jugadas:
            self.pregunta_actual = random.choice(preguntas_no_jugadas)
            self.preguntas_jugadas_ids.append(self.pregunta_actual[0])
            self.input_text = ""
        else:
            if self.dificultad_actual < 3:
                self.subir_nivel_dificultad()
                self.obtener_nueva_pregunta()
            else:
                self.ir_a_resultados()

        conn.close()

    def verificar_respuesta(self):
        if self.pregunta_actual is None:
            return

        respuesta_correcta = self.pregunta_actual[2].lower().strip()
        respuesta_usuario = self.input_text.lower().strip()
        
        if respuesta_usuario == respuesta_correcta:
            self.mensaje_feedback = "¡Correcto! ✅✨"
            self.puntaje += 1
            self.preguntas_correctas_nivel += 1
            if self.preguntas_correctas_nivel >= self.correctas_para_subir and self.dificultad_actual < 3:
                self.subir_nivel_dificultad()
            self.crear_particulas(True)
        else:
            self.mensaje_feedback = "Incorrecto. ❌💔"
            self.crear_particulas(False)
        
        self.reloj_feedback = pygame.time.get_ticks()
        pygame.time.set_timer(pygame.USEREVENT, 2000)

    def crear_particulas(self, es_correcto):
        emoticones = ["✅", "✨", "🚀", "🎉"] if es_correcto else ["❌", "💔", "😥", "😵"]
        color = VERDE_CLARO if es_correcto else ROJO_CLARO
        for _ in range(30):
            x = self.input_box_rect.centerx + random.randint(-50, 50)
            y = self.input_box_rect.top
            self.particulas.append(ParticulaAnimada(x, y, random.choice(emoticones), color))

    def subir_nivel_dificultad(self):
        self.dificultad_actual += 1
        self.preguntas_correctas_nivel = 0
        self.mensaje_feedback = f"¡Subiste a Dificultad {self.dificultad_actual}! 🎉"

    def ir_a_resultados(self):
        self.estado_juego = "resultados"
        self.reloj_feedback = 0

    def dibujar_pantalla(self):
        PANTALLA.fill(GRIS_OSCURO)
        
        if self.estado_juego == "menu_principal":
            self.dibujar_menu_principal()
        elif self.estado_juego == "jugando":
            self.dibujar_juego()
        elif self.estado_juego == "estadisticas":
            self.dibujar_estadisticas()
        elif self.estado_juego == "ayuda":
            self.dibujar_ayuda()
        elif self.estado_juego == "resultados":
            self.dibujar_resultados()

        for particula in self.particulas[:]:
            particula.actualizar()
            particula.dibujar(PANTALLA)
            if particula.vida <= 0:
                self.particulas.remove(particula)
        
        pygame.display.flip()

    def dibujar_menu_principal(self):
        titulo_texto = FONT_TITULO.render("Menú Principal", True, BLANCO)
        titulo_rect = titulo_texto.get_rect(center=(ANCHO // 2, ALTO // 2 - 150))
        PANTALLA.blit(titulo_texto, titulo_rect)
        for boton in self.botones_menu_principal:
            boton.dibujar(PANTALLA)

    def dibujar_juego(self):
        s = pygame.Surface((ANCHO - 100, ALTO - 200), pygame.SRCALPHA)
        s.fill((50, 50, 60, 150))
        pygame.draw.rect(s, (100, 100, 100, 50), (0, 0, ANCHO-100, ALTO-200), border_radius=20)
        PANTALLA.blit(s, (50, 100))
        
        for boton in self.botones_juego:
            boton.dibujar(PANTALLA)
        
        puntaje_texto = FONT_NORMAL.render(f"Puntaje: {self.puntaje}", True, BLANCO)
        dificultad_texto = FONT_NORMAL.render(f"Dificultad: {self.dificultad_actual}", True, BLANCO)
        idioma_texto = FONT_NORMAL.render(self.pregunta_actual[4].capitalize(), True, BLANCO)
        
        PANTALLA.blit(puntaje_texto, (50, 50))
        PANTALLA.blit(dificultad_texto, (ANCHO - 250, 50))
        PANTALLA.blit(idioma_texto, (ANCHO // 2 - idioma_texto.get_width() // 2, 50))

        tipo_texto = FONT_NORMAL.render(f"Transforma a: {self.pregunta_actual[3].capitalize()}", True, BLANCO)
        pregunta_texto = FONT_PREGUNTA.render(self.pregunta_actual[1], True, BLANCO)

        tipo_rect = tipo_texto.get_rect(center=(ANCHO // 2, ALTO // 2 - 100))
        pregunta_rect = pregunta_texto.get_rect(center=(ANCHO // 2, ALTO // 2))

        PANTALLA.blit(tipo_texto, tipo_rect)
        PANTALLA.blit(pregunta_texto, pregunta_rect)

        pygame.draw.rect(PANTALLA, BLANCO, self.input_box_rect, border_radius=5)
        superficie_texto_entrada = FONT_NORMAL.render(self.input_text, True, NEGRO)
        PANTALLA.blit(superficie_texto_entrada, (self.input_box_rect.x + 5, self.input_box_rect.y + 5))
        
        if self.mensaje_feedback:
            feedback_texto = FONT_FEEDBACK.render(self.mensaje_feedback, True, VERDE_CLARO)
            feedback_rect = feedback_texto.get_rect(center=(ANCHO // 2, ALTO // 2 + 50))
            PANTALLA.blit(feedback_texto, feedback_rect)

    def dibujar_estadisticas(self):
        titulo_texto = FONT_TITULO.render("Estadísticas", True, BLANCO)
        titulo_rect = titulo_texto.get_rect(center=(ANCHO // 2, 100))
        PANTALLA.blit(titulo_texto, titulo_rect)
        
        # Simulated Stats
        stats_data = [
            ("Puntaje más alto:", "150"),
            ("Oraciones correctas:", "75"),
            ("Dificultad máxima alcanzada:", "3")
        ]
        
        y_offset = 200
        for label, value in stats_data:
            label_text = FONT_NORMAL.render(label, True, BLANCO)
            value_text = FONT_NORMAL.render(value, True, VERDE_CLARO)
            PANTALLA.blit(label_text, (ANCHO // 2 - 150, y_offset))
            PANTALLA.blit(value_text, (ANCHO // 2 + 50, y_offset))
            y_offset += 60

        for boton in self.botones_estadisticas:
            boton.dibujar(PANTALLA)

    def dibujar_ayuda(self):
        titulo_texto = FONT_TITULO.render("Ayuda", True, BLANCO)
        titulo_rect = titulo_texto.get_rect(center=(ANCHO // 2, 100))
        PANTALLA.blit(titulo_texto, titulo_rect)
        
        help_text_lines = [
            "Instrucciones:",
            "1. Elige una opción del menú principal.",
            "2. En el juego, traduce la oración original a su equivalente en el idioma y la sintaxis especificada.",
            "3. Escribe tu respuesta en el cuadro de texto y presiona 'Enter'.",
            "4. Si tu respuesta es correcta, tu puntaje subirá.",
            "5. Para pasar de nivel, necesitas acertar 3 oraciones."
        ]
        
        y_offset = 200
        for line in help_text_lines:
            help_line_text = FONT_NORMAL.render(line, True, BLANCO)
            PANTALLA.blit(help_line_text, (100, y_offset))
            y_offset += 40

        for boton in self.botones_ayuda:
            boton.dibujar(PANTALLA)

    def dibujar_resultados(self):
        titulo_texto = FONT_TITULO.render("¡Resultados Finales!", True, BLANCO)
        titulo_rect = titulo_texto.get_rect(center=(ANCHO // 2, ALTO // 2 - 150))
        PANTALLA.blit(titulo_texto, titulo_rect)
        
        puntaje_texto = FONT_NORMAL.render(f"Tu puntaje es: {self.puntaje}", True, BLANCO)
        puntaje_rect = puntaje_texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        PANTALLA.blit(puntaje_texto, puntaje_rect)

        for boton in self.botones_resultados:
            boton.dibujar(PANTALLA)

    def correr(self):
        inicializar_db()
        while True:
            self.manejar_eventos()
            self.dibujar_pantalla()
            RELOJ.tick(FPS)
            
            if self.reloj_feedback and (pygame.time.get_ticks() - self.reloj_feedback > 2000):
                self.reloj_feedback = 0
                self.mensaje_feedback = ""
                if self.estado_juego == "jugando":
                    self.obtener_nueva_pregunta()

if __name__ == "__main__":
    juego = JuegoSintaxis()
    juego.correr()
