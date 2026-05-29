import json
import random
from gtts import gTTS
import os
from datetime import datetime

# --------------------------
# MÓDULO 1: Gestión de Base de Datos
# --------------------------
ARCHIVO_DATOS = "ortografia_db.json"

def cargar_base_datos():
    try:
        with open(ARCHIVO_DATOS, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_base_datos(datos):
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(datos, f, indent=2)

# --------------------------
# MÓDULO 2: Menú Interactivo y Gestión de Ejemplos
# --------------------------
CATEGORIAS = {
    'B/V': 'Palabras con b y v',
    'G/J': 'Uso de g y j',
    'C/Z/S': 'Reglas de c, z y s',
    'LL/Y': 'Diferencia entre ll e y',
    'QU/C/K': 'Uso de qu, c y k',
    'ACENTOS': 'Acentuación gráfica'
}

def mostrar_menu_principal():
    print("\n" + "═"*40)
    print(" TUTOR INTERACTIVO DE ORTOGRAFÍA ESPAÑOLA ")
    print("═"*40)
    print("1. 🎯 Practicar reglas ortográficas")
    print("2. 📝 Crear nuevo ejemplo")
    print("3. ✏️ Editar ejemplo existente")
    print("4. 👁️ Ver todos los ejemplos")
    print("5. 📊 Estadísticas de progreso")
    print("6. 🚪 Salir")
    return input("\nSelecciona una opción (1-6): ")

def crear_ejemplo():
    print("\n" + "─"*30 + " NUEVO EJEMPLO " + "─"*30)
    return {
        "palabra": input("Palabra correcta: ").strip(),
        "AFI": input("Transcripción AFI: ").strip(),
        "categoria": seleccionar_categoria(),
        "regla": input("Regla ortográfica: ").strip(),
        "significado": input("Significado/Observación: ").strip(),
        "intentos": 0,
        "aciertos": 0
    }

def editar_ejemplo(datos):
    mostrar_ejemplos(datos)
    try:
        idx = int(input("\nÍndice del ejemplo a editar: ")) - 1
        ejemplo = datos[idx]
        print("\nDejar en blanco para mantener el valor actual")
        for campo in ['palabra', 'AFI', 'regla', 'significado']:
            nuevo_valor = input(f"{campo.capitalize()} ({ejemplo[campo]}): ")
            if nuevo_valor: ejemplo[campo] = nuevo_valor
        ejemplo['categoria'] = seleccionar_categoria(ejemplo['categoria'])
        return True
    except (ValueError, IndexError):
        print("❌ Índice inválido")
        return False

def mostrar_ejemplos(datos):
    print("\n" + "─"*30 + " LISTA DE EJEMPLOS " + "─"*30)
    for i, item in enumerate(datos, 1):
        print(f"{i:3}. {item['palabra']:15} [{item['AFI']:10}] Cat: {item['categoria']}")

# --------------------------
# MÓDULO 3: Sistema de Práctica y Progreso
# --------------------------
def seleccionar_categoria(actual=None):
    print("\nCategorías disponibles:")
    for key, value in CATEGORIAS.items():
        prefijo = "➤ " if key == actual else "  "
        print(f"{prefijo}{key}: {value}")
    while True:
        cat = input("Ingresa categoría: ").upper()
        return cat if cat in CATEGORIAS else actual

def practicar_categoria(datos):
    categoria = seleccionar_categoria()
    ejemplos = [e for e in datos if e['categoria'] == categoria]
    random.shuffle(ejemplos)
    aciertos = 0
    
    for ejemplo in ejemplos:
        ejemplo['intentos'] += 1
        print(f"\n🔊 Pronunciación AFI: {ejemplo['AFI']}")
        respuesta = input("Escribe la palabra: ").strip()
        
        if respuesta.lower() == ejemplo['palabra'].lower():
            print(f"✅ Correcto! {ejemplo['significado']}")
            aciertos += 1
            ejemplo['aciertos'] += 1
        else:
            print(f"❌ Error: {ejemplo['palabra']} - {ejemplo['regla']}")
    
    print(f"\nResultado: {aciertos}/{len(ejemplos)} correctos")
    guardar_base_datos(datos)

# --------------------------
# MÓDULO 4: Estadísticas y Reportes
# --------------------------
def mostrar_estadisticas(datos):
    stats = {
        'total_ejemplos': len(datos),
        'categorias': {},
        'tasa_acierto': 0
    }
    
    for cat in CATEGORIAS:
        ejemplos_cat = [e for e in datos if e['categoria'] == cat]
        stats['categorias'][cat] = {
            'total': len(ejemplos_cat),
            'aciertos': sum(e['aciertos'] for e in ejemplos_cat),
            'intentos': sum(e['intentos'] for e in ejemplos_cat)
        }
    
    print("\n" + "═"*40 + " ESTADÍSTICAS " + "═"*40)
    print(f"Ejemplos en base de datos: {stats['total_ejemplos']}")
    for cat, valores in stats['categorias'].items():
        if valores['intentos'] > 0:
            porcentaje = (valores['aciertos'] / valores['intentos']) * 100
            print(f"\n{CATEGORIAS[cat]}:")
            print(f"  ↳ Aciertos: {valores['aciertos']}/{valores['intentos']} ({porcentaje:.1f}%)")

# --------------------------
# EJECUCIÓN PRINCIPAL
# --------------------------
def main():
    datos = cargar_base_datos()
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == '1':  # Practicar
            practicar_categoria(datos)
        elif opcion == '2':  # Crear
            datos.append(crear_ejemplo())
            guardar_base_datos(datos)
        elif opcion == '3':  # Editar
            if editar_ejemplo(datos):
                guardar_base_datos(datos)
        elif opcion == '4':  # Ver
            mostrar_ejemplos(datos)
        elif opcion == '5':  # Estadísticas
            mostrar_estadisticas(datos)
        elif opcion == '6':  # Salir
            print("\n¡Hasta pronto! ✨")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    main()
