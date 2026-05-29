import random

def generar_frase_organizadora(tipo):
    if tipo == 'recuento':
        return "A continuación, se presenta una lista de propiedades:"
    elif tipo == 'síntesis':
        return "Las siguientes propiedades resumen el objeto en cuestión:"
    elif tipo == 'encuadramiento':
        return "El objeto descrito se caracteriza por varias propiedades importantes:"
    else:
        return random.choice([
            "A continuación, se presenta una lista de propiedades:",
            "Las siguientes propiedades resumen el objeto en cuestión:",
            "El objeto descrito se caracteriza por varias propiedades importantes:"
        ])

def agregar_propiedad(propiedades):
    propiedad = input("Ingrese una nueva propiedad: ")
    propiedades.append(propiedad.strip())
    print(f"Propiedad '{propiedad}' agregada con éxito.")

def eliminar_propiedad(propiedades):
    print("Propiedades actuales:")
    for i, propiedad in enumerate(propiedades, 1):
        print(f"{i}. {propiedad}")
    try:
        eliminar = int(input("Ingrese el número de la propiedad que desea eliminar: "))
        if 1 <= eliminar <= len(propiedades):
            propiedad_eliminada = propiedades.pop(eliminar - 1)
            print(f"Propiedad '{propiedad_eliminada}' eliminada con éxito.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada no válida. Intente de nuevo.")

def generar_parrafo_enumeracion(tipo_frase, objeto, propiedades):
    # Generar la frase organizadora
    frase_organizadora = generar_frase_organizadora(tipo_frase)

    # Generar el párrafo de enumeración
    parrafo = f"{frase_organizadora}\n"  # Añadir la frase organizadora
    parrafo += f"El {objeto} tiene las siguientes características:\n"

    # Enumerar las propiedades
    for i, propiedad in enumerate(propiedades, 1):
        parrafo += f"{i}. {propiedad.capitalize()}\n"

    return parrafo

def generar_parrafo_descriptivo(objeto, propiedades):
    parrafo = f"El {objeto} se caracteriza por su capacidad de:\n"
    parrafo += ', '.join(propiedades) + ".\n"
    return parrafo

def generar_parrafo_argumentativo(objeto, propiedades):
    parrafo = f"El {objeto} es considerado importante porque:\n"
    for propiedad in propiedades:
        parrafo += f"- {propiedad.capitalize()}.\n"
    return parrafo

def mostrar_menu_principal():
    print("\nMenú Principal:")
    print("1. Agregar una propiedad")
    print("2. Eliminar una propiedad")
    print("3. Ver las propiedades actuales")
    print("4. Generar párrafo de enumeración")
    print("5. Generar párrafo descriptivo")
    print("6. Generar párrafo argumentativo")
    print("7. Salir")

def main():
    objeto = input("Ingrese el tipo de párrafo de enumeración, argumentativo o descriptivo con su objeto, hecho o idea que desea escribir: ")
    propiedades = []

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_propiedad(propiedades)

        elif opcion == '2':
            if propiedades:
                eliminar_propiedad(propiedades)
            else:
                print("No hay propiedades para eliminar.")

        elif opcion == '3':
            if propiedades:
                print("Propiedades actuales:")
                for i, propiedad in enumerate(propiedades, 1):
                    print(f"{i}. {propiedad}")
            else:
                print("No se han agregado propiedades.")

        elif opcion == '4':
            if propiedades:
                print("\nSeleccione el tipo de frase organizadora:")
                print("1. Recuento")
                print("2. Síntesis")
                print("3. Encuadramiento")
                print("4. Aleatorio")
                tipo_opcion = input("Seleccione una opción: ")

                if tipo_opcion == '1':
                    tipo_frase = 'recuento'
                elif tipo_opcion == '2':
                    tipo_frase = 'síntesis'
                elif tipo_opcion == '3':
                    tipo_frase = 'encuadramiento'
                else:
                    tipo_frase = 'aleatorio'

                parrafo = generar_parrafo_enumeracion(tipo_frase, objeto, propiedades)
                print("\nPárrafo de enumeración generado:\n")
                print(parrafo)
            else:
                print("No se han agregado propiedades para generar el párrafo.")

        elif opcion == '5':
            if propiedades:
                parrafo = generar_parrafo_descriptivo(objeto, propiedades)
                print("\nPárrafo descriptivo generado:\n")
                print(parrafo)
            else:
                print("No se han agregado propiedades para generar el párrafo.")

        elif opcion == '6':
            if propiedades:
                parrafo = generar_parrafo_argumentativo(objeto, propiedades)
                print("\nPárrafo argumentativo generado:\n")
                print(parrafo)
            else:
                print("No se han agregado propiedades para generar el párrafo.")

        elif opcion == '7':
            print("¡Gracias por usar el programa!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
