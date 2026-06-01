#!/usr/bin/env python3
"""
Duolingo-like (simplificado) — Python + Tkinter + SQLite + (pyttsx3 audio optional)

Guarda como: duo_like.py
Ejecuta: python3 duo_like.py

Características:
- Usuarios
- DB SQLite (duo.sqlite)
- Ejercicios: multiple choice, typing, listening (TTS)
- XP, niveles, mastery, spaced repetition simple
- Audio con pyttsx3 (opcional)
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
import os
import random
import datetime
import math

# Optional audio: pyttsx3 (offline TTS)
try:
    import pyttsx3
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False

DB_FILE = "duo.sqlite"

# ------------------------------
# Database setup & helpers
# ------------------------------
def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    first = not os.path.exists(DB_FILE)
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
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY,
        kind TEXT NOT NULL,    -- 'mcq', 'write', 'listen'
        prompt TEXT NOT NULL,
        choices TEXT,          -- JSON-like '||' separated for mcq
        answer TEXT NOT NULL,  -- canonical answer
        language TEXT DEFAULT 'es',
        created_at TEXT NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        exercise_id INTEGER NOT NULL,
        mastery INTEGER NOT NULL DEFAULT 0, -- 0..10
        last_seen TEXT,
        next_due TEXT,
        correct_count INTEGER DEFAULT 0,
        incorrect_count INTEGER DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(exercise_id) REFERENCES exercises(id),
        UNIQUE(user_id, exercise_id)
    )
    """)
    conn.commit()

    if first:
        seed_exercises(conn)
    conn.close()

def seed_exercises(conn):
    # Simple starter exercises; add more as needed
    now = datetime.datetime.utcnow().isoformat()
    samples = [
        ('mcq', "¿Cómo se dice 'hola' en inglés?", "hello||hi||bye||thanks", "hello"),
        ('mcq', "¿Cuál es el plural de 'mouse'?", "mice||mouses||mouse||mices", "mice"),
        ('write', "Traduce al español: 'apple'", None, "manzana"),
        ('write', "Traduce al inglés: 'gracias'", None, "thank you"),
        ('listen', "Escucha y escribe: 'Good morning'", None, "good morning"),
        ('mcq', "Seleccione la traducción de 'perro' al inglés", "cat||dog||bird||cow", "dog"),
        ('write', "Escribe el pasado de 'go' (inglés)", None, "went"),
        ('listen', "Escucha y escribe: 'How are you?'", None, "how are you"),
    ]
    cur = conn.cursor()
    for kind, prompt, choices, answer in samples:
        cur.execute("INSERT INTO exercises (kind,prompt,choices,answer,created_at) VALUES (?, ?, ?, ?, ?)",
                    (kind, prompt, choices, answer, now))
    conn.commit()

# ------------------------------
# XP & Leveling rules
# ------------------------------
def xp_for_correct(kind):
    # reward by difficulty
    return {'mcq': 10, 'write': 20, 'listen': 15}.get(kind, 10)

def level_from_xp(xp):
    # simple leveling: level = floor(sqrt(xp/50)) for gentle curve
    return int(math.sqrt(xp/50)) + 1

# ------------------------------
# Spaced repetition helper
# ------------------------------
def days_until_next(mastery):
    # mastery 0 -> 1 day, mastery 1 -> 1 day, mastery 2 -> 2d, 3->4, 4->7, 5->14, 6->30 ...
    schedule = [1,1,2,4,7,14,30,60,120,240,365]
    idx = min(max(0, mastery), len(schedule)-1)
    return schedule[idx]

# ------------------------------
# TTS wrapper
# ------------------------------
class TTS:
    def __init__(self):
        if TTS_AVAILABLE:
            try:
                self.engine = pyttsx3.init()
                # optional: adjust rate/volume
                self.engine.setProperty('rate', 160)
            except Exception:
                self.engine = None
        else:
            self.engine = None

    def speak(self, text, lang=None):
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception:
                pass

