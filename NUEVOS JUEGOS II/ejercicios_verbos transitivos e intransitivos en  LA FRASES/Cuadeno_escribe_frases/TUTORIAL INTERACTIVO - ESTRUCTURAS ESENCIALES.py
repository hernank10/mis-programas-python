import random
import time

# Base de datos inicial con 50 ejemplos completos
ejemplos = [
    # Solo VERBO (10)
    {"sentence": "¡Ganaron! 🎉", "quien": "", "verbo": "ganaron", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "pasado", "complejidad": 1},
    {"sentence": "¡Llueve! ☔", "quien": "", "verbo": "llueve", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "presente", "complejidad": 1},
    # ... (completar con 8 ejemplos más)

    # QUIÉN + VERBO (10)
    {"sentence": "El equipo de fútbol ⚽ ganó.", "quien": "El equipo de fútbol", "verbo": "ganó", "que": "", "a_quien": "", "contexto": "cotidiano", "tiempo": "pasado", "complejidad": 2},
    {"sentence": "La profesora 📚 explicó.", "quien": "La profesora", "verbo": "explicó", "que": "", "a_quien": "", "contexto": "académico", "tiempo": "pasado", "complejidad": 2},
    # ... (completar con 8 ejemplos más)

    # VERBO + QUÉ (10)
    {"sentence": "Publicaron 📢 los resultados del examen.", "quien": "", "verbo": "publicaron", "que": "los resultados del examen", "a_quien": "", "contexto": "académico", "tiempo": "pasado", "complejidad": 3},
    # ... (completar con 9 ejemplos más)

    # Completo (20)
    {"sentence": "El Ministerio de Salud 🏥 lanzó una campaña para adultos mayores 👵👴.", "quien": "El Ministerio de Salud", "verbo": "lanzó", "que": "una campaña", "a_quien": "adultos mayores", "contexto": "social", "tiempo": "pasado", "complejidad": 4},
    # ... (completar con 19 ejemplos más)
]

def mostrar_tutorial():
    print("\n" + "="*55)
    print("🌟 TUTORIAL INTERACTIVO - ESTRUCTURAS ESENCIALES 🌟")
    print("="*55)
    print("\n🔑 Componentes clave de una frase:")
    time.sleep(1)
    print("\n1. 👤 QUIÉN: Sujeto que realiza la acción")
    print("   Ej: 'El profesor' | 'La empresa' | 'Los niños'")
    time.sleep(1)
    print("\n2. 🎬 VERBO: Acción principal (tiempo clave)")
    print("   Ej: 'explicó' (pasado) | 'organizarán' (futuro)")
    time.sleep(1)
    print("\n3. 📦 QUÉ: Objeto/contenido de la acción")
    print("   Ej: 'los resultados' | 'un nuevo proyecto'")
    time.sleep(1)
    print("\n4. 🎯 A QUIÉN: Destinatario o beneficiario")
    print("   Ej: 'para estudiantes' | 'a las autoridades'")
    time.sleep(1)
    print("\n📚 Ejemplo completo:")
    print("   👤 QUIÉN: 'La biblioteca'")
    print("   🎬 VERBO: 'organizará'")
    print("   📦 QUÉ: 'un taller de escritura'")
    print("   🎯 A QUIÉN: 'para jóvenes autores'")
    print("\n» Frase resultante: 'La biblioteca organizará un taller de escritura para jóvenes autores. ✍️'")
    time.sleep(2)
    input("\nPresiona Enter para continuar al menú... 🚀")

def mostrar_menu():
    print("\n" + "="*55)
    print("📘 ENTRENADOR DE ESTRUCTURAS EN ESPAÑOL 2.0")
    print("="*55)
    print("1. Ver tutorial 📖")
    print("2. Practicar identificación 🧩")
    print("3. Modo memorización 🧠")
    print("4. Crear ejemplos ✏️ (Guardados: {}/100)".format(len(ejemplos)))
    print("5. Ver mis ejemplos 📚")
    print("6. Salir 🚪")
    return input("\n👉 Seleccione una opción: ")

