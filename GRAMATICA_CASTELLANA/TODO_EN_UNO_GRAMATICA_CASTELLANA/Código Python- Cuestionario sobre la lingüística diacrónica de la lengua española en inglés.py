import random

# Questions and answers
questions = [
    # Origins and evolution of Spanish
    {"type": "multiple_choice", "question": "🌟📜✏️🕵From which language does Spanish primarily originate?",
     "options": ["A) Arabic", "B) Latin", "C) Greek", "D) Germanic"], "answer": "B"},
    {"type": "true_false", "question": "🌟📜✏️🕵(F O V)Spanish is a Romance language.", "answer": "T"},
    {"type": "open", "question": "open question🌟📜✏️🕵What name is given to the form of Latin from which Spanish derives?",
     "answer": "Vulgar Latin"},
    {"type": "multiple_choice", "question": "🌟📜✏️🕵In which century was Castilian established as a written standard?",
     "options": ["A) 8th century", "B) 10th century", "C) 13th century", "D) 15th century"], "answer": "C"},
    
    # External influences
    {"type": "multiple_choice", "question": "🌟📜✏️🕵Which of these languages significantly influenced medieval Spanish?",
     "options": ["A) Arabic", "B) English", "C) Portuguese", "D) French"], "answer": "A"},
    {"type": "true_false", "question": "🌟📜✏️🕵(F O V) Arabic introduced over 4,000 words into Spanish.", "answer": "T"},
    {"type": "open", "question": "open question🌟📜✏️🕵Name one Spanish word of Arabic origin.",
     "answer": "Ojalá (or similar)"},
    {"type": "multiple_choice", "question": "🌟📜✏️🕵Which people introduced war-related terms into Spanish?",
     "options": ["A) Visigoths", "B) Romans", "C) Celtiberians", "D) Phoenicians"], "answer": "A"},
    
    # Development stages of Spanish
    {"type": "multiple_choice", "question": "🌟📜✏️🕵What is the first stage of Spanish?",
     "options": ["A) Medieval Castilian", "B) Modern Spanish", "C) Primitive Castilian", "D) Vulgar Latin"], "answer": "C"},
    {"type": "true_false", "question": "🌟📜✏️🕵(F O V) Modern Spanish began to develop in the 17th century.", "answer": "T"},
    {"type": "open", "question": "open question🌟📜✏️🕵What historical event marked the unification of Spanish as the official language in Spain?",
     "answer": "The publication of Nebrija's Grammar"},
    {"type": "multiple_choice", "question": "🌟📜✏️🕵Which stage of Spanish was marked by lexical and stylistic enrichment during the Golden Age?",
     "options": ["A) Medieval Spanish", "B) Early Modern Spanish", "C) Contemporary Spanish", "D) Primitive Castilian"], "answer": "B"},
    
    # Linguistic changes
    {"type": "multiple_choice", "question": "🌟📜✏️🕵Which phonetic change explains the disappearance of the initial Latin 'f' in words like *farina* > *harina*?",
     "options": ["A) Assimilation", "B) Lenition", "C) Voicing", "D) Aspiration"], "answer": "D"},
    {"type": "true_false", "question": "🌟📜✏️🕵(F O V) Voicing is a change in which a voiceless sound becomes voiced.", "answer": "T"},
    {"type": "open", "question": "open question🌟📜✏️🕵What phenomenon explains the change from *octo* to *ocho* in Spanish?",
     "answer": "Diphthongization"},
    {"type": "multiple_choice", "question": "What type of linguistic change affects the meaning of words?",
     "options": ["A) Phonetic", "B) Morphological", "C) Semantic", "D) Syntactic"], "answer": "C"},
    
    # Spanish expansion
    {"type": "multiple_choice", "question": "🌟📜✏️🕵In which century did Spanish begin its expansion to the Americas?",
     "options": ["A) 15th century", "B) 16th century", "C) 17th century", "D) 18th century"], "answer": "B"},
    {"type": "true_false", "question": "🌟📜✏️🕵(F O V) Spanish expanded primarily during the American colonization.", "answer": "T"},
    {"type": "open", "question": "What linguistic phenomenon describes the influence of indigenous languages on American Spanish?",
     "answer": "Linguistic borrowing"},
    {"type": "multiple_choice", "question": "🌟📜✏️🕵Which indigenous language had the most influence on Mexican Spanish?",
     "options": ["A) Quechua", "B) Nahuatl", "C) Guarani", "D) Mapudungun"], "answer": "B"},
    
    # Institutions and regulations
    {"type": "multiple_choice", "question": "🌟📜✏️🕵Which institution currently regulates the use of Spanish?",
     "options": ["A) Royal Spanish Academy", "B) Cervantes Institute", "C) Mexican Academy of Language", "D) History Academy"], "answer": "A"},
    {"type": "true_false", "question": "🌟📜✏️🕵(F O V) The Royal Spanish Academy was founded in the 18th century.", "answer": "T"},
    {"type": "open", "question": "open question🌟📜✏️🕵What work is considered the first attempt to standardize the use of Spanish?",
     "answer": "Nebrija's Grammar"},
    {"type": "multiple_choice", "question": "🌟📜✏️🕵Which country has the most native Spanish speakers in the world?",
     "options": ["A) Spain", "B) Mexico", "C) Argentina", "D) Colombia"], "answer": "B"},
]

# Questionnaire execution functions
def show_question(question):
    print("\n" + question["question"])
    if question["type"] == "multiple_choice":
        for option in question["options"]:
            print(option)
    response = input("Your answer: ").strip()
    return response

def validate_answer(question, response):
    if question["type"] == "open":
        return response.lower() == question["answer"].lower()
    return response.upper() == question["answer"].upper()

def questionnaire():
    score = 0
    random.shuffle(questions)  # Shuffle questions
    for i, question in enumerate(questions[:20]):  # Limit to 20 questions
        print(f"\nQuestion {i + 1}:")
        response = show_question(question)
        if validate_answer(question, response):
            print("🌟📜✏️🕵Correct!✅")
            score += 1
        else:
            print(f"Incorrect❌. The correct answer was: {question['answer']}")
    print(f"\n🌟📜✏️🕵You completed the questionnaire! Your final score is {score}/{len(questions[:20])}.")

# Run the questionnaire
questionnaire()