# ------------------------------
# Core app
# ------------------------------
class DuoLikeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Duolike (Python) — Práctica de idiomas")
        self.tts = TTS()
        self.conn = get_conn()
        self.user_id = None

        self.build_ui()
        self.refresh_users()
        self.update_stats()

    def build_ui(self):
        frm = ttk.Frame(self.root, padding=8)
        frm.pack(fill=tk.BOTH, expand=True)

        # Top: user selection
        top = ttk.Frame(frm)
        top.pack(fill=tk.X, pady=4)
        ttk.Label(top, text="Usuario:").pack(side=tk.LEFT)
        self.user_combo = ttk.Combobox(top, state='readonly')
        self.user_combo.pack(side=tk.LEFT, padx=4)
        ttk.Button(top, text="Select", command=self.select_user).pack(side=tk.LEFT, padx=2)
        ttk.Button(top, text="Nuevo usuario", command=self.create_user).pack(side=tk.LEFT, padx=2)

        # Left: practice area
        left = ttk.Frame(frm)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.prompt_label = ttk.Label(left, text="Inicia una sesión", wraplength=500, font=('Helvetica', 14))
        self.prompt_label.pack(pady=8)

        self.choices_frame = ttk.Frame(left)
        self.choices_frame.pack(fill=tk.X, pady=4)

        self.answer_entry = ttk.Entry(left)
        self.answer_entry.pack(fill=tk.X, padx=4, pady=6)
        self.answer_entry.bind("<Return>", lambda e: self.submit_answer())

        submit_row = ttk.Frame(left)
        submit_row.pack(fill=tk.X)
        ttk.Button(submit_row, text="Submit", command=self.submit_answer).pack(side=tk.LEFT)
        ttk.Button(submit_row, text="Hear (Audio)", command=self.play_prompt).pack(side=tk.LEFT, padx=6)
        ttk.Button(submit_row, text="Skip", command=self.skip).pack(side=tk.LEFT, padx=6)

        # Right: stats and controls
        right = ttk.Frame(frm, width=300)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=6)

        stats_box = ttk.LabelFrame(right, text="Estadísticas")
        stats_box.pack(fill=tk.X, pady=4)
        self.stats_text = tk.Text(stats_box, width=36, height=10, state='disabled')
        self.stats_text.pack(fill=tk.X)

        ctrl_box = ttk.LabelFrame(right, text="Controles")
        ctrl_box.pack(fill=tk.X, pady=4)
        ttk.Button(ctrl_box, text="Start Practice", command=self.start_practice).pack(fill=tk.X, pady=2)
        ttk.Button(ctrl_box, text="Ver progreso", command=self.show_progress).pack(fill=tk.X, pady=2)
        ttk.Button(ctrl_box, text="Añadir ejercicio", command=self.add_exercise_dialog).pack(fill=tk.X, pady=2)
        ttk.Button(ctrl_box, text="Exportar progreso", command=self.export_progress).pack(fill=tk.X, pady=2)

        log_box = ttk.LabelFrame(right, text="Registro")
        log_box.pack(fill=tk.BOTH, expand=True, pady=4)
        self.log = tk.Text(log_box, height=10, state='disabled')
        self.log.pack(fill=tk.BOTH, expand=True)

    # ---------------- UI helpers ----------------
    def append_log(self, text):
        self.log['state'] = 'normal'
        ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self.log.insert(tk.END, f"[{ts}] {text}\n")
        self.log.see(tk.END)
        self.log['state'] = 'disabled'

    def refresh_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, username FROM users ORDER BY username")
        rows = cur.fetchall()
        users = [r['username'] for r in rows]
        ids = [r['id'] for r in rows]
        self.user_map = dict(zip(users, ids))
        self.user_combo['values'] = users
        if users:
            self.user_combo.current(0)
            self.user_id = ids[0]
        else:
            self.user_id = None

    def select_user(self):
        sel = self.user_combo.get()
        if not sel:
            messagebox.showwarning("Usuario", "Selecciona un usuario o crea uno nuevo.")
            return
        self.user_id = self.user_map[sel]
        self.append_log(f"Usuario seleccionado: {sel}")
        self.update_stats()

    def create_user(self):
        name = simpledialog.askstring("Nuevo usuario", "Nombre de usuario:", parent=self.root)
        if not name:
            return
        now = datetime.datetime.utcnow().isoformat()
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, xp, created_at) VALUES (?, 0, ?)", (name, now))
            self.conn.commit()
            self.append_log(f"Usuario creado: {name}")
            self.refresh_users()
            self.user_combo.set(name)
            self.select_user()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El nombre de usuario ya existe.")

    # ---------------- Practice flow ----------------
    def start_practice(self):
        if not self.user_id:
            messagebox.showwarning("Usuario", "Selecciona o crea un usuario primero.")
            return
        # prepare a list of due exercises for this user (spaced repetition)
        cur = self.conn.cursor()
        today = datetime.datetime.utcnow().date().isoformat()
        # left join to find exercises without progress or with next_due <= today
        cur.execute("""
            SELECT e.*, p.mastery, p.next_due, p.correct_count, p.incorrect_count
            FROM exercises e
            LEFT JOIN progress p ON e.id = p.exercise_id AND p.user_id = ?
            """, (self.user_id,))
        rows = cur.fetchall()
        due = []
        for r in rows:
            next_due = r['next_due']
            if next_due is None:
                # never seen -> due
                due.append(r)
            else:
                try:
                    nd = datetime.date.fromisoformat(next_due)
                    if nd <= datetime.date.today():
                        due.append(r)
                except Exception:
                    due.append(r)
        if not due:
            messagebox.showinfo("Práctica", "No hay ejercicios programados para hoy. ¡Buen trabajo!")
            return
        random.shuffle(due)
        self.queue = due
        self.current = None
        self.append_log(f"Comienzo de sesión: {len(due)} ejercicios disponibles.")
        self.next_item()

    def next_item(self):
        # clear UI
        for w in self.choices_frame.winfo_children():
            w.destroy()
        self.answer_entry.delete(0, tk.END)
        if not hasattr(self, 'queue') or not self.queue:
            messagebox.showinfo("Fin de sesión", "Has terminado los ejercicios de hoy.")
            self.update_stats()
            return
        r = self.queue.pop(0)
        self.current = r
        kind = r['kind']
        prompt = r['prompt']
        self.prompt_label.config(text=prompt)
        # render choices if mcq
        if kind == 'mcq' and r['choices']:
            choices = r['choices'].split("||")
            random.shuffle(choices)
            self.choice_var = tk.StringVar()
            for c in choices:
                rb = ttk.Radiobutton(self.choices_frame, text=c, variable=self.choice_var, value=c)
                rb.pack(anchor=tk.W)
        else:
            # writing or listening: show entry
            ttk.Label(self.choices_frame, text="(Escribe la respuesta y pulsa Submit)").pack(anchor=tk.W)
        # If listen: play
        if kind == 'listen':
            self.play_prompt()
        # If mcq: focus on radiobuttons; else focus entry
        if kind == 'mcq':
            self.answer_entry.config(state='disabled')
        else:
            self.answer_entry.config(state='normal')
            self.answer_entry.focus_set()

    def play_prompt(self):
        if not self.current:
            return
        # Use TTS to speak the prompt or prompt text
        text = self.current['prompt']
        self.append_log(f"Audio: {text}")
        self.tts.speak(text)

    def submit_answer(self):
        if not self.current:
            return
        kind = self.current['kind']
        correct = False
        user_answer = ""
        if kind == 'mcq':
            if not hasattr(self, 'choice_var') or not self.choice_var.get():
                messagebox.showwarning("Respuesta", "Selecciona una opción.")
                return
            user_answer = self.choice_var.get().strip().lower()
            correct_answer = (self.current['answer'] or "").strip().lower()
            correct = (user_answer == correct_answer)
        else:
            user_answer = self.answer_entry.get().strip().lower()
            correct_answer = (self.current['answer'] or "").strip().lower()
            # normalize whitespace and punctuation lightly
            def norm(s): return " ".join(s.lower().split())
            correct = (norm(user_answer) == norm(correct_answer))
        # update DB: progress & user xp
        self.process_result(correct, user_answer)
        # feedback
        if correct:
            messagebox.showinfo("Correcto", f"Correcto ✓ (+{xp_for_correct(kind)} XP)")
        else:
            messagebox.showerror("Incorrecto", f"Incorrecto ✗\nRespuesta correcta: {self.current['answer']}")
        self.next_item()

    def process_result(self, correct, user_answer):
        cur = self.conn.cursor()
        uid = self.user_id
        exid = self.current['id']
        now = datetime.datetime.utcnow().isoformat()
        # ensure progress row exists
        cur.execute("SELECT * FROM progress WHERE user_id=? AND exercise_id=?", (uid, exid))
        row = cur.fetchone()
        if row is None:
            cur.execute("INSERT INTO progress (user_id, exercise_id, mastery, last_seen, next_due, correct_count, incorrect_count) VALUES (?, ?, 0, ?, ?, 0, 0)",
                        (uid, exid, now, None))
            self.conn.commit()
            cur.execute("SELECT * FROM progress WHERE user_id=? AND exercise_id=?", (uid, exid))
            row = cur.fetchone()
        mastery = row['mastery']
        correct_count = row['correct_count']
        incorrect_count = row['incorrect_count']
        # update counters
        if correct:
            mastery = min(10, mastery + 1)
            correct_count += 1
            # award xp
            xp = xp_for_correct(self.current['kind'])
            cur.execute("UPDATE users SET xp = xp + ? WHERE id = ?", (xp, uid))
            self.append_log(f"Usuario ganó {xp} XP.")
        else:
            mastery = max(0, mastery - 1)
            incorrect_count += 1
        # compute next_due
        days = days_until_next(mastery)
        next_due_date = (datetime.date.today() + datetime.timedelta(days=days)).isoformat()
        cur.execute("""UPDATE progress SET mastery=?, last_seen=?, next_due=?, correct_count=?, incorrect_count=? WHERE id=?""",
                    (mastery, now, next_due_date, correct_count, incorrect_count, row['id']))
        self.conn.commit()
        self.append_log(f"Ejercicio {exid} -> mastery {mastery}, next due {next_due_date}")
        self.update_stats()

    def skip(self):
        # mark last seen but not answered; push to end of queue
        if not self.current: return
        exid = self.current['id']
        self.append_log(f"Ejercicio {exid} omitido")
        self.queue.append(self.current)
        self.next_item()

    # ---------------- Progress / stats / export ----------------
    def update_stats(self):
        if not self.user_id:
            self.stats_text['state'] = 'normal'
            self.stats_text.delete('1.0', tk.END)
            self.stats_text.insert(tk.END, "Ningún usuario seleccionado.")
            self.stats_text['state'] = 'disabled'
            return
        cur = self.conn.cursor()
        cur.execute("SELECT username, xp, created_at FROM users WHERE id=?", (self.user_id,))
        user = cur.fetchone()
        xp = user['xp']
        level = level_from_xp(xp)
        cur.execute("SELECT COUNT(*) as cnt FROM progress WHERE user_id=? AND mastery>=5", (self.user_id,))
        mastered = cur.fetchone()['cnt']
        cur.execute("SELECT COUNT(*) as total FROM progress WHERE user_id=?", (self.user_id,))
        total = cur.fetchone()['total']
        self.stats_text['state'] = 'normal'
        self.stats_text.delete('1.0', tk.END)
        self.stats_text.insert(tk.END, f"Usuario: {user['username']}\n")
        self.stats_text.insert(tk.END, f"XP: {xp}\n")
        self.stats_text.insert(tk.END, f"Nivel: {level}\n")
        self.stats_text.insert(tk.END, f"Ejercicios dominados (mastery>=5): {mastered}/{total}\n")
        self.stats_text.insert(tk.END, f"Creado: {user['created_at']}\n")
        self.stats_text['state'] = 'disabled'

    def show_progress(self):
        if not self.user_id:
            messagebox.showwarning("Usuario", "Selecciona un usuario primero.")
            return
        cur = self.conn.cursor()
        cur.execute("""
            SELECT e.id as eid, e.kind, e.prompt, p.mastery, p.next_due, p.correct_count, p.incorrect_count
            FROM exercises e LEFT JOIN progress p ON e.id=p.exercise_id AND p.user_id=?
            ORDER BY p.mastery DESC NULLS LAST
            """, (self.user_id,))
        rows = cur.fetchall()
        lines = []
        for r in rows:
            mastery = r['mastery'] if r['mastery'] is not None else 0
            nd = r['next_due'] if r['next_due'] is not None else "never"
            lines.append(f"[{r['eid']}] {r['kind']} | mastery={mastery} | next={nd}\n  {r['prompt']}")
        txt = "\n\n".join(lines)
        dlg = tk.Toplevel(self.root)
        dlg.title("Progreso")
        t = tk.Text(dlg, wrap=tk.WORD)
        t.pack(fill=tk.BOTH, expand=True)
        t.insert(tk.END, txt)

    def add_exercise_dialog(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("Añadir ejercicio")
        ttk.Label(dlg, text="Tipo (mcq, write, listen)").pack()
        kind_e = ttk.Entry(dlg); kind_e.pack()
        ttk.Label(dlg, text="Prompt (texto para mostrar o para reproducir)").pack()
        prompt_e = ttk.Entry(dlg); prompt_e.pack()
        ttk.Label(dlg, text="Choices (si mcq) — separar con ||").pack()
        choices_e = ttk.Entry(dlg); choices_e.pack()
        ttk.Label(dlg, text="Respuesta canónica (exacta)").pack()
        answer_e = ttk.Entry(dlg); answer_e.pack()
        def save_it():
            kind = kind_e.get().strip()
            prompt = prompt_e.get().strip()
            choices = choices_e.get().strip() or None
            answer = answer_e.get().strip()
            if not kind or not prompt or not answer:
                messagebox.showwarning("Campos", "Completa tipo, prompt y respuesta.")
                return
            cur = self.conn.cursor()
            now = datetime.datetime.utcnow().isoformat()
            cur.execute("INSERT INTO exercises (kind,prompt,choices,answer,created_at) VALUES (?, ?, ?, ?, ?)",
                        (kind, prompt, choices, answer, now))
            self.conn.commit()
            self.append_log("Ejercicio añadido.")
            dlg.destroy()
        ttk.Button(dlg, text="Guardar", command=save_it).pack()

    def export_progress(self):
        # simple export: write a csv-like summary
        cur = self.conn.cursor()
        cur.execute("SELECT username, xp FROM users WHERE id=?", (self.user_id,))
        user = cur.fetchone()
        cur.execute("""
            SELECT e.id as eid, e.kind, e.prompt, e.answer, p.mastery, p.correct_count, p.incorrect_count, p.next_due
            FROM exercises e LEFT JOIN progress p ON e.id=p.exercise_id AND p.user_id=?
            """, (self.user_id,))
        rows = cur.fetchall()
        fname = f"{user['username']}_progress.txt"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(f"User: {user['username']}\nXP: {user['xp']}\n\n")
            for r in rows:
                f.write(f"ID:{r['eid']} kind:{r['kind']} mastery:{r['mastery']}\nPrompt: {r['prompt']}\nAnswer: {r['answer']}\nCorrect:{r['correct_count']} Incorrect:{r['incorrect_count']} Next:{r['next_due']}\n\n")
        messagebox.showinfo("Exportado", f"Progreso exportado a {fname}")
        self.append_log(f"Exportado progreso a {fname}")

# ------------------------------
# Start app
# ------------------------------
if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    style = ttk.Style(root)
    try:
        style.theme_use('clam')
    except Exception:
        pass
    app = DuoLikeApp(root)
    root.geometry("900x600")
    root.mainloop()
