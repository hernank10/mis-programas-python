import json
import re
import os
from collections import deque

# Configuración inicial
ARCHIVO_EJEMPLOS = "ejemplos_incisos.json"
MAX_EJEMPLOS = 100

# Lección teórica (Diapositivas)
DIAPOSITIVAS = [
    {
        "titulo": "¿Qué son los incisos explicativos?",
        "contenido": "Elementos sintácticos que añaden información adicional\n- Van entre comas, paréntesis o rayas\n- No son esenciales para el sentido principal\n- Ejemplo: 'Londres, capital del Reino Unido, tiene 9 millones de habitantes'"
    },
    {
        "titulo": "Reglas básicas",
        "contenido": "1. Coherencia: La oración debe mantener sentido sin el inciso\n2. Signos adecuados:\n   - Comas: información relacionada\n   - Paréntesis: datos técnicos\n   - Rayas: énfasis o interrupciones\n3. Máximo 2 incisos por oración"
    }
]

# Base de datos de ejercicios
EJERCICIOS = {
    "completar": deque(),
    "corregir": deque(),
    "creados": []
}

# Funciones principales
def cargar_ejemplos():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_ejemplos(ejemplos):
    with open(ARCHIVO_EJEMPLOS, 'w', encoding='utf-8') as f:
        json.dump(ejemplos, f, ensure_ascii=False, indent=2)

def mostrar_diapositivas():
    for idx, diapo in enumerate(DIAPOSITIVAS, 1):
        print(f"\n=== Diapositiva {idx}: {diapo['titulo']} ===")
        print(diapo['contenido'])
        input("\nPresiona Enter para continuar...")

def validar_inciso(oracion, inciso, puntuacion):
    patrones = {
        'comas': fr',\s*{re.escape(inciso)}\s*,',
        'paréntesis': fr'\(\s*{re.escape(inciso)}\s*\)',
        'rayas': fr'—\s*{re.escape(inciso)}\s*—'
    }
    
    if not re.search(patrones[puntuacion], oracion):
        return False
    
    oracion_limpia = re.sub(r'[(),—]|—.*?—', '', oracion)
    oracion_limpia = ' '.join(oracion_limpia.split())
    return oracion_limpia == re.sub(r'[(),—]', '', inciso) not in oracion_limpia

def practicar_completar():
    ejemplos = cargar_ejemplos()
    if not ejemplos:
        print("¡Primero crea algunos ejemplos!")
        return
    
    ejemplo = ejemplos.pop(0)
    ejemplos.append(ejemplo)
    
    print(f"\nComplete la oración:\n{ejemplo['base']}")
    print(f"Inciso a agregar: {ejemplo['inciso']} ({ejemplo['puntuacion'].capitalize()})")
    
    intentos = 3
    while intentos > 0:
        respuesta = input("Tu respuesta: ")
        if validar_inciso(respuesta, ejemplo['inciso'], ejemplo['puntuacion']):
            print("✅ ¡Correcto!")
            return
        print("❌ Intenta nuevamente")
        intentos -= 1
    
    print(f"\nSolución correcta:\n{ejemplo['base'].replace('{}', f'{ejemplo['inciso']}')}")

def corregir_oraciones():
    correcciones = [
        ("El presidente de Chile, Gabriel Boric electo en 2021, anunció reformas.", "comas"),
        ("La NASA—agencia espacial estadounidense— lanzó un nuevo cohete.", "rayas"),
        ("El café(colombiano) es considerado de los mejores del mundo.", "paréntesis")
    ]
    
    for idx, (oracion, puntuacion) in enumerate(correcciones, 1):
        print(f"\nOración {idx} a corregir:\n{oracion}")
        respuesta = input("Tu corrección: ")
        
        if any(s in respuesta for s in [',', '—', '(']):
            print("✅ Corrección aceptada")
        else:
            print("❌ Debes usar signos de puntuación adecuados")

def crear_ejemplo():
    ejemplos = cargar_ejemplos()
    
    if len(ejemplos) >= MAX_EJEMPLOS:
        print("Límite de ejemplos alcanzado")
        return
    
    base = input("Oración base (sin inciso): ")
    inciso = input("Inciso a agregar: ")
    puntuacion = input("Tipo de puntuación (comas/paréntesis/rayas): ")
    
    if puntuacion not in ['comas', 'paréntesis', 'rayas']:
        print("Tipo de puntuación inválido")
        return
    
    ejemplos.append({
        "base": base,
        "inciso": inciso,
        "puntuacion": puntuacion
    })
    
    guardar_ejemplos(ejemplos)
    print("✅ Ejemplo guardado exitosamente")

def menu_principal():
    while True:
        print("\n" + "="*50)
        print(" APRENDE INCISOS EXPLICATIVOS ".center(50, '★'))
        print("="*50)
        print("1. Ver lección teórica\n2. Practicar completar oraciones")
        print("3. Corregir oraciones\n4. Crear nuevos ejemplos")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == '1':
            mostrar_diapositivas()
        elif opcion == '2':
            practicar_completar()
        elif opcion == '3':
            corregir_oraciones()
        elif opcion == '4':
            crear_ejemplo()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

# Inicialización y ejecución
if __name__ == "__main__":
    # Cargar ejemplos iniciales si el archivo no existe
    if not os.path.exists(ARCHIVO_EJEMPLOS):
        ejemplos_iniciales = [
            {
                "base": "La Universidad de Buenos Aires ofrece cursos de posgrado.",
                "inciso": "UBA",
                "puntuacion": "paréntesis"
            },
            {
                "base": "El Río de la Plata separa Argentina de Uruguay.",
                "inciso": "el más ancho del mundo",
                "puntuacion": "comas"
            }
        ]
        guardar_ejemplos(ejemplos_iniciales)
    
    menu_principal()
