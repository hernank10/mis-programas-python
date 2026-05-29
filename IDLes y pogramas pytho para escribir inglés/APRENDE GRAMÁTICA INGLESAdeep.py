import json
import random
from dataclasses import dataclass
from typing import List, Optional
import os

# Estructuras de datos
@dataclass
class VocabularyItem:
    word: str
    translation: str
    category: str
    example: str

@dataclass
class Exercise:
    exercise_id: int
    type: str
    question: str
    options: Optional[List[str]]
    correct_answer: str
    explanation: str

@dataclass
class Lesson:
    lesson_id: int
    title: str
    objectives: List[str]
    grammar_rules: List[str]
    vocabulary: List[VocabularyItem]
    exercises: List[Exercise]

# Lección 1: Verbo "To Be" en presente
def create_lesson_1():
    return Lesson(
        lesson_id=1,
        title="El Verbo 'To Be' en Presente",
        objectives=[
            "Identificar las formas del verbo 'to be'",
            "Construir oraciones afirmativas, negativas e interrogativas",
            "Utilizar correctamente los pronombres personales"
        ],
        grammar_rules=[
            "El verbo 'to be' (ser/estar) tiene formas diferentes según el pronombre:",
            "I → am, You → are, He/She/It → is, We → are, They → are",
            "Para formar negativas: añadir 'not' después del verbo",
            "Para formar interrogativas: invertir el orden (verbo + sujeto)"
        ],
        vocabulary=[
            VocabularyItem("I", "yo", "pronoun", "I am here"),
            VocabularyItem("you", "tú/usted", "pronoun", "You are nice"),
            VocabularyItem("he", "él", "pronoun", "He is tall"),
            VocabularyItem("she", "ella", "pronoun", "She is a doctor"),
            VocabularyItem("it", "eso/ella/él (objeto/animal)", "pronoun", "It is a book"),
            VocabularyItem("we", "nosotros", "pronoun", "We are students"),
            VocabularyItem("they", "ellos/ellas", "pronoun", "They are friends"),
            VocabularyItem("student", "estudiante", "noun", "I am a student"),
            VocabularyItem("teacher", "profesor", "noun", "She is a teacher"),
            VocabularyItem("doctor", "doctor", "noun", "He is a doctor")
        ],
        exercises=[
            Exercise(
                exercise_id=1,
                type="fill_blank",
                question="Complete la oración: I ___ a student.",
                options=None,
                correct_answer="am",
                explanation="Con el pronombre 'I' usamos 'am'"
            ),
            Exercise(
                exercise_id=2,
                type="multiple_choice",
                question="Seleccione la forma correcta: He ___ a doctor.",
                options=["am", "is", "are", "be"],
                correct_answer="is",
                explanation="Con 'he/she/it' usamos 'is'"
            ),
            Exercise(
                exercise_id=3,
                type="transformation",
                question="Transforme a negativo: She is a teacher.",
                options=None,
                correct_answer="She is not a teacher",
                explanation="Añadimos 'not' después del verbo"
            ),
            Exercise(
                exercise_id=4,
                type="transformation",
                question="Transforme a interrogativa: They are students.",
                options=None,
                correct_answer="Are they students?",
                explanation="Invertimos el orden: verbo + sujeto"
            ),
            Exercise(
                exercise_id=5,
                type="matching",
                question="Relacione los pronombres con la forma correcta de 'to be':",
                options=["I", "You", "He", "We", "They"],
                correct_answer="I-am,You-are,He-is,We-are,They-are",
                explanation="Cada pronombre tiene su forma específica"
            ),
            Exercise(
                exercise_id=6,
                type="fill_blank",
                question="Complete la oración: We ___ from Spain.",
                options=None,
                correct_answer="are",
                explanation="Con 'we' usamos 'are'"
            ),
            Exercise(
                exercise_id=7,
                type="multiple_choice",
                question="Seleccione la forma correcta: It ___ a book.",
                options=["am", "is", "are", "be"],
                correct_answer="is",
                explanation="Con 'it' usamos 'is'"
            ),
            Exercise(
                exercise_id=8,
                type="transformation",
                question="Transforme a negativo: You are my friend.",
                options=None,
                correct_answer="You are not my friend",
                explanation="Añadimos 'not' después del verbo"
            ),
            Exercise(
                exercise_id=9,
                type="error_correction",
                question="Corrija el error: I is a student.",
                options=None,
                correct_answer="I am a student",
                explanation="Con 'I' usamos 'am', no 'is'"
            ),
            Exercise(
                exercise_id=10,
                type="sentence_formation",
                question="Forme una oración con estas palabras: are / friends / We / .",
                options=None,
                correct_answer="We are friends.",
                explanation="El orden correcto es: Sujeto + verbo + complemento"
            )
        ]
    )

