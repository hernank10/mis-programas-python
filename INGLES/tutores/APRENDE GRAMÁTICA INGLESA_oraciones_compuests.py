import os
import random
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from enum import Enum

# Tipos de oraciones compuestas
class CompoundType(Enum):
    COORDINATED = "coordinada"
    SUBORDINATED = "subordinada"
    CONDITIONAL = "condicional"
    RELATIVE = "relativa"
    CAUSAL = "causal"

# Conectores comunes
class Connectors:
    COORDINATING = ["and", "but", "or", "so", "yet", "for", "nor"]
    SUBORDINATING = ["because", "although", "while", "since", "if", "when", "until"]
    CONDITIONAL = ["if", "unless", "provided that", "as long as"]
    RELATIVE = ["who", "which", "that", "whom", "whose", "where", "when"]
    CAUSAL = ["because", "since", "as", "due to", "owing to"]

# Estructuras de datos
@dataclass
class GrammarRule:
    title: str
    explanation: str
    structure: str
    examples: List[str]
    connectors: List[str]

@dataclass
class ExampleSentence:
    sentence: str
    type: CompoundType
    translation: str
    explanation: str
    connector: str

@dataclass
class Exercise:
    exercise_id: int
    type: str
    question: str
    options: Optional[List[str]]
    correct_answer: str
    explanation: str
    difficulty: str = "intermediate"

@dataclass
class Lesson:
    lesson_id: int
    title: str
    objectives: List[str]
    grammar_rules: List[GrammarRule]
    examples: List[ExampleSentence]
    exercises: List[Exercise]

