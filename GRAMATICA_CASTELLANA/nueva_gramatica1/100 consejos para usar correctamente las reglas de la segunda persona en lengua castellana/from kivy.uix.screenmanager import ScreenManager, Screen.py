# Intentar nuevamente con contenido corregido para los archivos del proyecto Pluscuamperfecto Pro

import zipfile
import os

# Crear estructura de carpetas y archivos del proyecto Pluscuamperfecto Pro
base_path = "/mnt/data/pluscuamperfecto_pro"
os.makedirs(base_path, exist_ok=True)
os.makedirs(f"{base_path}/assets", exist_ok=True)

# Archivos principales
files = {
    "main.py": '''from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from database import DBHelper
from lang import LANG
from plyer import tts

db = DBHelper()
current_lang = "es"

def speak(text):
    tts.speak(text)

class MenuScreen(Screen):
    def on_enter(self):
        self.ids.title.text = LANG[current_lang]["title"]

class AdviceScreen(Screen):
    def on_pre_enter(self):
        advice = db.get_random_advice()
        self.ids.advice_text.text = advice
        speak(advice)

class LangSwitchScreen(Screen):
    def switch_lang(self):
        global current_lang
        current_lang = "en" if current_lang == "es" else "es"
        self.manager.current = "menu"

class PluscuamApp(App):
    def build(self):
        return Builder.load_file("ui.kv")

if __name__ == '__main__':
    PluscuamApp().run()
''',
    "database.py": '''import sqlite3
import random

class DBHelper:
    def __init__(self):
        self.conn = sqlite3.connect("historial.db")
        self.create_tables()

    def create_tables(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS consejos (id INTEGER PRIMARY KEY, texto TEXT, categoria TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS historial (id INTEGER PRIMARY KEY, ejercicio TEXT, puntuacion INTEGER)")
        self.conn.commit()

    def get_random_advice(self):
        cursor = self.conn.execute("SELECT texto FROM consejos ORDER BY RANDOM() LIMIT 1")
        result = cursor.fetchone()
        return result[0] if result else "No hay consejos disponibles."

    def insert_advice(self, texto, categoria):
        self.conn.execute("INSERT INTO consejos (texto, categoria) VALUES (?, ?)", (texto, categoria))
        self.conn.commit()
''',
    "lang.py": '''LANG = {
    "es": {
        "title": "Pluscuamperfecto Pro - Español",
        "menu": "Menú Principal",
        "start": "Comenzar práctica",
        "advice": "Ver consejo",
        "history": "Ver historial",
        "language": "Cambiar idioma",
        "exit": "Salir"
    },
    "en": {
        "title": "Pluscuamperfecto Pro - English",
        "menu": "Main Menu",
        "start": "Start practice",
        "advice": "View advice",
        "history": "View history",
        "language": "Switch language",
        "exit": "Exit"
    }
}
''',
    "ui.kv": '''ScreenManager:
    MenuScreen:
    AdviceScreen:
    LangSwitchScreen:

<MenuScreen>:
    name: "menu"
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: title
            text: "Pluscuamperfecto Pro"
            font_size: 24
        Button:
            text: "Ver Consejo"
            on_press: root.manager.current = "advice"
        Button:
            text: "Cambiar Idioma"
            on_press: root.manager.current = "lang"

<AdviceScreen>:
    name: "advice"
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: advice_text
            text: "Consejo aquí"
            font_size: 20
        Button:
            text: "Volver al Menú"
            on_press: root.manager.current = "menu"

<LangSwitchScreen>:
    name: "lang"
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Idioma cambiado."
        Button:
            text: "Volver al Menú"
            on_press: root.switch_lang()
''',
    "README.md": "# Pluscuamperfecto Pro\n\nApp educativa bilingüe con Kivy, soporte de voz, base de datos y ejercicios.",
    "buildozer.spec": "# buildozer.spec example - customize for your environment\n[app]\ntitle = Pluscuamperfecto Pro\npackage.name = pluscuamperfecto\npackage.domain = org.educativo\nsource.dir = .\nversion = 1.0\nrequirements = python3,kivy,sqlite3,plyer\norientation = portrait\nfullscreen = 1\nicon.filename = assets/icon.png\n[buildozer]\nlog_level = 2\nwarn_on_root = 1"
}

# Crear los archivos
for filename, content in files.items():
    with open(os.path.join(base_path, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Crear un ícono de muestra
with open(os.path.join(base_path, "assets/icon.png"), "wb") as f:
    f.write(b"\x89PNG\r\n\x1a\n")  # encabezado PNG mínimo

# Crear archivo ZIP del proyecto
zip_path = "/mnt/data/pluscuamperfecto_pro.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk(base_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, os.path.relpath(file_path, base_path))

zip_path
