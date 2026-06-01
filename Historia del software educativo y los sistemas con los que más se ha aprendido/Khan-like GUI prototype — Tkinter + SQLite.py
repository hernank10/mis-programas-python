#!/usr/bin/env python3
"""
Khan-like GUI prototype — Tkinter + SQLite

Guarda como: khan_gui.py
Ejecuta: python3 khan_gui.py

Interfaz gráfica para el prototipo Khan: muestra lecciones (micro-lecciones), progreso,
y ofrece sesiones de práctica con ejercicios (mcq, write). Conserva la DB SQLite del
prototipo por consola y admite TTS opcional con pyttsx3.
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import sqlite3
import os
import datetime
import random
import math
import textwrap

DB = "khan_proto.sqlite"

# Optional TTS
try:
    import pyttsx3
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False

# ---------------- DB helpers ----------------

def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    first = not os.path.exists(DB)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        xp INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        level INTEGER DEFAULT 1,
        created_at TEXT NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY,
        lesson_id INTEGER NOT NULL,
        kind TEXT NOT NULL,
        prompt TEXT NOT NULL,
        choices TEXT,
        answer TEXT NOT NULL,
        hint TEXT,
        created_at TEXT NOT NULL,
        FOREIGN KEY(lesson_id) REFERENCES lessons(id)
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        exercise_id INTEGER NOT NULL,
        mastery INTEGER NOT NULL DEFAULT 0,
        last_seen TEXT,
        next_due TEXT,
        correct_count INTEGER DEFAULT 0,
        incorrect_count INTEGER DEFAULT 0,
        UNIQUE(user_id, exercise_id)
    )
    """)
    conn.commit()
    if first:
        seed(conn)
    conn.close()


