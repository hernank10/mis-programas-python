# Función para mostrar las reglas ortográficas
def mostrar_reglas(reglas):
    print("Reglas ortográficas:")
    for clave, descripcion in reglas.items():
        print(f"- {descripcion}")
    say("Por favor, presta atención a las siguientes reglas ortográficas.")
    for descripcion in reglas.values():
        say(descripcion)
