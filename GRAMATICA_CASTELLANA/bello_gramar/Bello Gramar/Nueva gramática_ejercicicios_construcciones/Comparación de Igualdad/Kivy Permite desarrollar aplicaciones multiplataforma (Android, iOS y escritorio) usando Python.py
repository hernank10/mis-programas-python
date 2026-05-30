
from kivy.app import App
from kivy.uix.label import Label

class MiPrimeraApp(App):
    def build(self):
        return Label(text="¡Bienvenido a tu app educativa!")

MiPrimeraApp().run()
