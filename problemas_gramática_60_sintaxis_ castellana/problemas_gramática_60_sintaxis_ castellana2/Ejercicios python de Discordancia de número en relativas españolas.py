import json
import os
from collections import deque

# Configuración
EJERCICIOS_FILE = "ejercicios_usuario.json"
MAX_EJEMPLOS = 100
MAX_INTENTOS = 3

teoria = {
    "partitivas": {
        "definicion": (
            "Construcciones que expresan relación parte-todo usando 'de + grupo'. "
            "Ej: 'Ser de los que...', 'Uno de los que...'"
        ),
        "bilingue": (
            "Diferencias inglés-español:\n"
            "- En inglés el verbo siempre concuerda con el sustantivo principal\n"
            "- En español permite doble concordancia (sintaxis + semántica)\n"
            "Ej: EN: 'I was one of those who was there' vs ES: 'Fui de los que {estuvieron/estuvo}'"
        )
    }
}

ejercicios_bilingue = [
    {
        "en": "I was one of those who refused the proposal.",
        "es": "Fui de los que se { } a aceptar la propuesta.",
        "opciones": ["negaron", "negó"],
        "correcta": 0,
        "explicacion": "Concordancia plural: 'those who' (plural) → 'negaron'"
    },
    {
        "en": "She is part of the group that achieved the goals.",
        "es": "Es parte del grupo que { } las metas.",
        "opciones": ["alcanzaron", "alcanzó"],
        "correcta": 1,
        "explicacion": "Singular: concordancia con 'grupo' (colectivo)"
    }
]

def mostrar_menu_principal():
    print("\n" + "═"*50)
    print(" PARTITIVE CONSTRUCTIONS TRAINER ".center(50, "□"))
    print("═"*50)
    print("1. Teoría y diferencias EN/ES")
    print("2. Ejercicios de completación (ES)")
    print("3. Práctica bilingüe (EN→ES)")
    print("4. Ejercicios de redacción (Guardar ejemplos)")
    print("5. Mis ejemplos guardados")
    print("6. Repetir ejercicios fallados")
    print("7. Salir")
    return input("Seleccione (1-7): ")

def practicar_bilingue(puntuacion):
    print("\n" + " PRÁCTICA BILINGÜE ".center(50, "🌍"))
    print("Traduce las construcciones manteniendo la concordancia adecuada:")
    
    intentos_restantes = MAX_INTENTOS
    ejercicios_fallados = []
    
    for ej in ejercicios_bilingue:
        while intentos_restantes > 0:
            print("\n" + "-"*50)
            print(f"EN: {ej['en']}")
            print(f"ES: {ej['es']}")
            print(f"Opciones: 1) {ej['opciones'][0]} | 2) {ej['opciones'][1]}")
            
            try:
                resp = int(input("Tu elección (1/2): ")) - 1
                if resp not in [0,1]:
                    raise ValueError
            except:
                print("Error: ingresa 1 o 2")
                intentos_restantes -= 1
                continue
            
            if resp == ej["correcta"]:
                puntuacion += 15
                print(f"✅ Correcto! +15 puntos\nExplicación: {ej['explicacion']}")
                break
            else:
                intentos_restantes -= 1
                ejercicios_fallados.append(ej)
                print(f"❌ Incorrecto. Intentos restantes: {intentos_restantes}")
                print(f"Pista: {ej['explicacion']}")
    
    if ejercicios_fallados:
        print("\n=== Ejercicios para repasar ===")
        for ej in ejercicios_fallados:
            print(f"\nEN: {ej['en']}")
            print(f"ES correcta: {ej['es'].replace('{}', ej['opciones'][ej['correcta']])}")
    
    return puntuacion

def repetir_ejercicios(puntuacion):
    print("\n" + " REPETIR EJERCICIOS ".center(50, "🔄"))
    print("1. Completación\n2. Bilingües\n3. Ambos")
    opcion = input("Seleccione tipo a repetir: ")
    
    if opcion in ["1", "3"]:
        puntuacion = practicar_completacion(puntuacion)
    if opcion in ["2", "3"]:
        puntuacion = practicar_bilingue(puntuacion)
    
    return puntuacion

def cargar_ejemplos():
    if os.path.exists(EJERCICIOS_FILE):
        with open(EJERCICIOS_FILE, 'r', encoding='utf-8') as f:
            return deque(json.load(f), maxlen=MAX_EJEMPLOS)
    return deque(maxlen=MAX_INTENTOS)

# [...] (Funciones anteriores mantienen misma estructura con mejoras)

def main():
    puntuacion = 0
    ejemplos_usuario = cargar_ejemplos()
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == '1':
            mostrar_teoria()
        elif opcion == '2':
            puntuacion = practicar_completacion(puntuacion)
        elif opcion == '3':
            puntuacion = practicar_bilingue(puntuacion)
        elif opcion == '4':
            puntuacion = practicar_redaccion(puntuacion, ejemplos_usuario)
        elif opcion == '5':
            mostrar_ejemplos_guardados(ejemplos_usuario)
        elif opcion == '6':
            puntuacion = repetir_ejercicios(puntuacion)
        elif opcion == '7':
            break
        else:
            print("Opción inválida")
        
        input("\nPresione Enter para continuar...")
    
    # [...] (Mantener sistema de guardado y resumen final)

if __name__ == "__main__":
    main()
