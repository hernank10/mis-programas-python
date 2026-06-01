import random

def cargar_ejercicios_composicion_morfologica():
    """
    Carga los 100 ejercicios predefinidos de composición morfológica en castellano
    directamente en el código.
    """
    print("Cargando 100 ejercicios de Composición Morfológica y su Estructura Gramatical directamente...")
    return {
        "Morfología": {
            "Avanzado": {
                "Composición Morfológica y Estructura": [
                    {"pregunta": "Analiza la formación de 'paraguas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Para' (del verbo parar) + 'aguas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'sacapuntas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Saca' (del verbo sacar) + 'puntas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'abrelatas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Abre' (del verbo abrir) + 'latas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'cortacésped'.", "respuesta": "verbo + sustantivo", "explicacion": "'Corta' (del verbo cortar) + 'césped'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'guardarropa'.", "respuesta": "verbo + sustantivo", "explicacion": "'Guarda' (del verbo guardar) + 'ropa'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'rompecabezas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Rompe' (del verbo romper) + 'cabezas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'pisapapeles'.", "respuesta": "verbo + sustantivo", "explicacion": "'Pisa' (del verbo pisar) + 'papeles'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'cubrecama'.", "respuesta": "verbo + sustantivo", "explicacion": "'Cubre' (del verbo cubrir) + 'cama'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'lavavajillas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Lava' (del verbo lavar) + 'vajillas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'limpiabotas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Limpia' (del verbo limpiar) + 'botas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'correcaminos'.", "respuesta": "verbo + sustantivo", "explicacion": "'Corre' (del verbo correr) + 'caminos'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'tragaperras'.", "respuesta": "verbo + sustantivo", "explicacion": "'Traga' (del verbo tragar) + 'perras'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'lavarropas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Lava' (del verbo lavar) + 'ropas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'parabrisas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Para' (del verbo parar) + 'brisas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'portapapeles'.", "respuesta": "verbo + sustantivo", "explicacion": "'Porta' (del verbo portar) + 'papeles'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'cazafantasmas'.", "respuesta": "verbo + sustantivo", "explicacion": "'Caza' (del verbo cazar) + 'fantasmas'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'hazmerreír'.", "respuesta": "verbo + pronombre + verbo", "explicacion": "'Haz' (verbo) + 'me' (pronombre) + 'reír' (verbo). Es un caso especial de V+V con pronombre."},
                    {"pregunta": "Analiza la formación de 'sabelotodo'.", "respuesta": "verbo + pronombre + sustantivo", "explicacion": "'Sabe' (verbo) + 'lo' (pronombre) + 'todo' (sustantivo). Es un caso especial de V+N con pronombre."},
                    {"pregunta": "Analiza la formación de 'malvivir'.", "respuesta": "adverbio + verbo", "explicacion": "'Mal' (adverbio) + 'vivir' (verbo). Tipo Adv + V."},
                    {"pregunta": "Analiza la formación de 'bienestar'.", "respuesta": "adverbio + verbo", "explicacion": "'Bien' (adverbio) + 'estar' (verbo). Tipo Adv + V."},
                    {"pregunta": "Analiza la formación de 'maldecir'.", "respuesta": "adverbio + verbo", "explicacion": "'Mal' (adverbio) + 'decir' (verbo). Tipo Adv + V."},
                    {"pregunta": "Analiza la formación de 'malhumor'.", "respuesta": "adverbio + sustantivo", "explicacion": "'Mal' (adverbio) + 'humor' (sustantivo). Tipo Adv + N."},
                    {"pregunta": "Analiza la formación de 'malpensado'.", "respuesta": "adverbio + adjetivo", "explicacion": "'Mal' (adverbio) + 'pensado' (adjetivo). Tipo Adv + Adj."},
                    {"pregunta": "Analiza la formación de 'agridulce'.", "respuesta": "adjetivo + adjetivo", "explicacion": "'Agri' (de agrio) + 'dulce'. Tipo Adj + Adj."},
                    {"pregunta": "Analiza la formación de 'pelirojo'.", "respuesta": "sustantivo + adjetivo", "explicacion": "'Peli' (de pelo) + 'rojo'. Tipo N + Adj."},
                    {"pregunta": "Analiza la formación de 'manirroto'.", "respuesta": "sustantivo + adjetivo", "explicacion": "'Mani' (de mano) + 'roto'. Tipo N + Adj."},
                    {"pregunta": "Analiza la formación de 'sordomudo'.", "respuesta": "adjetivo + adjetivo", "explicacion": "'Sordo' + 'mudo'. Tipo Adj + Adj."},
                    {"pregunta": "Analiza la formación de 'altibajo'.", "respuesta": "adjetivo + adjetivo", "explicacion": "'Alti' (de alto) + 'bajo'. Tipo Adj + Adj."},
                    {"pregunta": "Analiza la formación de 'bajorrelieve'.", "respuesta": "adjetivo + sustantivo", "explicacion": "'Bajo' + 'relieve'. Tipo Adj + N."},
                    {"pregunta": "Analiza la formación de 'medianoche'.", "respuesta": "adjetivo + sustantivo", "explicacion": "'Media' + 'noche'. Tipo Adj + N."},
                    {"pregunta": "Analiza la formación de 'aguardiente'.", "respuesta": "sustantivo + adjetivo", "explicacion": "'Agua' + 'ardiente'. Tipo N + Adj."},
                    {"pregunta": "Analiza la formación de 'ciempiés'.", "respuesta": "sustantivo + sustantivo", "explicacion": "'Cien' + 'pies'. Tipo N + N (con cambio fonético del numeral)."},
                    {"pregunta": "Analiza la formación de 'pasodoble'.", "respuesta": "sustantivo + adjetivo", "explicacion": "'Paso' + 'doble'. Tipo N + Adj."},
                    {"pregunta": "Analiza la formación de 'milhojas'.", "respuesta": "sustantivo + sustantivo", "explicacion": "'Mil' + 'hojas'. Tipo N + N (con cambio fonético del numeral)."},
                    {"pregunta": "Analiza la formación de 'bocacalle'.", "respuesta": "sustantivo + sustantivo", "explicacion": "'Boca' + 'calle'. Tipo N + N."},
                    {"pregunta": "Analiza la formación de 'telaraña'.", "respuesta": "sustantivo + sustantivo", "explicacion": "'Tela' + 'araña'. Tipo N + N."},
                    {"pregunta": "Analiza la formación de 'nochebuena'.", "respuesta": "sustantivo + adjetivo", "explicacion": "'Noche' + 'buena'. Tipo N + Adj."},
                    {"pregunta": "Analiza la formación de 'bienvenida'.", "respuesta": "adverbio + adjetivo", "explicacion": "'Bien' + 'venida'. Tipo Adv + Adj."},
                    {"pregunta": "Analiza la formación de 'bajamar'.", "respuesta": "adjetivo + sustantivo", "explicacion": "'Baja' + 'mar'. Tipo Adj + N."},
                    {"pregunta": "Analiza la formación de 'saltamontes'.", "respuesta": "verbo + sustantivo", "explicacion": "'Salta' (del verbo saltar) + 'montes'. Tipo V + N."},
                    {"pregunta": "Analiza la formación de 'correveidile'.", "respuesta": "verbo + verbo + verbo", "explicacion": "'Corre' + 've' + 'i' (conjunción) + 'dile' (verbo). Es un caso especial de V+V+V."},
                    {"pregunta": "Analiza la formación de 'radioyente'.", "respuesta": "sustantivo + sustantivo", "explicacion": "'Radio' + 'oyente'. Tipo N + N."},
                    {"pregunta": "Analiza la formación de 'videollamada'.", "respuesta": "sustantivo + sustantivo", "explicacion": "'Video' + 'llamada'. Tipo N + N."},
                    {"pregunta": "Analiza la formación de 'telescopio'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Tele-' (distancia) + 'scopio' (ver). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'automóvil'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Auto-' (por sí mismo) + 'móvil'. Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'fotografía'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Foto-' (luz) + 'grafía' (escritura). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'teléfono'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Tele-' (distancia) + 'fono' (sonido). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'biología'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Bio-' (vida) + 'logía' (estudio). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'geología'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Geo-' (tierra) + 'logía' (estudio). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'cronómetro'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Crono-' (tiempo) + 'metro' (medida). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'hidroterapia'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Hidro-' (agua) + 'terapia'. Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'termómetro'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Termo-' (calor) + 'metro' (medida). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'ortografía'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Orto-' (correcto) + 'grafía' (escritura). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'microscopio'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Micro-' (pequeño) + 'scopio' (ver). Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'macroeconomía'.", "respuesta": "prefijo + sustantivo", "explicacion": "'Macro-' (grande) + 'economía'. Es un tipo de composición culta o prefijación culta."},
                    {"pregunta": "Analiza la formación de 'semanasanta'.", "respuesta": "sustantivo + sustantivo", "explicacion": "'Semana' + 'santa'. Tipo N + N."},
                    {"pregunta": "Analiza la formación de 'aguafiestas'.", "respuesta": "sustantivo + sustantivo", "explicacion": "'Agua' + 'fiestas'. Tipo N + N (con matiz verbal implícito)."},
                    {"pregunta": "Analiza la formación de 'bocata'.", "respuesta": "acortamiento", "explicacion": "'Bocata' es un acortamiento de 'bocadillo'."},
                    {"pregunta": "Analiza la formación de 'moto'.", "respuesta": "acortamiento", "explicacion": "'Moto' es un acortamiento de 'motocicleta'."},
                    {"pregunta": "Analiza la formación de 'foto'.", "respuesta": "acortamiento", "explicacion": "'Foto' es un acortamiento de 'fotografía'."},
                    {"pregunta": "Analiza la formación de 'boli'.", "respuesta": "acortamiento", "explicacion": "'Boli' es un acortamiento de 'bolígrafo'."},
                    {"pregunta": "Analiza la formación de 'cole'.", "respuesta": "acortamiento", "explicacion": "'Cole' es un acortamiento de 'colegio'."},
                    {"pregunta": "Analiza la formación de 'cine'.", "respuesta": "acortamiento", "explicacion": "'Cine' es un acortamiento de 'cinematógrafo'."},
                    {"pregunta": "Analiza la formación de 'tele'.", "respuesta": "acortamiento", "explicacion": "'Tele' es un acortamiento de 'televisión'."},
                    {"pregunta": "Analiza la formación de 'micro'.", "respuesta": "acortamiento", "explicacion": "'Micro' es un acortamiento de 'micrófono' o 'microondas'."},
                    {"pregunta": "Analiza la formación de 'auto'.", "respuesta": "acortamiento", "explicacion": "'Auto' es un acortamiento de 'automóvil'."},
                    {"pregunta": "Analiza la formación de 'bus'.", "respuesta": "acortamiento", "explicacion": "'Bus' es un acortamiento de 'autobús'."},
                    {"pregunta": "Analiza la formación de 'cama'.", "respuesta": "palabra simple", "explicacion": "'Cama' es una palabra simple, sin procesos de composición, derivación o acortamiento evidentes."},
                    {"pregunta": "Analiza la formación de 'sol'.", "respuesta": "palabra simple", "explicacion": "'Sol' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'mesa'.", "respuesta": "palabra simple", "explicacion": "'Mesa' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'flor'.", "respuesta": "palabra simple", "explicacion": "'Flor' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'papel'.", "respuesta": "palabra simple", "explicacion": "'Papel' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'botas'.", "respuesta": "palabra simple", "explicacion": "'Botas' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'agua'.", "respuesta": "palabra simple", "explicacion": "'Agua' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'lata'.", "respuesta": "palabra simple", "explicacion": "'Lata' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'libro'.", "respuesta": "palabra simple", "explicacion": "'Libro' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'verde'.", "respuesta": "palabra simple", "explicacion": "'Verde' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'grande'.", "respuesta": "palabra simple", "explicacion": "'Grande' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'bonito'.", "respuesta": "palabra simple", "explicacion": "'Bonito' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'comer'.", "respuesta": "palabra simple", "explicacion": "'Comer' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'saltar'.", "respuesta": "palabra simple", "explicacion": "'Saltar' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'escribir'.", "respuesta": "palabra simple", "explicacion": "'Escribir' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'blanco'.", "respuesta": "palabra simple", "explicacion": "'Blanco' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'negro'.", "respuesta": "palabra simple", "explicacion": "'Negro' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'rojo'.", "respuesta": "palabra simple", "explicacion": "'Rojo' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'azul'.", "respuesta": "palabra simple", "explicacion": "'Azul' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'amarillo'.", "respuesta": "palabra simple", "explicacion": "'Amarillo' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'casa'.", "respuesta": "palabra simple", "explicacion": "'Casa' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'perro'.", "respuesta": "palabra simple", "explicacion": "'Perro' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'gato'.", "respuesta": "palabra simple", "explicacion": "'Gato' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'ratón'.", "respuesta": "palabra simple", "explicacion": "'Ratón' es una palabra simple."},
                    {"pregunta": "Analiza la formación de 'florero'.", "respuesta": "derivación, sufijación", "explicacion": "Se forma añadiendo el sufijo '-ero' a 'flor'. No es composición."},
                    {"pregunta": "Analiza la formación de 'prever'.", "respuesta": "derivación, prefijación", "explicacion": "Se forma añadiendo el prefijo 'pre-' a 'ver'. No es composición."},
                    {"pregunta": "Analiza la formación de 'ilegal'.", "respuesta": "derivación, prefijación", "explicacion": "Se forma añadiendo el prefijo 'i-' a 'legal'. No es composición."},
                    {"pregunta": "Analiza la formación de 'belleza'.", "respuesta": "derivación, sufijación", "explicacion": "Se forma añadiendo el sufijo '-eza' a 'bello'. No es composición."},
                    {"pregunta": "Analiza la formación de 'cantante'.", "respuesta": "derivación, sufijación", "explicacion": "Se forma añadiendo el sufijo '-ante' a 'cantar'. No es composición."},
                    {"pregunta": "Analiza la formación de 'deshacer'.", "respuesta": "derivación, prefijación", "explicacion": "Se forma añadiendo el prefijo 'des-' a 'hacer'. No es composición."},
                    {"pregunta": "Analiza la formación de 'librería'.", "respuesta": "derivación, sufijación", "explicacion": "Se forma añadiendo el sufijo '-ería' a 'libro'. No es composición."},
                    {"pregunta": "Analiza la formación de 'incapaz'.", "respuesta": "derivación, prefijación", "explicacion": "Se forma añadiendo el prefijo 'in-' a 'capaz'. No es composición."},
                    {"pregunta": "Analiza la formación de 'bondad'.", "respuesta": "derivación, sufijación", "explicacion": "Se forma añadiendo el sufijo '-dad' a 'bueno'. No es composición."},
                    {"pregunta": "Analiza la formación de 'jardinero'.", "respuesta": "derivación, sufijación", "explicacion": "Se forma añadiendo el sufijo '-ero' a 'jardín'. No es composición."}
                ]
            }
        }
    }

