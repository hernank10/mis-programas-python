# Programa para aprender las reglas de la derivación en castellano mediante la repetición

# Lista de reglas de derivación
reglas_derivacion = [
    "Prefijo 'in-': Indica negación o privación. Ejemplo: visible - invisible.",
    "Prefijo 're-': Indica repetición o intensificación. Ejemplo: hacer - rehacer.",
    "Prefijo 'des-': Indica inversión del significado o acción contraria. Ejemplo: hacer - deshacer.",
    "Prefijo 'sub-': Indica inferioridad o posición por debajo. Ejemplo: marino - submarino.",
    "Prefijo 'pre-': Indica anterioridad en el tiempo o en el espacio. Ejemplo: histórico - prehistórico.",
    "Sufijo '-ción': Forma sustantivos a partir de verbos, indicando acción o efecto. Ejemplo: navegar - navegación.",
    "Sufijo '-dor(a)': Forma sustantivos que indican agente o instrumento. Ejemplo: hablar - hablador.",
    "Sufijo '-mente': Forma adverbios a partir de adjetivos. Ejemplo: rápido - rápidamente.",
    "Sufijo '-oso(a)': Forma adjetivos que indican abundancia o cualidad. Ejemplo: amor - amoroso.",
    "Sufijo '-ito(a)': Forma diminutivos, indicando menor tamaño o afecto. Ejemplo: perro - perrito.",
    "Sufijo '-ón(a)': Forma aumentativos, indicando mayor tamaño o intensidad. Ejemplo: casa - casón.",
    "Cambio de categoría gramatical: Verbos a sustantivos añadiendo sufijos como '-ción', '-miento'. Ejemplo: educar - educación.",
    "Cambio de categoría gramatical: Sustantivos a adjetivos añadiendo sufijos como '-al', '-oso', '-ico'. Ejemplo: naturaleza - natural.",
    "Cambio de categoría gramatical: Adjetivos a sustantivos añadiendo sufijos como '-dad', '-ura'. Ejemplo: libre - libertad.",
    "Modificación del significado: Prefijos como 'in-', 'des-' para indicar negación. Ejemplo: capaz - incapaz.",
    "Modificación del significado: Prefijos como 're-' para indicar repetición. Ejemplo: calcular - recalcular.",
    "Modificación del significado: Sufijos como '-ito' para diminutivos. Ejemplo: flor - florecita.",
    "Modificación del significado: Sufijos como '-ón' para aumentativos. Ejemplo: coche - cochazo.",
    "Cambios fonéticos: Adaptación de la base léxica para mantener la pronunciación adecuada. Ejemplo: feliz - felicidad.",
    "Cambios fonéticos: Asimilación de sonidos para facilitar la pronunciación. Ejemplo: público - publicidad."
]

def aprender_reglas():
    print("Aprende las reglas de la derivación en castellano mediante la repetición.\n")
    
    for i, regla in enumerate(reglas_derivacion):
        print(f"Regla {i+1}: {regla}")
        input("Presiona Enter para continuar...\n")
        
        respuesta = input(f"Escribe la regla {i+1} de nuevo: ")
        
        if respuesta.strip().lower() == regla.strip().lower():
            print("¡Correcto! Has recordado bien la regla.\n")
        else:
            print(f"Incorrecto. La regla correcta es:\n{regla}\n")
            
        input("Presiona Enter para continuar con la siguiente regla...\n")

if __name__ == "__main__":
    aprender_reglas()

