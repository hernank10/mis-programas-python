# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Lengua Española con interfaz gráfica (Tkinter)
# Inspirado en el "Diccionario de Construcción y Régimen de la Lengua Castellana" de R.J. Cuervo.
#
# Este programa presenta una serie de ejercicios interactivos en una ventana de Tkinter.

import tkinter as tk
from tkinter import messagebox
import random

class CuervoApp:
    def __init__(self, master):
        """Inicializa la aplicación Tkinter."""
        self.master = master
        master.title("R.J. Cuervo: Gramática y Lengua")
        master.geometry("600x400")
        master.resizable(False, False)

        # Configuración de los ejercicios
        self.ejercicios = {
            1: ("Un saludo 'bien bacano'", "Escribe un saludo 'bien bacano' (ej: ¡Qué más, [nombre]! ¿Todo bien o qué?)", "¡Qué más, [nombre]! ¿Todo bien o qué?"),
            2: ("El 'parche' de amigos", "Tienes una lista de amigos. Agrega dos nuevos (ej: 'Sofía', 'Carlos').", "['Juan', 'María', 'Pedro', 'Sofía', 'Carlos']"),
            3: ("Arepa con queso", "Si cada arepa cuesta 2500 COP, ¿cuál es el costo de 3 arepas?", "7500"),
            4: ("Manejar el cambio", "Un producto cuesta 12000 COP y pagas con 20000. ¿Cuál es el cambio?", "8000"),
            5: ("El 'guayabo'", "Si te acuestas tarde y tienes dolor de cabeza, ¿cuál es el resultado?", "guayabo"),
            6: ("El 'achaque' de la palabra", "Escribe el significado de 'achaque' (sentido figurado).", "pretexto"),
            7: ("'Dizque' la sinonimia", "Usa la palabra 'dizque' en una oración.", "Dizque va a llover."),
            8: ("¿'Por' o 'Para'?", "Completa: 'Este regalo es ... mi mamá.'", "para"),
            9: ("El error de bulto", "Corrige la palabra mal escrita: 'haiga'.", "haya"),
            10: ("Etimología de 'guaricha'", "Escribe el origen de la palabra 'guaricha'.", "chibcha"),
            11: ("'Afecto' vs. 'Efecto'", "Completa: 'El ... del calor es el vapor.'", "efecto"),
            12: ("La conjugación de 'haber'", "Completa: '... muchos carros en la calle.'", "hay"),
            13: ("Concordancia verbal", "Completa: 'El carro y la moto ... en la autopista.'", "corren"),
            14: ("La coma vocativa", "Corrige: 'Hola Juan como estas?'", "Hola, Juan, ¿cómo estás?"),
            15: ("La 'ñapa'", "Usa la palabra 'ñapa' en una oración.", "Dame la ñapa."),
            16: ("Palabras compuestas", "Forma una palabra compuesta con 'rompe'.", "rompecabezas"),
            17: ("Acentos diacríticos", "Completa: '... es el mejor.'", "él"),
            18: ("'Hacer el oso'", "Escribe una oración con 'hacer el oso'.", "Hice el oso en la fiesta."),
            19: ("Uso de mayúsculas", "Corrige: 'La ciudad de Bogota.'", "La ciudad de Bogotá."),
            20: ("El refrán", "Completa: 'Al que madruga...' ", "Dios le ayuda."),
            21: ("Ser o Estar", "Completa: 'El café ... caliente.'", "está"),
            22: ("Ser para profesiones", "Completa: 'Mi padre ... médico.'", "es"),
            23: ("Estar para localización", "Completa: 'Juan ... en la casa.'", "está"),
            24: ("Ser/Estar con adjetivos", "Completa: 'La manzana ... verde (color).'", "es"),
            25: ("Ser con hora y fecha", "Completa: 'Hoy ... 15 de marzo.'", "es"),
            26: ("Estar con ánimo", "Completa: 'Mi amigo ... muy feliz.'", "está"),
            27: ("Ser con nacionalidad", "Completa: 'Ella ... colombiana.'", "es"),
            28: ("Ser para origen", "Completa: 'Los estudiantes ... de Cali.'", "son"),
            29: ("Estar para condición", "Completa: 'Yo ... cansado.'", "estoy"),
            30: ("Ser/Estar en pasado", "Completa: 'Ayer, yo ... en la biblioteca.'", "estaba"),
            31: ("Uso de la coma", "Corrige: 'Compre frutas leche y pan.'", "Compré frutas, leche y pan."),
            32: ("Coma vocativa", "Corrige: 'Buenos días papa.'", "Buenos días, papá."),
            33: ("Punto y coma", "Completa con un punto y coma: 'El cielo está nublado... parece que va a llover.'", "El cielo está nublado; parece que va a llover."),
            34: ("Puntos suspensivos", "Completa: 'No sé qué decir...' ", "No sé qué decir..."),
            35: ("Dos puntos", "Completa: 'Mis colores favoritos son:...' ", "Mis colores favoritos son: azul, verde y rojo."),
            36: ("Comillas", "Cita a tu madre: 'El que mucho abarca, poco aprieta.'", "El que mucho abarca, poco aprieta."),
            37: ("Signos de interrogación", "Escribe una pregunta simple.", "¿Cómo estás?"),
            38: ("Signos de exclamación", "Escribe una exclamación.", "¡Qué sorpresa!"),
            39: ("Paréntesis", "Añade un paréntesis: 'El río Magdalena es el más largo de Colombia.'", "El río Magdalena (el más largo de Colombia)."),
            40: ("Guion largo", "Escribe un diálogo con guion largo.", "—¿Cómo estás? —Bien."),
            41: ("Concordancia adjetivo", "Completa: 'La casa ... (rojo).' ", "roja"),
            42: ("Género de sustantivos", "Completa: '... agua.' ", "el"),
            43: ("Concordancia verbal", "Completa: 'El libro y la revista ... interesantes.' ", "son"),
            44: ("Género y plural", "Escribe el plural de 'el lápiz'.", "los lápices"),
            45: ("Concordancia con números", "Completa: 'Veinte ... (día) de febrero.' ", "días"),
            46: ("Pronombres personales", "Sustituye 'Juan y yo' por un pronombre.", "Nosotros"),
            47: ("Concordancia con varios sustantivos", "Completa: 'El libro y la revista son ... (interesante).'", "interesantes"),
            48: ("Género de nombres", "Completa: '... Madrid.' ", "el"),
            49: ("Plural de 'z'", "Escribe el plural de 'pez'.", "peces"),
            50: ("Concordancia pronominal", "Sustituye 'a María' por un pronombre: 'Vi a María en el cine.'", "la vi"),
            51: ("Preposición 'a'", "Completa: 'Voy ... la escuela.' ", "a"),
            52: ("Preposición 'de'", "Completa: 'Soy ... Colombia.' ", "de"),
            53: ("Preposición 'con'", "Completa: 'Fui al cine ... mis amigos.' ", "con"),
            54: ("Preposición 'en'", "Completa: 'El libro está ... la mesa.' ", "en"),
            55: ("Preposición 'para'", "Completa: 'Estudio ... mi examen.' ", "para"),
            56: ("Preposición 'por'", "Completa: 'Lo hice ... ti.' ", "por"),
            57: ("Preposición 'entre'", "Completa: 'La tienda abre ... 8 a.m. y 6 p.m.' ", "entre"),
            58: ("Preposición 'sin'", "Completa: 'No puedo ver ... mis gafas.' ", "sin"),
            59: ("Preposición 'sobre'", "Completa: 'El libro está ... la mesa.' ", "sobre"),
            60: ("Preposición 'hasta'", "Completa: 'Corrí ... el final de la calle.' ", "hasta"),
            61: ("'Sino' vs. 'si no'", "Completa: 'No es blanco, ... negro.' ", "sino"),
            62: ("'Porque' vs. 'por qué'", "Completa: '¿... no fuiste?' ", "por qué"),
            63: ("'También' vs. 'tan bien'", "Completa: 'Cantas ... que me emocionas.' ", "tan bien"),
            64: ("'Adonde' vs. 'a donde'", "Completa: 'No sé ... vamos.' ", "a dónde"),
            65: ("'Demás' vs. 'de más'", "Completa: 'Los ... no vinieron.' ", "demás"),
            66: ("'Asimismo' vs. 'a sí mismo'", "Completa: 'Se habla ... cuando está solo.' ", "a sí mismo"),
            67: ("'Conque', 'con que', 'con qué'", "Completa: '¿... dinero compraste eso?' ", "con qué"),
            68: ("'Haber' vs. 'a ver'", "Completa: 'Tiene que ... un error.' ", "haber"),
            69: ("'Acerca de' vs. 'a cerca de'", "Completa: 'Hablamos ... la película.' ", "acerca de"),
            70: ("'Porvenir' vs. 'por venir'", "Completa: 'El ... es incierto.' ", "porvenir"),
            71: ("Leísmo vs Loísmo", "Corrige la frase: 'Le vi a Juan.' ", "Lo vi a Juan."),
            72: ("Leísmo de cortesía", "Completa: 'A su padre, ... respeto mucho.' ", "le"),
            73: ("Laísmo", "Completa: 'A mi hermana, ... vi en el parque.' ", "la"),
            74: ("Loísmo", "Corrige: 'A mi hermano, le vi.' ", "Lo vi."),
            75: ("Pronombre O.D.", "Sustituye 'la camisa': 'Compré la camisa.' ", "La compré."),
            76: ("Pronombre O.I.", "Sustituye 'a María': 'Di el libro a María.' ", "Le di el libro."),
            77: ("Combinación de pronombres", "Combina: 'Di el libro a Juan.' ", "Se lo di."),
            78: ("Leísmo plural", "Corrige: 'A los niños, les vi.' ", "Los vi."),
            79: ("Laísmo plural", "Completa: 'A las niñas, ... vi.' ", "las"),
            80: ("Loísmo plural", "Corrige: 'A mis amigos, los compré un regalo.' ", "Les compré un regalo."),
            81: ("Arcaísmo 'doquier'", "Usa la palabra 'doquier'.", "Voy doquier."),
            82: ("Arcaísmo 'empero'", "Usa la palabra 'empero'.", "Empero, no voy."),
            83: ("Arcaísmo 'maguer'", "Usa la palabra 'maguer'.", "Maguer el sol, salí."),
            84: ("Arcaísmo 'enderezar'", "Usa 'enderezar' en su sentido antiguo.", "Enderezó el rumbo."),
            85: ("Arcaísmo 'cuita'", "Usa la palabra 'cuita'.", "Sentía una gran cuita."),
            86: ("Arcaísmo 'encono'", "Usa la palabra 'encono'.", "Su encono era profundo."),
            87: ("Arcaísmo 'caduco'", "Usa la palabra 'caduco'.", "El reloj es caduco."),
            88: ("'A sabiendas de'", "Usa 'a sabiendas de' en una oración.", "Lo hizo a sabiendas de todo."),
            89: ("'Verbigracia'", "Usa la palabra 'verbigracia'.", "Verbigracia, el perro."),
            90: ("Arcaísmo 'crespo'", "Usa 'crespo' con sentido de ira.", "Se puso crespo."),
            91: ("Dicho: 'no dar papaya'", "Explica 'no dar papaya' y úsalo.", "No des papaya."),
            92: ("Dicho: 'mamando gallo'", "Explica 'estar mamando gallo' y úsalo.", "Estás mamando gallo."),
            93: ("Dicho: 'agarrar el palo'", "Explica 'agarrar el palo' y úsalo.", "Agarré el palo rápido."),
            94: ("Dicho: 'tener la pata mala'", "Explica 'tener la pata mala' y úsalo.", "Tengo la pata mala hoy."),
            95: ("Refrán: 'Al mal tiempo...' ", "Completa: 'Al mal tiempo, ...'", "buena cara."),
            96: ("Refrán: 'Más vale tarde...' ", "Completa: 'Más vale tarde que ...'", "nunca"),
            97: ("Refrán: 'No hay mal...' ", "Completa: 'No hay mal que por bien no ...'", "venga"),
            98: ("Refrán: 'A quien madruga...' ", "Completa: 'A quien madruga, ...'", "Dios le ayuda."),
            99: ("Refrán: 'El que mucho abarca...' ", "Completa: 'El que mucho abarca, poco ...'", "aprieta"),
            100: ("Refrán: 'Más sabe el diablo...' ", "Completa: 'Más sabe el diablo por viejo ...'", "que por diablo"),
        }
        
        # Variables de estado
        self.numero_ejercicio_actual = random.randint(1, 100)
        self.ejercicio_actual = self.ejercicios.get(self.numero_ejercicio_actual)
        
        # Widgets de la interfaz
        self.title_label = tk.Label(master, text="¡Pilas con la Lengua!", font=("Helvetica", 16, "bold"), fg="#004D40")
        self.title_label.pack(pady=10)
        
        self.frame_ejercicio = tk.Frame(master, padx=10, pady=10, bg="#E0F2F1")
        self.frame_ejercicio.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.numero_label = tk.Label(self.frame_ejercicio, text=f"Ejercicio {self.numero_ejercicio_actual}", font=("Helvetica", 12), bg="#E0F2F1")
        self.numero_label.pack()

        self.tarea_label = tk.Label(self.frame_ejercicio, text=self.ejercicio_actual[1], font=("Helvetica", 10), wraplength=450, justify="center", bg="#E0F2F1")
        self.tarea_label.pack(pady=10)

        self.respuesta_entry = tk.Entry(self.frame_ejercicio, width=50)
        self.respuesta_entry.pack(pady=5)

        self.feedback_label = tk.Label(self.frame_ejercicio, text="", font=("Helvetica", 10, "italic"), fg="#FF5722", bg="#E0F2F1")
        self.feedback_label.pack(pady=5)

        self.frame_botones = tk.Frame(master, pady=10)
        self.frame_botones.pack()

        self.boton_revisar = tk.Button(self.frame_botones, text="Revisar", command=self.revisar_respuesta, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white", activebackground="#66BB6A", relief="flat")
        self.boton_revisar.pack(side=tk.LEFT, padx=5)

        self.boton_siguiente = tk.Button(self.frame_botones, text="Siguiente", command=self.siguiente_ejercicio, font=("Helvetica", 10, "bold"), bg="#2196F3", fg="white", activebackground="#42A5F5", relief="flat")
        self.boton_siguiente.pack(side=tk.LEFT, padx=5)

        # Cargar el primer ejercicio al iniciar
        self.cargar_ejercicio()

    def cargar_ejercicio(self):
        """Carga el ejercicio actual en la interfaz."""
        self.ejercicio_actual = self.ejercicios.get(self.numero_ejercicio_actual)
        titulo, tarea, _ = self.ejercicio_actual
        self.master.title(f"Ejercicio {self.numero_ejercicio_actual}: {titulo}")
        self.numero_label.config(text=f"Ejercicio {self.numero_ejercicio_actual}: {titulo}")
        self.tarea_label.config(text=f"Tarea:\n{tarea}")
        self.respuesta_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def revisar_respuesta(self):
        """Comprueba la respuesta del usuario."""
        _, _, respuesta_correcta = self.ejercicio_actual
        respuesta_usuario = self.respuesta_entry.get().strip().lower()
        
        # Manejo de respuestas con variaciones
        correcta_limpia = respuesta_correcta.lower().strip()
        
        if respuesta_usuario == correcta_limpia:
            self.feedback_label.config(text="¡Correcto! ¡Qué bien!", fg="green")
        elif correcta_limpia in respuesta_usuario:
             self.feedback_label.config(text="¡Buena respuesta! Casi lo lograste por completo.", fg="#FFC107")
        else:
            self.feedback_label.config(text=f"Incorrecto. La respuesta esperada era: '{respuesta_correcta}'", fg="red")

    def siguiente_ejercicio(self):
        """Carga el siguiente ejercicio."""
        self.numero_ejercicio_actual = (self.numero_ejercicio_actual % 100) + 1
        self.cargar_ejercicio()

if __name__ == "__main__":
    root = tk.Tk()
    app = CuervoApp(root)
    root.mainloop()
