import random
import os
import time

# Datos para el juego Tower Defense Gramatical
enemigos_oraciones_incorrectas = [
    {
        "oracion": "Ellos cantan bonito",
        "error": "verbo",
        "correccion": "Ellos cantan bien",
        "explicacion": "'bonito' es adjetivo, debe usarse el adverbio 'bien' con verbos"
    },
    {
        "oracion": "La niña y el niño juega",
        "error": "sujeto",
        "correccion": "La niña y el niño juegan",
        "explicacion": "Sujeto plural requiere verbo plural: 'juegan'"
    },
    {
        "oracion": "Aunque hace sol, pero hace frío",
        "error": "conector",
        "correccion": "Aunque hace sol, hace frío",
        "explicacion": "'Aunque' y 'pero' no pueden usarse juntos"
    },
    {
        "oracion": "Habían muchas personas",
        "error": "verbo",
        "correccion": "Había muchas personas",
        "explicacion": "'Había' es impersonal, no concuerda con el sujeto"
    },
    {
        "oracion": "Mi hermana y yo vamos al cine",
        "error": "sujeto",
        "correccion": "Mi hermana y yo vamos al cine",
        "explicacion": "Correcto: sujeto compuesto bien conjugado"
    },
    {
        "oracion": "Porque estaba lloviendo, entonces me quedé en casa",
        "error": "conector",
        "correccion": "Porque estaba lloviendo, me quedé en casa",
        "explicacion": "'Entonces' es redundante después de 'porque'"
    },
    {
        "oracion": "Los libros está en la mesa",
        "error": "verbo",
        "correccion": "Los libros están en la mesa",
        "explicacion": "Sujeto plural requiere 'están', no 'está'"
    },
    {
        "oracion": "Cantamos y bailamos toda la noche",
        "error": "sujeto",
        "correccion": "Cantamos y bailamos toda la noche",
        "explicacion": "Correcto: sujeto tácito bien usado"
    },
    {
        "oracion": "Si estudias, entonces aprobarás",
        "error": "conector",
        "correccion": "Si estudias, aprobarás",
        "explicacion": "'Entonces' es innecesario en oraciones condicionales"
    },
    {
        "oracion": "Haigan más oportunidades",
        "error": "verbo",
        "correccion": "Haya más oportunidades",
        "explicacion": "'Haigan' no existe, la forma correcta es 'haya'"
    },
    {
        "oracion": "El presidente y su equipo trabaja duro",
        "error": "sujeto",
        "correccion": "El presidente y su equipo trabajan duro",
        "explicacion": "Sujeto compuesto requiere verbo plural"
    },
    {
        "oracion": "Como no tenía dinero, por eso no fui",
        "error": "conector",
        "correccion": "Como no tenía dinero, no fui",
        "explicacion": "'Por eso' es redundante después de 'como'"
    }
]

# Torres gramaticales disponibles
torres_gramaticales = {
    "sujeto": {
        "nombre": "🏰 Torre de Sujeto",
        "costo": 10,
        "daño": 2,
        "alcance": "Errores de concordancia sujeto-verbo",
        "símbolo": "🏰"
    },
    "verbo": {
        "nombre": "⚔️ Torre de Verbo",
        "costo": 15,
        "daño": 3,
        "alcance": "Errores de conjugación y uso verbal",
        "símbolo": "⚔️"
    },
    "conector": {
        "nombre": "🎯 Torre de Conectores",
        "costo": 12,
        "daño": 2,
        "alcance": "Errores de conectores lógicos",
        "símbolo": "🎯"
    }
}

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=" * 60)
    print("           JUEGOS GRAMATICALES - ESPAÑOL/INGLÉS")
    print("=" * 60)
    print("1. 🎯 Cazador de Sujeto y Predicado")
    print("2. 🧩 Puzzle de la Oración")
    print("3. 📊 Clasifica la Oración")
    print("4. ✏️  Corrector de Oraciones")
    print("5. 🧱 Construye tu Propia Oración")
    print("6. 🏎️  Carrera de Conectores")
    print("7. 🛡️  Defiende la Gramática (Tower Defense)")
    print("8. 📈 Ver Estadísticas")
    print("9. ❌ Salir")
    print("-" * 60)

