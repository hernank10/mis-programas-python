from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class WordManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.words = {
            "Tecnología": ["autopista", "microscopio"],
            "Ciencia": ["prehistoria", "posoperatorio"]
        }

        self.category_spinner = Spinner(text='Selecciona una categoría', values=list(self.words.keys()))
        self.add_widget(self.category_spinner)

        # Mostrar palabras
        self.word_display = GridLayout(cols=1, size_hint_y=None)
        self.word_display.bind(minimum_height=self.word_display.setter('height'))
        self.scroll = ScrollView(size_hint=(1, 0.3))
        self.scroll.add_widget(self.word_display)
        self.add_widget(self.scroll)

        # Entradas
        self.new_word_input = TextInput(hint_text="Nueva palabra", multiline=False)
        self.add_widget(self.new_word_input)

        self.new_category_input = TextInput(hint_text="Nueva categoría", multiline=False)
        self.add_widget(self.new_category_input)

        # Botones
        buttons = [
            ("Agregar palabra", self.add_word),
            ("Buscar palabra", self.search_word),
            ("Editar palabra", self.edit_word_popup),
            ("Eliminar palabra", self.delete_word),
            ("Eliminar categoría", self.delete_category),
            ("Guardar en archivo", self.save_to_file)
        ]

        for text, callback in buttons:
            self.add_widget(Button(text=text, on_press=callback))

        self.update_display()

    def update_display(self):
        self.word_display.clear_widgets()
        category = self.category_spinner.text
        if category in self.words:
            for word in self.words[category]:
                self.word_display.add_widget(Label(text=word, size_hint_y=None, height=30))

    def add_word(self, instance):
        word = self.new_word_input.text.strip()
        category = self.new_category_input.text.strip() or self.category_spinner.text
        if word and category:
            self.words.setdefault(category, []).append(word)
            self.category_spinner.values = list(self.words.keys())
            self.category_spinner.text = category
            self.new_word_input.text = ""
            self.new_category_input.text = ""
            self.update_display()

    def search_word(self, instance):
        def do_search(instance):
            query = search_input.text.strip().lower()
            results = []
            for cat, words in self.words.items():
                for w in words:
                    if query in w.lower():
                        results.append(f"{w} ({cat})")
            content.text = "\n".join(results) if results else "No se encontraron coincidencias."

        layout = BoxLayout(orientation='vertical')
        search_input = TextInput(hint_text="Buscar palabra", multiline=False)
        content = Label(size_hint_y=2)
        search_btn = Button(text="Buscar", on_press=do_search)
        close_btn = Button(text="Cerrar", on_press=lambda x: popup.dismiss())
        layout.add_widget(search_input)
        layout.add_widget(content)
        layout.add_widget(search_btn)
        layout.add_widget(close_btn)

        popup = Popup(title="Buscar palabra", content=layout, size_hint=(0.8, 0.6))
        popup.open()

    def edit_word_popup(self, instance):
        category = self.category_spinner.text
        if category not in self.words or not self.words[category]:
            return

        layout = BoxLayout(orientation='vertical')
        word_input = TextInput(hint_text="Palabra actual", multiline=False)
        new_input = TextInput(hint_text="Nueva palabra", multiline=False)
        update_btn = Button(text="Actualizar", on_press=lambda x: self.edit_word(category, word_input.text.strip(), new_input.text.strip(), popup))
        layout.add_widget(word_input)
        layout.add_widget(new_input)
        layout.add_widget(update_btn)
        layout.add_widget(Button(text="Cerrar", on_press=lambda x: popup.dismiss()))

        popup = Popup(title="Editar palabra", content=layout, size_hint=(0.8, 0.6))
        popup.open()

    def edit_word(self, category, old_word, new_word, popup):
        if category in self.words and old_word in self.words[category]:
            idx = self.words[category].index(old_word)
            self.words[category][idx] = new_word
            self.update_display()
            popup.dismiss()

    def delete_word(self, instance):
        category = self.category_spinner.text
        if category in self.words:
            def do_delete(instance):
                word = input_word.text.strip()
                if word in self.words[category]:
                    self.words[category].remove(word)
                    self.update_display()
                popup.dismiss()

            layout = BoxLayout(orientation='vertical')
            input_word = TextInput(hint_text="Palabra a eliminar", multiline=False)
            layout.add_widget(input_word)
            layout.add_widget(Button(text="Eliminar", on_press=do_delete))
            layout.add_widget(Button(text="Cancelar", on_press=lambda x: popup.dismiss()))

            popup = Popup(title="Eliminar palabra", content=layout, size_hint=(0.8, 0.4))
            popup.open()

    def delete_category(self, instance):
        category = self.category_spinner.text
        if category in self.words:
            del self.words[category]
            self.category_spinner.values = list(self.words.keys())
            self.category_spinner.text = 'Selecciona una categoría'
            self.update_display()

    def save_to_file(self, instance):
        with open("palabras_guardadas.txt", "w", encoding="utf-8") as f:
            for cat, words in self.words.items():
                f.write(f"[{cat}]\n")
                for w in words:
                    f.write(f"  - {w}\n")
        popup = Popup(title="Guardado", content=Label(text="Archivo guardado correctamente."), size_hint=(0.6, 0.3))
        popup.open()

class WordApp(App):
    def build(self):
        return WordManager()

if __name__ == '__main__':
    WordApp().run()