def seed(conn):
    cur = conn.cursor()
    now = datetime.datetime.utcnow().isoformat()
    lessons = [
        ("Fracciones: idea básica",
         "Una fracción representa una parte de un entero. Ejemplo: 1/4 es una de cuatro partes iguales. Aprende a sumar fracciones con igual denominador.", 1),
        ("Porcentaje: concepto esencial",
         "Porcentaje es fracción con denominador 100. 25% = 25/100 = 0.25.", 1),
    ]
    for title, content, level in lessons:
        cur.execute("INSERT INTO lessons (title,content,level,created_at) VALUES (?, ?, ?, ?)", (title, content, level, now))
    cur.execute("SELECT id FROM lessons ORDER BY id")
    rows = cur.fetchall()
    if len(rows) >= 2:
        l1 = rows[0]['id']
        l2 = rows[1]['id']
    else:
        l1 = 1
        l2 = 2
    exercises = [
        (l1, 'mcq', "¿Cuál es 1/4 + 1/4?", "1/2||1/4||1/8||2/4", "1/2", "Suma numeradores si denominador igual."),
        (l1, 'write', "Escribe 3/4 + 1/4 en forma simplificada", None, "1", "Suma y simplifica."),
        (l2, 'mcq', "¿Qué es 50% como fracción?", "1/2||1/3||1/4||1/5", "1/2", "Convierte porcentaje a fracción con denominador 100."),
        (l2, 'write', "Convierte 25% a decimal", None, "0.25", "Divide por 100."),
    ]
    for ex in exercises:
        cur.execute("INSERT INTO exercises (lesson_id,kind,prompt,choices,answer,hint,created_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (ex[0], ex[1], ex[2], ex[3], ex[4], ex[5], now))
    conn.commit()

# ---------------- XP / scheduling ----------------

def xp_for_correct(kind):
    return {'mcq': 5, 'write': 12}.get(kind, 5)


def level_from_xp(xp):
    return int(math.sqrt(xp/30)) + 1

SCHEDULE = [1,1,2,4,7,14,30,60,120,240,365]

def days_until_next(mastery):
    idx = min(max(0, mastery), len(SCHEDULE)-1)
    return SCHEDULE[idx]

# ---------------- TTS wrapper ----------------
class TTS:
    def __init__(self):
        if TTS_AVAILABLE:
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', 160)
            except Exception:
                self.engine = None
        else:
            self.engine = None

    def speak(self, text):
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception:
                pass

# ---------------- GUI Application ----------------
class KhanGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Khan Prototype — GUI")
        self.geometry("1000x600")
        self.conn = get_conn()
        self.tts = TTS()
        self.user_id = None
        self.username = None
        self.queue = []
        self.current_ex = None
        self.build_ui()
        self.refresh_users()
        self.refresh_lessons()
        self.update_stats_panel()

    def build_ui(self):
        top = ttk.Frame(self, padding=6)
        top.pack(fill=tk.X)
        ttk.Label(top, text="Usuario:").pack(side=tk.LEFT)
        self.user_combo = ttk.Combobox(top, state='readonly', width=30)
        self.user_combo.pack(side=tk.LEFT, padx=6)
        ttk.Button(top, text="Select", command=self.select_user).pack(side=tk.LEFT)
        ttk.Button(top, text="New", command=self.create_user_dialog).pack(side=tk.LEFT, padx=4)

        main = ttk.Frame(self, padding=6)
        main.pack(fill=tk.BOTH, expand=True)

        # Left: lessons list
        left = ttk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.Y)
        ttk.Label(left, text="Lecciones").pack(anchor=tk.W)
        self.lesson_list = tk.Listbox(left, width=40, height=25)
        self.lesson_list.pack(fill=tk.Y, expand=True)
        btns = ttk.Frame(left)
        btns.pack(fill=tk.X)
        ttk.Button(btns, text="Open", command=self.open_lesson).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(btns, text="Add", command=self.add_lesson_dialog).pack(side=tk.LEFT, fill=tk.X)

        # Center: lesson content & practice area
        center = ttk.Frame(main)
        center.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=8)
        self.lesson_title = ttk.Label(center, text="Selecciona una lección", font=(None,14,'bold'))
        self.lesson_title.pack(anchor=tk.W)
        self.lesson_text = tk.Text(center, height=8, wrap=tk.WORD)
        self.lesson_text.pack(fill=tk.BOTH, expand=False)
        self.lesson_text.config(state='disabled')

        # Practice panel
        practice_frame = ttk.LabelFrame(center, text="Práctica")
        practice_frame.pack(fill=tk.BOTH, expand=True, pady=8)
        self.prompt_label = ttk.Label(practice_frame, text="Pulsa Start Practice para obtener ejercicios", wraplength=500)
        self.prompt_label.pack(pady=6)
        self.choices_frame = ttk.Frame(practice_frame)
        self.choices_frame.pack(fill=tk.X, pady=4)
        self.answer_entry = ttk.Entry(practice_frame)
        self.answer_entry.pack(fill=tk.X, padx=6, pady=4)

        action_row = ttk.Frame(practice_frame)
        action_row.pack(fill=tk.X)
        ttk.Button(action_row, text="Start Practice", command=self.start_practice).pack(side=tk.LEFT)
        ttk.Button(action_row, text="Hear (TTS)", command=self.play_prompt).pack(side=tk.LEFT, padx=4)
        ttk.Button(action_row, text="Submit", command=self.submit_answer).pack(side=tk.LEFT, padx=4)
        ttk.Button(action_row, text="Skip", command=self.skip_exercise).pack(side=tk.LEFT)

        # Right: stats/log
        right = ttk.Frame(main, width=280)
        right.pack(side=tk.LEFT, fill=tk.Y)
        stats_box = ttk.LabelFrame(right, text="Estadísticas")
        stats_box.pack(fill=tk.X, padx=4, pady=4)
        self.stats_text = tk.Text(stats_box, width=34, height=12, state='disabled')
        self.stats_text.pack()

        ttk.Button(right, text="Show Progress", command=self.show_progress_window).pack(fill=tk.X, padx=4)
        ttk.Button(right, text="Export Progress", command=self.export_progress).pack(fill=tk.X, padx=4, pady=4)

        log_box = ttk.LabelFrame(right, text="Registro")
        log_box.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        self.log_text = tk.Text(log_box, state='disabled', height=10)
        self.log_text.pack(fill=tk.BOTH, expand=True)

    # ------------- UI helpers -------------
    def append_log(self, text):
        self.log_text['state'] = 'normal'
        ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self.log_text.insert(tk.END, f"[{ts}] {text}\n")
        self.log_text.see(tk.END)
        self.log_text['state'] = 'disabled'

    def refresh_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT username FROM users ORDER BY username")
        rows = cur.fetchall()
        users = [r['username'] for r in rows]
        self.user_combo['values'] = users
        if users:
            self.user_combo.current(0)
            self.user_id = None

    def create_user_dialog(self):
        name = simpledialog.askstring("Nuevo usuario", "Nombre de usuario:", parent=self)
        if not name:
            return
        cur = self.conn.cursor()
        now = datetime.datetime.utcnow().isoformat()
        try:
            cur.execute("INSERT INTO users (username,xp,created_at) VALUES (?, ?, ?)", (name, 0, now))
            self.conn.commit()
            self.append_log(f"Usuario creado: {name}")
            self.refresh_users()
            self.user_combo.set(name)
            self.select_user()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El usuario ya existe.")

    def select_user(self):
        sel = self.user_combo.get()
        if not sel:
            messagebox.showwarning("Usuario", "Selecciona un usuario.")
            return
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (sel,))
        row = cur.fetchone()
        if row:
            self.user_id = row['id']
            self.username = row['username']
            self.append_log(f"Usuario seleccionado: {self.username}")
            self.update_stats_panel()

    # ------------- Lessons UI -------------
    def refresh_lessons(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, title, level FROM lessons ORDER BY level, id")
        rows = cur.fetchall()
        self.lesson_list.delete(0, tk.END)
        for r in rows:
            self.lesson_list.insert(tk.END, f"[{r['id']}] (L{r['level']}) {r['title']}")

    def open_lesson(self):
        sel = self.lesson_list.curselection()
        if not sel:
            messagebox.showwarning("Lección", "Selecciona una lección.")
            return
        text = self.lesson_list.get(sel[0])
        lid = int(text.split(']')[0].strip('['))
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM lessons WHERE id=?", (lid,))
        r = cur.fetchone()
        if not r:
            return
        self.lesson_title.config(text=r['title'])
        self.lesson_text.config(state='normal')
        self.lesson_text.delete('1.0', tk.END)
        self.lesson_text.insert(tk.END, r['content'])
        self.lesson_text.config(state='disabled')

    def add_lesson_dialog(self):
        dlg = tk.Toplevel(self)
        dlg.title("Añadir lección")
        ttk.Label(dlg, text="Título").pack()
        t_e = ttk.Entry(dlg, width=60)
        t_e.pack()
        ttk.Label(dlg, text="Contenido (micro-lección)").pack()
        c_e = tk.Text(dlg, height=8, width=60)
        c_e.pack()
        ttk.Label(dlg, text="Nivel").pack()
        lvl_e = ttk.Entry(dlg, width=6)
        lvl_e.insert(0, '1')
        lvl_e.pack()
        def save():
            title = t_e.get().strip()
            content = c_e.get('1.0', tk.END).strip()
            try:
                lvl = int(lvl_e.get().strip())
            except:
                lvl = 1
            if not title or not content:
                messagebox.showwarning("Campos", "Completa título y contenido.")
                return
            now = datetime.datetime.utcnow().isoformat()
            cur = self.conn.cursor()
            cur.execute("INSERT INTO lessons (title,content,level,created_at) VALUES (?, ?, ?, ?)", (title, content, lvl, now))
            self.conn.commit()
            dlg.destroy()
            self.refresh_lessons()
            self.append_log(f"Lección añadida: {title}")
        ttk.Button(dlg, text="Guardar", command=save).pack(pady=6)

    # ------------- Practice flow -------------
    def start_practice(self):
        if not self.user_id:
            messagebox.showwarning("Usuario", "Selecciona o crea un usuario primero.")
            return
        self.queue = self.get_due_exercises(limit=12)
        if not self.queue:
            messagebox.showinfo("Práctica", "No hay ejercicios programados para hoy.")
            return
        random.shuffle(self.queue)
        self.next_exercise()
        self.append_log(f"Sesión iniciada: {len(self.queue)} ejercicios disponibles.")

    def get_due_exercises(self, limit=10):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT e.*, p.mastery, p.next_due
            FROM exercises e
            LEFT JOIN progress p ON e.id = p.exercise_id AND p.user_id = ?
            """, (self.user_id,))
        rows = cur.fetchall()
        due = []
        today = datetime.date.today()
        for r in rows:
            nd = r['next_due']
            if nd is None:
                due.append(r)
            else:
                try:
                    ndt = datetime.date.fromisoformat(nd)
                    if ndt <= today:
                        due.append(r)
                except:
                    due.append(r)
        due.sort(key=lambda x: (x['mastery'] if x['mastery'] is not None else 0))
        return due[:limit]

    def next_exercise(self):
        # clear UI
        for w in self.choices_frame.winfo_children():
            w.destroy()
        self.answer_entry.delete(0, tk.END)
        if not self.queue:
            messagebox.showinfo("Sesión", "Has terminado la sesión de práctica.")
            self.current_ex = None
            self.prompt_label.config(text="Sesión terminada")
            self.update_stats_panel()
            return
        ex = self.queue.pop(0)
        self.current_ex = ex
        self.prompt_label.config(text=ex['prompt'])
        kind = ex['kind']
        if kind == 'mcq' and ex['choices']:
            choices = ex['choices'].split('||')
            random.shuffle(choices)
            self.choice_var = tk.StringVar()
            for c in choices:
                rb = ttk.Radiobutton(self.choices_frame, text=c, variable=self.choice_var, value=c)
                rb.pack(anchor=tk.W)
            self.answer_entry.config(state='disabled')
        else:
            self.answer_entry.config(state='normal')
            self.answer_entry.focus_set()
        # auto-play for listen/write? we only speak prompt as option

    def play_prompt(self):
        if not self.current_ex:
            return
        text = self.current_ex['prompt']
        self.append_log(f"TTS: {text}")
        self.tts.speak(text)

    def submit_answer(self):
        if not self.current_ex:
            return
        kind = self.current_ex['kind']
        correct = False
        user_answer = ''
        if kind == 'mcq':
            if not hasattr(self, 'choice_var') or not self.choice_var.get():
                messagebox.showwarning("Respuesta", "Selecciona una opción.")
                return
            user_answer = self.choice_var.get().strip().lower()
            correct = user_answer == (self.current_ex['answer'] or '').strip().lower()
        else:
            user_answer = self.answer_entry.get().strip().lower()
            def norm(s): return " ".join(s.lower().split())
            correct = norm(user_answer) == norm(self.current_ex['answer'] or '')
        if correct:
            messagebox.showinfo("Correcto", f"Correcto ✓ (+{xp_for_correct(kind)} XP)")
            self.on_correct(self.current_ex)
        else:
            messagebox.showerror("Incorrecto", f"Incorrecto ✗\nRespuesta correcta: {self.current_ex['answer']}")
            if self.current_ex['hint']:
                messagebox.showinfo("Pista", self.current_ex['hint'])
            self.on_incorrect(self.current_ex)
        self.next_exercise()

    def skip_exercise(self):
        if not self.current_ex:
            return
        self.queue.append(self.current_ex)
        self.append_log(f"Ejercicio {self.current_ex['id']} omitido")
        self.next_exercise()

    def on_correct(self, ex):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM progress WHERE user_id=? AND exercise_id=?", (self.user_id, ex['id']))
        row = cur.fetchone()
        now = datetime.datetime.utcnow().isoformat()
        if row is None:
            mastery = 1
            next_due = (datetime.date.today() + datetime.timedelta(days=days_until_next(mastery))).isoformat()
            cur.execute("INSERT INTO progress (user_id,exercise_id,mastery,last_seen,next_due,correct_count,incorrect_count) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.user_id, ex['id'], mastery, now, next_due, 1, 0))
        else:
            mastery = min(10, row['mastery'] + 1)
            ndays = days_until_next(mastery)
            next_due = (datetime.date.today() + datetime.timedelta(days=ndays)).isoformat()
            cur.execute("UPDATE progress SET mastery=?, last_seen=?, next_due=?, correct_count=correct_count+1 WHERE id=?", (mastery, now, next_due, row['id']))
        xp = xp_for_correct(ex['kind'])
        cur.execute("UPDATE users SET xp = xp + ? WHERE id = ?", (xp, self.user_id))
        self.conn.commit()
        self.append_log(f"Ejercicio {ex['id']} correcto. mastery={mastery}, next_due={next_due}")
        self.update_stats_panel()

    def on_incorrect(self, ex):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM progress WHERE user_id=? AND exercise_id=?", (self.user_id, ex['id']))
        row = cur.fetchone()
        now = datetime.datetime.utcnow().isoformat()
        if row is None:
            mastery = 0
            next_due = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
            cur.execute("INSERT INTO progress (user_id,exercise_id,mastery,last_seen,next_due,correct_count,incorrect_count) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.user_id, ex['id'], mastery, now, next_due, 0, 1))
        else:
            mastery = max(0, row['mastery'] - 1)
            ndays = days_until_next(mastery)
            next_due = (datetime.date.today() + datetime.timedelta(days=ndays)).isoformat()
            cur.execute("UPDATE progress SET mastery=?, last_seen=?, next_due=?, incorrect_count=incorrect_count+1 WHERE id=?", (mastery, now, next_due, row['id']))
        self.conn.commit()
        self.append_log(f"Ejercicio {ex['id']} incorrecto. mastery={mastery}, next_due={next_due}")
        self.update_stats_panel()

    # ------------- Progress / export -------------
    def update_stats_panel(self):
        self.stats_text['state'] = 'normal'
        self.stats_text.delete('1.0', tk.END)
        if not self.user_id:
            self.stats_text.insert(tk.END, "Ningún usuario seleccionado.\n")
            self.stats_text['state'] = 'disabled'
            return
        cur = self.conn.cursor()
        cur.execute("SELECT username,xp,created_at FROM users WHERE id=?", (self.user_id,))
        u = cur.fetchone()
        level = level_from_xp(u['xp'])
        cur.execute("SELECT COUNT(*) as total FROM exercises")
        total = cur.fetchone()['total']
        cur.execute("SELECT COUNT(*) as mastered FROM progress WHERE user_id=? AND mastery>=5", (self.user_id,))
        mastered = cur.fetchone()['mastered']
        self.stats_text.insert(tk.END, f"Usuario: {u['username']}\n")
        self.stats_text.insert(tk.END, f"XP: {u['xp']}\nNivel: {level}\n\n")
        self.stats_text.insert(tk.END, f"Ejercicios totales: {total}\nDominados (>=5): {mastered}\n")
        self.stats_text['state'] = 'disabled'

    def show_progress_window(self):
        if not self.user_id:
            messagebox.showwarning("Usuario", "Selecciona un usuario.")
            return
        dlg = tk.Toplevel(self)
        dlg.title("Progreso del usuario")
        t = tk.Text(dlg, wrap=tk.WORD)
        t.pack(fill=tk.BOTH, expand=True)
        cur = self.conn.cursor()
        cur.execute("SELECT e.id as eid, e.prompt, p.mastery, p.next_due, p.correct_count, p.incorrect_count FROM exercises e LEFT JOIN progress p ON e.id=p.exercise_id AND p.user_id=? ORDER BY p.mastery DESC NULLS LAST", (self.user_id,))
        rows = cur.fetchall()
        for r in rows:
            mastery = r['mastery'] if r['mastery'] is not None else 0
            nd = r['next_due'] if r['next_due'] else 'never'
            t.insert(t.END, f"Ex {r['eid']}: mastery={mastery} next={nd} correct={r['correct_count']} incorrect={r['incorrect_count']}\nPrompt: {r['prompt']}\n\n")

    def export_progress(self):
        if not self.user_id:
            messagebox.showwarning("Usuario", "Selecciona un usuario.")
            return
        fn = filedialog.asksaveasfilename(defaultextension='.txt', initialfile=f"{self.username}_progress.txt")
        if not fn:
            return
        cur = self.conn.cursor()
        cur.execute("SELECT username,xp FROM users WHERE id=?", (self.user_id,))
        u = cur.fetchone()
        cur.execute("SELECT e.id as eid, e.prompt, p.mastery, p.next_due, p.correct_count, p.incorrect_count FROM exercises e LEFT JOIN progress p ON e.id=p.exercise_id AND p.user_id=?", (self.user_id,))
        rows = cur.fetchall()
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(f"Progreso de {u['username']}\nXP: {u['xp']}\n\n")
            for r in rows:
                f.write(f"Ex {r['eid']}: mastery={r['mastery']} next={r['next_due']} correct={r['correct_count']} incorrect={r['incorrect_count']}\nPrompt: {r['prompt']}\n\n")
        messagebox.showinfo("Exportado", f"Progreso exportado a {fn}")
        self.append_log(f"Exportado progreso a {fn}")

# ---------------- Entry point ----------------
if __name__ == '__main__':
    init_db()
    app = KhanGUI()
    app.mainloop()
