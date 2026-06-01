# ============================================================
# SISTEMA TRILINGÜE CON ESPIRAL DE APRENDIZAJE
# Griego transliterado – Español – Inglés
# ============================================================

import random
import time

conceptos = [
    ("logos", "razón", "reason", "Para los griegos, el logos era la estructura racional del mundo."),
    ("physis", "naturaleza", "nature", "Physis expresa el surgir, crecer y moverse de lo vivo."),
    ("arete", "virtud, excelencia", "virtue, excellence", "Arete es la excelencia moral y humana."),
    ("ethos", "carácter", "character", "Ethos designa la disposición habitual del individuo."),
    ("zoe", "vida", "life", "Zoe es la vida en su sentido más elemental."),
    ("psyche", "alma", "soul", "Psyche une alma, respiración y principio vital."),
    ("kosmos", "universo, orden", "cosmos, order", "Kosmos implica belleza, orden y armonía."),
    ("dikaiosyne", "justicia", "justice", "Dikaiosyne era la virtud de actuar correctamente."),
    ("aletheia", "verdad", "truth", "Aletheia significa desocultamiento, revelación de lo real."),
    ("sophia", "sabiduría", "wisdom", "Sophia es la sabiduría que guía la vida.")
]

# Datos para metacognición
estadisticas = {
    "aciertos": 0,
    "errores": 0,
    "historial": []
}

frases_usuario = []

# -------------------------------
# Mecanismos de exposición multimodal
# -------------------------------
def mostrar_exposicion(concepto):
    griego, esp, eng, nota = concepto
    print("\n=== EXPOSICIÓN MULTIMODAL ===")
    print(f"Griego transliterado : {griego}")
    print(f"Español              : {esp}")
    print(f"Inglés               : {eng}")
    print(f"Nota cultural        : {nota}")
    print("-" * 50)


# -------------------------------
# Retroalimentación con explicación
# -------------------------------
def retroalimentar(respuesta, correcta, campo):
    if respuesta.lower().strip() in correcta.lower():
        print(f"✔ {campo} correcto.")
        estadisticas["aciertos"] += 1
        return True
    else:
        print(f"✘ {campo} incorrecto. Respuesta esperada: {correcta}")
        estadisticas["errores"] += 1
        return False


# -------------------------------
# Actividad principal normal (griego → español/inglés)
# -------------------------------
def practicar_normal(concepto):
    griego, esp, eng, nota = concepto
    mostrar_exposicion(concepto)

    resp_es = input("Escriba el significado en español: ")
    retroalimentar(resp_es, esp.split(",")[0], "Español")

    resp_en = input("Escriba el significado en inglés: ")
    retroalimentar(resp_en, eng, "Inglés")

    # Contextualización guiada
    print("\nContextualización: Cree frases reales.")
    print("Ejemplo sugerido: Cómo usaría este concepto en una conversación o texto real.")
    frase_es = input("Frase en español: ")
    frase_en = input("Frase en inglés: ")

    frases_usuario.append((griego, frase_es, frase_en))
    estadisticas["historial"].append((griego, resp_es, resp_en))


# -------------------------------
# Actividad inversa (español/inglés → griego)
# -------------------------------
def practicar_inverso(concepto):
    griego, esp, eng, nota = concepto
    print("\n=== EJERCICIO INVERSO ===")
    print(f"Significado español : {esp}")
    print(f"Significado inglés  : {eng}")

    resp_gr = input("Escriba el término griego transliterado: ")
    retroalimentar(resp_gr, griego, "Griego transliterado")

    resp_es = input("Repita el significado en español: ")
    retroalimentar(resp_es, esp.split(",")[0], "Español")

    resp_en = input("Repita el significado en inglés: ")
    retroalimentar(resp_en, eng, "Inglés")

    estadisticas["historial"].append((resp_gr, resp_es, resp_en))


# -------------------------------
# Repetición espaciada
# (conceptos frecuentes → si fueron fallados)
# -------------------------------
def seleccionar_concepto():
    # si hay errores recientes, aumentar probabilidad de repetirlos
    if estadisticas["historial"]:
        ultimo = estadisticas["historial"][-1]
        griego_fallado = []
        # detectar fallos
        for g, es, en in estadisticas["historial"]:
            for c in conceptos:
                if c[0] == g:
                    griego_fallado.append(c)

        if griego_fallado and random.random() < 0.5:
            return random.choice(griego_fallado)

    return random.choice(conceptos)


# -------------------------------
# Metacognición
# -------------------------------
def mostrar_estadisticas():
    total = estadisticas["aciertos"] + estadisticas["errores"]
    porcentaje = (estadisticas["aciertos"] / total * 100) if total > 0 else 0

    print("\n=== ESTADÍSTICAS DE APRENDIZAJE ===")
    print(f"Aciertos totales : {estadisticas['aciertos']}")
    print(f"Errores totales  : {estadisticas['errores']}")
    print(f"Precisión global : {porcentaje:.2f}%")

    print("\nConceptos revisados:")
    for h in estadisticas["historial"]:
        print(" -", h[0])

    print("-" * 50)


# -------------------------------
# Mostrar frases del usuario
# -------------------------------
def mostrar_frases():
    print("\n=== FRASES CREADAS POR EL USUARIO ===")
    if not frases_usuario:
        print("Aún no hay frases registradas.")
    else:
        for g, es, en in frases_usuario:
            print(f"\n{g}:")
            print(f"  Español: {es}")
            print(f"  Inglés: {en}")
    print("-" * 50)


# -------------------------------
# Menú principal
# -------------------------------
def menu():
    print("\n=== SISTEMA TRILINGÜE DE ESPIRAL DE APRENDIZAJE ===")
    print("1. Practicar (griego → español/inglés)")
    print("2. Practicar inverso (español/inglés → griego)")
    print("3. Ver frases creadas")
    print("4. Ver estadísticas de progreso")
    print("5. Salir")
    return input("Seleccione una opción: ")


# -------------------------------
# Programa principal
# -------------------------------
if __name__ == "__main__":
    while True:
        op = menu()

        if op == "1":
            practicar_normal(seleccionar_concepto())

        elif op == "2":
            practicar_inverso(seleccionar_concepto())

        elif op == "3":
            mostrar_frases()

        elif op == "4":
            mostrar_estadisticas()

        elif op == "5":
            print("Gracias por usar el Sistema Trilingüe.")
            break

        else:
            print("Opción inválida.")
