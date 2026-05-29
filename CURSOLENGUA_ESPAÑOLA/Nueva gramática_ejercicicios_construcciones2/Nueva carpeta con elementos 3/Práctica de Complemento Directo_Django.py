# views.py en Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

EJEMPLOS_BASE = [
    ("He visto una película", "una película"),
    ("Compré un coche nuevo", "un coche nuevo"),
    ("Ella leyó el libro", "el libro"),
    ("Pedro pintó la casa", "la casa"),
    ("María cocinó la cena", "la cena"),
    ("Juan rompió el vaso", "el vaso"),
    ("Ana organizó la fiesta", "la fiesta"),
    ("Escuchamos la canción", "la canción"),
    ("Clara escribió una carta", "una carta"),
    ("Luis abrió la puerta", "la puerta"),
    ("El niño rompió el juguete", "el juguete"),
    ("Vi a tu hermano", "a tu hermano"),
    ("Tocamos la guitarra", "la guitarra"),
    ("Perdí el tren", "el tren"),
    ("Ganamos el partido", "el partido"),
    ("Leí la noticia", "la noticia"),
    ("Encontré las llaves", "las llaves"),
    ("Terminé el informe", "el informe"),
    ("Comprendí la explicación", "la explicación"),
    ("Guardó el documento", "el documento"),
    ("Encendió la luz", "la luz"),
    ("Apagó el televisor", "el televisor"),
    ("Escribí un poema", "un poema"),
    ("El perro encontró el hueso", "el hueso"),
    ("La profesora corrigió los exámenes", "los exámenes"),
    ("Vi la película dos veces", "la película"),
    ("Descargué la aplicación", "la aplicación"),
    ("Revisé los correos", "los correos"),
    ("Presenté el proyecto", "el proyecto"),
    ("Recibí el paquete", "el paquete"),
    ("El gato atrapó al ratón", "al ratón"),
    ("El policía detuvo al ladrón", "al ladrón"),
    ("Marina horneó un pastel", "un pastel"),
    ("El mecánico arregló el coche", "el coche"),
    ("Sandra limpió la cocina", "la cocina"),
    ("José vendió su bicicleta", "su bicicleta"),
    ("Miramos las estrellas", "las estrellas"),
    ("Guardé los documentos", "los documentos"),
    ("El niño abrazó a su madre", "a su madre"),
    ("Carmen escribió un correo", "un correo"),
    ("Tiré la basura", "la basura"),
    ("Compramos frutas frescas", "frutas frescas"),
    ("El pintor terminó el mural", "el mural"),
    ("Sara decoró la habitación", "la habitación"),
    ("Le mostré la foto", "la foto"),
    ("Claudia trajo el informe", "el informe"),
    ("El niño escondió el juguete", "el juguete"),
    ("Tomé el medicamento", "el medicamento"),
    ("El alumno entregó la tarea", "la tarea"),
    ("Luis bebió el jugo", "el jugo")
]

@csrf_exempt
def index(request):
    posicion = int(request.session.get("posicion", 0))
    if posicion >= len(EJEMPLOS_BASE):
        return HttpResponse("<h2>\u00a1Has completado todos los ejemplos!</h2>")

    ejemplo, correcto = EJEMPLOS_BASE[posicion]
    resultado = None

    if request.method == "POST":
        respuesta = request.POST.get("respuesta", "").strip().lower()
        if respuesta == correcto.lower():
            resultado = "\u00a1Correcto!"
        else:
            resultado = f"Incorrecto. La respuesta era: '{correcto}'"
        posicion += 1
        request.session["posicion"] = posicion

    return render(request, "cd/index.html", {
        "ejemplo": ejemplo,
        "resultado": resultado
    })
