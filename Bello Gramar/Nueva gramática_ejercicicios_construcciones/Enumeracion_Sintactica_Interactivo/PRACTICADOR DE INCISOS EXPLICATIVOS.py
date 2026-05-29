import re
import random

# Ejemplos organizados por categorías
EJEMPLOS = {
    "Comas explicativas (títulos/cargos)": [
        {
            "base": "El rector de la UIS tendrá a su cargo el discurso inaugural.",
            "inciso": "doctor Hernán Darío Díaz",
            "puntuacion": "comas"
        },
        # ... más ejemplos
    ],
    # ... otras categorías
}

def verificar_coherencia(oracion, incisos):
    limpio = re.sub(r'[(),—]|—.*?—', '', oracion).replace("  ", " ")
    return " ".join(limpio.split())

def practicar_categoria(categoria):
    ejemplos = EJEMPLOS[categoria]
    ejemplo = random.choice(ejemplos)
    
    print(f"\n--- {categoria} ---")
    print(f"Base: {ejemplo['base']}")
    print(f"Inciso a incluir: {ejemplo['inciso']}")
    
    while True:
        usuario = input("\nTu versión (o 'salir'): ").strip()
        if usuario.lower() == "salir":
            return
        
        # Verificar signos
        correcto = False
        if ejemplo['puntuacion'] == "comas":
            correcto = re.search(fr",\s*{re.escape(ejemplo['inciso'])}\s*,", usuario)
        elif ejemplo['puntuacion'] == "paréntesis":
            correcto = re.search(fr"\(\s*{re.escape(ejemplo['inciso'])}\s*\)", usuario)
        elif ejemplo['puntuacion'] == "rayas":
            correcto = re.search(fr"—\s*{re.escape(ejemplo['inciso'])}\s*—", usuario)
        
        # Verificar coherencia
        coherencia = verificar_coherencia(usuario, [ejemplo]['inciso'])

        # Validar máximo 2 incisos
        num_incisos = len(re.findall(r'[(),—]', usuario)) // 2
        
        # Retroalimentación
        print("\nAnálisis:")
        print(f"1. Uso de signos: {'✅' if correcto else '❌'}")
        print(f"2. Coherencia sin inciso: '{coherencia}'")
        print(f"3. Número de incisos: {num_incisos} {'✅' if num_incisos <= 2 else '❌ (máximo 2)'}")
        
        if correcto and coherencia == ejemplo['base'] and num_incisos <= 2:
            print("\n¡Perfecto! Cumple todas las reglas.")
            break
        else:
            print("\nIntenta nuevamente o escribe 'salir' para cambiar de categoría")

def menu_principal():
    while True:
        print("\n" + "="*50)
        print("PRACTICADOR DE INCISOS EXPLICATIVOS".center(50))
        print("="*50)
        
        categorias = list(EJEMPLOS.keys())
        for i, cat in enumerate(categorias, 1):
            print(f"{i}. {cat}")
        print("0. Salir")
        
        try:
            opcion = int(input("\nElige una categoría: "))
            if opcion == 0:
                break
            practicar_categoria(categorias[opcion-1])
        except (ValueError, IndexError):
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    # Inicializar datos de ejemplo
    EJEMPLOS = {
        # ... estructura completa de ejemplos
    }
    menu_principal()
