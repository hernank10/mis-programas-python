import tkinter as tk
from tkinter import messagebox
import random

# --- Definición de las Preguntas (Reutilizamos la misma estructura de datos) ---

# --- Lección 1: Ortografía Básica ---
lesson1_questions = [
    {
        "sentence": "El presidente de [Colombia/colombia] visitó ayer Bogotá.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Colombia", "colombia"],
        "correct_answer": "Colombia",
        "feedback_explanation": "Los nombres de países y ciudades (sustantivos propios) siempre se escriben con mayúscula inicial."
    },
    {
        "sentence": "Mi perro se llama [Max/max].",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Max", "max"],
        "correct_answer": "Max",
        "feedback_explanation": "Los nombres propios de personas o animales se escriben con mayúscula inicial."
    },
    {
        "sentence": "Después de un punto, siempre se escribe con ___.",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "mayúscula",
        "feedback_explanation": "La primera palabra después de un punto y seguido o un punto y aparte siempre comienza con mayúscula."
    },
    {
        "sentence": "El río [Magdalena/magdalena] es muy largo.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Magdalena", "magdalena"],
        "correct_answer": "Magdalena",
        "feedback_explanation": "Los nombres propios geográficos (ríos, montañas, etc.) llevan mayúscula inicial."
    },
    {
        "sentence": "Ella [iba/iva] todos los días al parque.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["iba", "iva"],
        "correct_answer": "iba",
        "feedback_explanation": "El pretérito imperfecto de 'ir' se escribe con 'b'."
    },
    {
        "sentence": "Es un [tubo/tuvo] de metal.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["tubo", "tuvo"],
        "correct_answer": "tubo",
        "feedback_explanation": "'Tubo' es el objeto cilíndrico. 'Tuvo' es del verbo 'tener'."
    },
    {
        "sentence": "Se escribe con B antes de L o ___ (ej: blanco, brazo).",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "R",
        "feedback_explanation": "Las sílabas 'bla, ble, bli, blo, blu' y 'bra, bre, bri, bro, bru' siempre llevan 'b'."
    },
    {
        "sentence": "La [casa/caza] es muy grande.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["casa", "caza"],
        "correct_answer": "casa",
        "feedback_explanation": "'Casa' es una vivienda. 'Caza' es la acción de cazar."
    },
    {
        "sentence": "Me gusta la [cereza/seresa].",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["cereza", "seresa"],
        "correct_answer": "cereza",
        "feedback_explanation": "Después de 'a', 'o', 'u' se usa 'z' (zapato, pozo, azul); antes de 'e', 'i' se usa 'c' (cena, cine)."
    },
    {
        "sentence": "Las palabras terminadas en '-ción' (cuando vienen de verbos terminados en '-ar') se escriben con ___.",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "c",
        "feedback_explanation": "Ejemplo: 'canción' (de cantar), 'oración' (de orar)."
    }
]