def dibujar_mapa_defensa(camino, torres_colocadas, enemigos_activos, vida_base, puntos_gramatica):
    """Dibuja el mapa del tower defense"""
    print("\n" + "="*70)
    print("🛡️  DEFIENDE LA GRAMÁTICA - TOWER DEFENSE SINTÁCTICO")
    print("="*70)
    
    print(f"❤️  Vida de la base: {vida_base}/100")
    print(f"📚 Puntos de gramática: {puntos_gramatica}")
    print(f"🎯 Enemigos activos: {len(enemigos_activos)}")
    print("-"*70)
    
    # Dibujar el camino y las posiciones
    print("CAMINO DE LA ORACIÓN INCORRECTA:")
    print("START ", end="")
    for i in range(10):
        # Verificar si hay enemigo en esta posición
        enemigo_en_pos = None
        for enemigo in enemigos_activos:
            if enemigo['posicion'] == i:
                enemigo_en_pos = enemigo
                break
        
        if enemigo_en_pos:
            print(f"[👾{i}]", end="-")
        else:
            print(f"[{i:02d}]", end="-")
    
    print(" BASE 🏠")
    print("-"*70)
    
    # Mostrar torres colocadas
    print("TORRES GRAMATICALES COLOCADAS:")
    if torres_colocadas:
        for torre in torres_colocadas:
            tipo_torre = torres_gramaticales[torre['tipo']]
            print(f"  {tipo_torre['símbolo']} {tipo_torre['nombre']} en posición {torre['posicion']}")
    else:
        print("  Ninguna torre colocada aún")
    
    print("-"*70)

def mostrar_torres_disponibles(puntos_gramatica):
    """Muestra las torres disponibles para comprar"""
    print("🏗️  TORRES DISPONIBLES:")
    for i, (tipo, torre) in enumerate(torres_gramaticales.items(), 1):
        puede_comprar = "✅" if puntos_gramatica >= torre['costo'] else "❌"
        print(f"{i}. {torre['símbolo']} {torre['nombre']}")
        print(f"   Costo: {torre['costo']} puntos {puede_comprar}")
        print(f"   Daño: {torre['daño']} | Alcance: {torre['alcance']}")
        print()

def juego_defiende_gramatica():
    limpiar_consola()
    print("🛡️  DEFIENDE LA GRAMÁTICA")
    print("=" * 60)
    print("Protege la base de las oraciones incorrectas usando torres gramaticales!")
    print("Cada torre corrige un tipo específico de error:")
    print("🏰 Torre de Sujeto - errores de concordancia")
    print("⚔️ Torre de Verbo - errores de conjugación") 
    print("🎯 Torre de Conectores - errores de conectores lógicos")
    print("-" * 60)
    
    # Estado del juego
    vida_base = 100
    puntos_gramatica = 30  # Puntos iniciales para comprar torres
    torres_colocadas = []
    enemigos_activos = []
    ronda = 1
    enemigos_eliminados = 0
    max_rondas = 10
    
    input("Presiona Enter para comenzar la defensa...")
    
    while vida_base > 0 and ronda <= max_rondas:
        limpiar_consola()
        
        print(f"🎮 RONDA {ronda}/{max_rondas}")
        dibujar_mapa_defensa(10, torres_colocadas, enemigos_activos, vida_base, puntos_gramatica)
        
        # Fase de compra de torres
        if puntos_gramatica >= min(torre['costo'] for torre in torres_gramaticales.values()):
            print("\n💳 FASE DE CONSTRUCCIÓN:")
            mostrar_torres_disponibles(puntos_gramatica)
            
            try:
                opcion = input("¿Quieres comprar una torre? (s/n): ").lower()
                if opcion == 's':
                    tipo_num = int(input("Selecciona el tipo de torre (1-3): "))
                    tipos = list(torres_gramaticales.keys())
                    
                    if 1 <= tipo_num <= len(tipos):
                        tipo_seleccionado = tipos[tipo_num - 1]
                        torre = torres_gramaticales[tipo_seleccionado]
                        
                        if puntos_gramatica >= torre['costo']:
                            # Seleccionar posición
                            print("Posiciones disponibles: 0-9")
                            try:
                                posicion = int(input("¿En qué posición quieres colocar la torre? (0-9): "))
                                if 0 <= posicion <= 9:
                                    torres_colocadas.append({
                                        'tipo': tipo_seleccionado,
                                        'posicion': posicion,
                                        'daño': torre['daño']
                                    })
                                    puntos_gramatica -= torre['costo']
                                    print(f"✅ Torre colocada en posición {posicion}")
                                else:
                                    print("❌ Posición inválida")
                            except ValueError:
                                print("❌ Posición debe ser un número")
                        else:
                            print("❌ No tienes suficientes puntos de gramática")
                    else:
                        print("❌ Opción inválida")
            except ValueError:
                print("❌ Opción inválida")
        
        # Generar nuevos enemigos
        if random.random() < 0.7:  # 70% de probabilidad de generar enemigo
            nuevo_enemigo = random.choice(enemigos_oraciones_incorrectas).copy()
            nuevo_enemigo['posicion'] = 0
            nuevo_enemigo['vida'] = 5
            enemigos_activos.append(nuevo_enemigo)
            print(f"\n⚠️  Nuevo enemigo apareció: {nuevo_enemigo['oracion']}")
        
        # Fase de ataque de torres
        print(f"\n⚔️  FASE DE ATAQUE:")
        enemigos_eliminados_ronda = 0
        
        for torre in torres_colocadas:
            for enemigo in enemigos_activos[:]:  # Copia para modificar durante iteración
                # Torre ataca si el enemigo está en su posición y es del tipo que corrige
                if (enemigo['posicion'] == torre['posicion'] and 
                    enemigo['error'] == torre['tipo']):
                    
                    enemigo['vida'] -= torre['daño']
                    print(f"   {torres_gramaticales[torre['tipo']]['símbolo']} "
                          f"corrige: {enemigo['oracion']} (-{torre['daño']} vida)")
                    
                    if enemigo['vida'] <= 0:
                        enemigos_activos.remove(enemigo)
                        puntos_gramatica += 8
                        enemigos_eliminados += 1
                        enemigos_eliminados_ronda += 1
                        print(f"   ✅ Enemigo eliminado! +8 puntos de gramática")
                        print(f"   💡 Corrección: {enemigo['correccion']}")
                        print(f"   📚 Explicación: {enemigo['explicacion']}")
        
        # Movimiento de enemigos
        print(f"\n👾 FASE DE MOVIMIENTO:")
        for enemigo in enemigos_activos:
            enemigo['posicion'] += 1
            print(f"   {enemigo['oracion']} avanza a posición {enemigo['posicion']}")
            
            # Si llega a la base
            if enemigo['posicion'] >= 10:
                vida_base -= 15
                enemigos_activos.remove(enemigo)
                print(f"   💔 Enemigo alcanzó la base! -15 vida")
                print(f"   ❌ Oración incorrecta: {enemigo['oracion']}")
                print(f"   💡 Debería ser: {enemigo['correccion']}")
        
        # Estadísticas de la ronda
        print(f"\n📊 RESUMEN RONDA {ronda}:")
        print(f"   Enemigos eliminados: {enemigos_eliminados_ronda}")
        print(f"   Enemigos activos: {len(enemigos_activos)}")
        print(f"   Vida base: {vida_base}/100")
        print(f"   Puntos gramática: {puntos_gramatica}")
        
        ronda += 1
        
        if vida_base <= 0:
            break
            
        if ronda <= max_rondas:
            input("\nPresiona Enter para continuar a la siguiente ronda...")
    
    # Resultado final
    limpiar_consola()
    print("🎮 FIN DEL JUEGO - DEFIENDE LA GRAMÁTICA")
    print("=" * 50)
    
    if vida_base > 0:
        print("🎉 ¡VICTORIA! Has defendido la gramática con éxito!")
        print("🏆 Eres un verdadero guardián del lenguaje español!")
    else:
        print("💔 Derrota... Las oraciones incorrectas han llegado a la base")
        print("💪 Sigue practicando para mejorar tu defensa gramatical!")
    
    print(f"\n📊 ESTADÍSTICAS FINALES:")
    print(f"   Rondas sobrevividas: {min(ronda-1, max_rondas)}/{max_rondas}")
    print(f"   Vida final: {max(0, vida_base)}/100")
    print(f"   Enemigos eliminados: {enemigos_eliminados}")
    print(f"   Torres construidas: {len(torres_colocadas)}")
    print(f"   Puntos de gramática finales: {puntos_gramatica}")
    
    # Calcular puntaje (0-100)
    puntaje = min(100, (
        (max(0, vida_base) * 0.4) +  # 40% por vida
        (enemigos_eliminados * 3) +   # 30% por enemigos eliminados
        (min(ronda-1, max_rondas) * 3)  # 30% por rondas sobrevividas
    ))
    
    input("\nPresiona Enter para continuar...")
    return int(puntaje), 100

