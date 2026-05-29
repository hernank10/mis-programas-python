import json

# Lista de ejercicios con ejemplos y respuestas modelo
EJERCICIOS = [
    {
        "titulo": "Forme los femeninos de una serie de sustantivos.",
        "ejemplo": "Ej: el león → la leona",
        "modelo": "el doctor → la doctora"
    },
    {
        "titulo": "Separe sujeto y predicado.",
        "ejemplo": "Ej: El niño juega en el parque → sujeto: El niño / predicado: juega en el parque",
        "modelo": "Mi hermana cocina galletas → sujeto: Mi hermana / predicado: cocina galletas"
    },
    {
        "titulo": "Escriba la familia de palabras del sustantivo 'flor'.",
        "ejemplo": "Ej: flor, florero, florista, florido",
        "modelo": "flor, floral, florecer, floreado"
    },
    {
        "titulo": "Determine cuántos fonemas y cuántas letras tienen las palabras de la serie.",
        "ejemplo": "Ej: casa → 4 letras, 4 fonemas",
        "modelo": "niño → 4 letras, 4 fonemas"
    },
    {
        "titulo": "Señale los complementos del sujeto.",
        "ejemplo": "Ej: El gato negro de mi vecina → núcleo: gato / complementos: negro, de mi vecina",
        "modelo": "La niña rubia con trenzas → núcleo: niña / complementos: rubia, con trenzas"
    },
    {
        "titulo": "Señale la función de los siguientes grupos.",
        "ejemplo": "Ej: en el jardín → complemento circunstancial de lugar",
        "modelo": "por la tarde → complemento circunstancial de tiempo"
    },
    {
        "titulo": "Forme el plural de los siguientes grupos sustantivos.",
        "ejemplo": "Ej: el árbol frondoso → los árboles frondosos",
        "modelo": "la casa blanca → las casas blancas"
    },
    {
        "titulo": "Extraiga los sustantivos abstractos.",
        "ejemplo": "Ej: La alegría, la bondad, la tristeza",
        "modelo": "La inteligencia, la amistad, la justicia"
    },
    {
        "titulo": "Enuncie la regla de los verbos terminados en '-bir'.",
        "ejemplo": "Ej: Se escriben con 'b' todos los verbos terminados en '-bir', excepto hervir, servir y vivir",
        "modelo": "Los verbos en '-bir' llevan 'b', salvo excepciones como hervir, servir y vivir"
    },
    {
        "titulo": "Señale los núcleos de los grupos subrayados.",
        "ejemplo": "Ej: El coche rojo → núcleo: coche",
        "modelo": "Los niños alegres → núcleo: niños"
    },
    {
        "titulo": "Extraiga del texto los adjetivos relacionales.",
        "ejemplo": "Ej: escolar, laboral, presidencial",
        "modelo": "infantil, cultural, profesional"
    },
    {
        "titulo": "De la siguiente lista de adjetivos y verbos derive sustantivos abstractos.",
        "ejemplo": "Ej: feliz → felicidad; crear → creación",
        "modelo": "generoso → generosidad; leer → lectura"
    }
]

RESPUESTAS_USUARIO = {}

# Guardar en archivo JSON
def guardar_respuestas():
    with open('respuestas_ejercicios.json', 'w', encoding='utf-8') as f:
        json.dump(RESPUESTAS_USUARIO, f, indent=4, ensure_ascii=False)

# Mostrar menú principal
def mostrar_menu():
    print("\n=== Ejercicios de lengua ===")
    for i, ejercicio in enumerate(EJERCICIOS):
        print(f"{i+1}. {ejercicio['titulo']}")
    print("0. Guardar y salir")

# Ejecutar programa
while True:
    mostrar_menu()
    opcion = input("Seleccione un número de ejercicio: ")
    
    if opcion == "0":
        guardar_respuestas()
        print("Respuestas guardadas. ¡Hasta luego!")
        break

    if opcion.isdigit() and 1 <= int(opcion) <= len(EJERCICIOS):
        idx = int(opcion) - 1
        ejercicio = EJERCICIOS[idx]
        print(f"\nEjercicio: {ejercicio['titulo']}")
        print(f"Ejemplo: {ejercicio['ejemplo']}")
        print(f"Respuesta modelo: {ejercicio['modelo']}")
        respuesta = input("Escriba una respuesta similar: ")
        RESPUESTAS_USUARIO[ejercicio['titulo']] = respuesta
        print("✔ Respuesta registrada.")
    else:
        print("Opción inválida. Intente nuevamente.")
