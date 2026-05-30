import os
import random
from dataclasses import dataclass
from typing import List, Optional, Tuple
from enum import Enum

# Tipos de oraciones
class SentenceType(Enum):
    AFFIRMATIVE = "afirmativa"
    NEGATIVE = "negativa"
    INTERROGATIVE = "interrogativa"
    EXCLAMATORY = "exclamativa"
    IMPERATIVE = "imperativa"

# Estructuras de datos
@dataclass
class GrammarRule:
    title: str
    explanation: str
    examples: List[str]
    structure: str

@dataclass
class ExampleSentence:
    sentence: str
    type: SentenceType
    translation: str
    explanation: str

@dataclass
class Exercise:
    exercise_id: int
    type: str
    question: str
    options: Optional[List[str]]
    correct_answer: str
    explanation: str
    difficulty: str = "beginner"

@dataclass
class Lesson:
    lesson_id: int
    title: str
    objectives: List[str]
    grammar_rules: List[GrammarRule]
    examples: List[ExampleSentence]
    exercises: List[Exercise]

# Lección 1: La Oración Simple y sus Tipos
def create_lesson_simple_sentence():
    return Lesson(
        lesson_id=1,
        title="La Oración Simple y sus Tipos",
        objectives=[
            "Identificar los diferentes tipos de oraciones simples",
            "Comprender la estructura básica de cada tipo de oración",
            "Transformar oraciones entre diferentes tipos",
            "Construir oraciones correctas de cada tipo"
        ],
        grammar_rules=[
            GrammarRule(
                title="Oración Afirmativa",
                explanation="Expresa una acción, hecho o idea de forma positiva.",
                examples=["She reads books.", "They play soccer.", "I study English."],
                structure="Sujeto + Verbo + Complemento"
            ),
            GrammarRule(
                title="Oración Negativa",
                explanation="Expresa la negación de una acción, hecho o idea.",
                examples=["She does not read books.", "They don't play soccer.", "I do not study English."],
                structure="Sujeto + Auxiliar Negativo (do not/does not) + Verbo + Complemento"
            ),
            GrammarRule(
                title="Oración Interrogativa",
                explanation="Formula una pregunta para obtener información.",
                examples=["Does she read books?", "Do they play soccer?", "Do you study English?"],
                structure="Auxiliar (Do/Does) + Sujeto + Verbo + Complemento + ?"
            ),
            GrammarRule(
                title="Oración Exclamativa",
                explanation="Expresa una emoción, sorpresa o énfasis.",
                examples=["What a beautiful day!", "How interesting that book is!", "I'm so happy!"],
                structure="What/How + [elemento exclamativo] + Sujeto + Verbo + !"
            ),
            GrammarRule(
                title="Oración Imperativa",
                explanation="Expresa una orden, consejo, solicitud o prohibición.",
                examples=["Read this book.", "Please help me.", "Don't touch that."],
                structure="Verbo + Complemento (sujeto tácito 'you')"
            )
        ],
        examples=[
            ExampleSentence(
                "Cats sleep a lot.",
                SentenceType.AFFIRMATIVE,
                "Los gatos duermen mucho.",
                "Oración afirmativa que describe un hecho"
            ),
            ExampleSentence(
                "Dogs don't like cats.",
                SentenceType.NEGATIVE,
                "A los perros no les gustan los gatos.",
                "Oración negativa que expresa una negación"
            ),
            ExampleSentence(
                "Do you speak English?",
                SentenceType.INTERROGATIVE,
                "¿Hablas inglés?",
                "Oración interrogativa que formula una pregunta"
            ),
            ExampleSentence(
                "What a beautiful day!",
                SentenceType.EXCLAMATORY,
                "¡Qué día tan hermoso!",
                "Oración exclamativa que expresa admiración"
            ),
            ExampleSentence(
                "Open the window, please.",
                SentenceType.IMPERATIVE,
                "Abre la ventana, por favor.",
                "Oración imperativa que expresa una petición"
            )
        ],
        exercises=[
            # Ejercicio 1: Identificación de tipos
            Exercise(
                exercise_id=1,
                type="sentence_identification",
                question="Identifica el tipo de oración: 'Students study for exams.'",
                options=[t.value for t in SentenceType],
                correct_answer="afirmativa",
                explanation="Es una oración afirmativa que expresa un hecho."
            ),
            # Ejercicio 2: Transformación afirmativa → negativa
            Exercise(
                exercise_id=2,
                type="sentence_transformation",
                question="Transforma a negativa: 'She plays the piano.'",
                options=None,
                correct_answer="She does not play the piano.",
                explanation="Añadimos 'does not' antes del verbo (porque 'she' es tercera persona singular)."
            ),
            # Ejercicio 3: Transformación afirmativa → interrogativa
            Exercise(
                exercise_id=3,
                type="sentence_transformation",
                question="Transforma a interrogativa: 'They speak French.'",
                options=None,
                correct_answer="Do they speak French?",
                explanation="Añadimos 'Do' al inicio e invertimos el orden (sujeto después del auxiliar)."
            ),
            # Ejercicio 4: Identificación de tipos
            Exercise(
                exercise_id=4,
                type="sentence_identification",
                question="Identifica el tipo de oración: 'What an amazing performance!'",
                options=[t.value for t in SentenceType],
                correct_answer="exclamativa",
                explanation="Es una oración exclamativa que expresa admiración."
            ),
            # Ejercicio 5: Construcción de oración
            Exercise(
                exercise_id=5,
                type="sentence_construction",
                question="Construye una oración imperativa con estas palabras: the / door / Close",
                options=None,
                correct_answer="Close the door.",
                explanation="Las oraciones imperativas comienzan con el verbo en forma base."
            ),
            # Ejercicio 6: Transformación interrogativa → afirmativa
            Exercise(
                exercise_id=6,
                type="sentence_transformation",
                question="Transforma a afirmativa: 'Does he work here?'",
                options=None,
                correct_answer="He works here.",
                explanation="Eliminamos el auxiliar 'does' y el verbo vuelve a su forma con -s (tercera persona)."
            ),
            # Ejercicio 7: Identificación de tipos
            Exercise(
                exercise_id=7,
                type="sentence_identification",
                question="Identifica el tipo de oración: 'Don't touch that button.'",
                options=[t.value for t in SentenceType],
                correct_answer="imperativa",
                explanation="Es una oración imperativa negativa que expresa una prohibición."
            ),
            # Ejercicio 8: Transformación negativa → afirmativa
            Exercise(
                exercise_id=8,
                type="sentence_transformation",
                question="Transforma a afirmativa: 'I don't like coffee.'",
                options=None,
                correct_answer="I like coffee.",
                explanation="Eliminamos 'don't' para convertir la negación en afirmación."
            ),
            # Ejercicio 9: Construcción de oración
            Exercise(
                exercise_id=9,
                type="sentence_construction",
                question="Construye una oración exclamativa: beautiful / What / day / a",
                options=None,
                correct_answer="What a beautiful day!",
                explanation="Las exclamativas con 'what' siguen el patrón: What + (a/an) + adjetivo + sustantivo"
            ),
            # Ejercicio 10: Identificación múltiple
            Exercise(
                exercise_id=10,
                type="multiple_identification",
                question="Selecciona todas las oraciones interrogativas:",
                options=[
                    "Where are you going?",
                    "I'm studying English.",
                    "Do they like pizza?",
                    "What time is it?",
                    "She doesn't know the answer."
                ],
                correct_answer="1,3,4",  # Índices de las oraciones interrogativas
                explanation="Las oraciones interrogativas son: 'Where are you going?', 'Do they like pizza?' y 'What time is it?'"
            )
        ]
    )