# Lección 1: La Oración Compuesta y sus Tipos
def create_lesson_compound_sentence():
    return Lesson(
        lesson_id=1,
        title="La Oración Compuesta en Inglés y sus Tipos",
        objectives=[
            "Identificar los diferentes tipos de oraciones compuestas",
            "Comprender el uso de conectores y conjunciones",
            "Diferenciar entre oraciones coordinadas y subordinadas",
            "Construir oraciones compuestas correctamente"
        ],
        grammar_rules=[
            GrammarRule(
                title="Oraciones Coordinadas",
                explanation="Unen dos cláusulas independientes de igual importancia.",
                structure="Cláusula Independiente + Conjunción Coordinativa + Cláusula Independiente",
                examples=[
                    "I like coffee, and my friend prefers tea.",
                    "She studied hard, so she passed the exam.",
                    "He wanted to go out, but it was raining."
                ],
                connectors=Connectors.COORDINATING
            ),
            GrammarRule(
                title="Oraciones Subordinadas",
                explanation="Una cláusula dependiente se une a una cláusula principal.",
                structure="Cláusula Principal + Conjunción Subordinativa + Cláusula Dependiente",
                examples=[
                    "I will call you when I arrive.",
                    "Although it was late, we decided to go out.",
                    "She succeeded because she worked hard."
                ],
                connectors=Connectors.SUBORDINATING
            ),
            GrammarRule(
                title="Oraciones Condicionales",
                explanation="Expresan una condición y su resultado.",
                structure="If + Condición + Resultado / Resultado + if + Condición",
                examples=[
                    "If it rains, we will stay home.",
                    "You will succeed if you work hard.",
                    "Unless you study, you won't pass the exam."
                ],
                connectors=Connectors.CONDITIONAL
            ),
            GrammarRule(
                title="Oraciones de Relativo",
                explanation="Proporcionan información adicional sobre un sustantivo.",
                structure="Sustantivo + Pronombre Relativo + Información Adicional",
                examples=[
                    "The book that I read was fascinating.",
                    "This is the house where I grew up.",
                    "The person who called you is my brother."
                ],
                connectors=Connectors.RELATIVE
            ),
            GrammarRule(
                title="Oraciones Causales",
                explanation="Expresan una relación de causa-efecto.",
                structure="Causa + Conector Causal + Efecto / Efecto + Conector Causal + Causa",
                examples=[
                    "Because it was cold, I wore a coat.",
                    "She was late due to the traffic.",
                    "Since you're tired, you should rest."
                ],
                connectors=Connectors.CAUSAL
            )
        ],
        examples=[
            ExampleSentence(
                "I wanted to go to the beach, but it started raining.",
                CompoundType.COORDINATED,
                "Quería ir a la playa, pero empezó a llover.",
                "Oración coordinada con 'but' que muestra contraste",
                "but"
            ),
            ExampleSentence(
                "Although she was tired, she finished her work.",
                CompoundType.SUBORDINATED,
                "Aunque estaba cansada, terminó su trabajo.",
                "Oración subordinada con 'although' que muestra contraste",
                "although"
            ),
            ExampleSentence(
                "If I win the lottery, I will travel around the world.",
                CompoundType.CONDITIONAL,
                "Si gano la lotería, viajaré por todo el mundo.",
                "Oración condicional que expresa una posibilidad futura",
                "if"
            ),
            ExampleSentence(
                "The book that you recommended was excellent.",
                CompoundType.RELATIVE,
                "El libro que recomendaste era excelente.",
                "Oración relativa que proporciona información sobre 'book'",
                "that"
            ),
            ExampleSentence(
                "Because he practiced daily, he became an expert pianist.",
                CompoundType.CAUSAL,
                "Como practicaba diariamente, se convirtió en un pianista experto.",
                "Oración causal que muestra la relación causa-efecto",
                "because"
            )
        ],
        exercises=[
            # Ejercicio 1: Identificación de tipos
            Exercise(
                exercise_id=1,
                type="sentence_identification",
                question="Identifica el tipo de oración compuesta: 'I will call you when I finish work.'",
                options=[t.value for t in CompoundType],
                correct_answer="subordinada",
                explanation="Es una oración subordinada que usa 'when' para conectar la cláusula dependiente."
            ),
            # Ejercicio 2: Elección de conector
            Exercise(
                exercise_id=2,
                type="connector_selection",
                question="Selecciona el conector apropiado: 'She didn't study, ___ she failed the exam.'",
                options=["so", "but", "although", "because"],
                correct_answer="so",
                explanation="'So' indica consecuencia o resultado lógico."
            ),
            # Ejercicio 3: Combinación de oraciones
            Exercise(
                exercise_id=3,
                type="sentence_combination",
                question="Combina estas dos oraciones usando 'although': 'It was raining. We decided to go for a walk.'",
                options=None,
                correct_answer="Although it was raining, we decided to go for a walk.",
                explanation="'Although' introduce un contraste entre dos ideas."
            ),
            # Ejercicio 4: Identificación de tipos
            Exercise(
                exercise_id=4,
                type="sentence_identification",
                question="Identifica el tipo de oración compuesta: 'The person who called yesterday wants to see you again.'",
                options=[t.value for t in CompoundType],
                correct_answer="relativa",
                explanation="Es una oración relativa que usa 'who' para proporcionar información sobre 'person'."
            ),
            # Ejercicio 5: Corrección de errores
            Exercise(
                exercise_id=5,
                type="error_correction",
                question="Corrige el error en esta oración: 'I'll go to the party, if you come with me.'",
                options=None,
                correct_answer="I'll go to the party if you come with me.",
                explanation="No se usa coma antes de 'if' cuando la cláusula condicional va después de la principal."
            ),
            # Ejercicio 6: Completa la oración
            Exercise(
                exercise_id=6,
                type="sentence_completion",
                question="Completa la oración con el conector apropiado: 'She didn't eat breakfast, ___ she was very hungry.'",
                options=None,
                correct_answer="so",
                explanation="'So' indica la consecuencia de no desayunar."
            ),
            # Ejercicio 7: Transformación de oración
            Exercise(
                exercise_id=7,
                type="sentence_transformation",
                question="Reescribe esta oración usando 'because': 'He missed the bus. He was late for work.'",
                options=None,
                correct_answer="He was late for work because he missed the bus.",
                explanation="'Because' establece una relación causal entre los dos eventos."
            ),
            # Ejercicio 8: Identificación de tipos
            Exercise(
                exercise_id=8,
                type="sentence_identification",
                question="Identifica el tipo de oración compuesta: 'Unless you apologize, I won't forgive you.'",
                options=[t.value for t in CompoundType],
                correct_answer="condicional",
                explanation="Es una oración condicional que usa 'unless' para expresar una condición."
            ),
            # Ejercicio 9: Elección múltiple de conectores
            Exercise(
                exercise_id=9,
                type="multiple_connectors",
                question="Selecciona todos los conectores de causa-efecto:",
                options=["because", "so", "although", "therefore", "since"],
                correct_answer="1,2,4,5",  # because, so, therefore, since
                explanation="Los conectores de causa-efecto son: because, so, therefore, since"
            ),
            # Ejercicio 10: Construcción de oración
            Exercise(
                exercise_id=10,
                type="sentence_construction",
                question="Construye una oración compuesta con estas palabras: decided / stay home / because / raining / it was",
                options=None,
                correct_answer="We decided to stay home because it was raining.",
                explanation="'Because' conecta la decisión (efecto) con la razón (causa)."
            )
        ]
    )

