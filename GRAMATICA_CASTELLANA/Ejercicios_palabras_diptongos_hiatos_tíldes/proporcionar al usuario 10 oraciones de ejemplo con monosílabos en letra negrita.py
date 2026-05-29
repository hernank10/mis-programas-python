import random

def mostrar_oracion_con_monosilabo():
    monosilabos = ["él", "el", "mi", "mí", "tu", "tú", "si", "sí", "te", "él"]

    # Seleccionar aleatoriamente un monosílabo
    monosilabo_seleccionado = random.choice(monosilabos)

    # Crear una oración de ejemplo con el monosílabo en letra negrita
    oracion = f"Me encontré con **{monosilabo_seleccionado}** en la tienda hoy."

    return oracion, monosilabo_seleccionado

def solicitar_respuesta(oracion):
    # Solicitar al usuario que identifique la palabra homónima o polisémica
    respuesta_usuario = input(f"\n{oracion}\nPalabra homónima o polisémica: ").strip().lower()
    return respuesta_usuario

def verificar_respuesta(respuesta_usuario, monosilabo_seleccionado):
    # Verificar si la respuesta del usuario es correcta
    return respuesta_usuario == monosilabo_seleccionado

# Generar y mostrar 10 oraciones con monosílabos
print("Identifica la palabra homónima o polisémica en cada oración:")
for _ in range(10):
    oracion, monosilabo_seleccionado = mostrar_oracion_con_monosilabo()

    # Solicitar respuesta al usuario
    respuesta_usuario = solicitar_respuesta(oracion)

    # Verificar respuesta y proporcionar retroalimentación
    if verificar_respuesta(respuesta_usuario, monosilabo_seleccionado):
        print("¡Correcto!\n")
    else:
        print(f"Incorrecto. La palabra correcta es **{monosilabo_seleccionado}**.\n")

print("Recuerda que la tilde diacrítica en monosílabos como 'el', 'mi', 'tu', 'si', etc., permite diferenciar su significado.")
