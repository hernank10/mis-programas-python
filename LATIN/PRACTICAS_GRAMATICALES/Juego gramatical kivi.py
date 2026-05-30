from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Datos de la misión
oraciones = [
    {"texto": "Salimos temprano, llegamos antes que todos.", "tipo": "yuxtapuesta"},
    {"texto": "Estudia mucho porque quiere aprobar el examen.", "tipo": "subordinada"},
    {"texto": "Juan juega fútbol y Pedro lee un libro.", "tipo": "coordinada"}
]

# Variables de estado
progreso = {"aciertos": 0, "actual": 0}

# ─── Pantallas ───

class Inicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="🌳 Bienvenido al Bosque de las Proposiciones"))
        layout.add_widget(Label(text="Clasifica cada oración compuesta para avanzar."))
        btn = Button(text="Iniciar misión")
        btn.bind(on_press=lambda x: self.manager.current == "mision")
        layout.add_widget(btn)
        self.add_widget(layout)

class Mision(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="")
        self.layout.add_widget(self.label)

        self.botones = []
        for tipo in ["coordinada", "subordinada", "yuxtapuesta"]:
            btn = Button(text=tipo)
            btn.bind(on_press=self.validar)
            self.botones.append(btn)
            self.layout.add_widget(btn)

        self.add_widget(self.layout)
        self.actualizar_oracion()

    def actualizar_oracion(self):
        if progreso["actual"] < len(oraciones):
            oracion = oraciones[progreso["actual"]]["texto"]
            self.label.text = f"📝 {oracion}"
        else:
            self.manager.current = "final"

    def validar(self, instance):
        tipo_usuario = instance.text
        tipo_correcto = oraciones[progreso["actual"]]["tipo"]
        if tipo_usuario == tipo_correcto:
            progreso["aciertos"] += 1
            self.label.text = "✅ ¡Correcto!"
        else:
            self.label.text = f"❌ Incorrecto. Era '{tipo_correcto}'."
        progreso["actual"] += 1
        self.layout.add_widget(Label(text="Presiona para continuar..."))
        continuar = Button(text="Siguiente")
        continuar.bind(on_press=lambda x: self.actualizar_oracion())
        self.layout.add_widget(continuar)

class Final(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        aciertos = progreso["aciertos"]
        total = len(oraciones)
        layout.add_widget(Label(text="🏁 Misión completada"))
        layout.add_widget(Label(text=f"Aciertos: {aciertos}/{total}"))
        if aciertos == total:
            layout.add_widget(Label(text="🏆 ¡Dominaste el bosque!"))
        elif aciertos >= 2:
            layout.add_widget(Label(text="💪 Buen trabajo, sigue explorando."))
        else:
            layout.add_widget(Label(text="🔄 Reintenta para mejorar."))
        self.add_widget(layout)

# ─── App principal ───

class MisionNarrativaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Inicio(name="inicio"))
        sm.add_widget(Mision(name="mision"))
        sm.add_widget(Final(name="final"))
        return sm

if __name__ == "__main__":
    MisionNarrativaApp().run()
