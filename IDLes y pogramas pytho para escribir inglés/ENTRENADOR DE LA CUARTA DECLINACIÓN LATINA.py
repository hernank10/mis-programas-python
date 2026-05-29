import random

# Diccionario con sustantivos de la cuarta declinación y sus significados
declinacion_cuarta = {
    "manus": "mano (f.)",
    "exercitus": "ejército (m.)",
    "fructus": "fruto (m.)",
    "senatus": "senado (m.)",
    "spiritus": "espíritu, aliento (m.)",
    "impetus": "ímpetu, ataque (m.)",
    "cornu": "cuerno (n.)",
    "genu": "rodilla (n.)",
    "casus": "caída, caso (m.)",
    "usus": "uso, costumbre (m.)"
}

# Formas de la cuarta declinación (ejemplo: manus, manus)
# Singular y plural: nominativo, genitivo, dativo, acusativo, ablativo
formas = {
    "singular": ["-us / -u", "-us", "-ui / -u", "-um / -u", "-u"],
    "plural": ["-us / -ua", "-uum", "-ibus", "-us / -ua", "-ibus"]
}

# Función para generar un ejercicio aleatorio
def generar_ejercicio():
    palabra, significado = random.choice(list(declinacion_cuarta.items()))
    numero = random.choice(["singular", "plural"])
    caso = random.randint(0, 4)  # 0=nom, 1=gen, 2=dat, 3=acc, 4=abl

    print(f"\nDeclina la palabra: {palabra} ({significado})")
    print(f"👉 Forma pedida: {numero} - {['NOM','GEN','DAT','ACC','ABL'][caso]}")
    respuesta = input("Tu respuesta: ")

    correcta = palabra[:-2] + formas[numero][caso]  # simplificación

    if respuesta.strip().lower() == correcta.lower():
        print("✅ ¡Correcto!")
        return True
    else:
        print(f"❌ Incorrecto. La forma esperada era: {correcta}")
        return False

# Entrenador con 30 ejercicios
def entrenador_cuarta():
    print("=== ENTRENADOR DE LA CUARTA DECLINACIÓN LATINA ===")
    print("Sustantivos de ejemplo: manus, exercitus, fructus, cornu, genu...\n")

    puntaje = 0
    for i in range(1, 31):
        print(f"\nEjercicio {i}/30")
        if generar_ejercicio():
            puntaje += 1

    print("\n=== RESULTADOS ===")
    print(f"Puntaje final: {puntaje}/30")
    if puntaje == 30:
        print("🌟 ¡Excelente dominio de la cuarta declinación!")
    elif puntaje > 20:
        print("💪 Muy bien, sigue practicando para perfeccionarte.")
    else:
        print("📖 Revisa las tablas de la cuarta declinación y vuelve a intentarlo.")

# Ejecutar el programa
if __name__ == "__main__":
    entrenador_cuarta()
