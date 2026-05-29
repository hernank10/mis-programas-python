import random

# Base de datos parcial (se puede ampliar a 100)
ejemplos = [
    {"palabra": "bello", "afi": "/ˈbe.ʎo/", "regla": "Se escribe con 'll' y no con 'y' porque proviene del latín 'bellus'."},
    {"palabra": "vello", "afi": "/ˈbe.ʎo/", "regla": "Se escribe con 'v' porque proviene del latín 'vellus'."},
    {"palabra": "queso", "afi": "/ˈke.so/", "regla": "La 'qu' representa el sonido /k/ antes de e, i."},
    {"palabra": "gente", "afi": "/ˈxen.te/", "regla": "La 'g' representa /x/ antes de e, i."},
    {"palabra": "zapato", "afi": "/θa.ˈpa.to/ o /sa.ˈpa.to/", "regla": "La 'z' representa /θ/ en España y /s/ en América."}
]

# Función principal
def practicar_ortografia():
    print("📝 Bienvenido al Práctico de Ortografía con AFI\n")
    aciertos = 0

    for i in range(5):  # Puedes cambiar a 10, 20, etc.
        palabra = random.choice(ejemplos)
        print(f"\nTranscripción fonética: {palabra['afi']}")
        print(f"Regla ortográfica: {palabra['regla']}")
        respuesta = input("Escribe la palabra correctamente: ").strip().lower()

        if respuesta == palabra["palabra"]:
            print("✅ ¡Correcto!\n")
            aciertos += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es: {palabra['palabra']}\n")

    print(f"Has tenido {aciertos} aciertos de 5.\n¡Sigue practicando!")

# Ejecutar
if __name__ == "__main__":
    practicar_ortografia()
