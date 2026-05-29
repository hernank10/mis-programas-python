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

def show_menu():
    """Displays the main menu."""
    print("\n📝 Bienvenido al Programa de Emoticones 📝")
    print("Selecciona una categoría para practicar:")
    for i, category in enumerate(emoticons.keys(), 1):
        print(f"{i}. {category}")
    print("0. Salir")

def quiz(category):
    """Conducts a quiz based on the selected category."""
    print(f"\n✨ Practicando: {category} ✨")
    items = emoticons[category]
    score = 0
    
    for item in items:
        print(f"\nEmoticón: {item['emoji']}")
        answer_es = input("¿Cómo se llama en español? ").strip()
        answer_en = input("¿Cómo se llama en inglés? ").strip()
        
        if answer_es.lower() == item['es'].lower() and answer_en.lower() == item['en'].lower():
            print("✅ ¡Correcto en ambos idiomas!")
            score += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta:")
            print(f"   Español: {item['es']} | Inglés: {item['en']}")
    
    print(f"\nPuntaje final: {score}/{len(items)}")
    print("¡Bien hecho!" if score > 0 else "¡Sigue practicando!")

def main():
    """Main function to run the program."""
    while True:
        show_menu()
        choice = input("\nElige una opción: ").strip()
        
        if choice == "0":
            print("¡Gracias por jugar! 🌟")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(emoticons):
            category = list(emoticons.keys())[int(choice) - 1]
            quiz(category)
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
