Download
import random

# Base de datos de palabras y reglas (ampliable)
base_datos = [
    {
        "regla": "B vs. V (fonema /b/)",
        "ejemplo": "Palabra que significa 'utensilio para beber' (AFI: [ˈbaθo])",
        "AFI": "[ˈba.θo]",
        "respuesta": "vaso",
        "explicacion": "Se escribe con V por provenir del latín 'vasum'."
    },
    {
        "regla": "C, Z, S (seseo)",
        "ejemplo": "Fruto del roble (AFI: [ˈθenθa] en España / [ˈsensa] en América)",
        "AFI": "[ˈθen.θa] o [ˈsen.sa]",
        "respuesta": "bellota",
        "explicacion": "Error común: ❌ 'zellota'. Regla: Siempre B inicial."
    },
    {
        "regla": "G vs. J (sonido /x/)",
        "ejemplo": "Sinónimo de 'feliz' (AFI: [xoˈʝo.so])",
        "AFI": "[xoˈʝo.so]",
        "respuesta": "gozoso",
        "explicacion": "Se escribe con G ante O (regla del /g/ suave)."
    },
    # Añadir aquí los 100 ejemplos restantes...
]

def practica_ortografia():
    print("¡Bienvenido al Tutor de Ortografía Española con AFI!\n")
    puntaje = 0
    random.shuffle(base_datos)
    
    for i, item in enumerate(base_datos, 1):
        print(f"\n--- Pregunta {i} ---")
        print(f"Regla: {item['regla']}")
        print(f"Pista: {item['ejemplo']}")
        print(f"Transcripción AFI: {item['AFI']}")
        
        respuesta = input("\nEscribe la palabra correctamente: ").strip().casefold()
        
        if respuesta == item['respuesta'].casefold():
            print(f"✅ Correcto! {item['explicacion']}")
            puntaje +=1
        else:
            print(f"❌ Error. La respuesta era: {item['respuesta']}. {item['explicacion']}")
        
        print(f"Puntaje actual: {puntaje}/{i}\n")
    
    print(f"🏆 Puntaje final: {puntaje}/{len(base_datos)}")
    if puntaje == len(base_datos):
        print("¡Excelente dominio ortográfico!")
    elif puntaje >= len(base_datos)*0.7:
        print("¡Buen trabajo! Revisa tus errores.")
    else:
        print("¡Sigue practicando!")

# Ejecutar el programa
if __name__ == "__main__":
    practica_ortografia()
