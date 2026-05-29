import random
import os
import time
import re

# Datos ampliados con 20 ejercicios para cada juego
oraciones_sujeto_predicado = [
    {"oracion": "El niño juega en el parque", "sujeto": "El niño", "predicado": "juega en el parque"},
    {"oracion": "María estudia matemáticas", "sujeto": "María", "predicado": "estudia matemáticas"},
    # ... (los mismos 20 ejercicios anteriores)
]

oraciones_desordenadas = [
    {"desordenada": ["casa", "la", "blanca", "es"], "correcta": "La casa es blanca"},
    # ... (los mismos 20 ejercicios anteriores)
]

tipos_oraciones = [
    {"oracion": "El niño juega y la niña estudia", "tipo": "Compuesta coordinada"},
    # ... (los mismos 20 ejercicios anteriores)
]

# Nuevo: Oraciones con errores para el corrector
oraciones_con_errores = [
    {
        "oracion_erronea": "Voy al cine porque tengo ganas de ver una pelicula y que sea de accion",
        "opciones": [
            "Voy al cine porque tengo ganas de ver una película de acción",
            "Voy al cine y tengo ganas de ver una película porque sea de acción",
            "Voy al cine que tengo ganas de ver una película de acción"
        ],
        "correcta": 0,
        "explicacion": "Eliminar 'y que sea' que sobra y une incorrectamente las ideas"
    },
    {
        "oracion_erronea": "El libro que me prestaste es muy interesante y lo leí en dos días",
        "opciones": [
            "El libro que me prestaste es muy interesante y lo leí en dos días",
            "El libro que me prestaste es muy interesante, lo leí en dos días",
            "El libro me prestaste es muy interesante y lo leí en dos días"
        ],
        "correcta": 1,
        "explicacion": "Usar coma en lugar de 'y' para mejor fluidez"
    },
    {
        "oracion_erronea": "Si estudias mucho entonces aprobarás el examen",
        "opciones": [
            "Si estudias mucho, aprobarás el examen",
            "Si estudias mucho entonces que aprobarás el examen",
            "Estudias mucho entonces aprobarás el examen"
        ],
        "correcta": 0,
        "explicacion": "Eliminar 'entonces' que es redundante con 'si'"
    },
    {
        "oracion_erronea": "Aunque llovía pero fuimos al parque igual",
        "opciones": [
            "Aunque llovía, fuimos al parque igual",
            "Aunque llovía pero fuimos al parque",
            "Llovía pero fuimos al parque igual"
        ],
        "correcta": 0,
        "explicacion": "Eliminar 'pero' que contradice a 'aunque'"
    },
    {
        "oracion_erronea": "Me gusta leer libros cuando tengo tiempo libre y también me gusta ver películas",
        "opciones": [
            "Me gusta leer libros cuando tengo tiempo libre y ver películas",
            "Me gusta leer libros y ver películas cuando tengo tiempo libre",
            "Cuando tengo tiempo libre me gusta leer libros y también ver películas"
        ],
        "correcta": 1,
        "explicacion": "Unificar las actividades bajo el mismo contexto temporal"
    },
    {
        "oracion_erronea": "El estudiante que estudió mucho él aprobó el examen",
        "opciones": [
            "El estudiante que estudió mucho aprobó el examen",
            "El estudiante estudió mucho y él aprobó el examen",
            "El estudiante que estudió mucho, él aprobó el examen"
        ],
        "correcta": 0,
        "explicacion": "Eliminar 'él' que es redundante con 'el estudiante'"
    },
    {
        "oracion_erronea": "Voy a la tienda para comprar pan y también para comprar leche",
        "opciones": [
            "Voy a la tienda para comprar pan y leche",
            "Voy a la tienda para comprar pan y para comprar leche",
            "Voy a la tienda y compro pan y también leche"
        ],
        "correcta": 0,
        "explicacion": "Simplificar la enumeración eliminando repeticiones"
    },
    {
        "oracion_erronea": "Cuando llegué a casa que cené rápido",
        "opciones": [
            "Cuando llegué a casa, cené rápido",
            "Llegué a casa que cené rápido",
            "Cuando llegué a casa y que cené rápido"
        ],
        "correcta": 0,
        "explicacion": "Eliminar 'que' incorrecto y usar coma"
    },
    {
        "oracion_erronea": "Los niños juegan en el parque y las niñas también juegan",
        "opciones": [
            "Los niños y las niñas juegan en el parque",
            "Los niños juegan en el parque y las niñas también",
            "Los niños juegan en el parque, y las niñas juegan también"
        ],
        "correcta": 0,
        "explicacion": "Evitar repetición del verbo uniendo los sujetos"
    },
    {
        "oracion_erronea": "Si tú quieres podemos ir al cine o si prefieres podemos quedarnos en casa",
        "opciones": [
            "Si quieres, podemos ir al cine o quedarnos en casa",
            "Si tú quieres ir al cine o si prefieres quedarnos en casa",
            "Podemos ir al cine si quieres o podemos quedarnos en casa si prefieres"
        ],
        "correcta": 0,
        "explicacion": "Simplificar la estructura condicional"
    }
]