# --- Lección 2: Acentuación ---
lesson2_questions = [
    {
        "sentence": "¿Lleva tilde la palabra 'CANCION'?",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Sí, canción", "No, cancion"],
        "correct_answer": "Sí, canción",
        "feedback_explanation": "Las palabras agudas que terminan en 'n', 's' o vocal llevan tilde."
    },
    {
        "sentence": "El niño comió un bombón en el parque. (Escribe la palabra con tilde correctamente)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "bombón",
        "feedback_explanation": "Bombón es aguda y termina en 'n', por lo tanto lleva tilde."
    },
    {
        "sentence": "¿Cómo se clasifica la palabra 'ÁRBOL'?",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Aguda", "Grave", "Esdrújula"],
        "correct_answer": "Grave",
        "feedback_explanation": "Árbol es una palabra grave (llana) que termina en 'l' (no en n, s o vocal), por eso lleva tilde."
    },
    {
        "sentence": "Mi padre es un buen [CANCER/CARACTER]. (Elige la opción correcta para 'personalidad')",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["carácter", "caracter"],
        "correct_answer": "carácter",
        "feedback_explanation": "Carácter es una palabra grave que termina en 'r', por lo tanto lleva tilde."
    },
    {
        "sentence": "La palabra 'MATEMÁTICAS' es una palabra...",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Aguda", "Grave", "Esdrújula"],
        "correct_answer": "Esdrújula",
        "feedback_explanation": "Todas las palabras esdrújulas y sobresdrújulas siempre llevan tilde."
    },
    {
        "sentence": "El [ULTIMO/ÚLTIMO] día de clase.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["ultimo", "último"],
        "correct_answer": "último",
        "feedback_explanation": "Último es una palabra esdrújula y siempre lleva tilde."
    },
    {
        "sentence": "La palabra 'PAIS' forma un hiato. ¿Lleva tilde?",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Sí, país", "No, pais"],
        "correct_answer": "Sí, país",
        "feedback_explanation": "Las vocales débiles (i, u) llevan tilde cuando forman hiato con una vocal fuerte (a, e, o), rompiendo el diptongo."
    },
    {
        "sentence": "La palabra 'CIUDAD' tiene un diptongo. ¿Lleva tilde?",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Sí, ciudad", "No, ciudad"],
        "correct_answer": "No, ciudad",
        "feedback_explanation": "Ciudad es una palabra aguda que termina en 'd', por lo tanto no lleva tilde. El diptongo no se rompe."
    },
    {
        "sentence": "[EL/ÉL] es mi hermano. (Elige la opción correcta)",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["El", "Él"],
        "correct_answer": "Él",
        "feedback_explanation": "'Él' con tilde es pronombre personal. 'El' sin tilde es artículo."
    },
    {
        "sentence": "[TE/TÉ] gusta el té verde. (Escribe la palabra con tilde correctamente que significa 'bebida')",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "té",
        "feedback_explanation": "'Té' con tilde se refiere a la bebida. 'Te' sin tilde es pronombre personal."
    }
]

# --- Lección 3: Transformación de Oraciones ---
lesson3_questions = [
    {
        "instruction": "Transforma la siguiente frase a voz pasiva: 'El perro mordió al cartero.'",
        "correct_answer": "El cartero fue mordido por el perro.",
        "feedback_explanation": "La voz pasiva se forma con el verbo 'ser' conjugado + el participio pasado del verbo principal + 'por' + el agente. Mantén la concordancia."
    },
    {
        "instruction": "Transforma la siguiente frase a singular: 'Las casas son grandes.'",
        "correct_answer": "La casa es grande.",
        "feedback_explanation": "Debes cambiar el sustantivo y el verbo a su forma singular, manteniendo la concordancia."
    },
    {
        "instruction": "Transforma la siguiente frase al futuro simple: 'Ellos comen manzanas.'",
        "correct_answer": "Ellos comerán manzanas.",
        "feedback_explanation": "El futuro simple de los verbos -er e -ir se forma añadiendo -erán o -irán a la raíz."
    },
    {
        "instruction": "Transforma la siguiente frase a forma negativa: 'Ella tiene un coche.'",
        "correct_answer": "Ella no tiene un coche.",
        "feedback_explanation": "Para formar la negación en español, simplemente coloca 'no' antes del verbo conjugado."
    },
    {
        "instruction": "Transforma la siguiente frase de género masculino a femenino: 'El actor es famoso.'",
        "correct_answer": "La actriz es famosa.",
        "feedback_explanation": "Cambia el artículo y el sustantivo a su forma femenina, y asegúrate de que el adjetivo concuerde en género."
    }
]

# --- Lección 4: Redacción de Reglas (Completar Huecos) ---
lesson4_questions = [
    {
        "sentence": "Las palabras agudas llevan tilde cuando terminan en N, S o ___.",
        "correct_answer": "vocal",
        "feedback_explanation": "Ejemplo: 'canción', 'además', 'café'."
    },
    {
        "sentence": "El subjuntivo se usa para expresar deseos, dudas o ___.",
        "correct_answer": "emociones",
        "feedback_explanation": "El modo subjuntivo es clave para expresar subjetividad, irrealidad, deseos, dudas, emociones, etc."
    },
    {
        "sentence": "Cuando dos vocales fuertes (a, e, o) están juntas, forman un ___.",
        "correct_answer": "hiato",
        "feedback_explanation": "Un hiato ocurre cuando dos vocales fuertes están juntas o una vocal fuerte y una débil tónica."
    },
    {
        "sentence": "Los adjetivos deben concordar en género y ___ con el sustantivo que modifican.",
        "correct_answer": "número",
        "feedback_explanation": "Si el sustantivo es femenino plural, el adjetivo también debe serlo (ej. 'las casas grandes')."
    },
    {
        "sentence": "Se utiliza 'qué' con tilde para preguntas o ___.",
        "correct_answer": "exclamaciones",
        "feedback_explanation": "Los pronombres y adverbios interrogativos y exclamativos (qué, quién, cómo, cuándo, dónde, etc.) llevan tilde."
    }
]

