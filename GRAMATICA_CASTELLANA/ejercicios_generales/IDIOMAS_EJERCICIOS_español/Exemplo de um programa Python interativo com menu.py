import random

def adivinhar_significado():
    dicionario = {"correr": "correr", "brilhante": "brilhante"}
    palavra, significado = random.choice(list(dicionario.items()))
    opcoes = [significado, "Resposta errada 1", "Resposta errada 2"]
    random.shuffle(opcoes)
    print(f"Qual é o significado da palavra '{palavra}'?")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    resposta = int(input("Escolha a resposta correta: "))
    print("Correto!" if opcoes[resposta - 1] == significado else "Errado.")

def sinonimos_antonimos():
    sinonimos = {"feliz": "alegre", "rápido": "veloz"}
    antonimos = {"feliz": "triste", "rápido": "lento"}
    palavra = random.choice(list(sinonimos.keys()))
    print(f"Digite um sinônimo ou antônimo para '{palavra}':")
    resposta = input().strip()
    if resposta in (sinonimos[palavra], antonimos[palavra]):
        print("Correto!")
    else:
        print(f"Errado. Resposta esperada: Sinônimo '{sinonimos[palavra]}', Antônimo '{antonimos[palavra]}'")

def completar_frase():
    frases = {"brilhante": "O sol está muito ______ hoje."}
    palavra, frase = random.choice(list(frases.items()))
    print(frase)
    resposta = input("Digite a palavra correta: ").strip()
    if resposta == palavra:
        print("Correto!")
    else:
        print(f"Errado. Resposta esperada: '{palavra}'")

def categorizar_palavra():
    categorias = {"científico": "técnico", "pitoresco": "literário"}
    palavra, categoria = random.choice(list(categorias.items()))
    print(f"A qual categoria pertence a palavra '{palavra}'?")
    resposta = input("Escolha entre: técnico, literário, cotidiano: ").strip().lower()
    if resposta == categoria:
        print("Correto!")
    else:
        print(f"Errado. Resposta esperada: '{categoria}'")

def definir_palavra():
    palavra = "correr"
    print(f"Defina a palavra '{palavra}':")
    input()
    print("Obrigado! A definição correta é 'mover-se rapidamente'.")

def menu():
    while True:
        print("\nMenu de Exercícios de Vocabulário")
        print("1. Adivinhar significado")
        print("2. Sinônimos e antônimos")
        print("3. Completar frase")
        print("4. Categorizar palavra")
        print("5. Definir palavra")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adivinhar_significado()
        elif escolha == "2":
            sinonimos_antonimos()
        elif escolha == "3":
            completar_frase()
        elif escolha == "4":
            categorizar_palavra()
        elif escolha == "5":
            definir_palavra()
        elif escolha == "6":
            print("Adeus!")
            break
        else:
            print("Entrada inválida. Tente novamente.")

menu()