# Sistema de evaluación
class ExerciseEvaluator:
    @staticmethod
    def evaluate_fill_blank(user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.lower()
    
    @staticmethod
    def evaluate_multiple_choice(user_answer, correct_answer, options):
        # Asumimos que el usuario ingresa el número de opción (1, 2, 3...)
        try:
            index = int(user_answer) - 1
            return options[index] == correct_answer
        except (ValueError, IndexError):
            return False
    
    @staticmethod
    def evaluate_transformation(user_answer, correct_answer):
        # Normalizar para comparación (minúsculas, sin espacios extras)
        normalized_user = " ".join(user_answer.strip().lower().split())
        normalized_correct = " ".join(correct_answer.strip().lower().split())
        return normalized_user == normalized_correct
    
    @staticmethod
    def evaluate_matching(user_answer, correct_answer):
        # Formato esperado: "1-2,3-4,5-1" o similar
        user_pairs = sorted([pair.strip() for pair in user_answer.split(',')])
        correct_pairs = sorted([pair.strip() for pair in correct_answer.split(',')])
        return user_pairs == correct_pairs
    
    @staticmethod
    def evaluate_error_correction(user_answer, correct_answer):
        return ExerciseEvaluator.evaluate_transformation(user_answer, correct_answer)
    
    @staticmethod
    def evaluate_sentence_formation(user_answer, correct_answer):
        return ExerciseEvaluator.evaluate_transformation(user_answer, correct_answer)

# Interfaz de consola
class ConsoleGrammarApp:
    def __init__(self):
        self.lessons = [create_lesson_1()]
        self.current_lesson = None
        self.score = 0
        self.total_exercises = 0
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        self.clear_screen()
        print("=" * 60)
        print("          APRENDE GRAMÁTICA INGLESA")
        print("=" * 60)
        print("\nBienvenido al programa de aprendizaje de gramática inglesa.")
        print("Este programa te ayudará a dominar las reglas gramaticales")
        print("a través de lecciones estructuradas y ejercicios prácticos.\n")
        input("Presiona Enter para continuar...")
    
    def display_lesson_menu(self):
        self.clear_screen()
        print("LECCIONES DISPONIBLES:")
        print("-" * 30)
        for i, lesson in enumerate(self.lessons, 1):
            print(f"{i}. {lesson.title}")
        print("0. Salir")
        
        try:
            choice = int(input("\nSelecciona una lección: "))
            if choice == 0:
                return None
            return self.lessons[choice - 1]
        except (ValueError, IndexError):
            print("Opción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")
            return self.display_lesson_menu()
    
    def display_lesson_intro(self, lesson):
        self.clear_screen()
        print("=" * 60)
        print(f"LECCIÓN {lesson.lesson_id}: {lesson.title}")
        print("=" * 60)
        
        print("\nOBJETIVOS:")
        for i, objective in enumerate(lesson.objectives, 1):
            print(f"  {i}. {objective}")
        
        print("\nREGLAS GRAMATICALES:")
        for rule in lesson.grammar_rules:
            print(f"  • {rule}")
        
        print("\nVOCABULARIO:")
        for vocab in lesson.vocabulary:
            print(f"  • {vocab.word}: {vocab.translation}")
            print(f"    Ejemplo: {vocab.example}")
        
        print("\n" + "-" * 60)
        input("Presiona Enter para comenzar los ejercicios...")
    
    def display_exercise(self, exercise, index, total):
        self.clear_screen()
        print(f"Ejercicio {index} de {total}")
        print("-" * 40)
        print(f"{exercise.question}\n")
        
        if exercise.type == "multiple_choice" and exercise.options:
            for i, option in enumerate(exercise.options, 1):
                print(f"  {i}. {option}")
            print()
            return input("Tu respuesta (número): ")
        
        elif exercise.type == "matching" and exercise.options:
            print("Opciones:")
            for i, option in enumerate(exercise.options, 1):
                print(f"  {i}. {option}")
            print("\nFormas de 'to be':")
            print("  a. am   b. are   c. is")
            print("\nFormato de respuesta: número-letra, número-letra, ...")
            print("Ejemplo: 1-a,2-b,3-c")
            return input("\nTu respuesta: ")
        
        else:
            return input("Tu respuesta: ")
    
    def evaluate_answer(self, exercise, user_answer):
        evaluator = ExerciseEvaluator()
        
        if exercise.type == "fill_blank":
            return evaluator.evaluate_fill_blank(user_answer, exercise.correct_answer)
        
        elif exercise.type == "multiple_choice":
            return evaluator.evaluate_multiple_choice(user_answer, exercise.correct_answer, exercise.options)
        
        elif exercise.type == "transformation":
            return evaluator.evaluate_transformation(user_answer, exercise.correct_answer)
        
        elif exercise.type == "matching":
            return evaluator.evaluate_matching(user_answer, exercise.correct_answer)
        
        elif exercise.type == "error_correction":
            return evaluator.evaluate_error_correction(user_answer, exercise.correct_answer)
        
        elif exercise.type == "sentence_formation":
            return evaluator.evaluate_sentence_formation(user_answer, exercise.correct_answer)
        
        return False
    
    def display_feedback(self, is_correct, explanation, correct_answer=None):
        if is_correct:
            print("✅ ¡Correcto!")
        else:
            print("❌ Incorrecto")
            if correct_answer:
                print(f"La respuesta correcta es: {correct_answer}")
        print(f"Explicación: {explanation}\n")
    
    def run_lesson(self, lesson):
        self.current_lesson = lesson
        self.score = 0
        self.total_exercises = len(lesson.exercises)
        
        self.display_lesson_intro(lesson)
        
        for i, exercise in enumerate(lesson.exercises, 1):
            user_answer = self.display_exercise(exercise, i, self.total_exercises)
            is_correct = self.evaluate_answer(exercise, user_answer)
            
            if is_correct:
                self.score += 1
            
            self.display_feedback(is_correct, exercise.explanation, 
                                 exercise.correct_answer if not is_correct else None)
            
            input("Presiona Enter para continuar...")
        
        self.display_lesson_summary()
    
    def display_lesson_summary(self):
        self.clear_screen()
        print("=" * 60)
        print("         RESUMEN DE LA LECCIÓN")
        print("=" * 60)
        print(f"Lección: {self.current_lesson.title}")
        print(f"Ejercicios completados: {self.total_exercises}")
        print(f"Respuestas correctas: {self.score}")
        print(f"Puntuación: {self.score}/{self.total_exercises} ({self.score/self.total_exercises*100:.1f}%)")
        
        if self.score == self.total_exercises:
            print("\n🎉 ¡Excelente! Dominaste completamente esta lección.")
        elif self.score >= self.total_exercises * 0.7:
            print("\n👍 Buen trabajo, pero podrías repasar algunos conceptos.")
        else:
            print("\n📚 Necesitas repasar esta lección antes de continuar.")
        
        print("\n" + "=" * 60)
        input("Presiona Enter para volver al menú principal...")
    
    def save_progress(self):
        # En una versión futura, esto guardaría el progreso en un archivo
        progress = {
            "lesson": self.current_lesson.lesson_id,
            "score": self.score,
            "total": self.total_exercises,
            "percentage": self.score / self.total_exercises * 100
        }
        print("Progreso guardado (simulado).")
    
    def run(self):
        self.display_welcome()
        
        while True:
            selected_lesson = self.display_lesson_menu()
            
            if selected_lesson is None:
                print("¡Gracias por usar el programa! Hasta pronto.")
                break
            
            self.run_lesson(selected_lesson)
            self.save_progress()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = ConsoleGrammarApp()
    app.run()
