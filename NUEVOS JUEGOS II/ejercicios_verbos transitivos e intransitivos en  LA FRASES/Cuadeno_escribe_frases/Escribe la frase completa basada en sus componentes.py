import random

# Base de datos inicial con 50 ejemplos
ejemplos = [
    # Solo VERBO (10 ejemplos)
    {"sentence": "¡Ganaron!", "quien": "", "verbo": "ganaron", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "pasado", "complejidad": 1},
    {"sentence": "¡Llueve!", "quien": "", "verbo": "llueve", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "presente", "complejidad": 1},
    {"sentence": "¡Corran!", "quien": "", "verbo": "corran", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "presente", "complejidad": 1},
    {"sentence": "¡Estudien!", "quien": "", "verbo": "estudien", "que": "", "a_quien": "", "contexto": "académico", "tiempo": "presente", "complejidad": 1},
    {"sentence": "¡Escuchen!", "quien": "", "verbo": "escuchen", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "presente", "complejidad": 1},
    {"sentence": "¡Firmó!", "quien": "", "verbo": "firmó", "que": "", "a_quien": "", "contexto": "laboral", "tiempo": "pasado", "complejidad": 1},
    {"sentence": "¡Llegó!", "quien": "", "verbo": "llegó", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "pasado", "complejidad": 1},
    {"sentence": "¡Aprobó!", "quien": "", "verbo": "aprobó", "que": "", "a_quien": "", "contexto": "académico", "tiempo": "pasado", "complejidad": 1},
    {"sentence": "¡Vendió!", "quien": "", "verbo": "vendió", "que": "", "a_quien": "", "contexto": "laboral", "tiempo": "pasado", "complejidad": 1},
    {"sentence": "¡Terminaron!", "quien": "", "verbo": "terminaron", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "pasado", "complejidad": 1},

    # QUIÉN + VERBO (10 ejemplos)
    {"sentence": "El equipo de fútbol ganó.", "quien": "El equipo de fútbol", "verbo": "ganó", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "pasado", "complejidad": 2},
    {"sentence": "La profesora de literatura explicó.", "quien": "La profesora de literatura", "verbo": "explicó", "que": "", "a_quien": "", "contexto": "académico", "tiempo": "pasado", "complejidad": 2},
    # ... (agregar 8 ejemplos más de esta categoría)

    # VERBO + QUÉ (10 ejemplos)
    {"sentence": "Publicaron los resultados del examen.", "quien": "", "verbo": "publicaron", "que": "los resultados del examen", "a_quien": "", "contexto": "académico", "tiempo": "pasado", "complejidad": 3},
    {"sentence": "Cancelaron el concierto de rock.", "quien": "", "verbo": "cancelaron", "que": "el concierto de rock", "a_quien": "", "contexto": "cotidiano", "tiempo": "pasado", "complejidad": 3},
    # ... (agregar 8 ejemplos más de esta categoría)

    # Completo QUIÉN+VERBO+QUÉ+A QUIÉN (20 ejemplos)
    {"sentence": "El Ministerio de Salud lanzó una campaña para adultos mayores.", "quien": "El Ministerio de Salud", "verbo": "lanzó", "que": "una campaña", "a_quien": "adultos mayores", "contexto": "social", "tiempo": "pasado", "complejidad": 4},
    {"sentence": "La universidad organizó un seminario sobre IA para ingenieros.", "quien": "La universidad", "verbo": "organizó", "que": "un seminario sobre IA", "a_quien": "ingenieros", "contexto": "académico", "tiempo": "pasado", "complejidad": 4},
    # ... (agregar 18 ejemplos más de esta categoría)
]

def mostrar_menu():
    print("\n" + "="*50)
    print("ENTRENADOR AVANZADO DE ESTRUCTURAS EN ESPAÑOL")
    print("="*50)
    print("1. Practicar identificación de componentes")
    print("2. Modo memorización (reescritura)")
    print("3. Crear y guardar ejemplos (hasta 100)")
    print("4. Ver todos los ejemplos guardados")
    print("5. Salir")
    return input("Seleccione una opción: ")

def modo_memorizacion():
    print("\nMODO MEMORIZACIÓN")
    print("Escribe la frase completa basada en sus componentes:\n")
    
    ejemplo = random.choice(ejemplos)
    print("Componentes:")
    print(f"- QUIÉN: {ejemplo['quien']}" if ejemplo['quien'] else "- QUIÉN: [Por determinar]")
    print(f"- VERBO: {ejemplo['verbo']}")
    print(f"- QUÉ: {ejemplo['que']}" if ejemplo['que'] else "- QUÉ: [Por determinar]")
    print(f"- A QUIÉN: {ejemplo['a_quien']}" if ejemplo['a_quien'] else "- A QUIÉN: [Por determinar]")
    
    intento = input("\nTu versión de la frase completa: ").strip()
    
    if intento.lower() == ejemplo['sentence'].lower():
        print("\n¡Correcto! Frase original:")
    else:
        print("\nTu versión necesita ajustes. Frase original:")
    
    print(f"» {ejemplo['sentence']}")

def crear_ejemplo():
    if len(ejemplos) >= 100:
        print("¡Base de datos llena! Máximo 100 ejemplos.")
        return
    
    print("\nCREAR NUEVO EJEMPLO:")
    contexto = input("Contexto (académico/laboral/cotidiano/creativo/social): ").lower()
    tiempo = input("Tiempo verbal (pasado/presente/futuro): ").lower()
    
    quien = input("¿QUIÉN? (dejar vacío si no aplica): ").strip()
    verbo = input("¿VERBO? (en el tiempo indicado): ").strip()
    que = input("¿QUÉ? (dejar vacío si no aplica): ").strip()
    a_quien = input("¿A QUIÉN? (dejar vacío si no aplica): ").strip()
    
    # Construir la frase automáticamente
    partes = []
    if quien: partes.append(quien)
    partes.append(verbo.capitalize() if not quien else verbo)
    if que: partes.append(que + ("." if not a_quien else ""))
    if a_quien: partes.append(f"para {a_quien}." if que else f"para {a_quien}.")
    
    nueva_frase = " ".join(partes).replace(" .", ".").replace("para.", "para")
    
    ejemplos.append({
        "sentence": nueva_frase,
        "quien": quien,
        "verbo": verbo,
        "que": que,
        "a_quien": a_quien,
        "contexto": contexto,
        "tiempo": tiempo,
        "complejidad": 1 + sum([1 for x in [quien, que, a_quien] if x])
    })
    
    print(f"\n¡Nuevo ejemplo guardado! (#{len(ejemplos)})\n» {nueva_frase}")

def ver_ejemplos():
    print(f"\nEJEMPLOS ALMACENADOS ({len(ejemplos)}/100)")
    for idx, ej in enumerate(ejemplos, 1):
        print(f"{idx}. {ej['sentence']}")
    input("\nPresiona Enter para continuar...")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "5":
            print("\n¡Hasta pronto! Recuerda practicar con tus ejemplos creados.")
            break
            
        elif opcion == "1":
            # Lógica original de práctica (omitiendo por brevedad)
            pass
            
        elif opcion == "2":
            modo_memorizacion()
            
        elif opcion == "3":
            crear_ejemplo()
            
        elif opcion == "4":
            ver_ejemplos()
            
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
