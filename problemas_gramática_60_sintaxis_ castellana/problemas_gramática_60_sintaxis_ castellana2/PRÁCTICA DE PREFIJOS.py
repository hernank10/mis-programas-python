import random
from os import system
import sys

# Configuración de emojis
EMOJIS = {
    "titulo": "📚✨ PRÁCTICA DE PREFIJOS ✍️🔍",
    "puntos": "🏆",
    "nivel": "🚀",
    "correcto": "✅",
    "error": "❌",
    "pista": "💡",
    "advertencia": "⚠️"
}

# Lista de 50 palabras para practicar
PALABRAS = [
    {"palabra": "polisílabo", "base": "sílaba", "categoria": "adjetivo"},
    {"palabra": "multicolor", "base": "color", "categoria": "adjetivo"},
    # ... (añadir las 48 restantes)
]

def limpiar_consola():
    system('cls' if sys.platform == 'win32' else 'clear')

def mostrar_cabecera(puntaje, nivel):
    print(f"\n{EMOJIS['titulo']}")
    print(f"{EMOJIS['puntos']} Puntos: {puntaje} | {EMOJIS['nivel']} Nivel: {nivel}\n")

def ocultar_letras(palabra, porcentaje):
    letras = list(palabra)
    indices = random.sample(range(len(letras)), max(1, int(len(letras) * porcentaje / 100)))
    return "".join(["_" if i in indices else c for i, c in enumerate(letras)])

def mostrar_pista(palabra_actual):
    print(f"\n{EMOJIS['pista']} Pista:")
    print(f"- Prefijo: {palabra_actual['palabra'][:3].upper()}")
    print(f"- Base: {palabra_actual['base']} (sustantivo)")
    print(f"- Categoría: {palabra_actual['categoria'].capitalize()}")
    print(f"- Longitud: {len(palabra_actual['palabra'])} letras")

def juego_prefijos():
    porcentaje_ocultar = 30
    puntaje = 0
    racha = 0
    historial = []
    
    while True:
        limpiar_consola()
        mostrar_cabecera(puntaje, porcentaje_ocultar // 10)
        
        palabra = random.choice(PALABRAS)
        palabra_oculta = ocultar_letras(palabra["palabra"], porcentaje_ocultar)
        intentos = 0
        
        while intentos < 2:
            print(f"\n🔠 Palabra: {palabra_oculta}")
            respuesta = input("✍️  Tu respuesta (o 'salir' para terminar): ").strip()
            
            if respuesta.lower() == "salir":
                print(f"\n{EMOJIS['pista']} ¡Hasta luego! Puntuación final: {puntaje}")
                return
            
            if respuesta.lower() == palabra["palabra"].lower():
                puntaje += 10
                racha += 1
                print(f"\n{EMOJIS['correcto']} ¡Correcto! +10 puntos")
                historial.append(f"{EMOJIS['correcto']} {palabra['palabra']}")
                
                if racha % 3 == 0 and porcentaje_ocultar < 70:
                    porcentaje_ocultar += 10
                    print(f"{EMOJIS['nivel']} ¡Nuevo nivel! Letras ocultas: {porcentaje_ocultar}%")
                break
            else:
                intentos += 1
                racha = 0
                print(f"\n{EMOJIS['error']} Intento {intentos}/2")
                
                if intentos == 1:
                    print(f"{EMOJIS['pista']} Prefijo: {palabra['palabra'][:3].upper()}")
                else:
                    mostrar_pista(palabra)
                    historial.append(f"{EMOJIS['error']} {respuesta}")
                    print(f"\n{EMOJIS['advertencia']} La respuesta era: {palabra['palabra']}")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    try:
        juego_prefijos()
    except KeyboardInterrupt:
        print(f"\n\n{EMOJIS['advertencia']} Juego interrumpido. ¡Hasta pronto!")
