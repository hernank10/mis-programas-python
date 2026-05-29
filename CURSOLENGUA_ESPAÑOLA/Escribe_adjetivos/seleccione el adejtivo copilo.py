# Lista de oraciones con adjetivos
oraciones = [
    "El perro juguetón corre por el parque.",
    "La casa antigua tiene un jardín hermoso.",
    "Ella es una excelente pianista.",
    "El cielo despejado anuncia un día soleado.",
    "El coche rojo está estacionado en la esquina.",
    "El bebé risueño se divierte con los juguetes.",
    "La película emocionante mantuvo a todos atentos.",
    "El vestido elegante es perfecto para la fiesta.",
    "El río caudaloso atraviesa el bosque.",
    "La comida deliciosa se sirve en este restaurante.",
    "El libro interesante me atrapó desde la primera página.",
    "El atardecer colorido pinta el horizonte.",
    "La montaña imponente desafía a los escaladores.",
    "El perfume dulce es mi favorito.",
    "La playa tranquila invita a relajarse.",
    "El avión rápido despegó hacia su destino.",
    "El bosque frondoso esconde secretos.",
    "La ciudad bulliciosa nunca duerme.",
    "El café caliente me reconforta en las mañanas.",
    "El parque verde es ideal para hacer ejercicio."
]

# Función para identificar el adjetivo en una oración
def identificar_adjetivo(oracion):
    palabras = oracion.split()
    for palabra in palabras:
        if palabra.lower() in adjetivos:
            return palabra.lower()
    return None

# Lista de adjetivos
adjetivos = [
    "juguetón", "antigua", "excelente", "despejado", "rojo",
    "risueño", "emocionante", "elegante", "caudaloso", "deliciosa",
    "interesante", "colorido", "imponente", "dulce", "tranquila",
    "rápido", "frondoso", "bulliciosa", "caliente", "verde"
]

# Procesamiento de cada oración
for i, oracion in enumerate(oraciones, 1):
    print(f"Oración {i}: {oracion}")
    adjetivo_correcto = identificar_adjetivo(oracion)
    if adjetivo_correcto:
        respuesta_usuario = input(f"Identifica el adjetivo en la oración: ")
        if respuesta_usuario.lower() == adjetivo_correcto:
            print("¡Correcto! Reescribe la oración:")
            nueva_oracion = input()
            print(f"Oración reescrita: {nueva_oracion}\n")
        else:
            print(f"El adjetivo correcto era '{adjetivo_correcto}'. Inténtalo de nuevo.\n")
    else:
        print("No se encontró un adjetivo en esta oración.\n")

# Mensaje de felicitaciones al final
print("¡Has completado todas las oraciones! ¡Bien hecho!")
