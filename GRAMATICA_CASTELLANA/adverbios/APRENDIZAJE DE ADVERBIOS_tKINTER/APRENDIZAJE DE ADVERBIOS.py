import json
import os
import random
from time import sleep

# Datos iniciales
categorias = {
    "lugar": ["cerca", "arriba", "dentro", "debajo", "mar afuera"],
    "tiempo": ["antes", "nunca", "pasado mañana", "aún", "siempre"],
    "modo": ["dulcemente", "mal", "quedo", "apenas", "alto y claro"],
    "cantidad": ["mucho", "demasiado", "casi", "harto", "nada"],
    "afirmacion": ["sí", "jamás", "ciertamente", "tampoco", "no"],
    "duda": ["quizá", "tal vez", "acaso"],
    "demostrativos": ["aquí", "allí", "ahora", "así", "tanto"],
    "relativos": ["donde", "cuando", "como", "cuanto", "mientras"],
    "interrogativos": ["dónde", "cuándo", "cómo", "cuánto", "qué"],
    "especiales": ["recién", "deprisa", "paso", "detrás", "cerquita"]
}

ejemplos = [
    {"categoria": "lugar", "ejemplo": "El parque está cerca de mi casa"},
    # ... (todos los 50 ejemplos aquí)
]

# Sistema de archivos
ARCHIVO_EJEMPLOS = "ejemplos_usuario.json"

def cargar_ejemplos_usuario():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, "r") as f:
            return json.load(f)
    return []

def guardar_ejemplo_usuario(ejemplo):
    ejemplos = cargar_ejemplos_usuario()
    if len(ejemplos) < 100:
        ejemplos.append(ejemplo)
        with open(ARCHIVO_EJEMPLOS, "w") as f:
            json.dump(ejemplos, f)
        return True
    return False

def mostrar_diapositiva_conceptual():
    print("\n" + "="*50)
    print(" ADVERBIOS - CLASIFICACIÓN CONCEPTUAL")
    print("="*50)
    print("1. Lugar: Indican ubicación espacial")
    print("2. Tiempo: Señalan momento temporal")
    print("3. Modo: Describen forma de acción")
    print("4. Cantidad: Expresan grado o medida")
    print("5. Afirmación/Negación: Confirmación o negación")
    print("6. Demostrativos: Señalan referentes contextuales")
    print("7. Relativos: Conectan proposiciones")
    print("8. Interrogativos: Formulan preguntas")
    print("9. Especiales: Casos únicos o compuestos")
    print("\nEj: 'Cerca' es adverbio de lugar")
    print("="*50 + "\n")

def practica_individual():
    for idx, item in enumerate(ejemplos, 1):
        print(f"\nEjemplo {idx}/50")
        print(f"Adverbio: {item['ejemplo'].split()[-2]}")
        print(f"Oración: {item['ejemplo']}")
        
        usuario_cat = input("¿Qué categoría es? (Escribe el nombre) > ").lower()
        if usuario_cat == item['categoria']:
            print("¡Correcto! ✅")
        else:
            print(f"❌ Incorrecto. Es de categoría: {item['categoria']}")
        
        user_oracion = input("Escribe tu propia oración con este adverbio > ")
        # Aquí podrías añadir validación gramatical básica
        
        sleep(1)

def cuestionario_interactivo():
    score = 0
    todas_categorias = list(categorias.keys())
    preguntas = ejemplos + cargar_ejemplos_usuario()
    random.shuffle(preguntas)
    
    for i, item in enumerate(preguntas[:10], 1):
        print(f"\nPregunta {i}/10")
        print(f"Oración: {item['ejemplo']}")
        print("Opciones:", ", ".join(todas_categorias[:5]))
        
        respuesta = input("Categoría > ").lower()
        if respuesta == item['categoria']:
            print("¡Correcto! +10 puntos 🎉")
            score += 10
        else:
            print(f"Error. Correcto: {item['categoria']} 💡")
    
    print(f"\nPuntuación final: {score}/100")
    if score >= 70:
        print("¡Excelente dominio! 🌟")
    else:
        print("Sigue practicando 💪")

def gestionar_ejemplos():
    while True:
        print("\n1. Crear nuevo ejemplo")
        print("2. Ver mis ejemplos")
        print("3. Volver al menú")
        opcion = input("> ")
        
        if opcion == "1":
            print("\nCategorías disponibles:", list(categorias.keys()))
            nueva_cat = input("Categoría > ").lower()
            nuevo_ej = input("Oración completa > ")
            
            if guardar_ejemplo_usuario({"categoria": nueva_cat, "ejemplo": nuevo_ej}):
                print("¡Ejemplo guardado exitosamente! 📚")
            else:
                print("❌ Límite alcanzado (100 ejemplos)")
        
        elif opcion == "2":
            mis_ejs = cargar_ejemplos_usuario()
            print(f"\nTienes {len(mis_ejs)} ejemplos guardados:")
            for e in mis_ejs:
                print(f"- [{e['categoria']}] {e['ejemplo']}")
        
        elif opcion == "3":
            break

def menu_principal():
    while True:
        print("\n" + "="*30)
        print(" APRENDIZAJE DE ADVERBIOS")
        print("="*30)
        print("1. Mostrar diapositiva conceptual")
        print("2. Iniciar práctica guiada")
        print("3. Cuestionario interactivo")
        print("4. Gestionar mis ejemplos")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción > ")
        
        if opcion == "1":
            mostrar_diapositiva_conceptual()
        elif opcion == "2":
            practica_individual()
        elif opcion == "3":
            cuestionario_interactivo()
        elif opcion == "4":
            gestionar_ejemplos()
        elif opcion == "5":
            print("¡Hasta pronto! 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
