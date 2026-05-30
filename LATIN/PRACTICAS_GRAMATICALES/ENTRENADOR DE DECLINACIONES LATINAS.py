import random

# Diccionario con las cinco declinaciones y sus ejercicios
declinaciones = {
    "Primera": [
        "Rosa (singular nominativo)", "Rosae (singular genitivo)", "Rosam (singular acusativo)",
        "Rosae (singular dativo)", "Rosa (singular ablativo)", "Rosae (plural nominativo)",
        "Rosarum (plural genitivo)", "Rosis (plural dativo)", "Rosas (plural acusativo)", "Rosis (plural ablativo)",
        "Poeta (singular nominativo)", "Poetae (singular genitivo)", "Poetam (singular acusativo)",
        "Poetae (singular dativo)", "Poeta (singular ablativo)", "Poetae (plural nominativo)",
        "Poetarum (plural genitivo)", "Poetis (plural dativo)", "Poetas (plural acusativo)", "Poetis (plural ablativo)",
        "Agricola (singular nominativo)", "Agricolae (singular genitivo)", "Agricolam (singular acusativo)",
        "Agricolae (singular dativo)", "Agricola (singular ablativo)", "Agricolae (plural nominativo)",
        "Agricolis (plural dativo)", "Agricolas (plural acusativo)", "Agricolis (plural ablativo)", "Agricolarum (plural genitivo)"
    ],
    "Segunda": [
        "Dominus (singular nominativo)", "Domini (singular genitivo)", "Dominum (singular acusativo)",
        "Domino (singular dativo)", "Domino (singular ablativo)", "Domini (plural nominativo)",
        "Dominorum (plural genitivo)", "Dominis (plural dativo)", "Dominos (plural acusativo)", "Dominis (plural ablativo)",
        "Puer (singular nominativo)", "Pueri (singular genitivo)", "Puerum (singular acusativo)",
        "Puero (singular dativo)", "Puero (singular ablativo)", "Pueri (plural nominativo)",
        "Puerorum (plural genitivo)", "Pueris (plural dativo)", "Pueros (plural acusativo)", "Pueris (plural ablativo)",
        "Bellum (singular nominativo)", "Belli (singular genitivo)", "Bellum (singular acusativo)",
        "Bello (singular dativo)", "Bello (singular ablativo)", "Bella (plural nominativo)",
        "Bellorum (plural genitivo)", "Bellis (plural dativo)", "Bella (plural acusativo)", "Bellis (plural ablativo)"
    ],
    "Tercera": [
        "Rex (singular nominativo)", "Regis (singular genitivo)", "Regem (singular acusativo)",
        "Regi (singular dativo)", "Rege (singular ablativo)", "Reges (plural nominativo)",
        "Regum (plural genitivo)", "Regibus (plural dativo)", "Reges (plural acusativo)", "Regibus (plural ablativo)",
        "Corpus (singular nominativo)", "Corporis (singular genitivo)", "Corpus (singular acusativo)",
        "Corpori (singular dativo)", "Corpore (singular ablativo)", "Corpora (plural nominativo)",
        "Corporum (plural genitivo)", "Corporibus (plural dativo)", "Corpora (plural acusativo)", "Corporibus (plural ablativo)",
        "Civis (singular nominativo)", "Civis (singular genitivo)", "Civem (singular acusativo)",
        "Civi (singular dativo)", "Cive (singular ablativo)", "Cives (plural nominativo)",
        "Civium (plural genitivo)", "Civibus (plural dativo)", "Cives (plural acusativo)", "Civibus (plural ablativo)"
    ],
    "Cuarta": [
        "Manus (singular nominativo)", "Manus (singular genitivo)", "Manum (singular acusativo)",
        "Manui (singular dativo)", "Manu (singular ablativo)", "Manus (plural nominativo)",
        "Manuum (plural genitivo)", "Manibus (plural dativo)", "Manus (plural acusativo)", "Manibus (plural ablativo)",
        "Fructus (singular nominativo)", "Fructus (singular genitivo)", "Fructum (singular acusativo)",
        "Fructui (singular dativo)", "Fructu (singular ablativo)", "Fructus (plural nominativo)",
        "Fructuum (plural genitivo)", "Fructibus (plural dativo)", "Fructus (plural acusativo)", "Fructibus (plural ablativo)",
        "Cornu (singular nominativo)", "Cornus (singular genitivo)", "Cornu (singular acusativo)",
        "Cornui (singular dativo)", "Cornu (singular ablativo)", "Cornua (plural nominativo)",
        "Cornuum (plural genitivo)", "Cornibus (plural dativo)", "Cornua (plural acusativo)", "Cornibus (plural ablativo)"
    ],
    "Quinta": [
        "Res (singular nominativo)", "Rei (singular genitivo)", "Rem (singular acusativo)",
        "Rei (singular dativo)", "Re (singular ablativo)", "Res (plural nominativo)",
        "Rerum (plural genitivo)", "Rebus (plural dativo)", "Res (plural acusativo)", "Rebus (plural ablativo)",
        "Dies (singular nominativo)", "Diei (singular genitivo)", "Diem (singular acusativo)",
        "Diei (singular dativo)", "Die (singular ablativo)", "Dies (plural nominativo)",
        "Dierum (plural genitivo)", "Diebus (plural dativo)", "Dies (plural acusativo)", "Diebus (plural ablativo)",
        "Fides (singular nominativo)", "Fidei (singular genitivo)", "Fidem (singular acusativo)",
        "Fidei (singular dativo)", "Fide (singular ablativo)", "Fides (plural nominativo)",
        "Fidearum (plural genitivo)", "Fidibus (plural dativo)", "Fides (plural acusativo)", "Fidibus (plural ablativo)"
    ]
}

def mostrar_menu():
    print("\n=== ENTRENADOR DE DECLINACIONES LATINAS ===")
    for i, decl in enumerate(declinaciones.keys(), 1):
        print(f"{i}. {decl} declinación")
    print("6. Salir")

def practicar(declinacion):
    print(f"\nPracticando la {declinacion} declinación...\n")
    ejercicios = declinaciones[declinacion]
    random.shuffle(ejercicios)
    for i in range(5):  # muestra 5 ejercicios aleatorios
        print(f"Ejercicio {i+1}: {ejercicios[i]}")
    input("\nPresiona Enter para volver al menú...")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "6":
            print("¡Hasta pronto! Vale, discipule.")
            break
        elif opcion in ["1","2","3","4","5"]:
            decl = list(declinaciones.keys())[int(opcion)-1]
            practicar(decl)
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
