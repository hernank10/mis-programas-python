import random
import speech_recognition as sr

# Ejercicio 1: Asociación de imágenes con palabras en ruso
def asociacion_imagenes_palabras():
    print("\n--- Упражнение 1: Ассоциация картинок со словами ---")
    imagenes_palabras = {
        "яблоко": "🍎",  # Manzana
        "собака": "🐕",  # Perro
        "солнце": "☀️",  # Sol
        "дом": "🏠",     # Casa
        "дерево": "🌳"   # Árbol
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"Какое слово соответствует этой картинке? {imagen}")
        respuesta = input("Напишите слово: ").strip().lower()
        if respuesta == palabra:
            print("Правильно! 🎉\n")
        else:
            print(f"Неправильно. Правильный ответ: {palabra}\n")

# Ejercicio 2: Dictado Interactivo en ruso
def dictado_interactivo():
    print("\n--- Упражнение 2: Интерактивный диктант ---")
    oraciones = [
        "Солнце светит в небе.",  # El sol brilla en el cielo.
        "Собака играет в парке.",  # El perro juega en el parque.
        "Яблоко красное и сладкое.",  # La manzana es roja y dulce.
        "Дом имеет большой сад.",  # La casa tiene un jardín grande.
        "Дерево дает тень летом."  # El árbol da sombra en verano.
    ]
    oracion = random.choice(oraciones)
    print(f"Напишите следующее предложение: '{oracion}'")
    respuesta = input("Ваш ответ: ").strip()
    
    if respuesta == oracion:
        print("Отлично! Ошибок нет. 🎉\n")
    else:
        print(f"Были ошибки. Правильное предложение: {oracion}\n")

# Ejercicio 3: Ordenar Palabras en ruso
def ordenar_palabras():
    print("\n--- Упражнение 3: Порядок слов ---")
    oraciones_desordenadas = [
        ["играет", "в", "парке", "собака", "в"],
        ["светит", "в", "небе", "солнце", "в"],
        ["красное", "и", "сладкое", "яблоко", "и"],
        ["большой", "сад", "имеет", "дом", "имеет"],
        ["дает", "тень", "летом", "дерево", "дает"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"Упорядочьте следующие слова, чтобы составить предложение: {', '.join(palabras)}")
    respuesta = input("Ваш ответ: ").strip()
    
    oracion_correcta = " ".join(palabras)
    if respuesta.lower() == oracion_correcta.lower():
        print("Правильно! Предложение составлено верно. 🎉\n")
    else:
        print(f"Неправильно. Правильное предложение: {oracion_correcta}\n")

# Ejercicio 4: Rellenar Espacios en Blanco en ruso
def rellenar_espacios():
    print("\n--- Упражнение 4: Заполните пропуски ---")
    oraciones = [
        "Солнце светит в ___.",  # El sol brilla en el cielo.
        "Собака играет в ___.",  # El perro juega en el parque.
        "Яблоко ___ и сладкое.",  # La manzana es roja y dulce.
        "Дом имеет ___ сад.",  # La casa tiene un jardín grande.
        "Дерево дает ___ летом."  # El árbol da sombra en verano.
    ]
    respuestas_correctas = ["небе", "парке", "красное", "большой", "тень"]
    
    oracion = random.choice(oraciones)
    print(f"Заполните пропуск в предложении: {oracion}")
    respuesta = input("Ваш ответ: ").strip().lower()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("Правильно! 🎉\n")
    else:
        print(f"Неправильно. Правильный ответ: {respuestas_correctas[indice]}\n")

# Ejercicio 5: Lectura en Voz Alta en ruso
def lectura_voz_alta():
    print("\n--- Упражнение 5: Чтение вслух ---")
    oraciones = [
        "Солнце светит в небе.",  # El sol brilla en el cielo.
        "Собака играет в парке.",  # El perro juega en el parque.
        "Яблоко красное и сладкое.",  # La manzana es roja y dulce.
        "Дом имеет большой сад.",  # La casa tiene un jardín grande.
        "Дерево дает тень летом."  # El árbol da sombra en verano.
    ]
    oracion = random.choice(oraciones)
    print(f"Прочитайте следующее предложение вслух: '{oracion}'")
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)
        
        try:
            texto_reconocido = recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {texto_reconocido}")
            if texto_reconocido.lower() == oracion.lower():
                print("Отлично! Вы прочитали правильно. 🎉\n")
            else:
                print(f"Были ошибки. Правильное предложение: {oracion}\n")
        except sr.UnknownValueError:
            print("Не удалось распознать речь. Попробуйте еще раз.\n")
        except sr.RequestError:
            print("Ошибка в сервисе распознавания речи.\n")

# Menú principal
def main():
    while True:
        print("Добро пожаловать в приложение для изучения русского языка")
        print("1. Ассоциация картинок со словами")
        print("2. Интерактивный диктант")
        print("3. Порядок слов")
        print("4. Заполните пропуски")
        print("5. Чтение вслух")
        print("6. Выход")
        opcion = input("Выберите опцию (1-6): ").strip()
        
        if opcion == "1":
            asociacion_imagenes_palabras()
        elif opcion == "2":
            dictado_interactivo()
        elif opcion == "3":
            ordenar_palabras()
        elif opcion == "4":
            rellenar_espacios()
        elif opcion == "5":
            lectura_voz_alta()
        elif opcion == "6":
            print("Спасибо за использование приложения! До свидания. 👋")
            break
        else:
            print("Неверная опция. Попробуйте снова.\n")

if __name__ == "__main__":
    main()
