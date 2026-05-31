import random

# 50 oraciones por tipo
adjetivo_absoluto = [
    "Libros, tiene miles.", "Amigos, conserva pocos.", "Ideas, le sobran.",
    "Problemas, ha enfrentado bastantes.", "Sueños, mantiene vivos muchos.",
    "Miedos, ha superado varios.", "Trabajos, ha tenido muchos.",
    "Secretos, guarda pocos.", "Dudas, todavía conserva algunas.",
    "Recuerdos, le quedan pocos.", "Historias, conoce muchas.",
    "Enemigos, se ha hecho varios.", "Consejos, ha dado muchísimos.",
    "Oportunidades, ha dejado pasar muchas.", "Momentos, ha vivido intensos.",
    "Errores, cometió incontables.", "Clases, ha tomado bastantes.",
    "Pasiones, ha tenido muchas.", "Disgustos, sufrió varios.",
    "Ilusiones, perdió muchas.", "Pesadillas, tiene constantes.",
    "Fracasos, ha acumulado varios.", "Satisfacciones, ha tenido bastantes.",
    "Hobbies, practica diversos.", "Canciones, canta muchísimas.",
    "Recetas, conoce infinidad.", "Juegos, disfruta muchos.",
    "Experiencias, ha vivido únicas.", "Responsabilidades, carga pesadas.",
    "Aventuras, ha tenido increíbles.", "Vacaciones, ha disfrutado espléndidas.",
    "Fiestas, ha celebrado incontables.", "Metas, ha alcanzado numerosas.",
    "Planes, ha hecho muchos.", "Tareas, ha cumplido todas.",
    "Promesas, ha roto algunas.", "Proyectos, ha realizado ambiciosos.",
    "Duelos, ha enfrentado difíciles.", "Obstáculos, ha superado duros.",
    "Éxitos, ha logrado grandes.", "Conversaciones, ha sostenido profundas.",
    "Malentendidos, ha aclarado varios.", "Objetivos, ha definido claros.",
    "Libros, ha escrito valiosos.", "Temores, ha vencido antiguos.",
    "Aciertos, ha tenido certeros.", "Pensamientos, ha compartido sinceros.",
    "Discursos, ha dado emotivos.", "Regalos, ha recibido bellos.",
    "Anécdotas, ha contado graciosas."
]

pronombre_retoma = [
    "Libros, los guarda con celo.", "Amigos, los valora muchísimo.",
    "Ideas, las organiza con cuidado.", "Problemas, los enfrenta con valentía.",
    "Sueños, los persigue sin cesar.", "Miedos, los ha dejado atrás.",
    "Trabajos, los hizo todos bien.", "Secretos, los mantiene en silencio.",
    "Dudas, las expresa sin miedo.", "Recuerdos, los guarda en fotos.",
    "Historias, las relata con pasión.", "Enemigos, los evita siempre.",
    "Consejos, los escucha con atención.", "Oportunidades, las desperdició.",
    "Momentos, los revive constantemente.", "Errores, los repasa para aprender.",
    "Clases, las aprobó todas.", "Pasiones, las alimenta a diario.",
    "Disgustos, los maneja con calma.", "Ilusiones, las perdió con el tiempo.",
    "Pesadillas, las sufre en silencio.", "Fracasos, los analiza con madurez.",
    "Satisfacciones, las celebra con alegría.", "Hobbies, los practica los fines de semana.",
    "Canciones, las canta con emoción.", "Recetas, las mejora cada vez.",
    "Juegos, los comparte con amigos.", "Experiencias, las escribe en su diario.",
    "Responsabilidades, las asume con madurez.", "Aventuras, las narra con orgullo.",
    "Vacaciones, las planea con entusiasmo.", "Fiestas, las organiza con esmero.",
    "Metas, las cumple con disciplina.", "Planes, los modifica con frecuencia.",
    "Tareas, las completa a tiempo.", "Promesas, las rompe sin querer.",
    "Proyectos, los presenta con detalle.", "Duelos, los sobrelleva en silencio.",
    "Obstáculos, los supera con esfuerzo.", "Éxitos, los celebra con humildad.",
    "Conversaciones, las recuerda con cariño.", "Malentendidos, los aclara pronto.",
    "Objetivos, los persigue sin pausa.", "Libros, los lee de noche.",
    "Temores, los enfrenta con decisión.", "Aciertos, los reconoce siempre.",
    "Pensamientos, los plasma en papel.", "Discursos, los practica antes de hablar.",
    "Regalos, los agradece con emoción.", "Anécdotas, las cuenta con humor."
]

puntos = 0
registro = []

def mostrar_menu():
    print("\n--- Ejercicio de Anticipación Enfática ---")
    print("1. Ver ejemplos por categoría")
    print("2. Escribir una oración y clasificarla")
    print("3. Ver puntuación actual")
    print("4. Salir y guardar registro")

def ver_ejemplos():
    print("\nEjemplos con adjetivo absoluto:")
    for oracion in random.sample(adjetivo_absoluto, 5):
        print(" →", oracion)
    print("\nEjemplos con pronombre que retoma el sustantivo:")
    for oracion in random.sample(pronombre_retoma, 5):
        print(" →", oracion)

def clasificar_oracion_usuario(oracion, eleccion_usuario):
    global puntos
    correcta = False

    if any(pron in oracion.lower() for pron in [" los ", " las ", " lo ", " la "]):
        categoria = "Pronombre"
        correcta = eleccion_usuario == "2"
    elif any(adj in oracion.lower() for adj in ["muchos", "pocos", "varios", "bastantes", "numerosas", "incontables"]):
        categoria = "Adjetivo"
        correcta = eleccion_usuario == "1"
    else:
        categoria = "No clara"

    resultado = "✔️ Correcto" if correcta else "❌ Incorrecto"
    if correcta:
        puntos += 1

    registro.append(f"Oración: {oracion}\nClasificación del usuario: {eleccion_usuario}\nClasificación real: {categoria}\nResultado: {resultado}\n")
    print(f"\nResultado: {resultado}\nClasificación real: {categoria}\n")

def escribir_y_clasificar():
    print("\nEscribe una oración con anticipación enfática:")
    oracion = input("→ ")

    print("\n¿Qué tipo de estructura crees que tiene?")
    print("1. Adjetivo absoluto (Ej: Problemas, tiene muchos.)")
    print("2. Pronombre que retoma el sustantivo (Ej: Problemas, los tiene a montones.)")
    eleccion = input("Tu elección (1 o 2): ")

    if eleccion not in ["1", "2"]:
        print("Opción inválida.")
        return
    clasificar_oracion_usuario(oracion, eleccion)

def guardar_registro():
    with open("registro_ejercicios.txt", "w", encoding="utf-8") as f:
        f.write("Registro de respuestas - Ejercicio de anticipación enfática\n\n")
        for r in registro:
            f.write(r + "\n")
    print("✅ Registro guardado en 'registro_ejercicios.txt'")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            ver_ejemplos()
        elif opcion == "2":
            escribir_y_clasificar()
        elif opcion == "3":
            print(f"\n🏆 Puntuación actual: {puntos}")
        elif opcion == "4":
            guardar_registro()
            print("¡Hasta luego! Sigue practicando 😊")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
