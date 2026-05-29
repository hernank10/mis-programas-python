import json
import random

# Base de datos de ejemplos (puede crecer hasta 100)
ejemplos = [
    {"texto": "Esto me parece injusto.", "categoria": "Demostrativo neutro"},
    {"texto": "Eso no tiene sentido alguno.", "categoria": "Demostrativo neutro"},
    {"texto": "Aquello fue un momento inolvidable.", "categoria": "Demostrativo neutro"},
    {"texto": "Ello no justifica su comportamiento.", "categoria": "Demostrativo neutro"},
    {"texto": "No comprendo lo que intentas decir.", "categoria": "Demostrativo neutro"},
    {"texto": "Tal fue su vergüenza, que no volvió.", "categoria": "Demostrativo neutro"},
    {"texto": "No sé cuánto costará esto.", "categoria": "Demostrativo neutro"},
    {"texto": "No me gustó lo que hizo.", "categoria": "Demostrativo neutro"},
    {"texto": "Cuanto dijo resultó ser falso.", "categoria": "Demostrativo neutro"},
    {"texto": "¿Qué te ha hecho pensar eso?", "categoria": "Demostrativo neutro"},
    {"texto": "Cantar me relaja por las noches.", "categoria": "Infinitivo sustantivado"},
    {"texto": "El comer saludable mejora la salud.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Vender no es tan fácil como parece.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Me molesta el gritar sin motivo.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Viajar es su mayor pasión.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Saber esperar también es sabiduría.", "categoria": "Infinitivo sustantivado"},
    {"texto": "El callar a tiempo evita conflictos.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Soñar despierto tiene sus beneficios.", "categoria": "Infinitivo sustantivado"},
    {"texto": "No hay mayor arte que el vivir bien.", "categoria": "Infinitivo sustantivado"},
    {"texto": "El reír alivia muchas penas.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Todo se solucionará con paciencia.", "categoria": "Cantidad"},
    {"texto": "Mucho se dijo, pero poco se hizo.", "categoria": "Cantidad"},
    {"texto": "Él tiene más de lo que aparenta.", "categoria": "Cantidad"},
    {"texto": "Yo tengo menos tiempo que tú.", "categoria": "Cantidad"},
    {"texto": "Fue demasiado para tan poco.", "categoria": "Cantidad"},
    {"texto": "Bastante se ha hecho por hoy.", "categoria": "Cantidad"},
    {"texto": "Te he escuchado harto esta semana.", "categoria": "Cantidad"},
    {"texto": "Me queda poco dinero.", "categoria": "Cantidad"},
    {"texto": "Había asaz razones para creerle.", "categoria": "Cantidad"},
    {"texto": "Todo en esta vida tiene un sentido.", "categoria": "Cantidad"},
    {"texto": "Algo extraño está ocurriendo.", "categoria": "Concepto general"},
    {"texto": "Nada puede detenernos ahora.", "categoria": "Concepto general"},
    {"texto": "No me dijo nonada de importancia.", "categoria": "Concepto general"},
    {"texto": "Uno no sabe a veces cómo actuar.", "categoria": "Concepto general"},
    {"texto": "Otro decidió continuar con la tarea.", "categoria": "Concepto general"},
    {"texto": "No tengo ganas de ál.", "categoria": "Concepto general"},
    {"texto": "Nada en este mundo es eterno.", "categoria": "Concepto general"},
    {"texto": "¿Me puedes dar algo para leer?", "categoria": "Concepto general"},
    {"texto": "Nonada de lo dicho tenía valor.", "categoria": "Concepto general"},
    {"texto": "El uno piensa distinto al otro.", "categoria": "Concepto general"},
    {"texto": "El vivir con miedo no es vivir.", "categoria": "Construcción con artículo"},
    {"texto": "Los cantares antiguos aún emocionan.", "categoria": "Construcción con artículo"},
    {"texto": "Me pareció una nonada su reclamo.", "categoria": "Construcción con artículo"},
    {"texto": "Por una nada se enfadó.", "categoria": "Construcción con artículo"},
    {"texto": "El todo está compuesto de partes.", "categoria": "Construcción con artículo"},
    {"texto": "No vi más que una nonada de esfuerzo.", "categoria": "Construcción con artículo"},
    {"texto": "Disfruto mucho el leer por las noches.", "categoria": "Construcción con artículo"},
    {"texto": "El murmurar de las hojas me tranquiliza.", "categoria": "Construcción con artículo"},
    {"texto": "Escuchamos varios dares y tomares en la reunión.", "categoria": "Construcción con artículo"},
    {"texto": "El hablar bien abre muchas puertas.", "categoria": "Construcción con artículo"},
]

