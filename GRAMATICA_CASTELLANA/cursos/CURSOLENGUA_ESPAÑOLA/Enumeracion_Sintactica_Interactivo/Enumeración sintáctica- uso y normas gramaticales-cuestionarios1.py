import json
import os

def crear_archivos_json():
    preguntas = [
        # Pregunta original
        {
            "pregunta": "¿Dónde van las comas en: 'Compré manzanas peras uvas y naranjas'?",
            "opciones": [
                "A) manzanas, peras, uvas y naranjas",
                "B) manzanas peras, uvas y naranjas"
            ],
            "correcta": "A"
        },

        # 10 nuevas preguntas
        {
            "pregunta": "Selecciona la oración correctamente puntuada:",
            "opciones": [
                "A) Los conferencistas García, López, Martínez y Ruiz hablaron durante horas",
                "B) Los conferencistas, García López, Martínez y Ruiz hablaron durante horas"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "Corrige la enumeración: 'En el taller hay sillas mesas pizarra y proyectores'",
            "opciones": [
                "A) sillas, mesas, pizarra y proyectores",
                "B) sillas mesas, pizarra, y proyectores"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "¿Cuál es el error en: 'Los alumnos, entregaron ensayos trabajos y ejercicios'?",
            "opciones": [
                "A) Coma innecesaria entre sujeto y verbo",
                "B) Falta coma después de 'trabajos'"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "Elige la versión correcta:",
            "opciones": [
                "A) Necesito tela, tijeras, aguja e hilo",
                "B) Necesito tela tijeras, aguja, e hilo"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "Identifica el error de puntuación: 'Visitamos París Londres Roma y Madrid'",
            "opciones": [
                "A) Falta coma después de París y Londres",
                "B) Sobra coma antes de 'y Madrid'"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "Puntuación correcta para: 'El menú incluye sopa pescado arroz postre y café'",
            "opciones": [
                "A) sopa, pescado, arroz, postre y café",
                "B) sopa, pescado arroz, postre y café"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "¿Dónde está el error en: 'María, Pedro y Juan, ganaron el premio'?",
            "opciones": [
                "A) Coma innecesaria después de Juan",
                "B) Falta coma después de Pedro"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "Selecciona la versión correcta:",
            "opciones": [
                "A) Requerimos ingenieros, diseñadores, contadores y abogados",
                "B) Requerimos ingenieros diseñadores, contadores, y abogados"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "Corrige: 'En la caja había libros cuadernos lápices y marcadores'",
            "opciones": [
                "A) libros, cuadernos, lápices y marcadores",
                "B) libros cuadernos, lápices, y marcadores"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "Identifica la oración bien puntuada:",
            "opciones": [
                "A) Los departamentos Quindío, Risaralda, Caldas y Valle conforman la región",
                "B) Los departamentos Quindío Risaralda, Caldas y Valle conforman la región"
            ],
            "correcta": "A"
        },
        {
            "pregunta": "¿Cuál es el error en: 'Los invitados, bailaron comieron y rieron'?",
            "opciones": [
                "A) Coma entre sujeto y verbo",
                "B) Falta coma después de 'bailaron'"
            ],
            "correcta": "A"
        }
    ]

    # ... (resto del código igual)

if __name__ == "__main__":
    crear_archivos_json()
    print("\n¡Archivos actualizados con 10 nuevas preguntas!")
