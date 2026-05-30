def mostrar_menu():
    print("1. Praticar antônimos")
    print("2. Sair")

def praticar_antonimos():
    palavras = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardio"],
        "alto": ["baixo", "pequeno", "reduzido"]
    }
    for palavra, antonimos in palavras.items():
        print(f"Palavra: {palavra}")
        print(f"Antônimos: {', '.join(antonimos)}")
        print()

def main():
    while True:
        mostrar_menu()
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            praticar_antonimos()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