# Sistema de evaluación
class CompoundSentenceEvaluator:
    @staticmethod
    def evaluate_identification(user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.lower()
    
    @staticmethod
    def evaluate_connector_selection(user_answer, correct_answer, options):
        # Para ejercicios de selección de opciones
        if user_answer.isdigit():
            index = int(user_answer) - 1
            if 0 <= index < len(options):
                return options[index] == correct_answer
        return user_answer.strip().lower() == correct_answer.lower()
    
    @staticmethod
    def evaluate_sentence_combination(user_answer, correct_answer):
        # Normalizar para comparación
        normalized_user = " ".join(user_answer.strip().lower().split())
        normalized_correct = " ".join(correct_answer.strip().lower().split())
        
        # Verificar similitud semántica (aproximada)
        key_elements = [word for word in normalized_correct.split() if word not in [",", ".", "!"]]
        user_elements = normalized_user.split()
        
        # Contar elementos coincidentes
        matches = sum(1 for word in key_elements if word in user_elements)
        similarity = matches / len(key_elements)
        
        return similarity >= 0.8  # 80% de similitud
    
    @staticmethod
    def evaluate_error_correction(user_answer, correct_answer):
        return CompoundSentenceEvaluator.evaluate_sentence_combination(user_answer, correct_answer)
    
    @staticmethod
    def evaluate_sentence_completion(user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.lower()
    
    @staticmethod
    def evaluate_sentence_transformation(user_answer, correct_answer):
        return CompoundSentenceEvaluator.evaluate_sentence_combination(user_answer, correct_answer)
    
    @staticmethod
    def evaluate_multiple_connectors(user_answer, correct_answer):
        # Formato esperado: "1,3,4" o "1 3 4"
        user_selections = []
        if "," in user_answer:
            user_selections = [item.strip() for item in user_answer.split(",")]
        else:
            user_selections = user_answer.split()
        
        correct_selections = correct_answer.split(",")
        
        return set(user_selections) == set(correct_selections)
    
    @staticmethod
    def evaluate_sentence_construction(user_answer, correct_answer):
        return CompoundSentenceEvaluator.evaluate_sentence_combination(user_answer, correct_answer)

# Interfaz de consola
class CompoundSentenceConsoleApp:
    def __init__(self):
        self.lesson = create_lesson_compound_sentence()
        self.score = 0
        self.total_exercises = len(self.lesson.exercises)
        self.evaluator = CompoundSentenceEvaluator()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        self.clear_screen()
        print("=" * 80)
        print("           LA ORACIÓN COMPUESTA EN INGLÉS Y SUS TIPOS")
        print("=" * 80)
        print("\nBienvenido a la lección sobre oraciones compuestas en inglés.")
        print("Aprenderás a identificar, construir y usar diferentes tipos de")
        print("oraciones compuestas: coordinadas, subordinadas, condicionales,")
        print("relativas y causales.\n")
        input("Presiona Enter para continuar...")
    
    def display_lesson_intro(self):
        self.clear_screen()
        print("=" * 80)
        print(f"LECCIÓN {self.lesson.lesson_id}: {self.lesson.title}")
        print("=" * 80)
        
        print("\nOBJETIVOS:")
        for i, objective in enumerate(self.lesson.objectives, 1):
            print(f"  {i}. {objective}")
        
        print("\nTIPOS DE ORACIONES COMPUESTAS:")
        for rule in self.lesson.grammar_rules:
            print(f"\n  {rule.title.upper()}")
            print(f"  {rule.explanation}")
            print(f"  Estructura: {rule.structure}")
            print("  Conectores comunes:", ", ".join(rule.connectors))
            print("  Ejemplos:")
            for example in rule.examples:
                print(f"    • {example}")
        
        print("\nEJEMPLOS:")
        for example in self.lesson.examples:
            print(f"  • {example.sentence}")
            print(f"    Tipo: {example.type.value} | Conector: {example.connector}")
            print(f"    Traducción: {example.translation}")
            print(f"    Explicación: {example.explanation}\n")
        
        print("\n" + "-" * 80)
        input("Presiona Enter para comenzar los ejercicios...")
    
    def display_exercise(self, exercise, index):
        self.clear_screen()
        print(f"Ejercicio {index} de {self.total_exercises}")
        print("-" * 60)
        print(f"{exercise.question}\n")
        
        if exercise.options:
            if exercise.type == "sentence_identification":
                print("Opciones:")
                for i, option in enumerate(exercise.options, 1):
                    print(f"  {i}. {option}")
                print()
                return input("Tu respuesta (número): ")
            
            elif exercise.type == "connector_selection":
                print("Opciones:")
                for i, option in enumerate(exercise.options, 1):
                    print(f"  {i}. {option}")
                print()
                return input("Tu respuesta (número): ")
            
            elif exercise.type == "multiple_connectors":
                print("Opciones:")
                for i, option in enumerate(exercise.options, 1):
                    print(f"  {i}. {option}")
                print("\nFormato de respuesta: números separados por comas (ej: 1,3,4)")
                return input("Tu respuesta: ")
        
        return input("Tu respuesta: ")
    
    def evaluate_answer(self, exercise, user_answer):
        if exercise.type == "sentence_identification":
            return self.evaluator.evaluate_identification(user_answer, exercise.correct_answer)
        
        elif exercise.type == "connector_selection":
            return self.evaluator.evaluate_connector_selection(user_answer, exercise.correct_answer, exercise.options)
        
        elif exercise.type == "sentence_combination":
            return self.evaluator.evaluate_sentence_combination(user_answer, exercise.correct_answer)
        
        elif exercise.type == "error_correction":
            return self.evaluator.evaluate_error_correction(user_answer, exercise.correct_answer)
        
        elif exercise.type == "sentence_completion":
            return self.evaluator.evaluate_sentence_completion(user_answer, exercise.correct_answer)
        
        elif exercise.type == "sentence_transformation":
            return self.evaluator.evaluate_sentence_transformation(user_answer, exercise.correct_answer)
        
        elif exercise.type == "multiple_connectors":
            return self.evaluator.evaluate_multiple_connectors(user_answer, exercise.correct_answer)
        
        elif exercise.type == "sentence_construction":
            return self.evaluator.evaluate_sentence_construction(user_answer, exercise.correct_answer)
        
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
        print("=" * 80)
        print("         RESUMEN DE LA LECCIÓN")
        print("=" * 80)
        print(f"Lección: {self.lesson.title}")
        print(f"Ejercicios completados: {self.total_exercises}")
        print(f"Respuestas correctas: {self.score}")
        percentage = (self.score / self.total_exercises) * 100
        print(f"Puntuación: {self.score}/{self.total_exercises} ({percentage:.1f}%)")
        
        # Evaluación del desempeño
        if percentage >= 90:
            print("\n🎉 ¡Excelente! Dominaste completamente las oraciones compuestas.")
        elif percentage >= 70:
            print("\n👍 Buen trabajo, pero podrías repasar algunos conceptos.")
        else:
            print("\n📚 Necesitas repasar esta lección antes de continuar.")
        
        # Recomendaciones de estudio basadas en el desempeño
        print("\nRECOMENDACIONES:")
        if percentage < 70:
            print("  - Repasa los diferentes tipos de oraciones compuestas")
            print("  - Estudia los conectores específicos para cada tipo")
            print("  - Practica la combinación de oraciones simples")
        elif percentage < 90:
            print("  - Practica con textos más complejos que contengan varios tipos de oraciones")
            print("  - Intenta escribir párrafos usando diferentes tipos de oraciones compuestas")
        else:
            print("  - ¡Perfecto! Ahora practica con textos académicos o literarios")
            print("  - Intenta analizar oraciones compuestas en artículos o libros")
        
        # Áreas específicas para mejorar
        print("\nPRÓXIMOS TEMAS SUGERIDOS:")
        print("  - Oraciones complejas con múltiples cláusulas")
        print("  - Estilo indirecto (reported speech)")
        print("  - Voz pasiva en oraciones compuestas")
        print("  - Uso de modales en oraciones condicionales")
        
        print("\n" + "=" * 80)
        input("Presiona Enter para volver al menú principal...")
    
    def run(self):
        self.display_welcome()
        self.display_lesson_intro()
        self.run_exercises()
        self.display_summary()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = CompoundSentenceConsoleApp()
    app.run()