# Bloques para construir oraciones
bloques_linguisticos = {
    "sustantivos": [
        "niño", "niña", "profesor", "estudiante", "libro", "casa", "perro", "gato",
        "ciudad", "parque", "amigo", "familia", "trabajo", "escuela", "comida"
    ],
    "verbos": [
        "juega", "estudia", "lee", "escribe", "corre", "camina", "habla", "escucha",
        "come", "bebe", "trabaja", "aprende", "enseña", "visita", "construye"
    ],
    "adjetivos": [
        "grande", "pequeño", "interesante", "divertido", "importante", "hermoso",
        "rápido", "lento", "feliz", "triste", "nuevo", "viejo", "bueno", "malo"
    ],
    "conectores": [
        "y", "pero", "porque", "cuando", "si", "aunque", "mientras", "después",
        "antes", "donde", "que", "como", "para", "o", "ni"
    ],
    "articulos": ["el", "la", "los", "las", "un", "una", "unos", "unas"],
    "adverbios": ["mucho", "poco", "bien", "mal", "siempre", "nunca", "aquí", "allí"]
}

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=" * 60)
    print("           JUEGOS GRAMATICALES - ESPAÑOL/INGLÉS")
    print("=" * 60)
    print("1. 🎯 Cazador de Sujeto y Predicado")
    print("2. 🧩 Puzzle de la Oración")
    print("3. 📊 Clasifica la Oración")
    print("4. ✏️  Corrector de Oraciones")
    print("5. 🧱 Construye tu Propia Oración")
    print("6. 📈 Ver Estadísticas")
    print("7. ❌ Salir")
    print("-" * 60)

def juego_corrector_oraciones():
    limpiar_consola()
    print("✏️  CORRECTOR DE ORACIONES")
    print("=" * 50)
    print("Corrige los errores de estructura en las oraciones")
    print("Tienes 30 segundos por oración - ¡Más puntos por velocidad!")
    print("-" * 50)
    
    puntaje = 0
    total_preguntas = min(5, len(oraciones_con_errores))
    ejercicios_mezclados = random.sample(oraciones_con_errores, total_preguntas)
    puntos_velocidad = 0
    
    for i, ejercicio in enumerate(ejercicios_mezclados, 1):
        print(f"\n📝 Oración {i} con error:")
        print(f"\"{ejercicio['oracion_erronea']}\"")
        print("\nOpciones de corrección:")
        
        for j, opcion in enumerate(ejercicio['opciones']):
            print(f"{j + 1}. {opcion}")
        
        inicio_tiempo = time.time()
        
        try:
            respuesta = int(input("\nSelecciona la opción correcta (1-3): ")) - 1
            tiempo_usado = time.time() - inicio_tiempo
            
            if 0 <= respuesta < len(ejercicio['opciones']):
                if respuesta == ejercicio['correcta']:
                    # Puntos por corrección (5 puntos base)
                    puntos_correccion = 5
                    
                    # Puntos por velocidad (hasta 5 puntos adicionales)
                    if tiempo_usado < 10:
                        puntos_velocidad = 5
                    elif tiempo_usado < 20:
                        puntos_velocidad = 3
                    elif tiempo_usado < 30:
                        puntos_velocidad = 1
                    
                    puntaje_total_pregunta = puntos_correccion + puntos_velocidad
                    puntaje += puntaje_total_pregunta
                    
                    print(f"✅ ¡Correcto! +{puntos_correccion} puntos por corrección")
                    print(f"⏱️  +{puntos_velocidad} puntos por velocidad ({tiempo_usado:.1f}s)")
                    print(f"💡 Explicación: {ejercicio['explicacion']}")
                else:
                    print(f"❌ Incorrecto. La opción correcta era la {ejercicio['correcta'] + 1}")
                    print(f"💡 Explicación: {ejercicio['explicacion']}")
            else:
                print("❌ Opción inválida")
                
        except ValueError:
            print("❌ Por favor ingresa un número")
        
        print("-" * 50)
    
    print(f"\n🎉 Puntuación final: {puntaje}/{total_preguntas * 10}")
    input("\nPresiona Enter para continuar...")
    return puntaje, total_preguntas * 10