# --- Lección 5: Redacción de Reglas (Ejemplo) ---
lesson5_questions = [
    {
        "rule_template": "La regla es: Las palabras graves (llanas) llevan tilde cuando NO terminan en N, S o vocal. Escribe un ejemplo de una palabra grave con tilde.",
        "correct_answer": "árbol", # Esto es solo un ejemplo de referencia
        "feedback_explanation": "Otros ejemplos: 'difícil', 'ángel', 'césped'.",
        "example_check": lambda answer: answer.lower() in ["árbol", "dificil", "ángel", "cesped"]
    },
    {
        "rule_template": "La regla es: El verbo 'ir' en pretérito imperfecto de indicativo se escribe con 'b'. Escribe la conjugación para 'yo'.",
        "correct_answer": "iba",
        "feedback_explanation": "La conjugación es 'yo iba, tú ibas, él/ella/usted iba, nosotros/as íbamos, vosotros/as ibais, ellos/as/ustedes iban'."
    },
    {
        "rule_template": "La regla es: Se usa 'porque' (junto) para la conjunción causal (para responder '¿por qué?'). Escribe una frase de respuesta usando 'porque'.",
        "correct_answer": "Porque tengo frío.",
        "feedback_explanation": "Ejemplo: 'No voy al parque porque tengo que estudiar.' Es la forma para dar una razón.",
        "example_check": lambda answer: "porque" in answer.lower() and len(answer.split()) > 2
    },
    {
        "rule_template": "La regla es: El pretérito pluscuamperfecto se forma con el imperfecto de 'haber' + el participio del verbo principal. Escribe una frase usando el pluscuamperfecto con 'nosotros' del verbo 'comer'.",
        "correct_answer": "Habíamos comido.",
        "feedback_explanation": "Ejemplo: 'Cuando llegó, ya habíamos comido.'",
        "example_check": lambda answer: "habíamos" in answer.lower() and "comido" in answer.lower()
    },
    {
        "rule_template": "La regla es: El gerundio de los verbos terminados en -er/-ir se forma con -iendo. Escribe el gerundio del verbo 'dormir'.",
        "correct_answer": "durmiendo",
        "feedback_explanation": "Recuerda que 'dormir' es irregular en el gerundio (oír -> oyendo, leer -> leyendo, etc.)."
    }
]

# --- Lección 6: Uso de Ser y Estar ---
lesson6_questions = [
    {
        "sentence": "Ella [ser/estar] de Colombia.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Usamos 'ser' para origen o nacionalidad (característica permanente)."
    },
    {
        "sentence": "Yo [ser/estar] cansado hoy.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["soy", "estoy"],
        "correct_answer": "estoy",
        "feedback_explanation": "Usamos 'estar' para estados temporales o condición física/emocional."
    },
    {
        "sentence": "La manzana [ser/estar] verde (color).",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Usamos 'ser' para características inherentes o permanentes (el color natural)."
    },
    {
        "sentence": "La manzana [ser/estar] verde (no madura).",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["es", "está"],
        "correct_answer": "está",
        "feedback_explanation": "Usamos 'estar' para un estado temporal o condición (madurez de una fruta)."
    },
    {
        "sentence": "Mi padre [ser/estar] médico.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Usamos 'ser' para profesiones u ocupaciones."
    },
    {
        "sentence": "La reunión [ser/estar] en la sala grande.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Aunque parezca ubicación, se usa 'ser' para eventos, reuniones, fiestas, etc., indicando dónde 'tienen lugar'."
    },
    {
        "sentence": "Yo [ser/estar] en casa ahora.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["soy", "estoy"],
        "correct_answer": "estoy",
        "feedback_explanation": "Usamos 'estar' para ubicación física."
    },
    {
        "sentence": "El café [ser/estar] caliente.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["es", "está"],
        "correct_answer": "está",
        "feedback_explanation": "Usamos 'estar' para describir una condición o estado temporal (temperatura, que puede cambiar)."
    },
    {
        "sentence": "El libro [ser/estar] interesante.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Usamos 'ser' para cualidades intrínsecas o permanentes (una característica del libro)."
    },
    {
        "sentence": "La puerta [ser/estar] abierta.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["es", "está"],
        "correct_answer": "está",
        "feedback_explanation": "Usamos 'estar' para un estado resultante de una acción o una condición temporal (la puerta puede cerrarse)."
    }
]

