# Lista de oraciones incompletas y respuestas
oraciones = [
    ("Subí la maleta a la ___ del coche.", "Baca"),
    ("La ___ está pastando en el campo.", "Vaca"),
    ("Este material es muy ___ para construir una mesa fina.", "Basto"),
    ("La extensión del desierto es muy ___.", "Vasto"),
    ("Ella tiene muchos ___ materiales.", "Bienes"),
    ("¿Cuándo ___ a la reunión?", "Vienes"),
    ("Voy a ___ esta canción en mi teléfono.", "Grabar"),
    ("El gobierno decidió ___ los productos de lujo.", "Gravar"),
    ("Los ciudadanos decidieron ___ contra la opresión.", "Rebelar"),
    ("El fotógrafo va a ___ las fotos del evento.", "Revelar"),
    ("La ___ de los árboles es esencial para su nutrición.", "Savia"),
    ("Ella es una persona muy ___.", "Sabia"),
    ("Este paisaje es realmente ___.", "Bello"),
    ("El ___ del brazo es muy fino.", "Vello"),
    ("Necesitamos un ___ para reparar la tubería.", "Tubo"),
    ("Él ___ un día muy ocupado ayer.", "Tuvo"),
    ("Vamos a ___ esa basura.", "Botar"),
    ("¿Ya fuiste a ___ en las elecciones?", "Votar"),
    ("El médico encontró un ___ en la muestra.", "Bacilo"),
    ("Yo ___ antes de tomar una decisión.", "Vacilo"),
    ("El ___ tiene un castillo en Inglaterra.", "Barón"),
    ("El ___ es el jefe de la familia.", "Varón"),
    ("Yo ___ diferentes estilos en mi ropa.", "Combino"),
    ("Él ___ que era la mejor opción.", "Convino"),
    ("Ella ___ la entrevista para su podcast.", "Graba"),
    ("El camino está cubierto de ___.", "Grava"),
    ("No ___ más azúcar en el té.", "Basta"),
    ("La ___ llanura se extiende hasta el horizonte.", "Vasta"),
    ("El ___ de la camisa está suelto.", "Botón"),
    ("Él es un gran ___.", "Votón")
]

# Función para revisar oraciones
def revisar_oraciones(oraciones):
    for i, (oracion, respuesta) in enumerate(oraciones, 1):
        print(f"Oración {i}: {oracion}")
        respuesta_usuario = input("Completa la oración con la palabra correcta: ")
        if respuesta_usuario.strip().lower() == respuesta.lower():
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta}")
        print()

# Ejecutar la función
if __name__ == "__main__":
    revisar_oraciones(oraciones)
