familias_lexicas = {
    "b": [["buscar", "buscador", "busca", "búsqueda"],
         ["besar", "beso", "besuqueo", "besuque"],
         ["bueno", "bondad", "bonito", "bonanza"]],
    "v": [["venir", "venida", "vendedor", "vendedor"],
         ["volver", "vuelta", "volveré", "envoltorio"],
         ["vida", "vivir", "vivo", "vivienda"]]
}

def practicar_familias_lexicas():
    puntaje = 0
    total_preguntas = 0
    
    for letra, familias in familias_lexicas.items():
        print(f"\nFamilias léxicas con '{letra}':")
        for familia in familias:
            for palabra in familia:
                total_preguntas += 1
                respuesta_usuario = input(f"Escribe la palabra: {palabra} ")
                if respuesta_usuario.lower() == palabra.lower():
                    print("¡Correcto!")
                    puntaje += 1
                else:
                    print(f"Incorrecto. La palabra correcta era: {palabra}")

    print(f"\n¡Has terminado! Tu puntaje es: {puntaje}/{total_preguntas}")

practicar_familias_lexicas()