# --- Lección 7: Pretérito Perfecto Simple vs. Imperfecto ---
lesson7_questions = [
    {
        "sentence": "Ayer yo ___ a mis abuelos. (visitar)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "visité",
        "feedback_explanation": "Se usa el pretérito perfecto simple para acciones terminadas en un momento específico del pasado ('ayer')."
    },
    {
        "sentence": "El año pasado, ellos ___ una casa nueva. (comprar)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "compraron",
        "feedback_explanation": "Se usa el pretérito perfecto simple para acciones terminadas en un periodo específico del pasado ('el año pasado')."
    },
    {
        "sentence": "Ella ___ en 1990. (nacer)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "nació",
        "feedback_explanation": "Se usa el pretérito perfecto simple para eventos puntuales en el pasado."
    },
    {
        "sentence": "Cuando ___ niño, siempre ___ en el parque. (ser, jugar)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "era, jugaba",
        "feedback_explanation": "Se usa el pretérito imperfecto para describir acciones habituales o repetidas en el pasado ('cuando era niño', 'siempre')."
    },
    {
        "sentence": "Mientras yo ___, mi hermana ___ música. (leer, escuchar)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "leía, escuchaba",
        "feedback_explanation": "Se usa el pretérito imperfecto para describir acciones simultáneas o en progreso en el pasado ('mientras')."
    },
    {
        "sentence": "La casa ___ un jardín grande y ___ muy bonita. (tener, ser)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "tenía, era",
        "feedback_explanation": "Se usa el pretérito imperfecto para descripciones en el pasado (características, estados)."
    },
    {
        "sentence": "Ayer, [fui/iba] al supermercado y [compré/compraba] pan.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["fui, compré", "iba, compraba", "fui, compraba", "iba, compré"],
        "correct_answer": "fui, compré",
        "feedback_explanation": "Ambas son acciones terminadas y puntuales en el pasado ('ayer')."
    },
    {
        "sentence": "Cuando [era/fui] joven, [vivía/viví] en Barcelona.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["era, vivía", "fui, viví", "era, viví", "fui, vivía"],
        "correct_answer": "era, vivía",
        "feedback_explanation": "'Era' describe una etapa de la vida (imperfecto). 'Vivía' describe una acción habitual o un estado prolongado en el pasado."
    },
    {
        "sentence": "De repente, [empezó/empezaba] a llover mientras [caminaba/caminó] por la calle.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["empezó, caminaba", "empezaba, caminó", "empezó, caminó", "empezaba, caminaba"],
        "correct_answer": "empezó, caminaba",
        "feedback_explanation": "'Empezó' es una acción puntual e inesperada (simple). 'Caminaba' es una acción en progreso que fue interrumpida (imperfecto)."
    },
    {
        "sentence": "Ella [estudió/estudiaba] medicina cuando [conoció/conocía] a su esposo.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["estudió, conoció", "estudiaba, conocía", "estudiaba, conoció", "estudió, conocía"],
        "correct_answer": "estudiaba, conoció",
        "feedback_explanation": "'Estudiaba' describe una acción en progreso o habitual en el pasado (imperfecto). 'Conoció' es una acción puntual que interrumpió o ocurrió durante la otra (simple)."
    }
]

