def mostrar_menu():
    print("1. Praticar sinônimos")
    print("2. Sair")

def praticar_sinonimos():
    palavras = {
        "feliz": ["contento", "alegre", "satisfeito"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligeiro"]
    }
    for palavra, sinonimos in palavras.items():
        print(f"Palavra: {palavra}")
        print(f"Sinônimos: {', '.join(sinonimos)}")
        print()

def main():
    while True:
        mostrar_menu()
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            praticar_sinonimos()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
