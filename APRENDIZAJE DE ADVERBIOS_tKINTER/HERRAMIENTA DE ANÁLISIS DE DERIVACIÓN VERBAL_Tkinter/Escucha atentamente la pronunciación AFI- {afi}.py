import random
import json
from gtts import gTTS
import os

# --------------------------
# MÓDULO 1: Base de Datos Ampliada (100 ejemplos)
# --------------------------
base_datos = [
    # Categoría: B/V
    {"categoria": "B vs V", "regla": "B inicial en palabras germánicas",
     "ejemplo": "Animal bovino (AFI: [ˈbaka])", "AFI": "[ˈba.ka]",
     "respuesta": "vaca", "explicacion": "Viene del latín 'vacca' (siempre V)"},
    
    {"categoria": "B vs V", "regla": "V después de N",
     "ejemplo": "Estación del año (AFI: [imˈbjeɾno])", "AFI": "[imˈbjeɾ.no]",
     "respuesta": "invierno", "explicacion": "Tras N se usa V: enviar, invitar"},
    
    # Categoría: C/Z/S
    {"categoria": "C/Z/S", "regla": "Seseo americano",
     "ejemplo": "Capital de Perú (AFI: [ˈli.ma])", "AFI": "[ˈli.ma]",
     "respuesta": "Lima", "explicacion": "En todas las variantes se escribe con M"},
    
    # Añadir aquí los 100 ejemplos restantes...
    # (Mantener misma estructura con categorías)
]

# --------------------------
# MÓDULO 2: Sistema de Progreso (JSON)
# --------------------------
def guardar_progreso(usuario, puntaje, categoria):
    try:
        with open('progreso.json', 'r+') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    if usuario not in data:
        data[usuario] = []
    
    data[usuario].append({
        "fecha": str(datetime.now()),
        "categoria": categoria,
        "puntaje": puntaje
    })
    
    with open('progreso.json', 'w') as f:
        json.dump(data, f, indent=4)

def ver_progreso(usuario):
    try:
        with open('progreso.json') as f:
            data = json.load(f)
            return data.get(usuario, [])
    except FileNotFoundError:
        return []

# --------------------------
# MÓDULO 3: Sistema de Audio (gTTS)
# --------------------------
def reproducir_audio(texto, idioma='es'):
    tts = gTTS(text=texto, lang=idioma)
    tts.save('temp.mp3')
    os.system('start temp.mp3' if os.name == 'nt' else 'afplay temp.mp3')

# --------------------------
# MÓDULO 4: Núcleo Interactivo
# --------------------------
def menu_categorias():
    categorias = list(set(item['categoria'] for item in base_datos))
    print("\nCategorías Disponibles:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            eleccion = int(input("\nElige una categoría (número): ")) - 1
            return categorias[eleccion]
        except (ValueError, IndexError):
            print("Error: Ingresa un número válido")

def modo_dictado(palabra, afi):
    print(f"\n🔊 Escucha atentamente la pronunciación AFI: {afi}")
    reproducir_audio(palabra)
    return input("Escribe lo que escuchaste: ").strip().lower()

def practica_ortografia():
    usuario = input("Ingresa tu nombre de usuario: ").strip()
    categoria = menu_categorias()
    preguntas = [q for q in base_datos if q['categoria'] == categoria]
    random.shuffle(preguntas)
    puntaje = 0
    
    for i, item in enumerate(preguntas, 1):
        print(f"\n--- Pregunta {i} ---")
        print(f"Regla: {item['regla']}")
        
        # Modo Dictado
        respuesta = modo_dictado(item['respuesta'], item['AFI'])
        
        # Verificación
        if respuesta == item['respuesta'].lower():
            print(f"✅ Correcto! {item['explicacion']}")
            puntaje += 1
        else:
            print(f"❌ Error. Correcto: {item['respuesta']}. {item['explicacion']}")
        
        print(f"Puntaje: {puntaje}/{i}")
    
    guardar_progreso(usuario, puntaje, categoria)
    print(f"\n🏆 Resultados guardados. Historial:")
    for intento in ver_progreso(usuario):
        print(f"- {intento['fecha']}: {intento['categoria']} - {intento['puntaje']}/10")

# --------------------------
# EJECUCIÓN
# --------------------------
if __name__ == "__main__":
    practica_ortografia()