# --- Lección 8: Usos de "Haber" y "Hacer" ---
lesson8_questions = [
    {
        "sentence": "En la fiesta [hubo/hubieron] mucha gente.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["hubo", "hubieron"],
        "correct_answer": "hubo",
        "feedback_explanation": "El verbo 'haber' para indicar existencia es impersonal y siempre se usa en singular: 'Hay', 'Había', 'Hubo', 'Habrá'."
    },
    {
        "sentence": "[Hay/Han] muchos libros en la biblioteca.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Hay", "Han"],
        "correct_answer": "Hay",
        "feedback_explanation": "'Hay' es la forma impersonal de 'haber' y se usa para indicar existencia. 'Han' es del verbo 'haber' como auxiliar de tiempos compuestos."
    },
    {
        "sentence": "En ese lugar no ___ problemas. (haber, en pasado, indicar existencia)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "había",
        "feedback_explanation": "Para indicar existencia en pasado (imperf.), se usa 'había'."
    },
    {
        "sentence": "Ellos ___ comido ya. (haber, en presente)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "han",
        "feedback_explanation": "'Han' es la forma del verbo 'haber' que se usa como auxiliar para formar tiempos compuestos (ej. 'han comido', 'han visto')."
    },
    {
        "sentence": "Yo ___ visto esa película antes. (haber, en presente)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "he",
        "feedback_explanation": "'He' es la forma correcta del verbo 'haber' en primera persona singular del presente para formar el pretérito perfecto compuesto."
    },
    {
        "sentence": "Nosotros ___ estudiado mucho para el examen. (haber, en pretérito pluscuamperfecto)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "habíamos",
        "feedback_explanation": "El pretérito pluscuamperfecto se forma con el imperfecto de 'haber' + participio. Para 'nosotros' es 'habíamos'."
    },
    {
        "sentence": "[Hace/Hacen] dos años que no la veo.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Hace", "Hacen"],
        "correct_answer": "Hace",
        "feedback_explanation": "Para expresar duración de tiempo, el verbo 'hacer' en estas construcciones es siempre impersonal y se usa en singular: 'Hace'."
    },
    {
        "sentence": "[Hizo/Hacía] mucho calor cuando estuvimos de vacaciones.",
        "question_type": "SELECCION_MULTIPLE",
        "options": ["Hizo", "Hacía"],
        "correct_answer": "Hacía",
        "feedback_explanation": "Para describir condiciones climáticas en el pasado (que son duraderas o habituales), se usa el imperfecto de 'hacer'."
    },
    {
        "sentence": "___ diez minutos que salió. (Hacer, en presente)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "Hace",
        "feedback_explanation": "Para indicar un punto de partida en el pasado, se usa 'hace' seguido del tiempo transcurrido."
    },
    {
        "sentence": "Siempre ___ frío en invierno en esa ciudad. (hacer, en imperfecto)",
        "question_type": "COMPLETAR_HUECO",
        "correct_answer": "hacía",
        "feedback_explanation": "Para describir condiciones habituales o repetidas en el pasado, se usa el imperfecto de 'hacer'."
    }
]


# Diccionario que mapea los números de lección a sus preguntas
all_lessons_questions = {
    1: lesson1_questions,
    2: lesson2_questions,
    3: lesson3_questions,
    4: lesson4_questions,
    5: lesson5_questions,
    6: lesson6_questions,
    7: lesson7_questions,
    8: lesson8_questions,
}

lesson_titles = {
    1: "Ortografía Básica 📚",
    2: "Acentuación ✨",
    3: "Transformación de Oraciones 🔄",
    4: "Redacción de Reglas (Completar Huecos) ✍️",
    5: "Redacción de Reglas (Ejemplo) 🧠",
    6: "Uso de Ser y Estar 🇪🇸",
    7: "Pretérito Simple vs. Imperfecto 🕰️",
    8: "Usos de \"Haber\" y \"Hacer\" 💡",
}


