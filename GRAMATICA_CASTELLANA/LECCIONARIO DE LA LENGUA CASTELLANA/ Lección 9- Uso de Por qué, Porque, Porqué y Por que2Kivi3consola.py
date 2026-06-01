# main.py
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock # Importar Clock para programar eventos
from kivy.core.window import Window # Para acceder a la ventana principal

# Establecer la versión mínima de Kivy
kivy.require('2.0.0') # Reemplaza con la versión que uses

class BasicConsoleApp(App):

    def build(self):
        # Configurar el título de la ventana
        self.title = 'Aplicación Kivy de Consola Básica'
        
        print("--- Kivy App Iniciada ---")
        print("Ventana creada. Interactúa con la consola o cierra la ventana.")

        # Creamos un layout simple para la ventana
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 1. Un Label para mostrar mensajes en la UI
        self.status_label = Label(text="¡Hola desde Kivy!", font_size='24sp', size_hint_y=0.2)
        main_layout.add_widget(self.status_label)

        # 2. Un TextInput para entrada de usuario
        self.input_field = TextInput(hint_text="Escribe algo aquí...", multiline=False, size_hint_y=0.1)
        main_layout.add_widget(self.input_field)

        # 3. Un botón para enviar la entrada
        send_button = Button(text="Enviar a Consola", size_hint_y=0.1)
        send_button.bind(on_release=self.send_to_console)
        main_layout.add_widget(send_button)

        # 4. Un botón para ejecutar una acción programada
        schedule_button = Button(text="Programar Mensaje en Consola", size_hint_y=0.1)
        schedule_button.bind(on_release=self.schedule_message)
        main_layout.add_widget(schedule_button)

        # 5. Un botón para salir
        exit_button = Button(text="Salir", background_color=(0.8, 0.2, 0.2, 1), size_hint_y=0.1)
        exit_button.bind(on_release=self.stop) # El método stop() cierra la aplicación
        main_layout.add_widget(exit_button)

        # Configurar un evento para cerrar la ventana desde la consola
        # Puedes añadir una lógica para que si escribes 'exit' en la consola, se cierre la app
        # Esto requiere un hilo separado o una forma no bloqueante de leer la entrada,
        # lo cual es más complejo para un ejemplo básico.
        # Por ahora, nos centraremos en imprimir información a la consola.
        
        # Opcional: enlazar la función on_key_down de Kivy para capturar pulsaciones de teclas
        # Window.bind(on_key_down=self.on_keyboard_down)

        return main_layout

    def send_to_console(self, instance):
        user_text = self.input_field.text
        if user_text:
            print(f"Usuario escribió (desde UI): '{user_text}'")
            self.status_label.text = f"Recibido: '{user_text}'"
            self.input_field.text = "" # Limpiar el campo de entrada
        else:
            print("El campo de entrada está vacío.")
            self.status_label.text = "¡Campo vacío!"

    def schedule_message(self, instance):
        print("Programando un mensaje en consola para dentro de 3 segundos...")
        self.status_label.text = "Mensaje programado..."
        # Clock.schedule_once(callback, delay_in_seconds)
        Clock.schedule_once(self._print_scheduled_message, 3)

    def _print_scheduled_message(self, dt):
        # dt es el delta time, el tiempo que ha pasado desde que se programó
        print(f"--- Mensaje programado (después de {dt:.2f} segundos) ---")
        print("Este mensaje aparece en la consola después de un retraso.")
        self.status_label.text = "¡Mensaje programado impreso!"

    # Opcional: un ejemplo de cómo capturar eventos del teclado
    def on_keyboard_down(self, window, keycode, text, modifiers):
        # print(f"Tecla presionada: keycode={keycode}, text='{text}', modifiers={modifiers}")
        if keycode == 27:  # 27 es el código para la tecla ESC
            print("Tecla ESC detectada. Cerrando aplicación...")
            self.stop() # Cierra la aplicación

    def on_start(self):
        # Se ejecuta justo después de build, cuando la app ya está visible
        print("La aplicación Kivy ha sido construida y está lista.")
        # Podemos enlazar el teclado aquí si queremos que actúe a nivel global
        Window.bind(on_key_down=self.on_keyboard_down)

    def on_stop(self):
        # Se ejecuta cuando la aplicación se cierra
        print("--- Kivy App Detenida ---")
        # Desenlazar el teclado para evitar errores si la ventana ya no existe
        Window.unbind(on_key_down=self.on_keyboard_down)


if __name__ == '__main__':
    # Ejecuta la aplicación
    BasicConsoleApp().run()
