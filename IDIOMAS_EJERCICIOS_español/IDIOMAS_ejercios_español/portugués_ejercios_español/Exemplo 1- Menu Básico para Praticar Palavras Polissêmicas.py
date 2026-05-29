def mostrar_menu():
    print("1. Praticar palavras polissêmicas")
    print("2. Sair")

def praticar_polissemias():
    palavras = {
        "banco": ["Assento para várias pessoas", "Instituição financeira"],
        "carta": ["Documento escrito", "Carta de baralho"],
        "corte": ["Ação de cortar", "Tribunal de justiça"]
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
            praticar_polissemias()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