class SpanishLessonsApp:
    def __init__(self, master):
        self.master = master
        master.title("Programa de Lecciones de Castellano")
        master.geometry("800x600") # Tamaño de la ventana

        self.current_lesson_number = None
        self.current_questions = []
        self.current_question_index = 0
        self.score = 0

        self.create_main_menu()

    def clear_frame(self):
        # Limpia todos los widgets del frame actual
        for widget in self.master.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        self.clear_frame()

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        main_frame = tk.Frame(self.master, padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_rowconfigure(0, weight=1)
        for i in range(len(lesson_titles) + 2): # +2 for title and exit
            main_frame.grid_rowconfigure(i, weight=0)
        main_frame.grid_columnconfigure(0, weight=1)


        tk.Label(main_frame, text="--- Programa de Lecciones de Castellano ---", font=("Arial", 18, "bold"), fg="#0056b3").pack(pady=20)

        for lesson_num, lesson_title in lesson_titles.items():
            btn = tk.Button(main_frame, text=f"Lección {lesson_num}: {lesson_title}",
                            command=lambda num=lesson_num: self.start_lesson(num),
                            font=("Arial", 12), bg="#4CAF50", fg="white",
                            padx=10, pady=5, relief="raised")
            btn.pack(pady=5, fill="x", ipadx=50)

        tk.Button(main_frame, text="Salir", command=self.master.quit,
                  font=("Arial", 12), bg="#dc3545", fg="white",
                  padx=10, pady=5, relief="raised").pack(pady=20, fill="x", ipadx=50)

    def start_lesson(self, lesson_number):
        self.current_lesson_number = lesson_number
        self.current_questions = list(all_lessons_questions.get(lesson_number, []))
        random.shuffle(self.current_questions) # Mezclar preguntas
        self.current_question_index = 0
        self.score = 0

        if not self.current_questions:
            messagebox.showinfo("Lección No Disponible", f"La Lección {lesson_number} aún no tiene contenido. ¡Pronto estará aquí!")
            return

        self.show_lesson_intro()

    def show_lesson_intro(self):
        self.clear_frame()
        title = lesson_titles.get(self.current_lesson_number, f"Lección {self.current_lesson_number} (Sin Título)")

        intro_frame = tk.Frame(self.master, padx=20, pady=20)
        intro_frame.pack(expand=True, fill="both")

        tk.Label(intro_frame, text=f"--- {title} ---", font=("Arial", 18, "bold"), fg="#0056b3").pack(pady=10)

        intro_text = ""
        if self.current_lesson_number == 1:
            intro_text = "Aquí repasaremos y practicaremos las reglas esenciales de mayúsculas y el uso correcto de letras que a menudo se confunden."
        elif self.current_lesson_number == 2:
            intro_text = "Dominar las tildes es clave para leer y escribir correctamente en español. Aquí practicaremos las reglas de palabras agudas, graves, esdrújulas, y los casos especiales."
        elif self.current_lesson_number == 3:
            intro_text = "En esta lección, te desafiaremos a transformar oraciones, un ejercicio clave para comprender la estructura gramatical del español."
        elif self.current_lesson_number == 4:
            intro_text = "Aprenderás a formular y completar reglas gramaticales, afianzando tu conocimiento teórico del idioma."
        elif self.current_lesson_number == 5:
            intro_text = "Aquí, no solo identificarás reglas, sino que también las aplicarás creando tus propios ejemplos."
        elif self.current_lesson_number == 6:
            intro_text = "Uno de los mayores desafíos en español es el uso de 'ser' y 'estar'. ¡Aquí lo dominarás!"
        elif self.current_lesson_number == 7:
            intro_text = "Estos dos tiempos verbales se usan para hablar del pasado, pero con diferencias clave. Aprenderás a distinguirlos para narrar eventos y describir situaciones con precisión."
        elif self.current_lesson_number == 8:
            intro_text = "Estos verbos son esenciales y a menudo generan dudas. Aprenderás a usar 'haber' correctamente para indicar existencia y formar tiempos compuestos, y 'hacer' para hablar del tiempo. ¡Domina estos verbos y eleva tu español!"
        else:
             intro_text = "¡Bienvenido a esta lección interactiva!"


        tk.Label(intro_frame, text=intro_text, font=("Arial", 12), wraplength=700, justify="center").pack(pady=20)
        tk.Button(intro_frame, text="Iniciar Ejercicios 📝", command=self.show_question,
                  font=("Arial", 12), bg="#007bff", fg="white", padx=15, pady=8, relief="raised").pack(pady=10)

    def show_question(self):
        self.clear_frame()
        if self.current_question_index >= len(self.current_questions):
            self.show_lesson_results()
            return

        question_data = self.current_questions[self.current_question_index]
        question_frame = tk.Frame(self.master, padx=20, pady=20)
        question_frame.pack(expand=True, fill="both")

        tk.Label(question_frame, text=f"Pregunta {self.current_question_index + 1} de {len(self.current_questions)}",
                 font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(question_frame, text=question_data["sentence"], font=("Arial", 14), wraplength=700, justify="center").pack(pady=15)

        self.feedback_label = tk.Label(question_frame, text="", font=("Arial", 12, "bold"), pady=10)
        self.feedback_label.pack(pady=5)

        self.user_input_widget = None # Para Entry
        self.radio_var = tk.StringVar() # Para Radiobuttons

        if question_data["question_type"] == "SELECCION_MULTIPLE":
            options_frame = tk.Frame(question_frame)
            options_frame.pack(pady=10)
            for option in question_data["options"]:
                rb = tk.Radiobutton(options_frame, text=option, variable=self.radio_var, value=option,
                                    font=("Arial", 12), command=self.enable_check_button)
                rb.pack(anchor="w")
            self.radio_var.set("") # Resetear selección

        elif question_data["question_type"] == "COMPLETAR_HUECO":
            self.user_input_widget = tk.Entry(question_frame, font=("Arial", 14), width=50)
            self.user_input_widget.pack(pady=10)
            self.user_input_widget.bind("<KeyRelease>", self.enable_check_button_entry)
            self.user_input_widget.focus_set() # Poner el foco en el campo de entrada

        # Specific handling for Lesson 3 and 5 questions if they have a custom instruction/template
        elif self.current_lesson_number == 3 and "instruction" in question_data:
            tk.Label(question_frame, text=question_data["instruction"], font=("Arial", 14), wraplength=700, justify="center").pack(pady=15)
            self.user_input_widget = tk.Entry(question_frame, font=("Arial", 14), width=50)
            self.user_input_widget.pack(pady=10)
            self.user_input_widget.bind("<KeyRelease>", self.enable_check_button_entry)
            self.user_input_widget.focus_set()

        elif self.current_lesson_number == 5 and "rule_template" in question_data:
            tk.Label(question_frame, text=question_data["rule_template"], font=("Arial", 14), wraplength=700, justify="center").pack(pady=15)
            self.user_input_widget = tk.Entry(question_frame, font=("Arial", 14), width=50)
            self.user_input_widget.pack(pady=10)
            self.user_input_widget.bind("<KeyRelease>", self.enable_check_button_entry)
            self.user_input_widget.focus_set()


        self.check_button = tk.Button(question_frame, text="Verificar Respuesta ✅",
                                       command=self.check_answer, state=tk.DISABLED,
                                       font=("Arial", 12), bg="#28a745", fg="white", padx=15, pady=8)
        self.check_button.pack(pady=10)

        self.next_button = tk.Button(question_frame, text="Siguiente Pregunta ➡️",
                                      command=self.next_question, state=tk.DISABLED,
                                      font=("Arial", 12), bg="#007bff", fg="white", padx=15, pady=8)
        self.next_button.pack(pady=5)

        self.score_label = tk.Label(question_frame, text=f"Puntuación: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Inicialmente deshabilitar el botón de verificar si no hay entrada
        if question_data["question_type"] == "SELECCION_MULTIPLE":
            self.check_button.config(state=tk.DISABLED)
        elif question_data["question_type"] == "COMPLETAR_HUECO" or self.current_lesson_number in [3, 5]:
             self.check_button.config(state=tk.DISABLED)


    def enable_check_button(self):
        # Para Radiobuttons
        if self.radio_var.get():
            self.check_button.config(state=tk.NORMAL)
        else:
            self.check_button.config(state=tk.DISABLED)

    def enable_check_button_entry(self, event=None):
        # Para Entry
        if self.user_input_widget.get().strip():
            self.check_button.config(state=tk.NORMAL)
        else:
            self.check_button.config(state=tk.DISABLED)


    def check_answer(self):
        question_data = self.current_questions[self.current_question_index]
        user_answer = ""
        is_correct = False

        if question_data["question_type"] == "SELECCION_MULTIPLE":
            user_answer = self.radio_var.get()
            is_correct = (user_answer == question_data["correct_answer"])
        elif question_data["question_type"] == "COMPLETAR_HUECO":
            user_answer = self.user_input_widget.get().strip()
            is_correct = (user_answer.lower() == question_data["correct_answer"].lower())
        elif self.current_lesson_number == 3: # Lógica para Lección 3
            user_answer = self.user_input_widget.get().strip()
            is_correct = (user_answer.lower() == question_data["correct_answer"].lower())
        elif self.current_lesson_number == 5: # Lógica para Lección 5
            user_answer = self.user_input_widget.get().strip()
            if "example_check" in question_data and callable(question_data["example_check"]):
                is_correct = question_data["example_check"](user_answer)
            else:
                is_correct = (user_answer.lower() == question_data["correct_answer"].lower())


        if is_correct:
            self.score += 10
            feedback_text = f"¡Correcto! ✅ {question_data['feedback_explanation']}"
            feedback_color = "green"
        else:
            feedback_text = f"Incorrecto. ❌ La respuesta correcta es '{question_data['correct_answer']}'. {question_data['feedback_explanation']}"
            feedback_color = "red"

        self.feedback_label.config(text=feedback_text, fg=feedback_color)
        self.score_label.config(text=f"Puntuación: {self.score} / {(self.current_question_index + 1) * 10}")

        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

        # Deshabilitar las opciones de entrada/radiobuttons después de verificar
        if self.user_input_widget:
            self.user_input_widget.config(state=tk.DISABLED)
        else: # Deshabilitar radiobuttons
            for child in self.feedback_label.winfo_parent().winfo_children():
                if isinstance(child, tk.Frame): # Find the frame with radiobuttons
                    for rb_widget in child.winfo_children():
                        if isinstance(rb_widget, tk.Radiobutton):
                            rb_widget.config(state=tk.DISABLED)


    def next_question(self):
        self.current_question_index += 1
        self.show_question()

    def show_lesson_results(self):
        self.clear_frame()

        results_frame = tk.Frame(self.master, padx=20, pady=20)
        results_frame.pack(expand=True, fill="both")

        total_possible_score = len(self.current_questions) * 10

        tk.Label(results_frame, text=f"--- ¡Lección {self.current_lesson_number} Completada! ---",
                 font=("Arial", 18, "bold"), fg="#0056b3").pack(pady=20)

        message = f"Tu puntuación final es: {self.score} de {total_possible_score} puntos."
        tk.Label(results_frame, text=message, font=("Arial", 14)).pack(pady=10)

        motivational_message = ""
        if self.score == total_possible_score:
            motivational_message = "¡Felicidades! Has dominado esta lección a la perfección. ¡Eres un experto! ⭐⭐⭐"
        elif self.score >= total_possible_score * 0.7:
            motivational_message = "¡Muy bien! Estás dominando las reglas. ¡Sigue así! 👍"
        else:
            motivational_message = "¡Buen intento! Repasa las reglas y vuelve a intentarlo. ¡La práctica te hará un experto! 💪"

        tk.Label(results_frame, text=motivational_message, font=("Arial", 12), wraplength=700, justify="center").pack(pady=20)

        tk.Button(results_frame, text="Volver a Intentar Lección", command=lambda: self.start_lesson(self.current_lesson_number),
                  font=("Arial", 12), bg="#ffc107", fg="black", padx=15, pady=8, relief="raised").pack(pady=10)
        tk.Button(results_frame, text="Volver al Menú Principal", command=self.create_main_menu,
                  font=("Arial", 12), bg="#6c757d", fg="white", padx=15, pady=8, relief="raised").pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpanishLessonsApp(root)
    root.mainloop()
