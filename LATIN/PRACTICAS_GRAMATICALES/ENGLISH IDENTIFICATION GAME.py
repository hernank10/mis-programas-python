import os
import random
import json
from datetime import datetime

class EnglishGame:
    def __init__(self):
        self.current_level = 1
        self.score = 0
        self.lives = 3
        self.max_lives = 3
        self.unlocked_levels = {1: True, 2: False, 3: False}
        self.completed_levels = set()
        self.streak = 0
        self.max_streak = 0
        self.player_name = ""
        self.save_file = "english_game_save.json"
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_title(self):
        print("=" * 60)
        print("       🎮 ENGLISH IDENTIFICATION GAME 🎮")
        print("=" * 60)
    
    def load_game(self):
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    data = json.load(f)
                    self.unlocked_levels = data.get('unlocked_levels', {1: True, 2: False, 3: False})
                    self.completed_levels = set(data.get('completed_levels', []))
                    self.score = data.get('score', 0)
                    self.max_streak = data.get('max_streak', 0)
                    print(f"Partida cargada para {data.get('player_name', '')}")
                    return True
            except:
                print("Error al cargar la partida guardada.")
        return False
    
    def save_game(self):
        data = {
            'player_name': self.player_name,
            'score': self.score,
            'unlocked_levels': self.unlocked_levels,
            'completed_levels': list(self.completed_levels),
            'max_streak': self.max_streak,
            'save_date': datetime.now().isoformat()
        }
        
        try:
            with open(self.save_file, 'w') as f:
                json.dump(data, f)
            return True
        except:
            return False
    
    def start_game(self):
        self.clear_screen()
        self.show_title()
        
        if not self.player_name:
            self.player_name = input("¡Bienvenido! Por favor, ingresa tu nombre: ").strip()
            if not self.player_name:
                self.player_name = "Jugador"
        
        # Intentar cargar partida previa
        if not self.load_game():
            print(f"¡Hola {self.player_name}! Comenzamos una nueva partida.")
            input("Presiona Enter para continuar...")
        
        self.show_main_menu()
    
    def show_main_menu(self):
        while True:
            self.clear_screen()
            self.show_title()
            print(f"Jugador: {self.player_name} | Puntos: {self.score} | Vidas: {self.lives} ♥")
            print(f"Racha actual: {self.streak} | Mejor racha: {self.max_streak}")
            print("\n" + "=" * 30 + " MENÚ PRINCIPAL " + "=" * 30)
            
            # Mostrar niveles con estado de desbloqueo
            for i in range(1, 4):
                status = "🔓" if self.unlocked_levels.get(i, False) else "🔒"
                completed = " ✓" if i in self.completed_levels else ""
                print(f"{i}. Nivel {i} {status}{completed}")
            
            print("\n4. Módulos de práctica complementaria")
            print("5. Tienda de vidas (100 puntos por vida)")
            print("6. Ver progreso y estadísticas")
            print("7. Guardar y salir")
            print("=" * 60)
            
            choice = input("Selecciona una opción: ")
            
            if choice == "1" and self.unlocked_levels.get(1, False):
                self.play_level(1)
            elif choice == "2" and self.unlocked_levels.get(2, False):
                self.play_level(2)
            elif choice == "3" and self.unlocked_levels.get(3, False):
                self.play_level(3)
            elif choice == "4":
                self.show_practice_modules()
            elif choice == "5":
                self.buy_lives()
            elif choice == "6":
                self.show_stats()
            elif choice == "7":
                if self.save_game():
                    print("¡Partida guardada correctamente!")
                else:
                    print("Error al guardar la partida.")
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida o nivel bloqueado.")
                input("Presiona Enter para continuar...")
    
    def play_level(self, level):
        self.clear_screen()
        print(f"🏁 INICIANDO NIVEL {level} 🏁")
        print(f"Vidas: {self.lives} ♥ | Puntos: {self.score}")
        print("=" * 50)
        
        # Definir preguntas para cada nivel
        questions = []
        if level == 1:
            questions = self.get_level1_questions()
        elif level == 2:
            questions = self.get_level2_questions()
        elif level == 3:
            questions = self.get_level3_questions()
        
        # Mezclar preguntas
        random.shuffle(questions)
        questions = questions[:5]  # Usar solo 5 preguntas por nivel
        
        level_score = 0
        for i, q in enumerate(questions, 1):
            if self.lives <= 0:
                print("❌ ¡Te has quedado sin vidas! Volviendo al menú principal...")
                input("Presiona Enter para continuar...")
                return False
                
            print(f"\nPregunta {i}/5:")
            print(f"{q['question']}")
            user_answer = input("Tu respuesta: ").strip()
            
            if self.check_answer(user_answer, q['answers']):
                print("✅ ¡Correcto! +10 puntos")
                self.score += 10
                level_score += 10
                self.streak += 1
                if self.streak > self.max_streak:
                    self.max_streak = self.streak
                
                # Bonus por racha
                if self.streak % 5 == 0:
                    bonus = self.streak * 2
                    print(f"🎉 ¡Racha de {self.streak} respuestas correctas! +{bonus} puntos de bonus")
                    self.score += bonus
            else:
                print("❌ Incorrecto")
                self.lives -= 1
                self.streak = 0
                print(f"Te quedan {self.lives} vidas")
            
            if q.get('explanation'):
                print(f"💡 {q['explanation']}")
            
            print(f"Puntuación actual: {self.score} | Racha: {self.streak}")
        
        # Verificar si pasó el nivel (al menos 70% de aciertos)
        if level_score >= 35:  # 35/50 = 70%
            print(f"\n🎊 ¡Felicidades! Has completado el nivel {level} con {level_score}/50 puntos")
            self.completed_levels.add(level)
            
            # Desbloquear siguiente nivel si existe
            if level < 3:
                self.unlocked_levels[level + 1] = True
                print(f"🔓 ¡Nivel {level + 1} desbloqueado!")
            
            # Recompensa por completar nivel
            reward = level * 25
            self.score += reward
            print(f"💰 Recompensa por completar nivel: +{reward} puntos")
            
            # Restaurar una vida por completar nivel
            if self.lives < self.max_lives:
                self.lives += 1
                print("❤️ ¡Has ganado una vida extra!")
        else:
            print(f"\n😞 No has alcanzado la puntuación necesaria para pasar el nivel {level}")
            print("Puedes intentarlo de nuevo cuando quieras")
        
        input("\nPresiona Enter para volver al menú...")
        return level_score >= 35
    
    def get_level1_questions(self):
        return [
            {
                "question": "¿Él es alto?",
                "answers": ["Is he tall?", "Is he tall"],
                "explanation": "Usamos 'is' con he/she/it, y la estructura interrogativa invierte el orden"
            },
            {
                "question": "¿Ellos son estudiantes?",
                "answers": ["Are they students?", "Are they students"],
                "explanation": "Usamos 'are' con they/we/you, y la estructura interrogativa invierte el orden"
            },
            {
                "question": "¿Tú eres mexicano?",
                "answers": ["Are you Mexican?", "Are you Mexican"],
                "explanation": "Usamos 'are' con you, y los adjetivos de nacionalidad no llevan artículo"
            },
            {
                "question": "¿Ella es de España?",
                "answers": ["Is she from Spain?", "Is she from Spain"],
                "explanation": "Para preguntar por origen, usamos 'from + país'"
            },
            {
                "question": "¿Nosotros somos amigos?",
                "answers": ["Are we friends?", "Are we friends"],
                "explanation": "Usamos 'are' con we, y los sustantivos plurales no llevan artículo"
            }
        ]
    
    def get_level2_questions(self):
        return [
            {
                "question": "¿Él es un doctor?",
                "answers": ["Is he a doctor?", "Is he a doctor"],
                "explanation": "Los sustantivos singulares contables necesitan artículo indefinido (a/an)"
            },
            {
                "question": "¿Ella es mi hermana?",
                "answers": ["Is she my sister?", "Is she my sister"],
                "explanation": "Los adjetivos posesivos (my, your, his, her) van antes del sustantivo"
            },
            {
                "question": "¿Ellos son nuestros padres?",
                "answers": ["Are they our parents?", "Are they our parents"],
                "explanation": "Parentesco en plural no lleva artículo. 'Our' es el posesivo para we"
            },
            {
                "question": "¿Tú eres el profesor?",
                "answers": ["Are you the teacher?", "Are you the teacher"],
                "explanation": "Usamos 'the' cuando nos referimos a algo específico o único"
            },
            {
                "question": "¿Ella es una buena estudiante?",
                "answers": ["Is she a good student?", "Is she a good student"],
                "explanation": "Los adjetivos (good) van antes del sustantivo (student)"
            }
        ]
    
    def get_level3_questions(self):
        return [
            {
                "question": "¿Él es un desarrollador de software?",
                "answers": ["Is he a software developer?", "Is he a software developer"],
                "explanation": "En inglés, los modificadores van antes del sustantivo"
            },
            {
                "question": "¿Ella es la gerente de recursos humanos?",
                "answers": ["Is she the human resources manager?", "Is she the HR manager"],
                "explanation": "Los sustantivos compuestos se forman con adjetivos + sustantivo"
            },
            {
                "question": "¿Ellos son los dueños de la empresa?",
                "answers": ["Are they the company owners?", "Are they the owners of the company?"],
                "explanation": "Podemos usar el genitivo sajón o la estructura con of"
            },
            {
                "question": "¿Él es una persona de confianza?",
                "answers": ["Is he a trustworthy person?", "Is he a reliable person?"],
                "explanation": "En inglés, preferimos usar un adjetivo compuesto"
            },
            {
                "question": "¿Ella es una esperanza para la familia?",
                "answers": ["Is she a hope for the family?", "Is she hope for the family?"],
                "explanation": "Aunque 'hope' es abstracto, en este contexto contable lleva artículo"
            }
        ]
    
    def check_answer(self, user_answer, correct_answers):
        user_normalized = user_answer.strip().lower()
        correct_normalized = [answer.strip().lower() for answer in correct_answers]
        return user_normalized in correct_normalized
    
    def show_practice_modules(self):
        self.clear_screen()
        print("📚 MÓDULOS DE PRÁCTICA COMPLEMENTARIA")
        print("=" * 50)
        print("Estos módulos no afectan tu progreso en el juego principal")
        print("pero te ayudarán a practicar conceptos específicos.\n")
        
        print("1. Preguntas con Do/Does")
        print("2. Preguntas con Wh- Words")
        print("3. What...like vs How")
        print("4. Diálogos contextualizados")
        print("5. Volver al menú principal")
        
        choice = input("\nSelecciona una opción: ")
        # Aquí podrías implementar los módulos de práctica
        print("Funcionalidad en desarrollo...")
        input("Presiona Enter para continuar...")
    
    def buy_lives(self):
        self.clear_screen()
        print("🛒 TIENDA DE VIDAS")
        print("=" * 50)
        print(f"Tienes {self.score} puntos")
        print("Cada vida adicional cuesta 100 puntos")
        print(f"Tienes {self.lives}/{self.max_lives} vidas")
        
        if self.lives >= self.max_lives:
            print("¡Ya tienes el máximo de vidas!")
            input("Presiona Enter para continuar...")
            return
        
        if self.score < 100:
            print("No tienes puntos suficientes para comprar vidas")
            input("Presiona Enter para continuar...")
            return
        
        confirm = input("¿Quieres comprar una vida por 100 puntos? (s/n): ").lower()
        if confirm == "s":
            self.score -= 100
            self.lives += 1
            print("¡Vida comprada con éxito!")
            print(f"Ahora tienes {self.lives} vidas y {self.score} puntos")
        
        input("Presiona Enter para continuar...")
    
    def show_stats(self):
        self.clear_screen()
        print("📊 ESTADÍSTICAS Y PROGRESO")
        print("=" * 50)
        print(f"Jugador: {self.player_name}")
        print(f"Puntuación total: {self.score}")
        print(f"Mejor racha de respuestas: {self.max_streak}")
        print(f"Niveles completados: {len(self.completed_levels)}/3")
        
        print("\nNiveles desbloqueados:")
        for i in range(1, 4):
            status = "✓" if self.unlocked_levels.get(i, False) else "✗"
            print(f"  Nivel {i}: {status}")
        
        print("\nRecompensas disponibles:")
        print("- Completar nivel 1: 25 puntos ✓" if 1 in self.completed_levels else "- Completar nivel 1: 25 puntos")
        print("- Completar nivel 2: 50 puntos ✓" if 2 in self.completed_levels else "- Completar nivel 2: 50 puntos")
        print("- Completar nivel 3: 75 puntos ✓" if 3 in self.completed_levels else "- Completar nivel 3: 75 puntos")
        print("- Completar todos los niveles: 100 puntos ✓" if len(self.completed_levels) == 3 else "- Completar todos los niveles: 100 puntos")
        
        input("\nPresiona Enter para volver al menú...")

# Ejecutar el juego
if __name__ == "__main__":
    game = EnglishGame()
    game.start_game()
