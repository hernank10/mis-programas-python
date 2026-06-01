"""
Aplicación Tkinter: Sistema Trilingüe de Espiral de Aprendizaje
Archivo: app_trilingue_tkinter.py

Descripción:
- Interfaz gráfica con Tkinter que implementa los principios:
  Exposición multimodal, Práctica activa, Contextualización,
  Espaciado (repetición distrib.), Retroalimentación con explicaciones,
  Metacognición (estadísticas de progreso).
- Guarda el progreso en 'progress.json' en la carpeta local.

Cómo usar:
1. Guardar este archivo como `app_trilingue_tkinter.py`.
2. Ejecutar: python app_trilingue_tkinter.py

Requisitos: Python 3.x (la librería tkinter incluida en la mayoría de distribuciones).
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import json
import os
from datetime import datetime

# -----------------------------
# Datos: conceptos y notas
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

PROGRESS_FILE = "progress.json"

# -----------------------------
# Utilidades de guardado/carga
# -----------------------------

def cargar_progreso():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return crear_progreso_base()
    else:
        return crear_progreso_base()


def crear_progreso_base():
    progreso = {
        "per_concept": {},
        "historial": [],
        "total_aciertos": 0,
        "total_errores": 0,
        "created_at": datetime.utcnow().isoformat()
    }
    for c in CONCEPTOS:
        progreso["per_concept"][c["gr"]] = {"weight": 1.0, "aciertos": 0, "errores": 0}
    return progreso


def guardar_progreso(data):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# -----------------------------
# Lógica de selección espaciada
# -----------------------------

def seleccionar_concepto(progreso):
    # Construir lista ponderada según weight
    items = []
    for c in CONCEPTOS:
        w = progreso["per_concept"].get(c["gr"], {}).get("weight", 1.0)
        # evitar weights nulos
        w = max(0.1, float(w))
        items.extend([c] * int(round(w * 10)))
    if not items:
        return random.choice(CONCEPTOS)
    return random.choice(items)


def ajustar_peso(progreso, gr, correcto):
    entry = progreso["per_concept"].get(gr)
    if not entry:
        progreso["per_concept"][gr] = {"weight": 1.0, "aciertos": 0, "errores": 0}
        entry = progreso["per_concept"][gr]

    if correcto:
        # disminuir peso ligeramente para espaciar
        entry["weight"] = max(0.2, entry["weight"] * 0.85)
        entry["aciertos"] += 1
        progreso["total_aciertos"] += 1
    else:
        # aumentar peso para repetir más
        entry["weight"] = min(5.0, entry["weight"] * 1.5)
        entry["errores"] += 1
        progreso["total_errores"] += 1


# -----------------------------
# Interfaz Tkinter
# -----------------------------

class TrilingueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Trilingüe - Espiral de Aprendizaje")
        self.geometry("900x600")
        self.resizable(True, True)

        # Cargar progreso
        self.progreso = cargar_progreso()

        # Estado actual
        self.actual = None  # concepto actual

        # Crear GUI
        self._crear_widgets()

        # Actualizar panel de estadísticas
        self._actualizar_panel_estadisticas()

    def _crear_widgets(self):
        # panel izquierdo: menú y controls
        left = ttk.Frame(self, padding=(10, 10))
        left.pack(side=tk.LEFT, fill=tk.Y)

        # Botones principales
        ttk.Label(left, text="Acciones", font=(None, 12, "bold")).pack(pady=(0,6))
        ttk.Button(left, text="Practicar (griego → es/en)", command=self._practicar).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="Practicar inverso (es/en → griego)", command=self._practicar_inverso).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="Ver frases creadas", command=self._mostrar_frases).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="Guardar progreso", command=lambda: guardar_progreso(self.progreso)).pack(fill=tk.X, pady=4)
        ttk.Button(left, text="Reiniciar progreso", command=self._reset_progreso).pack(fill=tk.X, pady=4)
        ttk.Separator(left, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=8)

        # Panel de ayuda / sugerencias
        ttk.Label(left, text="Sugerencia:", font=(None, 10, "bold")).pack(anchor=tk.W)
        help_text = "Siga la espiral: escriba siempre; cree frases; revise estadísticas." 
        ttk.Label(left, text=help_text, wraplength=200).pack(pady=(0,8))

        # panel derecho: contenido principal
        right = ttk.Frame(self, padding=(10,10))
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Exposición multimodal
        exp_frame = ttk.LabelFrame(right, text="Exposición Multimodal")
        exp_frame.pack(fill=tk.X, pady=(0,8))

        self.lbl_gr = ttk.Label(exp_frame, text="Griego: ", font=(None, 12, "bold"))
        self.lbl_gr.grid(row=0, column=0, sticky=tk.W, padx=6, pady=4)
        self.lbl_es = ttk.Label(exp_frame, text="Español: ")
        self.lbl_es.grid(row=1, column=0, sticky=tk.W, padx=6)
        self.lbl_en = ttk.Label(exp_frame, text="Inglés: ")
        self.lbl_en.grid(row=2, column=0, sticky=tk.W, padx=6)
        self.lbl_note = ttk.Label(exp_frame, text="Nota cultural: ", wraplength=600)
        self.lbl_note.grid(row=3, column=0, columnspan=3, sticky=tk.W, padx=6, pady=6)

        # Área de práctica
        prac_frame = ttk.LabelFrame(right, text="Práctica activa")
        prac_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(prac_frame, text="Ingrese respuestas (escriba siempre):").pack(anchor=tk.W, padx=6, pady=(6,0))

        form = ttk.Frame(prac_frame)
        form.pack(fill=tk.X, padx=6, pady=6)

        ttk.Label(form, text="Español:").grid(row=0, column=0, sticky=tk.W, pady=4)
        self.entry_es = ttk.Entry(form, width=60)
        self.entry_es.grid(row=0, column=1, sticky=tk.W, padx=6)

        ttk.Label(form, text="Inglés:").grid(row=1, column=0, sticky=tk.W, pady=4)
        self.entry_en = ttk.Entry(form, width=60)
        self.entry_en.grid(row=1, column=1, sticky=tk.W, padx=6)

        ttk.Label(form, text="Griego (transliterado):").grid(row=2, column=0, sticky=tk.W, pady=4)
        self.entry_gr = ttk.Entry(form, width=30)
        self.entry_gr.grid(row=2, column=1, sticky=tk.W, padx=6)

        ttk.Label(prac_frame, text="Contextualización: escriba frases reales").pack(anchor=tk.W, padx=6)
        self.txt_frase_es = scrolledtext.ScrolledText(prac_frame, height=4)
        self.txt_frase_es.pack(fill=tk.X, padx=6, pady=(4,6))
        self.txt_frase_en = scrolledtext.ScrolledText(prac_frame, height=4)
        self.txt_frase_en.pack(fill=tk.X, padx=6, pady=(0,6))

        # Botones de acciones
        btns = ttk.Frame(prac_frame)
        btns.pack(fill=tk.X, padx=6, pady=(4,6))
        self.btn_submit = ttk.Button(btns, text="Enviar respuestas", command=self._enviar_respuestas)
        self.btn_submit.pack(side=tk.LEFT)
        self.btn_skip = ttk.Button(btns, text="Siguiente concepto", command=self._siguiente_concepto)
        self.btn_skip.pack(side=tk.LEFT, padx=6)

        # Retroalimentación inmediata
        self.lbl_feedback = ttk.Label(prac_frame, text="Feedback:", foreground="blue", wraplength=700)
        self.lbl_feedback.pack(fill=tk.X, padx=6, pady=6)

        # Panel inferior: estadísticas
        stats_frame = ttk.LabelFrame(right, text="Metacognición y progreso")
        stats_frame.pack(fill=tk.X, pady=(8,0))

        self.lbl_aciertos = ttk.Label(stats_frame, text="Aciertos: 0")
        self.lbl_aciertos.grid(row=0, column=0, padx=6, pady=4)
        self.lbl_errores = ttk.Label(stats_frame, text="Errores: 0")
        self.lbl_errores.grid(row=0, column=1, padx=6, pady=4)
        self.lbl_precision = ttk.Label(stats_frame, text="Precisión: 0.00 %")
        self.lbl_precision.grid(row=0, column=2, padx=6, pady=4)

        ttk.Label(stats_frame, text="Conceptos revisados:").grid(row=1, column=0, sticky=tk.W, padx=6)
        self.lst_hist = tk.Listbox(stats_frame, height=4)
        self.lst_hist.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E, padx=6, pady=(0,6))

        # Inicializar primer concepto
        self._siguiente_concepto()

    # -------------------------
    # Funciones de flujo
    # -------------------------
    def _siguiente_concepto(self):
        self.actual = seleccionar_concepto(self.progreso)
        self._mostrar_exposicion(self.actual)
        self._limpiar_entradas()
        self.lbl_feedback.config(text="")

    def _mostrar_exposicion(self, concepto):
        self.lbl_gr.config(text=f"Griego: {concepto['gr']}")
        self.lbl_es.config(text=f"Español: {concepto['es']}")
        self.lbl_en.config(text=f"Inglés: {concepto['en']}")
        self.lbl_note.config(text=f"Nota cultural: {concepto['note']}")

    def _limpiar_entradas(self):
        self.entry_es.delete(0, tk.END)
        self.entry_en.delete(0, tk.END)
        self.entry_gr.delete(0, tk.END)
        self.txt_frase_es.delete(1.0, tk.END)
        self.txt_frase_en.delete(1.0, tk.END)

    def _enviar_respuestas(self):
        if not self.actual:
            messagebox.showwarning("Atención", "No hay un concepto activo.")
            return

        gr = self.actual['gr']
        esp_correcta = self.actual['es'].split(',')[0].strip().lower()
        en_correcta = self.actual['en'].strip().lower()

        resp_es = self.entry_es.get().strip().lower()
        resp_en = self.entry_en.get().strip().lower()
        resp_gr = self.entry_gr.get().strip().lower()

        # Evaluaciones simples
        ok_es = esp_correcta in resp_es
        ok_en = en_correcta in resp_en
        ok_gr = (resp_gr == gr)

        feedback_msgs = []

        if ok_gr:
            feedback_msgs.append("✔ Griego transliterado correcto.")
        else:
            feedback_msgs.append(f"✘ Griego esperado: {gr} — Intenta recordar la transliteración.")

        if ok_es:
            feedback_msgs.append("✔ Español correcto.")
        else:
            feedback_msgs.append(f"✘ Español: se esperaba '{self.actual['es']}'. Considera la raíz y el contexto.")

        if ok_en:
            feedback_msgs.append("✔ Inglés correcto.")
        else:
            feedback_msgs.append(f"✘ Inglés: se esperaba '{self.actual['en']}'. Busque equivalentes técnicos (ej.: 'flourishing').")

        # Guardar frases/contextos si usuario escribió algo
        frase_es = self.txt_frase_es.get(1.0, tk.END).strip()
        frase_en = self.txt_frase_en.get(1.0, tk.END).strip()
        if frase_es or frase_en:
            self.progreso['historial'].append({
                'tipo': 'frase', 'gr': gr, 'frase_es': frase_es, 'frase_en': frase_en, 'ts': datetime.utcnow().isoformat()
            })

        # Ajustar pesos según aciertos
        correcto_global = ok_gr and ok_es and ok_en
        ajustar_peso(self.progreso, gr, correcto_global)

        # Actualizar estadísticas
        self.progreso['historial'].append({'tipo': 'prueba', 'gr': gr, 'ok_gr': ok_gr, 'ok_es': ok_es, 'ok_en': ok_en, 'ts': datetime.utcnow().isoformat()})
        guardar_progreso(self.progreso)

        # Mostrar feedback
        self.lbl_feedback.config(text="\n".join(feedback_msgs))

        # Actualizar panel de estadísticas
        self._actualizar_panel_estadisticas()

    def _practicar(self):
        # Mismo que siguiente pero resetea entradas
        self._siguiente_concepto()

    def _practicar_inverso(self):
        # Llenar exposicion con sólo significados y pedir griego
        self.actual = seleccionar_concepto(self.progreso)
        self.lbl_gr.config(text="Griego: (escriba el término) ")
        self.lbl_es.config(text=f"Español: {self.actual['es']}")
        self.lbl_en.config(text=f"Inglés: {self.actual['en']}")
        self.lbl_note.config(text=f"Nota cultural: {self.actual['note']}")
        self._limpiar_entradas()

    def _mostrar_frases(self):
        # Mostrar ventana con frases guardadas
        win = tk.Toplevel(self)
        win.title("Frases creadas")
        win.geometry("700x500")
        txt = scrolledtext.ScrolledText(win)
        txt.pack(fill=tk.BOTH, expand=True)

        lines = []
        for e in self.progreso['historial']:
            if e.get('tipo') == 'frase':
                lines.append(f"[{e['ts']}] {e['gr']}\nES: {e['frase_es']}\nEN: {e['frase_en']}\n")
        if not lines:
            txt.insert(tk.END, "No hay frases registradas todavía.\n")
        else:
            txt.insert(tk.END, "\n\n".join(lines))

    def _actualizar_panel_estadisticas(self):
        ac = self.progreso.get('total_aciertos', 0)
        er = self.progreso.get('total_errores', 0)
        total = ac + er
        precision = (ac / total * 100) if total > 0 else 0.0

        self.lbl_aciertos.config(text=f"Aciertos: {ac}")
        self.lbl_errores.config(text=f"Errores: {er}")
        self.lbl_precision.config(text=f"Precisión: {precision:.2f} %")

        # Lista de conceptos revisados
        self.lst_hist.delete(0, tk.END)
        seen = set()
        for item in reversed(self.progreso.get('historial', [])):
            gr = item.get('gr')
            if gr and gr not in seen:
                seen.add(gr)
                self.lst_hist.insert(tk.END, gr)
                if len(seen) >= 20:
                    break

    def _reset_progreso(self):
        if messagebox.askyesno("Confirmar", "¿Desea reiniciar todo el progreso? Esto no se puede deshacer."):
            self.progreso = crear_progreso_base()
            guardar_progreso(self.progreso)
            self._actualizar_panel_estadisticas()
            messagebox.showinfo("Listo", "Progreso reiniciado.")


# -----------------------------
# Ejecutar aplicación
# -----------------------------

if __name__ == '__main__':
    app = TrilingueApp()
    app.mainloop()