def normalizar_respuesta(respuesta):
    """Normaliza una respuesta para comparación (quitar espacios, minúsculas, eliminar tildes, ordenar las partes)."""
    if isinstance(respuesta, str):
        # Eliminar tildes y convertir a minúsculas
        respuesta = respuesta.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        # Dividir por comas, limpiar espacios y ordenar las partes para mayor flexibilidad
        partes = [p.strip() for p in respuesta.split(',') if p.strip()]
        return ', '.join(sorted(partes))
    return respuesta

def comparar_respuestas(respuesta_usuario, respuesta_correcta):
    """Compara la respuesta del usuario con la respuesta correcta después de normalizar."""
    return normalizar_respuesta(respuesta_usuario) == normalizar_respuesta(respuesta_correcta)

def iniciar_practica_composicion_morfologica():
    """Inicia la práctica de composición morfológica en castellano en consola."""
    ejercicios_castellano = cargar_ejercicios_composicion_morfologica()
    
    # Accedemos directamente a los ejercicios de composición morfológica
    ejercicios_composicion = ejercicios_castellano["Morfología"]["Avanzado"]["Composición Morfológica y Estructura"]
    
    if not ejercicios_composicion:
        print("No hay ejercicios de composición morfológica disponibles.")
        return

    random.shuffle(ejercicios_composicion) # Mezclar los ejercicios

    puntuacion = 0
    resultados = []

    print("\n--- ¡Bienvenido a la Práctica de Composición Morfológica en Lengua Castellana! ---")
    print("Para cada palabra, indica el tipo de composición o proceso de formación.")
    print("Tipos de composición común: 'verbo + sustantivo', 'sustantivo + sustantivo', 'adjetivo + adjetivo', 'adverbio + verbo', etc.")
    print("Para los casos especiales de prefijos cultos (origen griego/latino que funcionan como elementos de composición) puedes usar 'prefijo + sustantivo'.")
    print("Si es un acortamiento, indica 'acortamiento'.")
    print("Si no es composición, indica 'palabra simple' o el tipo de derivación (ej: 'derivación, prefijación').")
    print(f"Tienes {len(ejercicios_composicion)} ejercicios para practicar.\n")

    for i, ejercicio in enumerate(ejercicios_composicion):
        print(f"\n--- Ejercicio {i + 1} de {len(ejercicios_composicion)} ---")
        print(f"Palabra: '{ejercicio['pregunta']}'")
        
        respuesta_usuario = input("Tu respuesta (ej: verbo + sustantivo): ").strip()

        es_correcta = comparar_respuestas(respuesta_usuario, ejercicio['respuesta'])

        if es_correcta:
            print("¡Correcto! ✅")
            puntuacion += 1
        else:
            print("Incorrecto. ❌")
        
        print(f"La respuesta correcta era: **{ejercicio['respuesta']}**")
        print(f"Explicación: {ejercicio['explicacion']}")
        
        resultados.append({
            "pregunta": ejercicio['pregunta'],
            "tu_respuesta": respuesta_usuario,
            "correcta": es_correcta,
            "respuesta_correcta": ejercicio['respuesta'],
            "explicacion": ejercicio['explicacion']
        })

    print("\n--- Práctica Terminada ---")
    print(f"Has obtenido {puntuacion} de {len(ejercicios_composicion)} respuestas correctas.")
    print("\n--- Resumen de Resultados ---")
    for res in resultados:
        estado = "✅ CORRECTO" if res['correcta'] else "❌ INCORRECTO"
        print(f"\nPalabra: '{res['pregunta']}'")
        print(f"Tu respuesta: {res['tu_respuesta']}")
        print(f"Respuesta correcta: **{res['respuesta_correcta']}**")
        print(f"Estado: {estado}")
        print(f"Explicación: {res['explicacion']}")
    
    print("\n¡Gracias por practicar!")

if __name__ == "__main__":
    iniciar_practica_composicion_morfologica()
