def mostrar_menu():
    print("1. Praticar homônimos")
    print("2. Sair")

def praticar_homonimos():
    palavras = {
        "vino": ["Bebida alcoólica", "Passado do verbo 'venir'"],
        "llama": ["Animal sul-americano", "Fogo", "Forma do verbo 'llamar'"],
        "banco": ["Banco para sentar", "Instituição financeira"]
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
            praticar_homonimos()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
