"""
Aplicación Kivy: Sistema Trilingüe - Espiral de Aprendizaje
Archivo: app_trilingue_kivy.py

Características:
- Interfaz en Kivy (Python)
- Exposición multimodal: griego transliterado, español, inglés, nota cultural
- Práctica activa: entradas para español, inglés y griego
- Ejercicio inverso (español/inglés -> griego)
- Transliteración a Devanagari, Árabe y Pinyin
- Repetición espaciada: peso por concepto guardado en progress.json
- Retroalimentación inmediata + explicación
- Metacognición: estadísticas básicas y lista de conceptos revisados

Cómo usar:
1) Instalar Kivy (por ejemplo: pip install kivy)
2) Guardar este archivo como `app_trilingue_kivy.py`
3) Ejecutar: python app_trilingue_kivy.py

Nota: el conjunto de `CONCEPTOS` incluido es muestral (10). Puedes reemplazarlo
por la lista completa de 100 conceptos en el formato indicado.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import random, json, os
from datetime import datetime

Window.size = (1000, 700)

KV = '''
<MainWidget>:
    orientation: 'horizontal'
    padding: 10
    spacing: 10

    BoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.28
        spacing: 8

        Label:
            text: 'Acciones'
            size_hint_y: None
            height: 32
            bold: True

        Button:
            text: 'Practicar (griego → es/en)'
            on_release: root.practicar()
            size_hint_y: None
            height: 44

        Button:
            text: 'Practicar inverso (es/en → griego)'
            on_release: root.practicar_inverso()
            size_hint_y: None
            height: 44

        Button:
            text: 'Siguiente concepto'
            on_release: root.siguiente_concepto()
            size_hint_y: None
            height: 44

        Button:
            text: 'Ver transliteraciones (HI-AR-ZH)'
            on_release: root.mostrar_transliteraciones()
            size_hint_y: None
            height: 44

        Button:
            text: 'Mostrar frases creadas'
            on_release: root.mostrar_frases()
            size_hint_y: None
            height: 44

        Button:
            text: 'Guardar progreso'
            on_release: root.guardar_progreso()
            size_hint_y: None
            height: 44

        Button:
            text: 'Reiniciar progreso'
            on_release: root.reset_progreso()
            size_hint_y: None
            height: 44

        Label:
            text: 'Sugerencia:\nSigue la espiral: escribe siempre, crea frases, revisa estadísticas.'
            text_size: self.width, None
            size_hint_y: None
            height: 120
            halign: 'left'
            valign: 'top'

    BoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.72
        spacing: 8

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.28
            padding: 6
            spacing: 6
            canvas.before:
                Color:
                    rgba: (.95, .95, .97, 1)
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text: 'Exposición Multimodal'
                size_hint_y: None
                height: 26
                bold: True

            GridLayout:
                cols: 2
                size_hint_y: None
                height: 120
                Label:
                    text: 'Griego transliterado:'
                    halign: 'left'
                Label:
                    text: root.lbl_gr
                    halign: 'left'

                Label:
                    text: 'Español:'
                    halign: 'left'
                Label:
                    text: root.lbl_es
                    halign: 'left'

                Label:
                    text: 'Inglés:'
                    halign: 'left'
                Label:
                    text: root.lbl_en
                    halign: 'left'

                Label:
                    text: 'Nota cultural:'
                    halign: 'left'
                Label:
                    text: root.lbl_note
                    halign: 'left'

        BoxLayout:
            orientation: 'vertical'
            padding: 6
            spacing: 6

            Label:
                text: 'Práctica activa (escribe siempre)'
                size_hint_y: None
                height: 26
                bold: True

            GridLayout:
                cols: 2
                size_hint_y: None
                height: 120
                Label:
                    text: 'Español:'
                    halign: 'left'
                TextInput:
                    id: entry_es
                    multiline: False

                Label:
                    text: 'Inglés:'
                    halign: 'left'
                TextInput:
                    id: entry_en
                    multiline: False

                Label:
                    text: 'Griego (transliterado):'
                    halign: 'left'
                TextInput:
                    id: entry_gr
                    multiline: False

            Label:
                text: 'Contextualización: escribe frases reales (ES / EN)'
                size_hint_y: None
                height: 22

            GridLayout:
                cols: 2
                TextInput:
                    id: frase_es
                    size_hint_y: None
                    height: 90
                TextInput:
                    id: frase_en
                    size_hint_y: None
                    height: 90

            BoxLayout:
                size_hint_y: None
                height: 40
                spacing: 8
                Button:
                    text: 'Enviar respuestas'
                    on_release: root.enviar_respuestas()
                Button:
                    text: 'Saltar'
                    on_release: root.siguiente_concepto()

            Label:
                id: feedback_label
                text: root.feedback
                text_size: self.width, None
                size_hint_y: None
                height: 60
                halign: 'left'
                valign: 'top'

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.28
            padding: 6
            spacing: 6
            canvas.before:
                Color:
                    rgba: (.98, .98, 1, 1)
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text: 'Metacognición y Progreso'
                size_hint_y: None
                height: 26
                bold: True

            GridLayout:
                cols: 3
                Label:
                    text: 'Aciertos:'
                Label:
                    text: str(root.total_aciertos)
                Label:
                    text: 'Errores:'
                Label:
                    text: str(root.total_errores)
                Label:
                    text: 'Precisión:'
                Label:
                    text: root.precision_str

            Label:
                text: 'Conceptos revisados (últimos):'
                size_hint_y: None
                height: 22
            TextInput:
                id: hist_display
                text: root.hist_text
                readonly: True
                size_hint_y: None
                height: 90
'''

# -----------------------------
# Datos muestrales (reemplaza por 100 para uso real)
# -----------------------------
CONCEPTOS = [
    {"gr": "logos", "es": "razón", "en": "reason", "note": "El logos era la estructura racional del mundo."},
    {"gr": "physis", "es": "naturaleza", "en": "nature", "note": "Physis expresa el surgir, crecer y moverse de lo vivo."},
    {"gr": "arete", "es": "virtud, excelencia", "en": "virtue, excellence", "note": "Arete es la excelencia moral y humana."},
    {"gr": "ethos", "es": "carácter", "en": "character", "note": "Ethos designa la disposición habitual del individuo."},
    {"gr": "zoe", "es": "vida", "en": "life", "note": "Zoe es la vida en su sentido más elemental."},
    {"gr": "psyche", "es": "alma", "en": "soul", "note": "Psyche une alma, respiración y principio vital."},
    {"gr": "kosmos", "es": "universo, orden", "en": "cosmos, order", "note": "Kosmos implica belleza, orden y armonía."},
    {"gr": "dikaiosyne", "es": "justicia", "en": "justice", "note": "Dikaiosyne era la virtud de actuar correctamente."},
    {"gr": "aletheia", "es": "verdad", "en": "truth", "note": "Aletheia significa desocultamiento, revelación de lo real."},
    {"gr": "sophia", "es": "sabiduría", "en": "wisdom", "note": "Sophia es la sabiduría que guía la vida."}
]

PROGRESS_FILE = 'progress_kivy.json'

# -----------------------------
# Transliteración: tablas aproximadas
# -----------------------------
DEVANAGARI_MAP = {
    'ph': 'फ', 'th': 'थ', 'ch': 'च', 'ps': 'प्स',
    'a': 'a', 'e': 'े', 'i': 'ि', 'o': 'ो', 'u': 'ु',
    'k': 'क', 'g': 'ग', 'l': 'ल', 'r': 'र', 't': 'त',
    's': 'स', 'm': 'म', 'n': 'न', 'd': 'द'
}

ARABIC_MAP = {
    'ph': 'ف', 'th': 'ث', 'ch': 'تش', 'ps': 'بس',
    'a': 'ا', 'e': 'ي', 'i': 'ي', 'o': 'و', 'u': 'و',
    'k': 'ك', 'g': 'ج', 'l': 'ل', 'r': 'ر', 't': 'ت',
    's': 'س', 'm': 'م', 'n': 'ن', 'd': 'د'
}

PINYIN_MAP = {
    'ph': 'f', 'th': 't', 'ch': 'q', 'ps': 'pusi',
    'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u',
    'k': 'k', 'g': 'g', 'l': 'l', 'r': 'r', 't': 't',
    's': 's', 'm': 'm', 'n': 'n', 'd': 'd'
}


def transliterate(word, mapping):
    w = word.lower()
    # ordenar claves por longitud descendente
    for key in sorted(mapping.keys(), key=lambda x: len(x), reverse=True):
        w = w.replace(key, mapping[key])
    return w


def to_devanagari(word):
    return transliterate(word, DEVANAGARI_MAP)


def to_arabic(word):
    return transliterate(word, ARABIC_MAP)


def to_pinyin(word):
    return transliterate(word, PINYIN_MAP)

# -----------------------------
# Progreso: carga/guardar
# -----------------------------

def crear_progreso_base():
    prog = {'per_concept': {}, 'historial': [], 'total_aciertos': 0, 'total_errores': 0, 'created': datetime.utcnow().isoformat()}
    for c in CONCEPTOS:
        prog['per_concept'][c['gr']] = {'weight': 1.0, 'aciertos': 0, 'errores': 0}
    return prog


def cargar_progreso():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return crear_progreso_base()
    else:
        return crear_progreso_base()


def guardar_progreso(prog):
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(prog, f, ensure_ascii=False, indent=2)

# -----------------------------
# Selección espaciada
# -----------------------------

def seleccionar_concepto(prog):
    items = []
    for c in CONCEPTOS:
        w = prog['per_concept'].get(c['gr'], {}).get('weight', 1.0)
        w = max(0.1, float(w))
        count = int(round(w * 10))
        items.extend([c] * max(1, count))
    return random.choice(items) if items else random.choice(CONCEPTOS)


def ajustar_peso(prog, gr, correcto):
    ent = prog['per_concept'].get(gr)
    if not ent:
        prog['per_concept'][gr] = {'weight': 1.0, 'aciertos': 0, 'errores': 0}
        ent = prog['per_concept'][gr]
    if correcto:
        ent['weight'] = max(0.2, ent['weight'] * 0.85)
        ent['aciertos'] += 1
        prog['total_aciertos'] += 1
    else:
        ent['weight'] = min(5.0, ent['weight'] * 1.5)
        ent['errores'] += 1
        prog['total_errores'] += 1

# -----------------------------
# Widget principal
# -----------------------------
class MainWidget(BoxLayout):
    lbl_gr = StringProperty('')
    lbl_es = StringProperty('')
    lbl_en = StringProperty('')
    lbl_note = StringProperty('')
    feedback = StringProperty('')
    total_aciertos = NumericProperty(0)
    total_errores = NumericProperty(0)
    precision_str = StringProperty('0.00 %')
    hist_text = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prog = cargar_progreso()
        self.actual = None
        self.siguiente_concepto()

    def siguiente_concepto(self):
        self.actual = seleccionar_concepto(self.prog)
        self._mostrar_exposicion(self.actual)
        self._limpiar_campos()
        self.feedback = ''

    def _mostrar_exposicion(self, c):
        self.lbl_gr = c['gr']
        self.lbl_es = c['es']
        self.lbl_en = c['en']
        self.lbl_note = c.get('note', '')

    def _limpiar_campos(self):
        self.ids.entry_es.text = ''
        self.ids.entry_en.text = ''
        self.ids.entry_gr.text = ''
        self.ids.frase_es.text = ''
        self.ids.frase_en.text = ''

    def practicar(self):
        # resetea con nuevo concepto
        self.siguiente_concepto()

    def practicar_inverso(self):
        self.actual = seleccionar_concepto(self.prog)
        # mostrar solo significados
        self.lbl_gr = '(escriba el término)'
        self.lbl_es = self.actual['es']
        self.lbl_en = self.actual['en']
        self.lbl_note = self.actual.get('note','')
        self._limpiar_campos()

    def enviar_respuestas(self):
        if not self.actual:
            self.feedback = 'No hay concepto activo.'
            return
        gr = self.actual['gr']
        esp_correct = self.actual['es'].split(',')[0].strip().lower()
        en_correct = self.actual['en'].strip().lower()

        resp_es = self.ids.entry_es.text.strip().lower()
        resp_en = self.ids.entry_en.text.strip().lower()
        resp_gr = self.ids.entry_gr.text.strip().lower()

        ok_es = esp_correct in resp_es
        ok_en = en_correct in resp_en
        ok_gr = (resp_gr == gr)

        msgs = []
        if ok_gr:
            msgs.append('✔ Griego correcto.')
        else:
            msgs.append(f'✘ Griego esperado: {gr}. Revisa la transliteración.')
        if ok_es:
            msgs.append('✔ Español correcto.')
        else:
            msgs.append(f'✘ Español: se esperaba "{self.actual["es"]}". Considera la raíz.')
        if ok_en:
            msgs.append('✔ Inglés correcto.')
        else:
            msgs.append(f'✘ Inglés: se esperaba "{self.actual["en"]}". Busca equivalentes técnicos.')

        frase_es = self.ids.frase_es.text.strip()
        frase_en = self.ids.frase_en.text.strip()
        if frase_es or frase_en:
            self.prog['historial'].append({'tipo':'frase','gr':gr,'frase_es':frase_es,'frase_en':frase_en,'ts':datetime.utcnow().isoformat()})

        correcto_global = ok_gr and ok_es and ok_en
        ajustar_peso(self.prog, gr, correcto_global)
        self.prog['historial'].append({'tipo':'prueba','gr':gr,'ok_gr':ok_gr,'ok_es':ok_es,'ok_en':ok_en,'ts':datetime.utcnow().isoformat()})
        guardar_progreso(self.prog)

        self.feedback = '\n'.join(msgs)
        self._actualizar_estadisticas()

    def mostrar_transliteraciones(self):
        if not self.actual:
            self.feedback = 'Seleccione un concepto primero.'
            return
        gr = self.actual['gr']
        msg = f"Devanagari: {to_devanagari(gr)}\nArábico: {to_arabic(gr)}\nPinyin: {to_pinyin(gr)}"
        self.feedback = msg

    def mostrar_frases(self):
        lines = []
        for e in self.prog['historial']:
            if e.get('tipo') == 'frase':
                lines.append(f"[{e['ts']}] {e['gr']}\nES: {e['frase_es']}\nEN: {e['frase_en']}\n")
        if not lines:
            self.feedback = 'No hay frases registradas.'
        else:
            self.feedback = '\n'.join(lines[:30])

    def _actualizar_estadisticas(self):
        ac = self.prog.get('total_aciertos', 0)
        er = self.prog.get('total_errores', 0)
        total = ac + er
        precision = (ac / total * 100) if total > 0 else 0.0
        self.total_aciertos = ac
        self.total_errores = er
        self.precision_str = f"{precision:.2f} %"

        # hist text
        seen = []
        for it in reversed(self.prog.get('historial', [])):
            g = it.get('gr')
            if g and g not in seen:
                seen.append(g)
                if len(seen) >= 20:
                    break
        self.hist_text = ', '.join(seen)

    def guardar_progreso(self):
        guardar_progreso(self.prog)
        self.feedback = 'Progreso guardado.'
        self._actualizar_estadisticas()

    def reset_progreso(self):
        self.prog = crear_progreso_base()
        guardar_progreso(self.prog)
        self._actualizar_estadisticas()
        self.feedback = 'Progreso reiniciado.'

# -----------------------------
# App
# -----------------------------
class TrilingueKivyApp(App):
    def build(self):
        Builder.load_string(KV)
        return MainWidget()

if __name__ == '__main__':
    TrilingueKivyApp().run








