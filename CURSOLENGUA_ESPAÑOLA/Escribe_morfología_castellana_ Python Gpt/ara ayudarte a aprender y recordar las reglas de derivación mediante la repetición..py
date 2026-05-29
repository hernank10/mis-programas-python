# Programa para aprender las reglas de la composición en castellano mediante la repetición

# Lista de reglas de composición
reglas_composicion = [
    "Compuestos Propios: Palabras que se escriben juntas sin espacios ni guiones. Ejemplo: parabrisas (para + brisas), sacapuntas (sacar + puntas).",
    "Compuestos Impropios: Palabras que se escriben separadas pero funcionan como una sola unidad. Ejemplo: hombre rana (hombre + rana), coche cama (coche + cama).",
    "Compuestos por Yuxtaposición: Palabras que se combinan mediante un guion. Ejemplo: teórico-práctico (teoría + práctica), histórico-artístico (historia + arte).",
    "Composición Nominal: Combinación de dos sustantivos para formar un nuevo sustantivo. Ejemplo: montaña rusa (montaña + rusa), paraguas (para + aguas).",
    "Composición Adjetival: Combinación de un sustantivo y un adjetivo para formar un nuevo adjetivo. Ejemplo: hispanoamericano (hispano + americano), verde oliva (verde + oliva).",
    "Composición Verbal: Combinación de un verbo y un sustantivo para formar un nuevo verbo. Ejemplo: malgastar (mal + gastar), sobrellevar (sobre + llevar).",
    "Composición Adverbial: Combinación de dos adverbios para formar un nuevo adverbio. Ejemplo: bienvenido (bien + venido), malhumorado (mal + humorado)."
]

def aprender_reglas_composicion():
    print("Aprende las reglas de la composición en castellano mediante la repetición.\n")
    
    for i, regla in enumerate(reglas_composicion):
        print(f"Regla {i+1}: {regla}")
        input("Presiona Enter para continuar...\n")
        
        respuesta = input(f"Escribe la regla {i+1} de nuevo: ")
        
        if respuesta.strip().lower() == regla.strip().lower():
            print("¡Correcto! Has recordado bien la regla.\n")
        else:
            print(f"Incorrecto. La regla correcta es:\n{regla}\n")
            
        input("Presiona Enter para continuar con la siguiente regla...\n")

if __name__ == "__main__":
    aprender_reglas_composicion()
