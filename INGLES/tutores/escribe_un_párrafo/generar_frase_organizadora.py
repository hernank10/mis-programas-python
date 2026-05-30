import random

def generar_frase_organizadora(tipo):
    if tipo == 'recuento':
        return "A continuación, se presenta una lista de propiedades:"
    elif tipo == 'síntesis':
        return "Las siguientes propiedades resumen el objeto en cuestión:"
    elif tipo == 'encuadramiento':
        return "El objeto descrito se caracteriza por varias propiedades importantes:"
    else:
        return "Esta es una lista de propiedades destacadas:"

def generar_parrafo_enumeracion():
    # Pedir al usuario el tema central
    objeto = input("Ingrese el objeto, hecho o idea que desea describir: ")

    # Pedir al usuario que ingrese las propiedades (separadas por comas)
    propiedades = input("Ingrese las propiedades que describen el objeto (separadas por comas): ").split(',')

    # Limpiar espacios innecesarios en las propiedades
    propiedades = [prop.strip() for prop in propiedades]

    # Seleccionar el tipo de frase organizadora
    tipos_frases = ['recuento', 'síntesis', 'encuadramiento']
    tipo_frase = random.choice(tipos_frases)

    # Generar la frase organizadora
    frase_organizadora = generar_frase_organizadora(tipo_frase)

    # Generar el párrafo de enumeración
    parrafo = f"{frase_organizadora}\n"  # Añadir la frase organizadora
    parrafo += f"El {objeto} tiene las siguientes características:\n"

    # Enumerar las propiedades
    for i, propiedad in enumerate(propiedades, 1):
        parrafo += f"{i}. {propiedad.capitalize()}\n"

    return parrafo

# Ejecutar el programa
if __name__ == "__main__":
    parrafo_generado = generar_parrafo_enumeracion()
    print("\nPárrafo generado:\n")
    print(parrafo_generado)