def analizar_oracion(oracion):
    """Analiza básicamente una oración y da feedback"""
    oracion = oracion.strip().lower()
    
    # Verificaciones básicas
    problemas = []
    sugerencias = []
    
    # 1. Verificar que tenga verbo
    verbos_encontrados = []
    for verbo in bloques_linguisticos["verbos"]:
        if verbo in oracion:
            verbos_encontrados.append(verbo)
    
    if not verbos_encontrados:
        problemas.append("No se detectó un verbo principal")
        sugerencias.append("Añade un verbo como 'juega', 'estudia', 'lee', etc.")
    else:
        sugerencias.append(f"Verbos detectados: {', '.join(verbos_encontrados)}")
    
    # 2. Verificar que tenga sustantivo
    sustantivos_encontrados = []
    for sustantivo in bloques_linguisticos["sustantivos"]:
        if sustantivo in oracion:
            sustantivos_encontrados.append(sustantivo)
    
    if not sustantivos_encontrados:
        problemas.append("No se detectaron sustantivos")
        sugerencias.append("Añade un sustantivo como 'niño', 'libro', 'casa', etc.")
    else:
        sugerencias.append(f"Sustantivos detectados: {', '.join(sustantivos_encontrados)}")
    
    # 3. Verificar estructura básica (sujeto + verbo)
    palabras = oracion.split()
    if len(palabras) < 3:
        problemas.append("La oración parece muy corta")
        sugerencias.append("Intenta añadir más elementos como adjetivos o complementos")
    
    # 4. Verificar conectores usados
    conectores_usados = []
    for conector in bloques_linguisticos["conectores"]:
        if conector in palabras:
            conectores_usados.append(conector)
    
    if conectores_usados:
        sugerencias.append(f"Conectores usados: {', '.join(conectores_usados)}")
    
    # Calcular puntaje básico
    puntaje = 10
    if problemas:
        puntaje -= len(problemas) * 2
    
    return problemas, sugerencias, max(0, puntaje)

def juego_construye_oracion():
    limpiar_consola()
    print("🧱 CONSTRUYE TU PROPIA ORACIÓN")
    print("=" * 50)
    print("Usa los bloques lingüísticos para construir oraciones")
    print("La 'IA' analizará tu creación y dará feedback")
    print("-" * 50)
    
    # Mostrar bloques disponibles
    print("\n📦 BLOQUES DISPONIBLES:")
    for categoria, bloques in bloques_linguisticos.items():
        print(f"{categoria.upper()}: {', '.join(bloques[:5])}...")
    
    puntaje_total = 0
    intentos = 3
    
    for intento in range(1, intentos + 1):
        print(f"\n{'='*40}")
        print(f"🎯 INTENTO {intento} de {intentos}")
        print('='*40)
        
        oracion_usuario = input("\nConstruye tu oración: ").strip()
        
        if not oracion_usuario:
            print("❌ No ingresaste ninguna oración")
            continue
        
        print("\n🔍 Analizando tu oración...")
        time.sleep(1)
        
        problemas, sugerencias, puntaje = analizar_oracion(oracion_usuario)
        
        print(f"\n📊 RESULTADO DEL ANÁLISIS:")
        print(f"Puntuación: {puntaje}/10")
        
        if problemas:
            print("\n⚠️  PROBLEMAS DETECTADOS:")
            for problema in problemas:
                print(f"   • {problema}")
        else:
            print("✅ ¡Estructura básica correcta!")
        
        print("\n💡 SUGERENCIAS:")
        for sugerencia in sugerencias:
            print(f"   • {sugerencia}")
        
        # Feedback adicional basado en complejidad
        palabras = oracion_usuario.split()
        if len(palabras) >= 6:
            print("   • ¡Buena longitud de oración!")
        if any(conector in oracion_usuario.lower() for conector in ['y', 'pero', 'porque', 'cuando']):
            print("   • ¡Uso apropiado de conectores!")
        
        puntaje_total += puntaje
        
        if intento < intentos:
            print(f"\n💭 Puedes intentar mejorar tu oración...")
    
    promedio = puntaje_total / intentos
    print(f"\n🎉 PUNTAJE FINAL: {promedio:.1f}/10")
    
    # Feedback final
    if promedio >= 8:
        print("🏅 ¡Excelente constructor de oraciones!")
    elif promedio >= 6:
        print("👍 ¡Buen trabajo! Sigue practicando")
    else:
        print("💪 ¡Sigue intentándolo! La práctica hace al maestro")
    
    input("\nPresiona Enter para continuar...")
    return puntaje_total, intentos * 10

# ... (las funciones anteriores de juego_sujeto_predicado, juego_puzzle_oracion, 
# juego_clasifica_oracion y mostrar_estadisticas se mantienen igual)

def main():
    estadisticas = {}
    
    while True:
        limpiar_consola()
        mostrar_menu()
        
        opcion = input("Selecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            puntos, maximo = juego_sujeto_predicado()
            estadisticas["🎯 Cazador de Sujeto"] = (puntos, maximo)
        elif opcion == "2":
            puntos, maximo = juego_puzzle_oracion()
            estadisticas["🧩 Puzzle de Oración"] = (puntos, maximo)
        elif opcion == "3":
            puntos, maximo = juego_clasifica_oracion()
            estadisticas["📊 Clasifica Oración"] = (puntos, maximo)
        elif opcion == "4":
            puntos, maximo = juego_corrector_oraciones()
            estadisticas["✏️  Corrector Oraciones"] = (puntos, maximo)
        elif opcion == "5":
            puntos, maximo = juego_construye_oracion()
            estadisticas["🧱 Construye Oración"] = (puntos, maximo)
        elif opcion == "6":
            mostrar_estadisticas(estadisticas)
        elif opcion == "7":
            print("\n¡Gracias por jugar! Hasta pronto 👋")
            break
        else:
            print("❌ Opción inválida. Por favor selecciona 1-7")
            time.sleep(1)

if __name__ == "__main__":
    main()
