import random
import os
import time

# Datos ampliados con 20 ejercicios para cada juego
oraciones_sujeto_predicado = [
    {"oracion": "El niño juega en el parque", "sujeto": "El niño", "predicado": "juega en el parque"},
    {"oracion": "María estudia matemáticas", "sujeto": "María", "predicado": "estudia matemáticas"},
    {"oracion": "Los pájaros cantan hermosamente", "sujeto": "Los pájaros", "predicado": "cantan hermosamente"},
    {"oracion": "Mi hermano cocina muy bien", "sujeto": "Mi hermano", "predicado": "cocina muy bien"},
    {"oracion": "La profesora explica la lección", "sujeto": "La profesora", "predicado": "explica la lección"},
    {"oracion": "El sol brilla intensamente", "sujeto": "El sol", "predicado": "brilla intensamente"},
    {"oracion": "Los estudiantes leen libros interesantes", "sujeto": "Los estudiantes", "predicado": "leen libros interesantes"},
    {"oracion": "Mi madre trabaja en un hospital", "sujeto": "Mi madre", "predicado": "trabaja en un hospital"},
    {"oracion": "El perro corre en el jardín", "sujeto": "El perro", "predicado": "corre en el jardín"},
    {"oracion": "Las flores crecen en primavera", "sujeto": "Las flores", "predicado": "crecen en primavera"},
    {"oracion": "El presidente dará un discurso importante", "sujeto": "El presidente", "predicado": "dará un discurso importante"},
    {"oracion": "Los niños cantan canciones alegres", "sujeto": "Los niños", "predicado": "cantan canciones alegres"},
    {"oracion": "El equipo ganó el campeonato", "sujeto": "El equipo", "predicado": "ganó el campeonato"},
    {"oracion": "La lluvia cae suavemente", "sujeto": "La lluvia", "predicado": "cae suavemente"},
    {"oracion": "Mi abuela cocina delicioso", "sujeto": "Mi abuela", "predicado": "cocina delicioso"},
    {"oracion": "Los turistas visitan el museo", "sujeto": "Los turistas", "predicado": "visitan el museo"},
    {"oracion": "El médico atiende a los pacientes", "sujeto": "El médico", "predicado": "atiende a los pacientes"},
    {"oracion": "Las estrellas brillan en la noche", "sujeto": "Las estrellas", "predicado": "brillan en la noche"},
    {"oracion": "El coche necesita reparaciones", "sujeto": "El coche", "predicado": "necesita reparaciones"},
    {"oracion": "Los árboles dan sombra en verano", "sujeto": "Los árboles", "predicado": "dan sombra en verano"}
]

oraciones_desordenadas = [
    {"desordenada": ["casa", "la", "blanca", "es"], "correcta": "La casa es blanca"},
    {"desordenada": ["perro", "el", "corre", "rápidamente"], "correcta": "El perro corre rápidamente"},
    {"desordenada": ["estudian", "los", "alumnos", "mucho"], "correcta": "Los alumnos estudian mucho"},
    {"desordenada": ["sol", "el", "brilla", "intensamente"], "correcta": "El sol brilla intensamente"},
    {"desordenada": ["libro", "un", "leo", "yo", "interesante"], "correcta": "Yo leo un libro interesante"},
    {"desordenada": ["canta", "hermana", "mi", "bien", "muy"], "correcta": "Mi hermana canta muy bien"},
    {"desordenada": ["parque", "en", "juegan", "niños", "los"], "correcta": "Los niños juegan en el parque"},
    {"desordenada": ["trabaja", "padre", "mi", "oficina", "en", "una"], "correcta": "Mi padre trabaja en una oficina"},
    {"desordenada": ["gato", "el", "leche", "toma", "la"], "correcta": "El gato toma la leche"},
    {"desordenada": ["escuela", "a", "van", "niñas", "las"], "correcta": "Las niñas van a la escuela"},
    {"desordenada": ["cocina", "madre", "mi", "cena", "la"], "correcta": "Mi madre cocina la cena"},
    {"desordenada": ["estación", "llegó", "tren", "el", "a", "la"], "correcta": "El tren llegó a la estación"},
    {"desordenada": ["flores", "las", "jardín", "en", "crecen", "el"], "correcta": "Las flores crecen en el jardín"},
    {"desordenada": ["película", "vimos", "una", "anoche", "interesante"], "correcta": "Anoche vimos una película interesante"},
    {"desordenada": ["mesa", "sobre", "libro", "está", "el", "la"], "correcta": "El libro está sobre la mesa"},
    {"desordenada": ["cielo", "el", "azul", "está", "muy"], "correcta": "El cielo está muy azul"},
    {"desordenada": ["cantando", "pájaros", "los", "amanecer", "al", "están"], "correcta": "Los pájaros están cantando al amanecer"},
    {"desordenada": ["estudiando", "universidad", "en", "ella", "está", "la"], "correcta": "Ella está estudiando en la universidad"},
    {"desordenada": ["mañana", "trabajar", "voy", "a", "temprano"], "correcta": "Mañana voy a trabajar temprano"},
    {"desordenada": ["playa", "en", "verano", "vamos", "la", "al"], "correcta": "En verano vamos a la playa"}
]

