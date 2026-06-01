def mostrar_estructura():
    # Configuración de colores para la consola
    class Color:
        AMARILLO = '\033[93m'
        VERDE = '\033[92m'
        AZUL = '\033[94m'
        DORADO = '\033[33m'
        RESET = '\033[0m'
        NEGRITA = '\033[1m'

    # Mapa de niveles educativos
    niveles = {
        "Primaria (1-30)": {
            "lecciones": 30,
            "temas": ["Abecedario", "Sílabas", "Vocales", "Consonantes", "Ortografía básica"]
        },
        "Secundaria (31-60)": {
            "lecciones": 30,
            "temas": ["Acentuación", "Verbos regulares", "Puntuación", "Sustantivos/adjetivos"]
        },
        "Bachillerato (61-99)": {
            "lecciones": 39,
            "temas": ["Subjuntivo", "Reglas B/V", "G/J", "Concordancias", "Estilo académico"]
        },
        "Evaluación Final (100)": {
            "lecciones": 1,
            "temas": ["Exhaustiva", "50 preguntas", "85% para aprobar"]
        }
    }

    # Progreso de hitos
    hitos = [
        {"leccion": 10, "recompensa": "🥉 Medalla Bronce", "requisito": "Fundamentos completados"},
        {"leccion": 50, "recompensa": "🥈 Medalla Plata", "requisito": "Gramática esencial dominada"},
        {"leccion": 99, "recompensa": "📘 Diploma Preparación", "requisito": "Preparación universitaria"},
        {"leccion": 100, "recompensa": "🥇 MEDALLA DORADA", "requisito": "85% en evaluación final"}
    ]

    # Mostrar estructura general
    print(f"\n{Color.NEGRITA}{Color.AZUL}=== ESTRUCTURA DEL PROYECTO: 100 LECCIONES DE CASTELLANO ==={Color.RESET}")
    
    for nivel, datos in niveles.items():
        print(f"\n{Color.VERDE}➤ {nivel}{Color.RESET}")
        print(f"  Lecciones: {Color.AMARILLO}{datos['lecciones']}{Color.RESET}")
        print(f"  Temas principales: {', '.join(datos['temas'])}")
        
        if nivel == "Bachillerato (61-99)":
            print(f"  {Color.NEGRITA}Preparación universitaria:{Color.RESET} Ensayos académicos, análisis literario")
        
        if nivel == "Evaluación Final (100)":
            print(f"  {Color.NEGRITA}Requisito:{Color.RESET} Completar todas las lecciones")
            print(f"  {Color.NEGRITA}Recompensa:{Color.DORADO} {datos['temas'][2]}{Color.RESET}")

    # Mostrar sistema de recompensas
    print(f"\n{Color.NEGRITA}{Color.AZUL}=== SISTEMA DE RECOMPENSAS ==={Color.RESET}")
    for hito in hitos:
        recompensa = f"{Color.DORADO}{hito['recompensa']}{Color.RESET}" if "DORADA" in hito['recompensa'] else hito['recompensa']
        print(f"\n{Color.VERDE}Lección {hito['leccion']}:{Color.RESET}")
        print(f"  • Recompensa: {recompensa}")
        print(f"  • Requisito: {hito['requisito']}")

    # Mostrar estadísticas clave
    print(f"\n{Color.NEGRITA}{Color.AZUL}=== ESTADÍSTICAS CLAVE ==={Color.RESET}")
    print(f"• Total lecciones: {Color.AMARILLO}100{Color.RESET}")
    print(f"• Ejercicios estimados: {Color.AMARILLO}350+{Color.RESET} (3-7 por lección)")
    print(f"• Duración estimada: {Color.AMARILLO}1 año académico{Color.RESET} (3 lecciones/semana)")
    print(f"• Puntos máximos posibles: {Color.AMARILLO}2,500 XP{Color.RESET}")
    print(f"• Tasa aprobación esperada: {Color.AMARILLO}85% con medalla dorada{Color.RESET}")

    # Mostrar ejemplo de progreso
    print(f"\n{Color.NEGRITA}{Color.AZUL}=== EJEMPLO DE PROGRESO ==={Color.RESET}")
    print(f"{Color.VERDE}Estudiante modelo:{Color.RESET} María (completa todo el programa)")
    print(f"• Lecciones completadas: {Color.AMARILLO}100/100{Color.RESET}")
    print(f"• Puntos acumulados: {Color.AMARILLO}2,500 XP{Color.RESET}")
    print(f"• Recompensas: {Color.AMARILLO}🥉 🥈 📘 {Color.DORADO}🥇{Color.RESET}")
    print(f"• Evaluación final: {Color.AMARILLO}92% {Color.VERDE}(APROBADO){Color.RESET}")
    print(f"{Color.DORADO}¡MEDALLA DORADA OBTENIDA!{Color.RESET}")

    # Mensaje final
    print(f"\n{Color.NEGRITA}{Color.AZUL}El proyecto está listo para implementación con:{Color.RESET}")
    print("- Flask como backend")
    print("- SQLite para almacenamiento")
    print("- Sistema gamificado completo")
    print(f"- {Color.VERDE}100 lecciones estructuradas pedagógicamente{Color.RESET}")

# Ejecutar visualización
mostrar_estructura()
