def mostrar_menu():
    print("1. Praticar palavras com múltiplos significados")
    print("2. Sair")

def praticar_multiplos_significados():
    palavras = {
        "cabeza": ["Parte superior do corpo", "Líder de um grupo"],
        "lengua": ["Órgão muscular na boca", "Idioma"],
        "ojo": ["Órgão da visão", "Furo de agulha"]
    }
    for palavra, significados in palavras.items():
        print(f"Palavra: {palavra}")
        for i, significado in enumerate(significados, 1):
            print(f"{i}. {significado}")
        print()

def main():
    while True:
        mostrar_menu()
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            praticar_multiplos_significados()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
