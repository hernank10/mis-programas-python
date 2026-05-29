import random

# Ejercicios para español
def asociacion_imagenes_palabras_es():
    print("\n--- Ejercicio 1: Asociación de imágenes con palabras ---")
    imagenes_palabras = {
        "manzana": "🍎",  # Manzana
        "perro": "🐕",    # Perro
        "sol": "☀️",      # Sol
        "casa": "🏠",     # Casa
        "árbol": "🌳"     # Árbol
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"¿Qué palabra corresponde a esta imagen? {imagen}")
        respuesta = input("Escribe la palabra: ").strip().lower()
        if respuesta == palabra:
            print("¡Correcto! 🎉\n")
        else:
            print(f"Incorrecto. La respuesta correcta es: {palabra}\n")

def dictado_interactivo_es():
    print("\n--- Ejercicio 2: Dictado Interactivo ---")
    oraciones = [
        "El sol brilla en el cielo.",
        "El perro juega en el parque.",
        "La manzana es roja y dulce.",
        "La casa tiene un jardín grande.",
        "El árbol da sombra en verano."
    ]
    oracion = random.choice(oraciones)
    print(f"Escribe la siguiente oración: '{oracion}'")
    respuesta = input("Tu respuesta: ").strip()
    
    if respuesta == oracion:
        print("¡Perfecto! No hay errores. 🎉\n")
    else:
        print(f"Hubo algunos errores. La oración correcta es: {oracion}\n")

