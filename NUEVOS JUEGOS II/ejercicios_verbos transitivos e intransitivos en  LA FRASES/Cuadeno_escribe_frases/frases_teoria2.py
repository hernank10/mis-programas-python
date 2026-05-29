import json
from datetime import datetime

# Configuración
ARCHIVO_DATOS = "frases_consola.json"
EMOJIS = {
    "simplifica": "✂️",
    "metaforas": "🌄",
    "contrastes": "⚖️",
    "verbos": "🏃",
    "experiencia": "🌍",
    "exit": "🚪",
    "error": "❌",
    "success": "✅"
}

CATEGORIAS = {
    "1": {
        "nombre": "Simplifica",
        "regla": "Elimina redundancias ➡️ Conserva la esencia",
        "ejemplo": f"{EMOJIS['simplifica']} 'Vivir la vida plenamente cada día' → 'Vivir con intensidad'"
    },
    "2": {
        "nombre": "Metáforas",
        "regla": "Abstracto + Concreto = 🎨",
        "ejemplo": f"{EMOJIS['metaforas']} 'La esperanza es un faro en la tormenta'"
    },
    "3": {
        "nombre": "Contrastes",
        "regla": "Luz 🌞 vs Oscuridad 🌚",
        "ejemplo": f"{EMOJIS['contrastes']} 'El silencio grita más fuerte'"
    },
    "4": {
        "nombre": "Verbos Activos",
        "regla": "Acción > Descripción 🏋️",
        "ejemplo": f"{EMOJIS['verbos']} 'Construye puentes, no muros'"
    },
    "5": {
        "nombre": "Experiencia Universal",
        "regla": "Todos lo hemos sentido ❤️",
        "ejemplo": f"{EMOJIS['experiencia']} 'El primer amor nunca se olvida'"
    }
}

def mostrar_menu():
    print(f"\n{EMOJIS['success']} FRASES FILOSÓFICAS {EMOJIS['success']}")
    print("1. 📝 Crear nueva frase")
    print("2. 📚 Ver frases guardadas")
    print(f"3. {EMOJIS['exit']} Salir")
    return input("👉 Elige una opción: ")

def mostrar_categorias():
    print(f"\n{EMOJIS['success']} CATEGORÍAS DISPONIBLES {EMOJIS['success']}")
    for key, value in CATEGORIAS.items():
        print(f"{key}. {value['nombre']}")
        print(f"   Regla: {value['regla']}")
        print(f"   Ejemplo: {value['ejemplo']}\n")

def cargar_frases():
    try:
        with open(ARCHIVO_DATOS, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {cat["nombre"]: [] for cat in CATEGORIAS.values()}

def guardar_frases(frases):
    with open(ARCHIVO_DATOS, "w") as f:
        json.dump(frases, f, indent=2)

def crear_frase(frases):
    mostrar_categorias()
    eleccion = input("\n🎯 Elige categoría (1-5): ")
    
    if eleccion not in CATEGORIAS:
        print(f"{EMOJIS['error']} Categoría inválida")
        return
    
    categoria = CATEGORIAS[eleccion]["nombre"]
    if len(frases[categoria]) >= 100:
        print(f"{EMOJIS['error']} ¡Categoría llena! (100/100)")
        return
    
    frase = input("\n💡 Escribe tu frase (máx. 12 palabras): ")
    palabras = frase.split()
    
    if len(palabras) > 12:
        print(f"{EMOJIS['error']} ¡Demasiadas palabras! ({len(palabras)}/12)")
        return
    
    if not palabras:
        print(f"{EMOJIS['error']} ¡La frase no puede estar vacía!")
        return
    
    frases[categoria].append({
        "texto": frase,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "emojis": "".join(EMOJIS.values())
    })
    
    guardar_frases(frases)
    print(f"\n{EMOJIS['success']} ¡Frase guardada! {CATEGORIAS[eleccion]['ejemplo']}")

def ver_frases(frases):
    print(f"\n{EMOJIS['success']} 📚 FRASES GUARDADAS {EMOJIS['success']}")
    for categoria, lista in frases.items():
        print(f"\n⭐ {categoria} ({len(lista)}/100)")
        for i, frase in enumerate(lista, 1):
            print(f"  {i}. [{frase['fecha']}] {frase['texto']}")

def main():
    print(f"\n{EMOJIS['success']} ¡Bienvenido al Taller de Frases! {EMOJIS['success']}")
    print("Crea frases memorables con estas reglas:")
    print("✨ Máximo 12 palabras\n🎯 Elige categoría\n💾 Se guardan automáticamente")
    
    frases = cargar_frases()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            crear_frase(frases)
        elif opcion == "2":
            ver_frases(frases)
        elif opcion == "3":
            print(f"\n{EMOJIS['success']} ¡Hasta luego! Recuerda: 'Las grandes ideas caben en frases pequeñas' 🌟")
            break
        else:
            print(f"{EMOJIS['error']} Opción inválida")

if __name__ == "__main__":
    main()