def animar_carga(mensaje):
    print(f"\n{mensaje}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print("🔄", end="", flush=True)
    time.sleep(0.5)
    print(" ✅")

def modo_memorizacion():
    animar_carga("Cargando modo memorización")
    ejemplo = random.choice(ejemplos)
    print("\n" + "🎯 RECONSTRUYE LA FRASE 🎯")
    print(f"\nComponentes clave:")
    print(f"👤 QUIÉN: {ejemplo['quien'] or '[Por determinar]'}")
    print(f"🎬 VERBO: {ejemplo['verbo'].upper()} ({ejemplo['tiempo'].capitalize()})")
    print(f"📦 QUÉ: {ejemplo['que'] or '[Por determinar]'}")
    print(f"🎯 A QUIÉN: {ejemplo['a_quien'] or '[Por determinar]'}")
    
    intento = input("\n✍️ Tu versión (incluye emoticonos opcionales): ").strip()
    
    print("\n" + "="*30)
    print("🔍 Comparación de frases:")
    print(f"Tu versión:    {intento}")
    print(f"Versión original: {ejemplo['sentence']}")
    
    if intento.lower() == ejemplo['sentence'].lower().replace("🎯", "").replace("👤", "").strip():
        print("\n🎉 ¡Perfecto! Estructura dominada ✅")
    else:
        print("\n💡 ¡Buen intento! Revisa las diferencias 🔄")

def crear_ejemplo():
    animar_carga("Preparando creador")
    print("\n" + "✨ CREADOR DE EJEMPLOS ✨")
    print("\nInstrucciones:")
    print("1. Usa emoticonos relevantes (opcional)")
    print("2. Sigue el orden: 👤 → 🎬 → 📦 → 🎯")
    
    contexto = input("\n🌍 Contexto (académico/laboral/cotidiano/creativo/social): ").lower()
    tiempo = input("⏳ Tiempo verbal (pasado/presente/futuro): ").lower()
    
    quien = input("\n👤 QUIÉN realiza la acción? (ej: El chef 🧑🍳): ").strip()
    verbo = input("🎬 VERBO principal (en el tiempo indicado): ").strip()
    que = input("📦 QUÉ objeto/contenido? (ej: una receta especial 📜): ").strip()
    a_quien = input("🎯 A QUIÉN está dirigido? (ej: para cocineros novatos 👨🍳): ").strip()
    
    # Construcción automática con emojis
    partes = []
    if quien: partes.append(f"{quien} ")
    if verbo: partes.append(f"{verbo} ")
    if que: partes.append(f"{que} ")
    if a_quien: partes.append(f"para {a_quien} ")
    
    # Añadir emojis aleatorios según contexto
    emojis = {
        "académico": ["📚", "✏️", "🎓", "📝"],
        "laboral": ["💼", "👔", "🏢", "📈"],
        "cotidiano": ["🏠", "🛒", "🚶", "☕"],
        "creativo": ["🎨", "🎭", "🖌️", "🎼"],
        "social": ["🌍", "🤝", "🗣️", "👥"]
    }
    emoji = random.choice(emojis.get(contexto, ["✨"]))
    
    frase = " ".join(partes).strip().capitalize()
    frase += f" {emoji}"
    
    ejemplos.append({
        "sentence": frase,
        "quien": quien.split(' ')[0],  # Remueve emojis del análisis
        "verbo": verbo,
        "que": que.split(' ')[0],
        "a_quien": a_quien,
        "contexto": contexto,
        "tiempo": tiempo,
        "complejidad": sum([1 for x in [quien, que, a_quien] if x])
    })
    
    print(f"\n💾 ¡Ejemplo guardado! Número {len(ejemplos)}:")
    print(f"📌 Frase: {frase}")

def main():
    mostrar_tutorial()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "6":
            print("\n🚀 ¡Hasta pronto! Sigue practicando tus estructuras.")
            break
            
        elif opcion == "1":
            mostrar_tutorial()
            
        elif opcion == "2":
            # Lógica de práctica existente (mejorada con emojis)
            
        elif opcion == "3":
            modo_memorizacion()
            
        elif opcion == "4":
            crear_ejemplo()
            
        elif opcion == "5":
            ver_ejemplos()
            
        else:
            print("\n⚠️ Opción no válida. Intenta nuevamente.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
