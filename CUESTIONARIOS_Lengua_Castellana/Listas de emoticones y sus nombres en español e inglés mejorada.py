# Listas de emoticones y sus nombres en español e inglés
emoticons = {
    "Poetas y Escritura": [
        {"emoji": "✍️", "es": "Escribiendo", "en": "Writing"},
        {"emoji": "📜", "es": "Pergamino", "en": "Scroll"},
        {"emoji": "🖋️", "es": "Pluma estilográfica", "en": "Fountain pen"},
        {"emoji": "📖", "es": "Libro abierto", "en": "Open book"},
        {"emoji": "🏺", "es": "Jarrón con poemas grabados", "en": "Vase with engraved poems"}
    ],
    "Filosofía y Sabiduría": [
        {"emoji": "🧠", "es": "Intelecto", "en": "Intellect"},
        {"emoji": "🌀", "es": "Reflexión profunda", "en": "Deep reflection"},
        {"emoji": "🤔", "es": "Pensador", "en": "Thinker"},
        {"emoji": "📚", "es": "Libros de filosofía", "en": "Philosophy books"},
        {"emoji": "⚖️", "es": "Balanza", "en": "Balance"}
    ],
    "Gramática y Lenguaje": [
        {"emoji": "🔤", "es": "Letras del alfabeto", "en": "Alphabet letters"},
        {"emoji": "📝", "es": "Notas escritas", "en": "Written notes"},
        {"emoji": "📒", "es": "Cuaderno de gramática", "en": "Grammar notebook"},
        {"emoji": "📕", "es": "Reglamento lingüístico", "en": "Rulebook of linguistic norms"},
        {"emoji": "📊", "es": "Diagramas de oraciones", "en": "Sentence diagrams"}
    ]
}

def show_intro():
    """Displays the introduction to the program."""
    print("""
🌟📜✏️🕵🏛 ¡Bienvenido al Programa de Emoticones! 🌟📜✏️🕵🏛
Aquí aprenderás vocabulario en español e inglés mientras te diviertes.
🌍 Explora categorías llenas de creatividad y sabiduría, desde poetas hasta gramática.
🎯 Tu objetivo es escribir correctamente el nombre de los emoticones en ambos idiomas.
¡Comencemos! 🚀
    """)

def show_menu():
    """Displays the main menu."""
    print("\n🌟📜✏️🕵🏛 Menú Principal 📝")
    print("Selecciona una opción:")
    print("1️⃣ Ver la lista de emoticones con sus nombres.")
    for i, category in enumerate(emoticons.keys(), 2):
        print(f"{i}️⃣ Practicar: {category}")
    print("0️⃣ Salir")

def show_emoticons():
    """Displays the emoticons and their names in both languages."""
    print("\n📜 Lista de Emoticones 📜")
    for category, items in emoticons.items():
        print(f"\n🔸 {category} 🔸")
        for item in items:
            print(f"{item['emoji']} - Español: {item['es']} | Inglés: {item['en']}")

def quiz(category):
    """Conducts a quiz based on the selected category."""
    print(f"\n✨ Practicando: {category} ✨")
    items = emoticons[category]
    score = 0
    
    for item in items:
        print(f"\nEmoticón: {item['emoji']}")
        answer_es = input("🌟📜✏️🕵🏛¿Cómo se llama en español? ").strip()
        answer_en = input("🌟📜✏️🕵🏛 ¿Cómo se llama en inglés? ").strip()
        
        if answer_es.lower() == item['es'].lower() and answer_en.lower() == item['en'].lower():
            print("🌟📜✏️🕵🏛 ¡Correcto en ambos idiomas!✅")
            score += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta:")
            print(f"   Español: {item['es']} | Inglés: {item['en']}")
    
    print(f"\n🏆 Puntaje final: {score}/{len(items)}")
    print("🎉 ¡Bien hecho!" if score > 0 else "😅 ¡Sigue practicando!")

def main():
    """Main function to run the program."""
    show_intro()
    while True:
        show_menu()
        choice = input("\nElige una opción: ").strip()
        
        if choice == "0":
            print("🌟 ¡Gracias por jugar! 🌟")
            break
        elif choice == "1":
            show_emoticons()
        elif choice.isdigit() and 2 <= int(choice) <= len(emoticons) + 1:
            category = list(emoticons.keys())[int(choice) - 2]
            quiz(category)
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