# Sistema de evaluación
class SentenceEvaluator:
    @staticmethod
    def evaluate_identification(user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.lower()
    
    @staticmethod
    def evaluate_transformation(user_answer, correct_answer):
        # Normalizar para comparación (minúsculas, sin espacios extras, sin diferencia en puntuación)
        normalized_user = " ".join(user_answer.strip().lower().split())
        normalized_correct = " ".join(correct_answer.strip().lower().split())
        
        # Permitir variaciones en contracciones (don't vs do not)
        variations = {
            "does not": "doesn't",
            "do not": "don't",
            "is not": "isn't",
            "are not": "aren't"
        }
        
        # Verificar si es igual o una variación aceptable
        if normalized_user == normalized_correct:
            return True
        
        # Verificar variaciones
        for formal, contraction in variations.items():
            if (normalized_user == normalized_correct.replace(formal, contraction) or 
                normalized_user == normalized_correct.replace(contraction, formal)):
                return True
        
        return False
    
    @staticmethod
    def evaluate_construction(user_answer, correct_answer):
        return SentenceEvaluator.evaluate_transformation(user_answer, correct_answer)
    
    @staticmethod
    def evaluate_multiple_identification(user_answer, correct_answer):
        # Formato esperado: "1,3,4" o "1 3 4"
        user_selections = []
        if "," in user_answer:
            user_selections = [item.strip() for item in user_answer.split(",")]
        else:
            user_selections = user_answer.split()
        
        correct_selections = correct_answer.split(",")
        
        return set(user_selections) == set(correct_selections)

# Interfaz de consola
class SimpleSentenceConsoleApp:
    def __init__(self):
        self.lesson = create_lesson_simple_sentence()
        self.score = 0
        self.total_exercises = len(self.lesson.exercises)
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        self.clear_screen()
        print("=" * 70)
        print("           LA ORACIÓN SIMPLE Y SUS TIPOS")
        print("=" * 70)
        print("\nBienvenido a la lección sobre tipos de oraciones simples en inglés.")
        print("Aprenderás a identificar, transformar y construir diferentes tipos")
        print("de oraciones: afirmativas, negativas, interrogativas, exclamativas e imperativas.\n")
        input("Presiona Enter para continuar...")
    
    def display_lesson_intro(self):
        self.clear_screen()
        print("=" * 70)
        print(f"LECCIÓN {self.lesson.lesson_id}: {self.lesson.title}")
        print("=" * 70)
        
        print("\nOBJETIVOS:")
        for i, objective in enumerate(self.lesson.objectives, 1):
            print(f"  {i}. {objective}")
        
        print("\nREGLAS GRAMATICALES:")
        for rule in self.lesson.grammar_rules:
            print(f"\n  {rule.title.upper()}")
            print(f"  {rule.explanation}")
            print(f"  Estructura: {rule.structure}")
            print("  Ejemplos:")
            for example in rule.examples:
                print(f"    • {example}")
        
        print("\nEJEMPLOS:")
        for example in self.lesson.examples:
            print(f"  • {example.sentence} ({example.type.value})")
            print(f"    Traducción: {example.translation}")
            print(f"    Explicación: {example.explanation}")
        
        print("\n" + "-" * 70)
        input("Presiona Enter para comenzar los ejercicios...")
    
    def display_exercise(self, exercise, index):
        self.clear_screen()
        print(f"Ejercicio {index} de {self.total_exercises}")
        print("-" * 50)
        print(f"{exercise.question}\n")
        
        if exercise.options:
            if exercise.type == "sentence_identification":
                print("Opciones:")
                for i, option in enumerate(exercise.options, 1):
                    print(f"  {i}. {option}")
                print()
                return input("Tu respuesta (número): ")
            
            elif exercise.type == "multiple_identification":
                print("Opciones:")
                for i, option in enumerate(exercise.options, 1):
                    print(f"  {i}. {option}")
                print("\nFormato de respuesta: números separados por comas (ej: 1,3,4)")
                return input("Tu respuesta: ")
        
        return input("Tu respuesta: ")
    
    def evaluate_answer(self, exercise, user_answer):
        evaluator = SentenceEvaluator()
        
        if exercise.type == "sentence_identification":
            # Convertir número de opción a texto
            if user_answer.isdigit():
                index = int(user_answer) - 1
                if 0 <= index < len(exercise.options):
                    user_answer = exercise.options[index]
            
            return evaluator.evaluate_identification(user_answer, exercise.correct_answer)
        
        elif exercise.type == "sentence_transformation":
            return evaluator.evaluate_transformation(user_answer, exercise.correct_answer)
        
        elif exercise.type == "sentence_construction":
            return evaluator.evaluate_construction(user_answer, exercise.correct_answer)
        
        elif exercise.type == "multiple_identification":
            return evaluator.evaluate_multiple_identification(user_answer, exercise.correct_answer)
        
        return False
    
    def display_feedback(self, is_correct, explanation, correct_answer=None):
        if is_correct:
            print("✅ ¡Correcto!")
        else:
            print("❌ Incorrecto")
            if correct_answer:
                print(f"La respuesta correcta es: {correct_answer}")
        print(f"Explicación: {explanation}\n")
    
    def run_exercises(self):
        self.score = 0
        
        for i, exercise in enumerate(self.lesson.exercises, 1):
            user_answer = self.display_exercise(exercise, i)
            is_correct = self.evaluate_answer(exercise, user_answer)
            
            if is_correct:
                self.score += 1
            
            self.display_feedback(is_correct, exercise.explanation, 
                                 exercise.correct_answer if not is_correct else None)
            
            input("Presiona Enter para continuar...")
    
    def display_summary(self):
        self.clear_screen()
        print("=" * 70)
        print("         RESUMEN DE LA LECCIÓN")
        print("=" * 70)
        print(f"Lección: {self.lesson.title}")
        print(f"Ejercicios completados: {self.total_exercises}")
        print(f"Respuestas correctas: {self.score}")
        percentage = (self.score / self.total_exercises) * 100
        print(f"Puntuación: {self.score}/{self.total_exercises} ({percentage:.1f}%)")
        
        # Evaluación del desempeño
        if percentage >= 90:
            print("\n🎉 ¡Excelente! Dominaste completamente los tipos de oraciones.")
        elif percentage >= 70:
            print("\n👍 Buen trabajo, pero podrías repasar algunos conceptos.")
        else:
            print("\n📚 Necesitas repasar esta lección antes de continuar.")
        
        # Mostrar áreas de mejora basadas en los ejercicios fallidos
        print("\n" + "=" * 70)
        
        # Recomendaciones de estudio
        print("\nRECOMENDACIONES:")
        if percentage < 100:
            print("  - Repasa las reglas de transformación entre tipos de oraciones")
            print("  - Practica la identificación de oraciones en contextos reales")
            print("  - Estudia las estructuras específicas de cada tipo de oración")
        else:
            print("  - ¡Perfecto! Ahora practica con textos más complejos")
            print("  - Intenta escribir párrafos usando diferentes tipos de oraciones")
        
        print("\n" + "=" * 70)
        input("Presiona Enter para volver al menú principal...")
    
    def run(self):
        self.display_welcome()
        self.display_lesson_intro()
        self.run_exercises()
        self.display_summary()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = SimpleSentenceConsoleApp()
    app.run()
