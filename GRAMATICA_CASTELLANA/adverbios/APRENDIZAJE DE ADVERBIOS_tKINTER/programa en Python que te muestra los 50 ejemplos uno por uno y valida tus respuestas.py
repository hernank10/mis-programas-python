ejemplos = [
    {"frase": "1___ libro está sobre la mesa.", "respuesta": "un"},
    {"frase": "1___ manzana cayó del árbol.", "respuesta": "una"},
    {"frase": "Compré 2 ___ cuadernos nuevos.", "respuesta": "dos"},
    {"frase": "3___ gatos jugaban en el jardín.", "respuesta": "tres"},
    {"frase": "___ hermanos viajarán mañana.", "respuesta": "cuatro"},
    {"frase": "___ estrellas brillan en el cielo.", "respuesta": "cinco"},
    {"frase": "Necesito ___ lápices para el examen.", "respuesta": "seis"},
    {"frase": "___ días forman una semana.", "respuesta": "siete"},
    {"frase": "___ personas asistieron a la reunión.", "respuesta": "ocho"},
    {"frase": "___ flores adornaban el jarrón.", "respuesta": "nueve"},
    {"frase": "___ años es una década.", "respuesta": "diez"},
    {"frase": "___ alumnos aprobaron el curso.", "respuesta": "once"},
    {"frase": "___ meses tiene un año.", "respuesta": "doce"},
    {"frase": "___ panes había en la canasta.", "respuesta": "trece"},
    {"frase": "___ canciones componen el álbum.", "respuesta": "catorce"},
    {"frase": "___ minutos son un cuarto de hora.", "respuesta": "quince"},
    {"frase": "___ páginas faltan.", "respuesta": "dieciséis"},
    {"frase": "___ días de viaje.", "respuesta": "diecisiete"},
    {"frase": "___ años cumplirá.", "respuesta": "dieciocho"},
    {"frase": "___ estudiantes llenaron el aula.", "respuesta": "veinte"},
    {"frase": "___ días de espera.", "respuesta": "veintiún"},
    {"frase": "___ personas confirmaron.", "respuesta": "veintidós"},
    {"frase": "___ libros en la estantería.", "respuesta": "treinta y un"},
    {"frase": "___ grados de temperatura.", "respuesta": "cuarenta y cinco"},
    {"frase": "___ años es un jubileo.", "respuesta": "cincuenta"},
    {"frase": "___ segundos hacen un minuto.", "respuesta": "sesenta"},
    {"frase": "___ pájaros volaron al sur.", "respuesta": "setenta"},
    {"frase": "___ kilómetros por hora.", "respuesta": "ochenta"},
    {"frase": "___ minutos dura el partido.", "respuesta": "noventa"},
    {"frase": "___ años de soledad.", "respuesta": "cien"},
    {"frase": "___ páginas leídas.", "respuesta": "ciento veinte"},
    {"frase": "___ árboles plantados.", "respuesta": "doscientos"},
    {"frase": "___ personas asistieron.", "respuesta": "trescientas"},
    {"frase": "___ metros de carrera.", "respuesta": "quinientos"},
    {"frase": "___ años de historia.", "respuesta": "setecientos"},
    {"frase": "___ noventa y nueve años.", "respuesta": "novecientos"},
    {"frase": "___ años es un milenio.", "respuesta": "mil"},
    {"frase": "___ pasos al día.", "respuesta": "dos mil"},
    {"frase": "___ estrellas visibles.", "respuesta": "cien mil"},
    {"frase": "___ kilómetros.", "respuesta": "ciento veinte mil"},
    {"frase": "___ habitantes.", "respuesta": "trescientos mil"},
    {"frase": "___ dólares invertidos.", "respuesta": "un millón de"},
    {"frase": "___ bacterias.", "respuesta": "dos billones de"},
    {"frase": "___ hermanos son altos.", "respuesta": "ambos"},
    {"frase": "___ lados del río están contaminados.", "respuesta": "entrambos"},
    {"frase": "___ días de descanso.", "respuesta": "unos"},
    {"frase": "___ flores crecieron silvestres.", "respuesta": "unas"},
    {"frase": "Los ___ en la fecha son coincidencia.", "respuesta": "treses"},
    {"frase": "El ___ es un número de la suerte.", "respuesta": "ocho"},
    {"frase": "El ___ de infantería avanzó.", "respuesta": "seis"}
]

def limpiar_texto(texto):
    return texto.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

puntaje = 0

print("¡Bienvenido al practicador de numerales cardinales!")
print("Escribe la forma correcta para cada espacio. (Respete acentos y espacios)\n")

for i, ejemplo in enumerate(ejemplos, 1):
    print(f"\nEjemplo {i}/50:")
    print(ejemplo["frase"])
    respuesta = input("Tu respuesta: ").strip()
    
    respuesta_limpia = limpiar_texto(respuesta)
    correcta_limpia = limpiar_texto(ejemplo["respuesta"])
    
    if respuesta_limpia == correcta_limpia:
        print("✅ ¡Correcto!")
        puntaje += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta es: {ejemplo['respuesta']}")
    
    print(f"Progreso: {i}/50 | Aciertos: {puntaje}\n")

print(f"\n¡Práctica completada! Puntuación final: {puntaje}/50")
if puntaje == 50:
    print("🎖️ ¡Perfecto! Dominas los numerales cardinales")
elif puntaje >= 40:
    print("🏅 ¡Excelente! Algún detalle por pulir")
elif puntaje >= 30:
    print("👍 ¡Buen trabajo! Sigue practicando")
else:
    print("💡 Sigue estudiando los casos especiales")