usuario_ejemplos = []

def mostrar_diapositiva():
    print("\n📘 DIAPOSITIVA CONCEPTUAL")
    print("""
Los sustantivos neutros en español no tienen género masculino ni femenino.
Se usan para conceptos generales, demostrativos, infinitivos sustantivados, cantidades u otras funciones abstractas.

CATEGORÍAS PRINCIPALES:
1. Demostrativos neutros
2. Infinitivos como sustantivos
3. Sustantivos de cantidad
4. Sustantivos de concepto general
5. Construcciones con artículo (el vivir, una nada, etc.)
    """)

def presentar_ejemplos():
    for ejemplo in ejemplos:
        print(f"\n➡️ Ejemplo: {ejemplo['texto']}")
        respuesta = input("¿Qué categoría crees que tiene?: ").strip()
        if respuesta.lower() == ejemplo['categoria'].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. Era: {ejemplo['categoria']}")
        oracion = input("Escribe una nueva oración con el sustantivo neutro: ").strip()
        if not oracion:
            print("⚠️ No escribiste ninguna oración.")
        else:
            print("📝 ¡Oración guardada!\n")

def cuestionario():
    seleccionados = random.sample(ejemplos, 5)
    puntaje = 0
    for ej in seleccionados:
        print(f"\n❓ Clasifica este ejemplo: {ej['texto']}")
        resp = input("Categoría: ").strip()
        if resp.lower() == ej['categoria'].lower():
            print("✅ Correcto.")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. Era: {ej['categoria']}")
    print(f"\n🎯 Tu puntaje: {puntaje}/5")

def agregar_ejemplo():
    if len(usuario_ejemplos) >= 100:
        print("🚫 Ya has alcanzado el límite de 100 ejemplos.")
        return
    texto = input("Escribe tu nuevo ejemplo: ").strip()
    categoria = input("¿Qué categoría tiene?: ").strip()
    usuario_ejemplos.append({"texto": texto, "categoria": categoria})
    print("✅ Ejemplo agregado.")

def ver_ejemplos_usuario():
    if not usuario_ejemplos:
        print("🔍 No has agregado ejemplos aún.")
    else:
        for i, ej in enumerate(usuario_ejemplos, 1):
            print(f"{i}. {ej['texto']} ({ej['categoria']})")

def guardar_ejemplos_usuario():
    with open("mis_ejemplos.json", "w", encoding="utf-8") as f:
        json.dump(usuario_ejemplos, f, ensure_ascii=False, indent=4)
    print("💾 Ejemplos guardados en 'mis_ejemplos.json'.")

def menu():
    while True:
        print("\n📚 MENÚ PRINCIPAL")
        print("1. Ver diapositiva conceptual")
        print("2. Practicar con los 50 ejemplos")
        print("3. Cuestionario clasificatorio")
        print("4. Agregar nuevo ejemplo")
        print("5. Ver ejemplos agregados")
        print("6. Guardar ejemplos en archivo")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_diapositiva()
        elif opcion == "2":
            presentar_ejemplos()
        elif opcion == "3":
            cuestionario()
        elif opcion == "4":
            agregar_ejemplo()
        elif opcion == "5":
            ver_ejemplos_usuario()
        elif opcion == "6":
            guardar_ejemplos_usuario()
        elif opcion == "7":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()
