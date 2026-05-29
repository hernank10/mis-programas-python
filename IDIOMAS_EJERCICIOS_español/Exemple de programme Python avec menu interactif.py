import random

def deviner_signification():
    dictionnaire = {"correr": "courir", "brillante": "brillant"}
    mot, signification = random.choice(list(dictionnaire.items()))
    options = [signification, "Mauvaise réponse 1", "Mauvaise réponse 2"]
    random.shuffle(options)
    print(f"Quelle est la signification du mot '{mot}' ?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    reponse = int(input("Choisissez la bonne réponse : "))
    print("Correct !" if options[reponse - 1] == signification else "Incorrect.")

def synonymes_antonymes():
    synonymes = {"heureux": "joyeux", "rapide": "vite"}
    antonymes = {"heureux": "triste", "rapide": "lent"}
    mot = random.choice(list(synonymes.keys()))
    print(f"Entrez un synonyme ou un antonyme du mot '{mot}' :")
    reponse = input().strip()
    if reponse in (synonymes[mot], antonymes[mot]):
        print("Correct !")
    else:
        print(f"Incorrect. Réponse attendue : Synonyme '{synonymes[mot]}', Antonyme '{antonymes[mot]}'")

def completer_phrase():
    phrases = {"brillant": "Le soleil est très ______ aujourd'hui."}
    mot, phrase = random.choice(list(phrases.items()))
    print(phrase)
    reponse = input("Entrez le mot correct : ").strip()
    if reponse == mot:
        print("Correct !")
    else:
        print(f"Incorrect. Réponse attendue : '{mot}'")

def classer_mot():
    categories = {"scientifique": "technique", "pittoresque": "littéraire"}
    mot, categorie = random.choice(list(categories.items()))
    print(f"À quelle catégorie appartient le mot '{mot}' ?")
    reponse = input("Choisissez parmi : technique, littéraire, courant : ").strip().lower()
    if reponse == categorie:
        print("Correct !")
    else:
        print(f"Incorrect. Réponse attendue : '{categorie}'")

def definir_mot():
    mot = "courir"
    print(f"Définissez le mot '{mot}' :")
    input()
    print("Merci ! La définition correcte est 'se déplacer rapidement'.")

def menu():
    while True:
        print("\nMenu des exercices de vocabulaire")
        print("1. Deviner la signification")
        print("2. Synonymes et antonymes")
        print("3. Compléter une phrase")
        print("4. Classer un mot")
        print("5. Définir un mot")
        print("6. Quitter")
        choix = input("Choisissez une option : ")
        if choix == "1":
            deviner_signification()
        elif choix == "2":
            synonymes_antonymes()
        elif choix == "3":
            completer_phrase()
        elif choix == "4":
            classer_mot()
        elif choix == "5":
            definir_mot()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Entrée invalide. Veuillez réessayer.")

menu()
