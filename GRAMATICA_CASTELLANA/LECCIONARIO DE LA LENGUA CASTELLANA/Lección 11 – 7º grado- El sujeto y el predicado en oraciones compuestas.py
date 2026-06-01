import os

def mostrar_teoria():
    print("\n📘 TEORÍA:")
    print("""
En las oraciones compuestas, se pueden encontrar varios sujetos y varios predicados.
Cada proposición dentro de la oración tiene su propio sujeto y predicado, aunque a veces el sujeto puede estar elíptico (implícito).
Tipos de sujeto:
1. Explícito o expreso: aparece directamente en la oración.
2. Implícito o tácito: no aparece, pero se sobreentiende por la conjugación verbal.
Ejemplo:
- María estudia y (ella) escribe poemas.
Aquí, en la segunda proposición, el sujeto 'ella' está implícito.
    """)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS:")
    print("""
1. Juan lee novelas y escribe cuentos. → Sujeto: Juan (implícito en la segunda proposición).
2. Los niños juegan en el parque y las niñas saltan la cuerda. → Dos sujetos explícitos.
3. Estudiamos mucho, pero no pasamos el examen. → Sujeto implícito: nosotros.
    """)

def actividades_sugeridas():
    print("\n🎲 ACTIVIDADES SUGERIDAS:")
    print("""
1. Escribe un cuento corto (3 a 5 oraciones). Luego identifica el sujeto y el predicado de cada oración.
2. Representa con un compañero una dramatización donde cada uno actúe como el sujeto de una oración.
3. Lee un párrafo breve de un texto literario y subraya los sujetos y predicados.
    """)
    nuevo = input("¿Deseas escribir y guardar una nueva actividad? (s/n): ").strip().lower()
    if nuevo == 's':
        actividad = input("Escribe tu nueva actividad: ")
        with open("actividades_leccion11_7grado.txt", "a", encoding="utf-8") as f:
            f.write(f"- {actividad}\n")
        print("✅ Actividad guardada.")

def ejercicio_escritura():
    print("\n📝 EJERCICIO INTERACTIVO:")
    print("Escribe una oración compuesta y luego identifica el sujeto y el predicado de cada proposición.")
    oracion = input("Escribe tu oración: ")
    sujeto = input("Identifica el/los sujeto(s): ")
    predicado = input("Identifica el/los predicado(s): ")
    with open("respuestas_alumno_leccion11_7grado.txt", "a", encoding="utf-8") as f:
        f.write(f"Oración: {oracion}\n")
        f.write(f"Sujeto(s): {sujeto}\n")
        f.write(f"Predicado(s): {predicado}\n\n")
    print("✅ Respuesta guardada.")

def menu():
    while True:
        print("\n🎓 MENÚ PRINCIPAL – Lección 11 (7º Grado)")
        print("1. Ver teoría sobre sujeto y predicado en oraciones compuestas")
        print("2. Ver ejemplos")
        print("3. Actividades sugeridas")
        print("4. Ejercicio de escritura")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            actividades_sugeridas()
        elif opcion == "4":
            ejercicio_escritura()
        elif opcion == "5":
            print("¡Hasta luego! Sigue practicando 🧠📖")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar programa
menu()
