import random

# Lista de sustantivos regulares en inglés (primera "declinación")
nouns = {
    "cat": "cats",
    "dog": "dogs",
    "book": "books",
    "car": "cars",
    "table": "tables",
    "chair": "chairs",
    "house": "houses",
    "pen": "pens",
    "apple": "apples",
    "banana": "bananas",
    "bus": "buses",
    "box": "boxes",
    "glass": "glasses",
    "watch": "watches",
    "dish": "dishes",
    "fox": "foxes",
    "class": "classes",
    "match": "matches",
    "potato": "potatoes",
    "tomato": "tomatoes",
    "hero": "heroes",
    "photo": "photos",
    "piano": "pianos",
    "baby": "babies",
    "lady": "ladies",
    "city": "cities",
    "story": "stories",
    "day": "days",
    "toy": "toys",
    "boy": "boys"
}

def practice_plural():
    print("=== Entrenador de la primera declinación del inglés (plurales regulares) ===\n")
    score = 0
    exercises = 10  # número de ejercicios por sesión
    
    words = random.sample(list(nouns.keys()), exercises)
    
    for singular in words:
        plural_correct = nouns[singular]
        answer = input(f"Escribe el plural de '{singular}': ").strip().lower()
        
        if answer == plural_correct:
            print("✅ ¡Correcto!\n")
            score += 1
        else:
            print(f"❌ Incorrecto. El plural correcto es: {plural_correct}\n")
    
    print(f"Tu puntaje final: {score}/{exercises}")

if __name__ == "__main__":
    practice_plural()
