# Sustantivos Neutros - Versión Kivy

Este es un ejemplo adaptado para una aplicación Kivy que permite:
- Mostrar una diapositiva conceptual
- Realizar práctica de sustantivos neutros
- Clasificar ejemplos mediante un cuestionario interactivo
- Agregar y guardar hasta 100 ejemplos personalizados

```python
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import json
import os

# Datos base
EJEMPLOS = [
    {"texto": "Todo nos habla de Dios.", "categoria": "Cantidad"},
    {"texto": "Algo ha sucedido que ignoramos.", "categoria": "Concepto general"},
    {"texto": "Mucho se espera de su prudencia.", "categoria": "Cantidad"},
    {"texto": "Nada veo que pueda causarnos inquietud.", "categoria": "Concepto general"},
    # ... (agrega más ejemplos hasta 50 o más)
]

if not os.path.exists("ejemplos_usuario.json"):
    with open("ejemplos_usuario.json", "w") as f:
        json.dump([], f)

# Pantallas
class MenuScreen(Screen):
    pass

class DiapositivaScreen(Screen):
    def on_enter(self):
        self.ids.contenido.text = "Los sustantivos neutros en español no tienen género y se usan para expresar ideas generales o abstractas..."

class PracticaScreen(Screen):
    index = 0

    def on_enter(self):
        self.index = 0
        self.mostrar_ejemplo()

    def mostrar_ejemplo(self):
        if self.index < len(EJEMPLOS):
            ejemplo = EJEMPLOS[self.index]
            self.ids.label_ejemplo.text = ejemplo['texto']
        else:
            self.ids.label_ejemplo.text = "¡Has terminado la práctica!"

    def verificar_categoria(self):
        respuesta = self.ids.input_categoria.text.strip().lower()
        correcta = EJEMPLOS[self.index]['categoria'].lower()
        if respuesta == correcta:
            self.popup("¡Correcto!")
        else:
            self.popup(f"Incorrecto. Era: {correcta}")
        self.index += 1
        self.mostrar_ejemplo()
        self.ids.input_categoria.text = ""

    def popup(self, mensaje):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=mensaje))
        btn = Button(text='Cerrar')
        content.add_widget(btn)
        popup = Popup(title='Resultado', content=content, size_hint=(0.6, 0.4))
        btn.bind(on_press=popup.dismiss)
        popup.open()

class CuestionarioScreen(Screen):
    def on_enter(self):
        self.ejemplos = EJEMPLOS.copy()
        self.index = 0
        self.cargar_pregunta()

    def cargar_pregunta(self):
        if self.index < len(self.ejemplos):
            self.ids.label_pregunta.text = self.ejemplos[self.index]['texto']
        else:
            self.ids.label_pregunta.text = "Cuestionario terminado."

    def verificar_respuesta(self):
        categoria = self.ejemplos[self.index]['categoria'].lower()
        resp = self.ids.input_respuesta.text.strip().lower()
        if resp == categoria:
            self.popup("¡Correcto!")
        else:
            self.popup(f"Incorrecto. La categoría correcta es: {categoria}")
        self.index += 1
        self.cargar_pregunta()
        self.ids.input_respuesta.text = ""

    def popup(self, mensaje):
        popup = Popup(title='Resultado',
                      content=Label(text=mensaje),
                      size_hint=(0.6, 0.4))
        popup.open()

class AgregarEjemploScreen(Screen):
    def guardar_ejemplo(self):
        texto = self.ids.input_nuevo_ejemplo.text.strip()
        categoria = self.ids.input_nueva_categoria.text.strip()
        if texto and categoria:
            with open("ejemplos_usuario.json") as f:
                datos = json.load(f)
            if len(datos) < 100:
                datos.append({"texto": texto, "categoria": categoria})
                with open("ejemplos_usuario.json", "w") as f:
                    json.dump(datos, f)
                self.ids.label_estado.text = "Ejemplo guardado correctamente."
            else:
                self.ids.label_estado.text = "Has alcanzado el límite de 100 ejemplos."
        else:
            self.ids.label_estado.text = "Faltan datos."

# Gestor de pantallas
class SustantivosApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(DiapositivaScreen(name='diapositiva'))
        sm.add_widget(PracticaScreen(name='practica'))
        sm.add_widget(CuestionarioScreen(name='cuestionario'))
        sm.add_widget(AgregarEjemploScreen(name='agregar'))
        return sm

if __name__ == '__main__':
    SustantivosApp().run()
```

### Notas adicionales:
- Para esta app necesitas también definir un archivo `.kv` con las pantallas (`menu.kv`, por ejemplo).
- Si deseas, puedo ayudarte a crear también las interfaces gráficas (`.kv`).

¿Quieres que continúe con eso?
