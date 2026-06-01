def mostrar_menu_ejemplos():
    class Color:
        AZUL = '\033[94m'
        VERDE = '\033[92m'
        AMARILLO = '\033[93m'
        MAGENTA = '\033[95m'
        RESET = '\033[0m'
    
    print(f"\n{Color.AZUL}=== MENÚ DE SECCIONES POR LECCIÓN ===")
    print(f"{Color.VERDE}Sección Teoría{Color.RESET}")
    print("  - Explicación conceptual completa")
    print("  - Estructuras gramaticales")
    print("  - Excepciones importantes")
    print("  - Consejos didácticos")
    
    print(f"\n{Color.VERDE}Sección Ejemplos{Color.RESET}")
    print(f"  {Color.MAGENTA}• Ejemplos básicos:{Color.RESET}")
    print("     - 'El niño come manzanas' (S+V+C)")
    print(f"  {Color.MAGENTA}• Ejemplos comparativos:{Color.RESET}")
    print("     - Correcto: 'Había muchas personas'")
    print("     - Incorrecto: 'Habían muchas personas'")
    print(f"  {Color.MAGENTA}• Ejemplos académicos:{Color.RESET}")
    print("     - 'Se evidencia una correlación significativa'")
    print(f"  {Color.MAGENTA}• Ejemplos literarios:{Color.RESET}")
    print("     - 'La noche se vistió de estrellas' (metáfora)")
    
    print(f"\n{Color.VERDE}Sección Ejercicios{Color.RESET}")
    print("  - Cuestionarios prácticos")
    print("  - Ejercicios de completar")
    print("  - Actividades de correlación")
    
    print(f"\n{Color.AMARILLO}Herramientas Interactivas en Ejemplos:{Color.RESET}")
    print("  ✓ Analizador de estructura gramatical")
    print("  ✓ Creador de ejemplos propios")
    print("  ✓ Verificador automático")
    
    print(f"\n{Color.AZUL}Este sistema permite:{Color.RESET}")
    print("- Aprendizaje teórico sólido")
    print("- Aplicación práctica inmediata")
    print("- Desarrollo de competencia creativa")
    print("- Preparación para producción escrita avanzada")

mostrar_menu_ejemplos()
