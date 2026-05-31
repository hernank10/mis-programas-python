import random

# Configuración inicial
ejemplos = [
    {
        "oracion": "Los estudiantes que entran a la Biblioteca con su carnet pueden pedir hasta tres libros en préstamo.",
        "tipo": "E",
        "explicacion": "\nSin el modificador: 'Los estudiantes pueden pedir...' → Incluye a TODOS, no solo a los con carnet.\nPor lo tanto, es ESENCIAL (restrictivo)."
    },
    {
        "oracion": "Los estudiantes, que entran a la Biblioteca con su carnet, pueden pedir hasta tres libros en préstamo.",
        "tipo": "X",
        "explicacion": "\nSin el inciso: 'Los estudiantes pueden pedir...' → La info del carnet es adicional.\nPor lo tanto, es EXPLICATIVO (no restrictivo)."
    },
    {
        "oracion": "Las ventanas que dan a la calle 9 serán reforzadas.",
        "tipo": "E",
        "explicacion": "\nSin el modificador: 'Las ventanas serán reforzadas' → Todas, no solo las de la calle 9.\n¡Cambia el significado! Es ESENCIAL."
    },
    {
        "oracion": "Las ventanas, que dan a la calle 9, serán reforzadas.",
        "tipo": "X",
        "explicacion": "\nSin el inciso: 'Las ventanas serán reforzadas' → Todas dan a la calle 9 y se reforzarán.\nInfo adicional. Es EXPLICATIVO."
    },
    {
        "oracion": "El alumno Óscar Mantilla y su hija Nayibe Alexandra son los ganadores.",
        "tipo": "E",
        "explicacion": "\nSin especificar: 'su hija son los ganadores' → Óscar tiene + de 1 hija.\nModificador ESENCIAL."
    },
    {
        "oracion": "El alumno Óscar Mantilla y su hija, Nayibe Alexandra, son los ganadores.",
        "tipo": "X",
        "explicacion": "\nSin el inciso: 'su hija son los ganadores' → Nayibe es su ÚNICA hija.\nInfo explicativa."
    },
    {
        "oracion": "Los empleados que lleguen tarde perderán el bono.",
        "tipo": "E",
        "explicacion": "\nSin el modificador: 'Los empleados perderán el bono' → Todos, no solo los tardíos.\n¡Es ESENCIAL!"
    },
    {
        "oracion": "Los empleados, que llegaron tarde, perderán el bono.",
        "tipo": "X",
        "explicacion": "\nSin el inciso: 'Los empleados perderán el bono' → Todos llegaron tarde y pierden.\nInfo no restrictiva."
    }
]

random.shuffle(ejemplos)  # Mezclar ejemplos
puntaje = 0

# Bienvenida
print("""
★☆★ Practiquemos modificadores ESENCIALES vs. EXPLICATIVOS ★☆★

Instrucciones:
1. Lee cada oración.
2. Decide si el modificador subrayado es ESENCIAL (E) o EXPLICATIVO (X).
3. Escribe 'E' o 'X' y presiona Enter.
4. ¡Gana puntos por cada respuesta correcta!

-----------------------------------------
""")

# Bucle principal
for idx, ejemplo in enumerate(ejemplos, 1):
    print(f"\n[{idx}/{len(ejemplos)}] Oración:")
    print(f"→ '{ejemplo['oracion']}'")
    
    while True:
        respuesta = input("\n¿Es ESENCIAL (E) o EXPLICATIVO (X)? → ").upper()
        if respuesta in ["E", "X"]:
            break
        print("⚠️ ¡Solo ingresa 'E' o 'X'!")
    
    if respuesta == ejemplo["tipo"]:
        puntaje += 10
        print(f"✅ ¡Correcto! +10 puntos {ejemplo['explicacion']}")
    else:
        print(f"❌ Incorrecto. La respuesta era '{ejemplo['tipo']}'. {ejemplo['explicacion']}")
    
    print("\n-----------------------------------------")

# Resultado final
print(f"\n★ Puntaje final: {puntaje}/{len(ejemplos)*10} puntos ★")
if puntaje == len(ejemplos)*10:
    print("¡Excelente! Dominas la diferencia. 🎓")
elif puntaje >= len(ejemplos)*7:
    print("¡Muy bien! Sigue practicando. 📚")
else:
    print("¡Sigue intentándolo! La práctica hace al maestro. 💪")