def ordenar_palabras_es():
    print("\n--- Ejercicio 3: Ordenar Palabras ---")
    oraciones_desordenadas = [
        ["juega", "el", "parque", "en", "perro", "el"],
        ["brilla", "cielo", "el", "en", "sol", "el"],
        ["roja", "es", "y", "dulce", "manzana", "la"],
        ["grande", "jardín", "un", "tiene", "casa", "la"],
        ["sombra", "da", "árbol", "verano", "el", "en"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"Ordena las siguientes palabras para formar una oración: {', '.join(palabras)}")
    respuesta = input("Tu respuesta: ").strip()
    
    oracion_correcta = " ".join(palabras)
    if respuesta.lower() == oracion_correcta.lower():
        print("¡Correcto! La oración está bien ordenada. 🎉\n")
    else:
        print(f"Incorrecto. La oración correcta es: {oracion_correcta}\n")

def rellenar_espacios_es():
    print("\n--- Ejercicio 4: Rellenar Espacios en Blanco ---")
    oraciones = [
        "El ___ brilla en el cielo.",
        "El perro juega en el ___.",
        "La manzana es ___ y dulce.",
        "La casa tiene un jardín ___.",
        "El árbol da ___ en verano."
    ]
    respuestas_correctas = ["sol", "parque", "roja", "grande", "sombra"]
    
    oracion = random.choice(oraciones)
    print(f"Completa la oración: {oracion}")
    respuesta = input("Tu respuesta: ").strip().lower()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("¡Correcto! 🎉\n")
    else:
        print(f"Incorrecto. La respuesta correcta es: {respuestas_correctas[indice]}\n")

# Ejercicios para portugués
def asociacion_imagenes_palabras_pt():
    print("\n--- Exercício 1: Associação de imagens com palavras ---")
    imagenes_palabras = {
        "maçã": "🍎",  # Manzana
        "cão": "🐕",    # Perro
        "sol": "☀️",    # Sol
        "casa": "🏠",   # Casa
        "árvore": "🌳"  # Árbol
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"Qual palavra corresponde a esta imagem? {imagen}")
        respuesta = input("Escreva a palavra: ").strip().lower()
        if respuesta == palabra:
            print("Correto! 🎉\n")
        else:
            print(f"Incorreto. A resposta correta é: {palabra}\n")

def dictado_interactivo_pt():
    print("\n--- Exercício 2: Ditado Interativo ---")
    oraciones = [
        "O sol brilha no céu.",
        "O cão brinca no parque.",
        "A maçã é vermelha e doce.",
        "A casa tem um jardim grande.",
        "A árvore dá sombra no verão."
    ]
    oracion = random.choice(oraciones)
    print(f"Escreva a seguinte frase: '{oracion}'")
    respuesta = input("Sua resposta: ").strip()
    
    if respuesta == oracion:
        print("Perfeito! Sem erros. 🎉\n")
    else:
        print(f"Houve alguns erros. A frase correta é: {oracion}\n")

def ordenar_palabras_pt():
    print("\n--- Exercício 3: Ordenar Palavras ---")
    oraciones_desordenadas = [
        ["brinca", "no", "parque", "o", "cão"],
        ["brilha", "no", "céu", "o", "sol"],
        ["vermelha", "e", "doce", "a", "maçã", "é"],
        ["grande", "jardim", "um", "tem", "a", "casa"],
        ["sombra", "dá", "a", "árvore", "no", "verão"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"Ordene as seguintes palavras para formar uma frase: {', '.join(palabras)}")
    respuesta = input("Sua resposta: ").strip()
    
    oracion_correcta = " ".join(palabras)
    if resposta.lower() == oracion_correcta.lower():
        print("Correto! A frase está bem ordenada. 🎉\n")
    else:
        print(f"Incorreto. A frase correta é: {oracion_correcta}\n")

def rellenar_espacios_pt():
    print("\n--- Exercício 4: Preencher Espaços em Branco ---")
    oraciones = [
        "O ___ brilha no céu.",
        "O cão brinca no ___.",
        "A maçã é ___ e doce.",
        "A casa tem um jardim ___.",
        "A árvore dá ___ no verão."
    ]
    respuestas_correctas = ["sol", "parque", "vermelha", "grande", "sombra"]
    
    oracion = random.choice(oraciones)
    print(f"Complete a frase: {oracion}")
    respuesta = input("Sua resposta: ").strip().lower()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("Correto! 🎉\n")
    else:
        print(f"Incorreto. A resposta correta é: {respuestas_correctas[indice]}\n")

# Ejercicios para francés
def asociacion_imagenes_palabras_fr():
    print("\n--- Exercice 1: Association d'images avec des mots ---")
    imagenes_palabras = {
        "pomme": "🍎",  # Manzana
        "chien": "🐕",  # Perro
        "soleil": "☀️", # Sol
        "maison": "🏠", # Casa
        "arbre": "🌳"   # Árbol
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"Quel mot correspond à cette image? {imagen}")
        respuesta = input("Écrivez le mot: ").strip().lower()
        if respuesta == palabra:
            print("Correct! 🎉\n")
        else:
            print(f"Incorrect. La réponse correcte est: {palabra}\n")

def dictado_interactivo_fr():
    print("\n--- Exercice 2: Dictée Interactive ---")
    oraciones = [
        "Le soleil brille dans le ciel.",
        "Le chien joue dans le parc.",
        "La pomme est rouge et sucrée.",
        "La maison a un grand jardin.",
        "L'arbre donne de l'ombre en été."
    ]
    oracion = random.choice(oraciones)
    print(f"Écrivez la phrase suivante: '{oracion}'")
    respuesta = input("Votre réponse: ").strip()
    
    if respuesta == oracion:
        print("Parfait! Aucune erreur. 🎉\n")
    else:
        print(f"Il y a quelques erreurs. La phrase correcte est: {oracion}\n")

def ordenar_palabras_fr():
    print("\n--- Exercice 3: Ordre des Mots ---")
    oraciones_desordenadas = [
        ["joue", "dans", "le", "parc", "le", "chien"],
        ["brille", "dans", "le", "ciel", "le", "soleil"],
        ["rouge", "et", "sucrée", "la", "pomme", "est"],
        ["grand", "jardin", "un", "a", "la", "maison"],
        ["donne", "de", "l'ombre", "l'arbre", "en", "été"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"Ordonnez les mots suivants pour former une phrase: {', '.join(palabras)}")
    respuesta = input("Votre réponse: ").strip()
    
    oracion_correcta = " ".join(palabras)
    if respuesta.lower() == oracion_correcta.lower():
        print("Correct! La phrase est bien ordonnée. 🎉\n")
    else:
        print(f"Incorrect. La phrase correcte est: {oracion_correcta}\n")

def rellenar_espacios_fr():
    print("\n--- Exercice 4: Remplir les Blancs ---")
    oraciones = [
        "Le ___ brille dans le ciel.",
        "Le chien joue dans le ___.",
        "La pomme est ___ et sucrée.",
        "La maison a un jardin ___.",
        "L'arbre donne de ___ en été."
    ]
    respuestas_correctas = ["soleil", "parc", "rouge", "grand", "l'ombre"]
    
    oracion = random.choice(oraciones)
    print(f"Complétez la phrase: {oracion}")
    respuesta = input("Votre réponse: ").strip().lower()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("Correct! 🎉\n")
    else:
        print(f"Incorrect. La réponse correcte est: {respuestas_correctas[indice]}\n")

# Ejercicios para italiano
def asociacion_imagenes_palabras_it():
    print("\n--- Esercizio 1: Associazione di immagini con parole ---")
    imagenes_palabras = {
        "mela": "🍎",  # Manzana
        "cane": "🐕",  # Perro
        "sole": "☀️",  # Sol
        "casa": "🏠",  # Casa
        "albero": "🌳" # Árbol
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"Quale parola corrisponde a questa immagine? {imagen}")
        respuesta = input("Scrivi la parola: ").strip().lower()
        if respuesta == palabra:
            print("Corretto! 🎉\n")
        else:
            print(f"Errato. La risposta corretta è: {palabra}\n")

def dictado_interactivo_it():
    print("\n--- Esercizio 2: Dettato Interattivo ---")
    oraciones = [
        "Il sole splende nel cielo.",
        "Il cane gioca nel parco.",
        "La mela è rossa e dolce.",
        "La casa ha un grande giardino.",
        "L'albero dà ombra in estate."
    ]
    oracion = random.choice(oraciones)
    print(f"Scrivi la seguente frase: '{oracion}'")
    respuesta = input("La tua risposta: ").strip()
    
    if respuesta == oracion:
        print("Perfetto! Nessun errore. 🎉\n")
    else:
        print(f"Ci sono alcuni errori. La frase corretta è: {oracion}\n")

def ordenar_palabras_it():
    print("\n--- Esercizio 3: Ordine delle Parole ---")
    oraciones_desordenadas = [
        ["gioca", "nel", "parco", "il", "cane"],
        ["splende", "nel", "cielo", "il", "sole"],
        ["rossa", "e", "dolce", "la", "mela", "è"],
        ["grande", "giardino", "un", "ha", "la", "casa"],
        ["dà", "ombra", "l'albero", "in", "estate"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"Ordina le seguenti parole per formare una frase: {', '.join(palabras)}")
    respuesta = input("La tua risposta: ").strip()
    
    oracion_correcta = " ".join(palabras)
    if respuesta.lower() == oracion_correcta.lower():
        print("Corretto! La frase è ben ordinata. 🎉\n")
    else:
        print(f"Errato. La frase corretta è: {oracion_correcta}\n")

def rellenar_espacios_it():
    print("\n--- Esercizio 4: Riempire gli Spazi Vuoti ---")
    oraciones = [
        "Il ___ splende nel cielo.",
        "Il cane gioca nel ___.",
        "La mela è ___ e dolce.",
        "La casa ha un giardino ___.",
        "L'albero dà ___ in estate."
    ]
    respuestas_correctas = ["sole", "parco", "rossa", "grande", "ombra"]
    
    oracion = random.choice(oraciones)
    print(f"Completa la frase: {oracion}")
    respuesta = input("La tua risposta: ").strip().lower()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("Corretto! 🎉\n")
    else:
        print(f"Errato. La risposta corretta è: {respuestas_correctas[indice]}\n")

# Ejercicios para alemán
def asociacion_imagenes_palabras_de():
    print("\n--- Übung 1: Bild-Wort-Assoziation ---")
    imagenes_palabras = {
        "Apfel": "🍎",  # Manzana
        "Hund": "🐕",   # Perro
        "Sonne": "☀️",  # Sol
        "Haus": "🏠",   # Casa
        "Baum": "🌳"    # Árbol
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"Welches Wort passt zu diesem Bild? {imagen}")
        respuesta = input("Schreiben Sie das Wort: ").strip().capitalize()
        if respuesta == palabra:
            print("Richtig! 🎉\n")
        else:
            print(f"Falsch. Die richtige Antwort ist: {palabra}\n")

def dictado_interactivo_de():
    print("\n--- Übung 2: Interaktives Diktat ---")
    oraciones = [
        "Die Sonne scheint am Himmel.",
        "Der Hund spielt im Park.",
        "Der Apfel ist rot und süß.",
        "Das Haus hat einen großen Garten.",
        "Der Baum spendet Schatten im Sommer."
    ]
    oracion = random.choice(oraciones)
    print(f"Schreiben Sie den folgenden Satz: '{oracion}'")
    respuesta = input("Ihre Antwort: ").strip()
    
    if respuesta == oracion:
        print("Perfekt! Keine Fehler. 🎉\n")
    else:
        print(f"Es gab einige Fehler. Der richtige Satz ist: {oracion}\n")

def ordenar_palabras_de():
    print("\n--- Übung 3: Wortreihenfolge ---")
    oraciones_desordenadas = [
        ["spielt", "im", "Park", "der", "Hund"],
        ["scheint", "am", "Himmel", "die", "Sonne"],
        ["rot", "und", "süß", "der", "Apfel", "ist"],
        ["großen", "Garten", "einen", "hat", "das", "Haus"],
        ["spendet", "Schatten", "der", "Baum", "im", "Sommer"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"Ordnen Sie die folgenden Wörter, um einen Satz zu bilden: {', '.join(palabras)}")
    respuesta = input("Ihre Antwort: ").strip()
    
    oracion_correcta = " ".join(palabras)
    if respuesta == oracion_correcta:
        print("Richtig! Der Satz ist korrekt geordnet. 🎉\n")
    else:
        print(f"Falsch. Der richtige Satz ist: {oracion_correcta}\n")

def rellenar_espacios_de():
    print("\n--- Übung 4: Lücken füllen ---")
    oraciones = [
        "Die ___ scheint am Himmel.",
        "Der Hund spielt im ___.",
        "Der Apfel ist ___ und süß.",
        "Das Haus hat einen ___ Garten.",
        "Der Baum spendet ___ im Sommer."
    ]
    respuestas_correctas = ["Sonne", "Park", "rot", "großen", "Schatten"]
    
    oracion = random.choice(oraciones)
    print(f"Vervollständigen Sie den Satz: {oracion}")
    respuesta = input("Ihre Antwort: ").strip().capitalize()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("Richtig! 🎉\n")
    else:
        print(f"Falsch. Die richtige Antwort ist: {respuestas_correctas[indice]}\n")

# Ejercicios para polaco
def asociacion_imagenes_palabras_pl():
    print("\n--- Ćwiczenie 1: Asocjacja obrazów ze słowami ---")
    imagenes_palabras = {
        "jabłko": "🍎",  # Manzana
        "pies": "🐕",    # Perro
        "słońce": "☀️",  # Sol
        "dom": "🏠",     # Casa
        "drzewo": "🌳"   # Árbol
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"Które słowo pasuje do tego obrazu? {imagen}")
        respuesta = input("Napisz słowo: ").strip().lower()
        if respuesta == palabra:
            print("Poprawnie! 🎉\n")
        else:
            print(f"Niepoprawnie. Prawidłowa odpowiedź to: {palabra}\n")

def dictado_interactivo_pl():
    print("\n--- Ćwiczenie 2: Interaktywny Dyktando ---")
    oraciones = [
        "Słońce świeci na niebie.",
        "Pies bawi się w parku.",
        "Jabłko jest czerwone i słodkie.",
        "Dom ma duży ogród.",
        "Drzewo daje cień latem."
    ]
    oracion = random.choice(oraciones)
    print(f"Napisz następujące zdanie: '{oracion}'")
    respuesta = input("Twoja odpowiedź: ").strip()
    
    if respuesta == oracion:
        print("Idealnie! Bez błędów. 🎉\n")
    else:
        print(f"Były pewne błędy. Prawidłowe zdanie to: {oracion}\n")

def ordenar_palabras_pl():
    print("\n--- Ćwiczenie 3: Kolejność Słów ---")
    oraciones_desordenadas = [
        ["bawi", "się", "w", "parku", "pies"],
        ["świeci", "na", "niebie", "słońce"],
        ["czerwone", "i", "słodkie", "jabłko", "jest"],
        ["duży", "ogród", "ma", "dom"],
        ["daje", "cień", "drzewo", "latem"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"Uporządkuj następujące słowa, aby utworzyć zdanie: {', '.join(palabras)}")
    respuesta = input("Twoja odpowiedź: ").strip()
    
    oracion_correcta = " ".join(palabras)
    if respuesta == oracion_correcta:
        print("Poprawnie! Zdanie jest dobrze ułożone. 🎉\n")
    else:
        print(f"Niepoprawnie. Prawidłowe zdanie to: {oracion_correcta}\n")

def rellenar_espacios_pl():
    print("\n--- Ćwiczenie 4: Uzupełnij Luki ---")
    oraciones = [
        "Słońce świeci na ___.",  # El sol brilla en el cielo.
        "Pies bawi się w ___.",    # El perro juega en el parque.
        "Jabłko jest ___ i słodkie.",  # La manzana es roja y dulce.
        "Dom ma ___ ogród.",  # La casa tiene un jardín grande.
        "Drzewo daje ___ latem."  # El árbol da sombra en verano.
    ]
    respuestas_correctas = ["niebie", "parku", "czerwone", "duży", "cień"]
    
    oracion = random.choice(oraciones)
    print(f"Uzupełnij zdanie: {oracion}")
    respuesta = input("Twoja odpowiedź: ").strip().lower()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("Poprawnie! 🎉\n")
    else:
        print(f"Niepoprawnie. Prawidłowa odpowiedź to: {respuestas_correctas[indice]}\n")

# Menú principal
def main():
    while True:
        print("Bienvenido a la aplicación de práctica de idiomas")
        print("1. Español")
        print("2. Portugués")
        print("3. Francés")
        print("4. Italiano")
        print("5. Alemán")
        print("6. Polaco")
        print("7. Salir")
        idioma = input("Elige un idioma (1-7): ").strip()
        
        if idioma == "1":
            while True:
                print("\n--- Ejercicios en Español ---")
                print("1. Asociación de imágenes con palabras")
                print("2. Dictado Interactivo")
                print("3. Ordenar Palabras")
                print("4. Rellenar Espacios en Blanco")
                print("5. Volver al menú principal")
                opcion = input("Elige una opción (1-5): ").strip()
                
                if opcion == "1":
                    asociacion_imagenes_palabras_es()
                elif opcion == "2":
                    dictado_interactivo_es()
                elif opcion == "3":
                    ordenar_palabras_es()
                elif opcion == "4":
                    rellenar_espacios_es()
                elif opcion == "5":
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.\n")
        
        elif idioma == "2":
            while True:
                print("\n--- Ejercicios en Portugués ---")
                print("1. Associação de imagens com palavras")
                print("2. Ditado Interativo")
                print("3. Ordenar Palavras")
                print("4. Preencher Espaços em Branco")
                print("5. Voltar ao menu principal")
                opcion = input("Escolha uma opção (1-5): ").strip()
                
                if opcion == "1":
                    asociacion_imagenes_palabras_pt()
                elif opcion == "2":
                    dictado_interactivo_pt()
                elif opcion == "3":
                    ordenar_palabras_pt()
                elif opcion == "4":
                    rellenar_espacios_pt()
                elif opcion == "5":
                    break
                else:
                    print("Opção inválida. Tente novamente.\n")
        
        elif idioma == "3":
            while True:
                print("\n--- Ejercicios en Francés ---")
                print("1. Association d'images avec des mots")
                print("2. Dictée Interactive")
                print("3. Ordre des Mots")
                print("4. Remplir les Blancs")
                print("5. Retour au menu principal")
                opcion = input("Choisissez une option (1-5): ").strip()
                
                if opcion == "1":
                    asociacion_imagenes_palabras_fr()
                elif opcion == "2":
                    dictado_interactivo_fr()
                elif opcion == "3":
                    ordenar_palabras_fr()
                elif opcion == "4":
                    rellenar_espacios_fr()
                elif opcion == "5":
                    break
                else:
                    print("Option invalide. Réessayez.\n")
        
        elif idioma == "4":
            while True:
                print("\n--- Ejercicios en Italiano ---")
                print("1. Associazione di immagini con parole")
                print("2. Dettato Interattivo")
                print("3. Ordine delle Parole")
                print("4. Riempire gli Spazi Vuoti")
                print("5. Torna al menu principale")
                opcion = input("Scegli un'opzione (1-5): ").strip()
                
                if opcion == "1":
                    asociacion_imagenes_palabras_it()
                elif opcion == "2":
                    dictado_interactivo_it()
                elif opcion == "3":
                    ordenar_palabras_it()
                elif opcion == "4":
                    rellenar_espacios_it()
                elif opcion == "5":
                    break
                else:
                    print("Opzione non valida. Riprova.\n")
        
        elif idioma == "5":
            while True:
                print("\n--- Ejercicios en Alemán ---")
                print("1. Bild-Wort-Assoziation")
                print("2. Interaktives Diktat")
                print("3. Wortreihenfolge")
                print("4. Lücken füllen")
                print("5. Zurück zum Hauptmenü")
                opcion = input("Wählen Sie eine Option (1-5): ").strip()
                
                if opcion == "1":
                    asociacion_imagenes_palabras_de()
                elif opcion == "2":
                    dictado_interactivo_de()
                elif opcion == "3":
                    ordenar_palabras_de()
                elif opcion == "4":
                    rellenar_espacios_de()
                elif opcion == "5":
                    break
                else:
                    print("Ungültige Option. Versuchen Sie es erneut.\n")
        
        elif idioma == "6":
            while True:
                print("\n--- Ejercicios en Polaco ---")
                print("1. Asocjacja obrazów ze słowami")
                print("2. Interaktywny Dyktando")
                print("3. Kolejność Słów")
                print("4. Uzupełnij Luki")
                print("5. Wróć do menu głównego")
                opcion = input("Wybierz opcję (1-5): ").strip()
                
                if opcion == "1":
                    asociacion_imagenes_palabras_pl()
                elif opcion == "2":
                    dictado_interactivo_pl()
                elif opcion == "3":
                    ordenar_palabras_pl()
                elif opcion == "4":
                    rellenar_espacios_pl()
                elif opcion == "5":
                    break
                else:
                    print("Nieprawidłowa opcja. Spróbuj ponownie.\n")
        
        elif idioma == "7":
            print("Gracias por usar la aplicación. ¡Hasta pronto! 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
