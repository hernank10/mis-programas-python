from dataclasses import dataclass
from typing import List, Dict, Tuple
import json

@dataclass
class GrammarExample:
    example: str
    translation: str
    explanation: str

@dataclass
class VocabularyItem:
    word: str
    translation: str
    category: str
    example: str

@dataclass
class Exercise:
    exercise_id: int
    type: str  # fill_blank, multiple_choice, matching, transformation
    question: str
    options: List[str] = None
    correct_answer: str
    explanation: str
    difficulty: str = "beginner"

@dataclass
class Lesson:
    lesson_id: int
    title: str
    objectives: List[str]
    grammar_rules: List[str]
    grammar_examples: List[GrammarExample]
    vocabulary: List[VocabularyItem]
    exercises: List[Exercise]
    review_questions: List[str]
