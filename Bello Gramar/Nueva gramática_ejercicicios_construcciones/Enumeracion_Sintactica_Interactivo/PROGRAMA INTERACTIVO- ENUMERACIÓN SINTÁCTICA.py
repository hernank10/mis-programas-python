import os
import json

# Rutas base
BASE_DIR = "./Enumeracion_Sintactica_Interactivo"
DIA_POS = os.path.join(BASE_DIR, "diapositivas")
QUIZ_DIR = os.path.join(BASE_DIR, "cuestionarios")
EJERCICIOS = os.path.join(BASE_DIR, "ejercicios_completar")
EJEMPLOS = os.path.join(BASE_DIR, "ejemplos_usuario")

# Crear carpetas si no existen
for path in [DIA_POS, QUIZ_DIR, EJERCICIOS, EJEMPLOS]:
    os.makedirs(path, exist_ok=True)

# Ensayo como diapositivas interactivas
diapos = [
    "\n[Diapositiva 1]\n\n**Enumeración Sintáctica**\n\nEs el uso de comas para separar elementos análogos dentro de una oración.",
    "\n[Diapositiva 2]\n\n**Ejemplo**: El Instituto ofrece cursos de inglés, francés, ruso, portugués, italiano y alemán.",
    "\n[Diapositiva 3]\n\n**Regla fundamental**: No se debe separar con coma el sujeto, el verbo y el complemento directo o indirecto.",
    "\n[Diapositiva 4]\n\n**Ejemplo correcto**: Los profesores Jaramillo, Silva y Palencia asesorarán a los alumnos Pérez y Sarmiento.",
    "\n[Diapositiva 5]\n\n**Uso correcto**: Las comas solo separan elementos dentro del sujeto o del complemento, nunca entre quién, verbo y qué."
]

def mostrar_diapositivas():
    for diap in diapos:
        input(f"{diap}\n\nPresiona ENTER para continuar...")

# Cuestionario interactivo
def cargar_preguntas():
    return [
        {
            "pregunta": "¿Cuál es el propósito de la coma en una enumeración sintáctica?",
            "opciones": ["Separar sujeto y verbo", "Separar elementos análogos", "Terminar la oración", "Unir oraciones distintas"],
            "respuesta": 1
        },
        {
            "pregunta": "¿Qué no debe separarse con comas en una oración?",
            "opciones": ["Elementos del sujeto", "Verbo de complemento", "Listas de nombres", "Series de adjetivos"],
            "respuesta": 1
        }
    ]

def hacer_cuestionario():
    preguntas = cargar_preguntas()
    puntuacion = 0
    for i, p in enumerate(preguntas):
        print(f"\nPregunta {i+1}: {p['pregunta']}")
        for idx, opcion in enumerate(p['opciones']):
            print(f"  {idx}. {opcion}")
        try:
            resp = int(input("Tu respuesta: "))
            if resp == p['respuesta']:
                print("¡Correcto!")
                puntuacion += 1
            else:
                print("Incorrecto.")
        except ValueError:
            print("Respuesta inválida.")
    print(f"\nTu puntuación final: {puntuacion}/{len(preguntas)}")

# Oraciones mal enumeradas
oraciones_incorrectas = [
    "Los estudiantes, aprobaron matemáticas, ciencias y, literatura.",
    "Los doctores Pérez, Ramírez operaron, a Juan y a, Carlos.",
    "Los músicos, tocaron la guitarra, el violín y el piano, en el festival.",
    "Los pintores, italianos, franceses y, españoles expusieron su obra.",
    "María, Pedro y Sofía, cocinan, pasteles, galletas y flanes."
] * 10  # total 50 oraciones

def ejercicio_corregir():
    for i, oracion in enumerate(oraciones_incorrectas[:10]):
        print(f"\nOración {i+1}: {oracion}")
        correcion = input("Corrige la oración: ")
        guardar_ejemplo(correcion)

# Gestión de ejemplos nuevos
def guardar_ejemplo(oracion):
    archivo = os.path.join(EJEMPLOS, "ejemplos.json")
    ejemplos = []
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            ejemplos = json.load(f)
    if len(ejemplos) < 100:
        ejemplos.append(oracion)
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(ejemplos, f, indent=4, ensure_ascii=False)
        print("✅ Ejemplo guardado correctamente.")
    else:
        print("❌ Límite de 100 ejemplos alcanzado.")

def menu():
    while True:
        print("\n=== PROGRAMA INTERACTIVO: ENUMERACIÓN SINTÁCTICA ===")
        print("1. Ver diapositivas del ensayo")
        print("2. Realizar cuestionario interactivo")
        print("3. Corregir oraciones con errores de enumeración")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_diapositivas()
        elif opcion == '2':
            hacer_cuestionario()
        elif opcion == '3':
            ejercicio_corregir()
        elif opcion == '4':
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
