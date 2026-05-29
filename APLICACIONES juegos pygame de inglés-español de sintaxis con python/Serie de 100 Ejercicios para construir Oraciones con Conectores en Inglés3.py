# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios para construir Oraciones con Conectores en Inglés
# Adaptado a una interfaz gráfica con Kivy.
#
# Este programa presenta ejercicios sobre el uso de conjunciones,
# adverbios conectores y pronombres relativos en una ventana interactiva.

import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image

class EnglishConnectorsApp(App):
    """
    Clase principal de la aplicación Kivy.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # La lista de ejercicios se mantiene igual
        self.exercises = {
            1: ("Coordinantes", "Traduce: 'Me gusta el café, pero a ella le gusta el té.'", "I like coffee, but she likes tea."),
            2: ("Subordinantes (Causa)", "Traduce: 'Él está feliz porque pasó el examen.'", "He is happy because he passed the exam."),
            3: ("Relativos ('Who')", "Traduce: 'El hombre que me llamó es mi hermano.'", "The man who called me is my brother."),
            4: ("Coordinantes", "Traduce: 'Puedes comer una manzana o puedes comer una naranja.'", "You can eat an apple or you can eat an orange."),
            5: ("Subordinantes (Tiempo)", "Traduce: 'Te llamaré cuando llegue a casa.'", "I will call you when I get home."),
            6: ("Relativos ('Which')", "Traduce: 'El libro, que es azul, es nuevo.'", "The book, which is blue, is new."),
            7: ("Adverbios Conectores", "Traduce: 'Estaba cansado; por lo tanto, fui a dormir.'", "I was tired; therefore, I went to sleep."),
            8: ("Subordinantes (Condición)", "Traduce: 'Si estudias, pasarás el examen.'", "If you study, you will pass the exam."),
            9: ("Relativos ('That')", "Traduce: 'La casa que compramos es grande.'", "The house that we bought is big."),
            10: ("Correlativas ('Either/Or')", "Traduce: 'O bien comes o bien bebes.'", "You can either eat or drink."),
            11: ("Subordinantes (Contraste)", "Traduce: 'Aunque es rico, es infeliz.'", "Although he is rich, he is unhappy."),
            12: ("Coordinantes", "Traduce: 'Ella no canta, ni tampoco baila.'", "She does not sing, nor does she dance."),
            13: ("Relativos", "Traduce: 'La chica que está hablando es mi amiga.'", "The girl who is talking is my friend."),
            14: ("Subordinantes (Tiempo)", "Traduce: 'Antes de que te vayas, por favor, cierra la puerta.'", "Before you leave, please close the door."),
            15: ("Subordinantes (Causa)", "Traduce: 'Nos quedamos en casa ya que estaba lloviendo.'", "We stayed home since it was raining."),
            16: ("Coordinantes", "Traduce: 'Lo intenté, mas no pude.'", "I tried, yet I could not."),
            17: ("Relativos", "Traduce: 'El perro que vive en la casa de al lado es ruidoso.'", "The dog that lives next door is loud."),
            18: ("Correlativas ('Both/And')", "Traduce: 'Ambos mi madre y mi padre trabajan aquí.'", "Both my mother and my father work here."),
            19: ("Subordinantes (Lugar)", "Traduce: 'Ve a donde quieras.'", "Go wherever you want."),
            20: ("Subordinantes (Condición)", "Traduce: 'No puedes pasar a menos que tengas un boleto.'", "You cannot enter unless you have a ticket."),
            21: ("Adverbios Conectores", "Traduce: 'Estudió mucho; sin embargo, no pasó.'", "He studied a lot; however, he did not pass."),
            22: ("Relativos", "Traduce: 'El coche, que es viejo, funciona bien.'", "The car, which is old, works well."),
            23: ("Subordinantes (Causa)", "Traduce: 'Él no vino al colegio porque estaba enfermo.'", "He did not come to school because he was sick."),
            24: ("Subordinantes (Tiempo)", "Traduce: 'Mientras yo estaba cocinando, él estaba viendo la televisión.'", "While I was cooking, he was watching television."),
            25: ("Correlativas ('Neither/Nor')", "Traduce: 'Ni mi hermano ni mi hermana están aquí.'", "Neither my brother nor my sister is here."),
            26: ("Subordinantes (Propósito)", "Traduce: 'Estudio para que pueda pasar.'", "I study so that I can pass."),
            27: ("Relativos", "Traduce: 'La persona a quien le hablé es mi jefa.'", "The person to whom I spoke is my boss."),
            28: ("Subordinantes (Manera)", "Traduce: 'Se comporta como si fuera el jefe.'", "He acts as if he is the boss."),
            29: ("Coordinantes", "Traduce: 'Ella es bonita, y también es inteligente.'", "She is pretty, and she is also smart."),
            30: ("Subordinantes (Grado)", "Traduce: 'Es más grande de lo que pensaba.'", "It is bigger than I thought."),
            31: ("Subordinantes (Tiempo)", "Traduce: 'Cuando llegué, ella ya se había ido.'", "When I arrived, she had already left."),
            32: ("Relativos", "Traduce: 'La película que viste es muy buena.'", "The movie that you saw is very good."),
            33: ("Subordinantes (Causa)", "Traduce: 'Dado que él no está aquí, podemos empezar.'", "Since he is not here, we can start."),
            34: ("Correlativas", "Traduce: 'Ambos el azul y el rojo me gustan.'", "I like both blue and red."),
            35: ("Subordinantes (Contraste)", "Traduce: 'A pesar de que tiene dinero, no lo gasta.'", "Even though he has money, he does not spend it."),
            36: ("Coordinantes", "Traduce: 'No tengo dinero, ni tengo un coche.'", "I have no money, nor do I have a car."),
            37: ("Subordinantes (Lugar)", "Traduce: 'Puedes sentarte donde quieras.'", "You can sit wherever you want."),
            38: ("Relativos", "Traduce: 'El coche que está estacionado afuera es mío.'", "The car which is parked outside is mine."),
            39: ("Subordinantes (Condición)", "Traduce: 'No iremos a menos que él venga.'", "We will not go unless he comes."),
            40: ("Subordinantes (Tiempo)", "Traduce: 'Mientras esperabas, yo estaba leyendo.'", "While you were waiting, I was reading."),
            41: ("Adverbios Conectores", "Traduce: 'Me gusta el chocolate; no obstante, me gustan más las galletas.'", "I like chocolate; nonetheless, I like cookies more."),
            42: ("Relativos", "Traduce: 'Las personas que viven allí son amables.'", "The people who live there are kind."),
            43: ("Correlativas", "Traduce: 'Ni el agua ni la comida estaban disponibles.'", "Neither the water nor the food was available."),
            44: ("Subordinantes (Manera)", "Traduce: 'Él canta como si fuera un profesional.'", "He sings as if he is a professional."),
            45: ("Subordinantes (Tiempo)", "Traduce: 'Tan pronto como él llegó, la fiesta comenzó.'", "As soon as he arrived, the party started."),
            46: ("Subordinantes (Contraste)", "Traduce: 'Él es alto, mientras que su hermano es bajo.'", "He is tall, whereas his brother is short."),
            47: ("Coordinantes", "Traduce: 'Ella habló, y todos la escucharon.'", "She spoke, and everyone listened to her."),
            48: ("Relativos", "Traduce: 'El libro del que estás hablando es interesante.'", "The book that you are talking about is interesting."),
            49: ("Subordinantes (Condición)", "Traduce: 'Puedes llamarme si necesitas ayuda.'", "You can call me if you need help."),
            50: ("Subordinantes (Propósito)", "Traduce: 'Trabajo duro para que pueda ganar dinero.'", "I work hard so that I can earn money."),
            51: ("Adverbios Conectores", "Traduce: 'El carro es caro; además, es viejo.'", "The car is expensive; moreover, it is old."),
            52: ("Subordinantes (Causa)", "Traduce: 'Estoy cansado porque no dormí.'", "I am tired because I did not sleep."),
            53: ("Relativos", "Traduce: 'Los niños, que estaban jugando, estaban felices.'", "The children, who were playing, were happy."),
            54: ("Subordinantes (Tiempo)", "Traduce: 'Desde que te vi, he sido feliz.'", "Since I saw you, I have been happy."),
            55: ("Correlativas", "Traduce: 'Puedes elegir o bien el rojo o bien el azul.'", "You can choose either red or blue."),
            56: ("Subordinantes (Lugar)", "Traduce: 'Vive donde pueda.'", "He lives wherever he can."),
            57: ("Subordinantes (Contraste)", "Traduce: 'Aunque está lloviendo, voy a salir.'", "Although it is raining, I am going out."),
            58: ("Coordinantes", "Traduce: 'Estudió, así que no reprobó.'", "He studied, so he did not fail."),
            59: ("Relativos", "Traduce: 'El restaurante que me recomendaste es bueno.'", "The restaurant that you recommended is good."),
            60: ("Subordinantes (Condición)", "Traduce: 'No lo compraré a menos que sea barato.'", "I will not buy it unless it is cheap."),
            61: ("Adverbios Conectores", "Traduce: 'El plan falló; como resultado, perdimos dinero.'", "The plan failed; as a result, we lost money."),
            62: ("Coordinantes", "Traduce: 'Estaba enfermo, por lo que no fui a trabajar.'", "I was sick, so I did not go to work."),
            63: ("Relativos", "Traduce: 'El libro, el cual es muy viejo, es valioso.'", "The book, which is very old, is valuable."),
            64: ("Correlativas", "Traduce: 'Ella es tanto una buena doctora como una buena persona.'", "She is both a good doctor and a good person."),
            65: ("Subordinantes (Causa)", "Traduce: 'Llegué tarde porque el bus estaba retrasado.'", "I was late because the bus was delayed."),
            66: ("Subordinantes (Tiempo)", "Traduce: 'Tan pronto como él vio al perro, corrió.'", "As soon as he saw the dog, he ran."),
            67: ("Coordinantes", "Traduce: 'No me gusta la leche, ni me gusta el queso.'", "I don't like milk, nor do I like cheese."),
            68: ("Relativos", "Traduce: 'La mujer que vive al lado es amable.'", "The woman who lives next door is kind."),
            69: ("Subordinantes (Contraste)", "Traduce: 'Aunque estaba cansado, no me rendí.'", "Although I was tired, I did not give up."),
            70: ("Subordinantes (Condición)", "Traduce: 'No lo haré si no me pagas.'", "I will not do it unless you pay me."),
            71: ("Adverbios Conectores", "Traduce: 'Primero, lava los platos; después, sécalos.'", "First, wash the dishes; then, dry them."),
            72: ("Coordinantes", "Traduce: 'Ella habla español, y él habla francés.'", "She speaks Spanish, and he speaks French."),
            73: ("Relativos", "Traduce: 'La idea que tienes es muy buena.'", "The idea that you have is very good."),
            74: ("Subordinantes (Tiempo)", "Traduce: 'Mientras el sol brilla, podemos jugar.'", "While the sun is shining, we can play."),
            75: ("Correlativas", "Traduce: 'Puedes o bien quedarte o bien irte.'", "You can either stay or leave."),
            76: ("Subordinantes (Manera)", "Traduce: 'Ellos actúan como si fueran famosos.'", "They act as if they are famous."),
            77: ("Subordinantes (Lugar)", "Traduce: 'Él va donde el dinero lo lleva.'", "He goes wherever the money takes him."),
            78: ("Subordinantes (Causa)", "Traduce: 'Como llegaste tarde, te perdiste el principio.'", "Since you arrived late, you missed the beginning."),
            79: ("Coordinantes", "Traduce: 'Él es pobre, mas es feliz.'", "He is poor, yet he is happy."),
            80: ("Relativos", "Traduce: 'La película, la cual es muy popular, es divertida.'", "The movie, which is very popular, is fun."),
            81: ("Adverbios Conectores", "Traduce: 'Hablé con él; por otra parte, me ignoró.'", "I spoke with him; on the other hand, he ignored me."),
            82: ("Coordinantes", "Traduce: 'Quería ir, pero no pude.'", "I wanted to go, but I could not."),
            83: ("Relativos", "Traduce: 'El profesor que nos enseña es bueno.'", "The teacher who teaches us is good."),
            84: ("Subordinantes (Tiempo)", "Traduce: 'Después de que comimos, caminamos.'", "After we ate, we walked."),
            85: ("Correlativas", "Traduce: 'Ni el blanco ni el negro se ven bien en ti.'", "Neither white nor black looks good on you."),
            86: ("Subordinantes (Lugar)", "Traduce: 'El restaurante está donde solía estar la tienda.'", "The restaurant is where the store used to be."),
            87: ("Subordinantes (Causa)", "Traduce: 'Estoy feliz porque te veo.'", "I am happy because I see you."),
            88: ("Subordinantes (Contraste)", "Traduce: 'Aunque estaba lloviendo, fuimos a caminar.'", "Although it was raining, we went for a walk."),
            89: ("Coordinantes", "Traduce: 'Toma un paraguas, o te mojarás.'", "Take an umbrella, or you will get wet."),
            90: ("Relativos", "Traduce: 'El coche, que es de mi padre, es nuevo.'", "The car, which is my father's, is new."),
            91: ("Adverbios Conectores", "Traduce: 'Estaba enfermo; por consiguiente, no pude ir.'", "He was sick; consequently, he could not go."),
            92: ("Subordinantes (Tiempo)", "Traduce: 'Ella se fue a dormir después de que terminó de leer.'", "She went to sleep after she finished reading."),
            93: ("Coordinantes", "Traduce: 'No tengo dinero, por lo que no puedo comprarlo.'", "I have no money, so I cannot buy it."),
            94: ("Relativos", "Traduce: 'El perro que está ladrando es mío.'", "The dog that is barking is mine."),
            95: ("Correlativas", "Traduce: 'Tanto mi padre como mi madre están trabajando.'", "Both my father and my mother are working."),
            96: ("Subordinantes (Manera)", "Traduce: 'Habla como si fuera un experto.'", "He talks as if he were an expert."),
            97: ("Subordinantes (Causa)", "Traduce: 'Estaba cansado, pues me acosté.'", "I was tired, for I went to bed."),
            98: ("Subordinantes (Tiempo)", "Traduce: 'Ella lloró cuando vio la película.'", "She cried when she saw the movie."),
            99: ("Coordinantes", "Traduce: 'Tenía hambre, pero la nevera estaba vacía.'", "I was hungry, but the fridge was empty."),
            100: ("Adverbios Conectores", "Traduce: 'Me gusta su estilo; sin embargo, no me gusta su personalidad.'", "I like her style; however, I do not like her personality."),
        }
        self.correct_answer = ""

    def build(self):
        """
        Método principal para construir la interfaz de usuario.
        """
        # Configurar el color de fondo de la ventana con un tono de arena
        Window.clearcolor = (0.96, 0.94, 0.88, 1)  # Color arena claro

        # Crear el layout principal que contendrá todos los widgets
        main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Título de la aplicación
        title_label = Label(text="Reto de Conectores en Inglés",
                            font_size='24sp', bold=True, color=(0.2, 0.2, 0.2, 1),
                            size_hint_y=0.2)

        # Etiqueta para el tipo de conector
        self.type_label = Label(text="", font_size='18sp', color=(0.4, 0.4, 0.4, 1),
                                size_hint_y=0.1)

        # Etiqueta para la tarea o pregunta
        self.task_label = Label(text="", font_size='16sp', color=(0.3, 0.3, 0.3, 1),
                                size_hint_y=0.2)

        # Campo de entrada para la respuesta del usuario
        self.answer_entry = TextInput(multiline=False, font_size='16sp', size_hint_y=0.1)

        # Botón para comprobar la respuesta
        check_button = Button(text="Comprobar", background_color=(0.27, 0.52, 0.43, 1), color=(1, 1, 1, 1),
                              size_hint_y=0.1, font_size='18sp') # Tono verde hoja
        check_button.bind(on_press=self.check_answer)

        # Etiqueta para la retroalimentación
        self.feedback_label = Label(text="", font_size='18sp', bold=True, size_hint_y=0.1)

        # Botón para el siguiente ejercicio
        next_button = Button(text="Siguiente Ejercicio", background_color=(0.4, 0.29, 0.17, 1), color=(1, 1, 1, 1),
                             size_hint_y=0.1, font_size='18sp') # Tono marrón tierra
        next_button.bind(on_press=self.next_exercise)

        # Agregar los widgets al layout principal
        main_layout.add_widget(title_label)
        main_layout.add_widget(self.type_label)
        main_layout.add_widget(self.task_label)
        main_layout.add_widget(self.answer_entry)
        main_layout.add_widget(check_button)
        main_layout.add_widget(self.feedback_label)
        main_layout.add_widget(next_button)

        self.next_exercise()
        return main_layout
    
    def next_exercise(self, instance=None):
        """
        Selecciona y muestra un nuevo ejercicio.
        """
        # Limpia los campos de texto y las etiquetas de retroalimentación
        self.answer_entry.text = ""
        self.feedback_label.text = ""
        self.feedback_label.color = (0.3, 0.3, 0.3, 1)

        # Selecciona un ejercicio aleatorio
        self.current_exercise_number = random.choice(list(self.exercises.keys()))
        title, task, correct_answer = self.exercises[self.current_exercise_number]
        self.correct_answer = correct_answer

        # Actualiza las etiquetas con la información del nuevo ejercicio
        self.type_label.text = f"[Ejercicio {self.current_exercise_number}: {title}]"
        self.task_label.text = task
        
    def check_answer(self, instance):
        """
        Verifica la respuesta del usuario y muestra la retroalimentación.
        """
        user_response = self.answer_entry.text.strip()
        
        # Normaliza las respuestas para una comparación más flexible
        clean_user_response = user_response.strip(".").strip().lower()
        clean_correct_answer = self.correct_answer.strip(".").strip().lower()

        if clean_user_response == clean_correct_answer or (clean_user_response + '.') == clean_correct_answer or (clean_user_response + '?') == clean_correct_answer:
            self.feedback_label.text = "¡Correcto! ¡Excelente trabajo!"
            self.feedback_label.color = (0.27, 0.52, 0.43, 1) # Verde hoja
        else:
            self.feedback_label.text = f"Incorrecto. La respuesta esperada era: '{self.correct_answer}'"
            self.feedback_label.color = (0.7, 0.1, 0.1, 1) # Rojo ladrillo

if __name__ == "__main__":
    EnglishConnectorsApp().run()
