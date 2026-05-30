# Lista de oraciones con adjetivos en Lengua Castellana
oraciones = [
    "Nos sirvió un camarero joven poco amistoso.",
    "Era una habitación incómoda, sucia y oscura.",
    "Usó una navaja grande afilada.",
    "Nos encontramos en una enorme sala de conferencias de cristal.",
    "Rompió un precioso plato blanco de porcelana japonesa.",
    "Susan salía con un atractivo estadounidense alto y moreno.",
    "Tenía un bonito perrito blanco de pelo rizado.",
    "Conocimos a un joven atractivo teniente de navio.",
    "La joven vivia sola en una bonita habitation limpia y clara.",
    "Se bebio un enorme vaso de leche helada.",
    "Llevaba un bolso de cuero negro grande y reluciente",
    "Era una mesa de cocina, de madera, hecha a mano.",
    "Fuimos a un pequeño restaurante italiano muy bonito.",
    "En la muñeca llevaba una pulsera de esmeraldas de un verde oscuro.",
    "En la casita vivía una vieja gruñona.",
    "El Sr.Martin estaba hablando con una bella mujer joven.",
    "Las dos familias vivían en una vieja choza decrepita.",
    "Vimos una película vieja",
    "Tenía unos ojos grandes, rojos, saltones.",
    "Era un día gris, lluvioso, deprimente.",
    "Tomó una refrescante ducha fría por la manana."
    ]

# Función para identificar el adjetivo en una oración
def identificar_adjetivo(oracion):
    palabras = oracion.split()
    for palabra in palabras:
        if palabra.lower() in adjetivos:
            return palabra.lower()
    return None

# Lista de adjetivos en Lengua Castellana
adjetivos = [
    "joven", "incómoda", "grande", "enorme", "blanco",
    "atractivo", "blanco", "atractivo", "bonita", "enorme",
    "cuero", "cocina", "italiano", "verde", "gruñona",
    "bella", "vieja", "vieja", "grandes", "gris", "fría"
    # ... Agrega más adjetivos aquí ...
]

# Procesamiento de cada oración
for i, oracion in enumerate(oraciones, 1):
    print(f"Oración {i}: {oracion}")
    adjetivo_correcto = identificar_adjetivo(oracion)
    if adjetivo_correcto:
        respuesta_usuario = input("Identifica el adjetivo en la oración: ")
        if respuesta_usuario.lower() == adjetivo_correcto:
            print("¡Correcto! Reescribe la oración en Lengua Castellana:")
            nueva_oracion = input()
            print(f"Oración reescrita: {nueva_oracion}\n")
        else:
            print(f"El adjetivo correcto era '{adjetivo_correcto}'. Inténtalo de nuevo.\n")
    else:
        print("No se encontró un adjetivo en esta oración.\n")

print("¡Has completado todas las oraciones! ¡Bien hecho!")
