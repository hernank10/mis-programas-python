import json
import os

# Datos base
diapositivas = [
    ["**Enumeración Sintáctica**", 
     "Separación de elementos análogos con comas:\nEj: cursos de inglés, francés, ruso..."],
    
    ["**Relaciones Gramaticales**",
     "No separar:\n1. SUJETO-VERBO\n2. VERBO-OBJETO\n3. OBJETO-DESTINATARIO"],
    
    ["**Ejemplo Completo**",
     "Profesores: Jaramillo, Silva, Maldonado...\nGraduandos: J. Pérez, M. Castaño..."]
]

ejemplos = {
    "Correcto": "El Instituto ofrece cursos de inglés, francés y alemán.",
    "Incorrecto": "Los profesores Jaramillo Silva, y Botero asesorarán."
}

ejercicios_corregir = [
    ("Los estudiantes, presentaron trabajos ensayos y proyectos", 
     "Los estudiantes presentaron trabajos, ensayos y proyectos")
]

# Sistema de archivos
ARCHIVO_EJEMPLOS = "ejemplos_guardados.json"

def cargar_ejemplos():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, 'r') as f:
            return json.load(f)
    return []

def guardar_ejemplo(incorrecto, correcto):
    ejemplos = cargar_ejemplos()
    if len(ejemplos) >= 100:
        print("Límite de 100 ejemplos alcanzado")
        return
    ejemplos.append({"incorrecto": incorrecto, "correcto": correcto})
    with open(ARCHIVO_EJEMPLOS, 'w') as f:
        json.dump(ejemplos, f)

# Módulo interactivo
def mostrar_diapositivas():
    for i, slide in enumerate(diapositivas, 1):
        print(f"\n[Diapositiva {i}] {slide[0]}")
        print(slide[1])
        input("\nPresione Enter para continuar...")

def cuestionario():
    preguntas = [
        {
            "pregunta": "¿Dónde va la coma en: 'Estudiamos historia geografía matemáticas y literatura'?",
            "opciones": ["A) historia, geografía...", "B) geografía matemáticas..."],
            "correcta": "A"
        }
    ]
    
    puntaje = 0
    for p in preguntas:
        print(f"\n{p['pregunta']}")
        for op in p['opciones']:
            print(op)
        respuesta = input("Su respuesta (A/B): ").upper()
        if respuesta == p['correcta']:
            puntaje +=1
            print("✓ Correcto")
        else:
            print("✗ Incorrecto")
    
    print(f"\nPuntaje final: {puntaje}/{len(preguntas)}")

def practica_correccion():
    ejemplos = cargar_ejemplos() + ejercicios_corregir
    for ejemplo in ejemplos:
        print(f"\nCorrija: {ejemplo['incorrecto']}")
        input("Su versión: ")
        print(f"Solución: {ejemplo['correcto']}\n")
        input("Enter para continuar...")

# Menú principal
def main():
    while True:
        print("\n" + "="*50)
        print("1. Ver diapositivas teóricas")
        print("2. Definiciones y ejemplos básicos")
        print("3. Cuestionario interactivo")
        print("4. Ejercicios de corrección (50 oraciones)")
        print("5. Crear/editar ejemplos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_diapositivas()
        elif opcion == "2":
            for k, v in ejemplos.items():
                print(f"\n{k}: {v}")
        elif opcion == "3":
            cuestionario()
        elif opcion == "4":
            practica_correccion()
        elif opcion == "5":
            inc = input("Ingrese oración incorrecta: ")
            cor = input("Ingrese versión corregida: ")
            guardar_ejemplo(inc, cor)
            print("Ejemplo guardado!")
        elif opcion == "6":
            break

if __name__ == "__main__":
    main()