# Añado un tercer juego: Clasifica la Oración
tipos_oraciones = [
    {"oracion": "El niño juega y la niña estudia", "tipo": "Compuesta coordinada"},
    {"oracion": "Cuando llegué a casa, cené rápido", "tipo": "Compuesta subordinada"},
    {"oracion": "Hace sol; hace calor", "tipo": "Yuxtapuesta"},
    {"oracion": "María lee un libro", "tipo": "Simple"},
    {"oracion": "Estudié mucho, por eso aprobé", "tipo": "Compuesta coordinada"},
    {"oracion": "El libro que me prestaste es interesante", "tipo": "Compuesta subordinada"},
    {"oracion": "Llueve; no podemos salir", "tipo": "Yuxtapuesta"},
    {"oracion": "El sol calienta la tierra", "tipo": "Simple"},
    {"oracion": "Compré pan y también leche", "tipo": "Compuesta coordinada"},
    {"oracion": "Si estudias, aprobarás el examen", "tipo": "Compuesta subordinada"},
    {"oracion": "Es tarde; me voy a casa", "tipo": "Yuxtapuesta"},
    {"oracion": "Los niños corren en el parque", "tipo": "Simple"},
    {"oracion": "Trabajo duro pero gano poco", "tipo": "Compuesta coordinada"},
    {"oracion": "El hombre que vi ayer es mi jefe", "tipo": "Compuesta subordinada"},
    {"oracion": "Hace frío; ponte el abrigo", "tipo": "Yuxtapuesta"},
    {"oracion": "La música suena alegre", "tipo": "Simple"},
    {"oracion": "Voy al cine o me quedo en casa", "tipo": "Compuesta coordinada"},
    {"oracion": "Aunque llovió, fuimos de paseo", "tipo": "Compuesta subordinada"},
    {"oracion": "Es temprano; podemos caminar", "tipo": "Yuxtapuesta"},
    {"oracion": "El río fluye lentamente", "tipo": "Simple"}
]

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=" * 60)
    print("           JUEGOS GRAMATICALES - ESPAÑOL/INGLÉS")
    print("=" * 60)
    print("1. 🎯 Cazador de Sujeto y Predicado (20 ejercicios)")
    print("2. 🧩 Puzzle de la Oración (20 ejercicios)")
    print("3. 📊 Clasifica la Oración (20 ejercicios)")
    print("4. 📈 Ver Estadísticas")
    print("5. ❌ Salir")
    print("-" * 60)

def juego_sujeto_predicado():
    limpiar_consola()
    print("🎯 CAZADOR DE SUJETO Y PREDICADO")
    print("=" * 50)
    print("Identifica el sujeto y predicado en las oraciones")
    print("-" * 50)
    
    puntaje = 0
    total_preguntas = 5  # Reducido para no hacerlo muy largo
    oraciones_mezcladas = random.sample(oraciones_sujeto_predicado, total_preguntas)
    
    for i, item in enumerate(oraciones_mezcladas, 1):
        print(f"\n📝 Oración {i}: {item['oracion']}")
        print("-" * 40)
        
        # Solicitar sujeto
        sujeto_usuario = input("¿Cuál es el sujeto? ").strip()
        if sujeto_usuario.lower() == item['sujeto'].lower():
            print("✅ ¡Correcto! Sujeto identificado correctamente")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. El sujeto era: '{item['sujeto']}'")
        
        # Solicitar predicado
        predicado_usuario = input("¿Cuál es el predicado? ").strip()
        if predicado_usuario.lower() == item['predicado'].lower():
            print("✅ ¡Correcto! Predicado identificado correctamente")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. El predicado era: '{item['predicado']}'")
    
    print(f"\n🎉 Puntuación final: {puntaje}/{total_preguntas*2}")
    input("\nPresiona Enter para continuar...")
    return puntaje, total_preguntas*2