# ... (las funciones anteriores de los otros juegos se mantienen)

def main():
    estadisticas = {}
    
    while True:
        limpiar_consola()
        mostrar_menu()
        
        opcion = input("Selecciona una opción (1-9): ").strip()
        
        if opcion == "1":
            puntos, maximo = juego_sujeto_predicado()
            estadisticas["🎯 Cazador de Sujeto"] = (puntos, maximo)
        elif opcion == "2":
            puntos, maximo = juego_puzzle_oracion()
            estadisticas["🧩 Puzzle de Oración"] = (puntos, maximo)
        elif opcion == "3":
            puntos, maximo = juego_clasifica_oracion()
            estadisticas["📊 Clasifica Oración"] = (puntos, maximo)
        elif opcion == "4":
            puntos, maximo = juego_corrector_oraciones()
            estadisticas["✏️  Corrector Oraciones"] = (puntos, maximo)
        elif opcion == "5":
            puntos, maximo = juego_construye_oracion()
            estadisticas["🧱 Construye Oración"] = (puntos, maximo)
        elif opcion == "6":
            puntos, maximo = juego_carrera_conectores()
            estadisticas["🏎️  Carrera Conectores"] = (puntos, maximo)
        elif opcion == "7":
            puntos, maximo = juego_defiende_gramatica()
            estadisticas["🛡️  Defiende Gramática"] = (puntos, maximo)
        elif opcion == "8":
            mostrar_estadisticas(estadisticas)
        elif opcion == "9":
            print("\n¡Gracias por jugar! Hasta pronto 👋")
            break
        else:
            print("❌ Opción inválida. Por favor selecciona 1-9")
            time.sleep(1)

if __name__ == "__main__":
    main()