def juego_puzzle_oracion():
    limpiar_consola()
    print("🧩 PUZZLE DE LA ORACIÓN")
    print("=" * 50)
    print("Ordena las palabras para formar una oración correcta")
    print("-" * 50)
    
    puntaje = 0
    total_preguntas = 5
    oraciones_mezcladas = random.sample(oraciones_desordenadas, total_preguntas)
    
    for i, item in enumerate(oraciones_mezcladas, 1):
        palabras_mezcladas = item['desordenada'].copy()
        random.shuffle(palabras_mezcladas)
        
        print(f"\n🔤 Palabras desordenadas {i}:")
        print("📦 " + " | ".join(palabras_mezcladas))
        print("-" * 30)
        
        respuesta_usuario = input("Escribe la oración ordenada: ").strip()
        
        if respuesta_usuario.lower() == item['correcta'].lower():
            print("🎉 ¡Correcto! Oración bien formada ✅")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La oración correcta es: '{item['correcta']}'")
    
    print(f"\n🏆 Puntuación final: {puntaje}/{total_preguntas}")
    input("\nPresiona Enter para continuar...")
    return puntaje, total_preguntas

def juego_clasifica_oracion():
    limpiar_consola()
    print("📊 CLASIFICA LA ORACIÓN")
    print("=" * 50)
    print("Clasifica cada oración en: Simple, Compuesta coordinada,")
    print("Compuesta subordinada o Yuxtapuesta")
    print("-" * 50)
    print("Opciones: 1-Simple, 2-Compuesta coordinada,")
    print("3-Compuesta subordinada, 4-Yuxtapuesta")
    print("-" * 50)
    
    puntaje = 0
    total_preguntas = 5
    oraciones_mezcladas = random.sample(tipos_oraciones, total_preguntas)
    
    for i, item in enumerate(oraciones_mezcladas, 1):
        print(f"\n📝 Oración {i}: {item['oracion']}")
        print("-" * 40)
        
        try:
            opcion = int(input("Tu respuesta (1-4): ").strip())
            tipos = {
                1: "Simple",
                2: "Compuesta coordinada", 
                3: "Compuesta subordinada",
                4: "Yuxtapuesta"
            }
            
            if opcion in tipos and tipos[opcion] == item['tipo']:
                print(f"✅ ¡Correcto! Es una oración {item['tipo']}")
                puntaje += 1
            else:
                print(f"❌ Incorrecto. Es una oración {item['tipo']}")
                
        except ValueError:
            print("❌ Por favor ingresa un número del 1 al 4")
    
    print(f"\n🏅 Puntuación final: {puntaje}/{total_preguntas}")
    input("\nPresiona Enter para continuar...")
    return puntaje, total_preguntas

def mostrar_estadisticas(estadisticas):
    limpiar_consola()
    print("📈 ESTADÍSTICAS DE JUEGO")
    print("=" * 50)
    
    if not estadisticas:
        print("Aún no hay estadísticas. ¡Juega algunos juegos!")
    else:
        total_puntos = 0
        total_maximo = 0
        
        for juego, (puntos, maximo) in estadisticas.items():
            porcentaje = (puntos / maximo) * 100 if maximo > 0 else 0
            print(f"\n{juego}:")
            print(f"  Puntos: {puntos}/{maximo}")
            print(f"  Porcentaje: {porcentaje:.1f}%")
            total_puntos += puntos
            total_maximo += maximo
        
        if total_maximo > 0:
            promedio = (total_puntos / total_maximo) * 100
            print(f"\n📊 Total general: {total_puntos}/{total_maximo}")
            print(f"📈 Promedio general: {promedio:.1f}%")
    
    input("\nPresiona Enter para continuar...")

def main():
    estadisticas = {}
    
    while True:
        limpiar_consola()
        mostrar_menu()
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
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
            mostrar_estadisticas(estadisticas)
        elif opcion == "5":
            print("\n¡Gracias por jugar! Hasta pronto 👋")
            break
        else:
            print("❌ Opción inválida. Por favor selecciona 1-5")
            time.sleep(1)

if __name__ == "__main__":
    main()
