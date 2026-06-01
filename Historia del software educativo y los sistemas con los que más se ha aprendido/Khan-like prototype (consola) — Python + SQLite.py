#!/usr/bin/env python3
"""
Khan-like prototype (consola) — Python + SQLite

Guarda como: khan_proto.py
Ejecuta: python3 khan_proto.py

Características:
- Usuarios
- Lecciones (micro-lección textual)
- Ejercicios (mcq, write)
- XP y niveles
- Spaced repetition simple con mastery 0..10
- CLI interactivo
"""
import sqlite3
import os
import datetime
import random
import math
import textwrap

DB = "khan_proto.sqlite"

# -------------------------
# DB helpers
# -------------------------
def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    first = not os.path.exists(DB)
    conn = get_conn()
    cur = conn.cursor()
    # users
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        xp INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL
    )
    """)
    # lessons
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        level INTEGER DEFAULT 1,
        created_at TEXT NOT NULL
    )
    """)
    # exercises
    cur.execute("""
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY,
        lesson_id INTEGER NOT NULL,
        kind TEXT NOT NULL,       -- mcq, write
        prompt TEXT NOT NULL,
        choices TEXT,             -- for mcq, '||' separated
        answer TEXT NOT NULL,
        hint TEXT,
        created_at TEXT NOT NULL,
        FOREIGN KEY(lesson_id) REFERENCES lessons(id)
    )
    """)
    # progress per user/exercise
    cur.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        exercise_id INTEGER NOT NULL,
        mastery INTEGER NOT NULL DEFAULT 0,   -- 0..10
        last_seen TEXT,
        next_due TEXT,
        correct_count INTEGER DEFAULT 0,
        incorrect_count INTEGER DEFAULT 0,
        UNIQUE(user_id, exercise_id),
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(exercise_id) REFERENCES exercises(id)
    )
    """)
    conn.commit()
    if first:
        seed(conn)
    conn.close()

# -------------------------
# Seed content (ejemplos)
# -------------------------
def seed(conn):
    cur = conn.cursor()
    now = datetime.datetime.utcnow().isoformat()
    lessons = [
        ("Fracciones: idea básica",
         "Una fracción representa una parte de un entero. Ejemplo: 1/4 es una de cuatro partes iguales. Aprende a sumar fracciones con igual denominador."),
         # level 1
    ]
    cur.execute("INSERT INTO lessons (title,content,level,created_at) VALUES (?, ?, ?, ?)",
                ("Fracciones: idea básica",
                 "Una fracción representa una parte de un entero. Ejemplo: 1/4 es una de cuatro partes iguales. Aprende a sumar fracciones con igual denominador.", 1, now))
    cur.execute("INSERT INTO lessons (title,content,level,created_at) VALUES (?, ?, ?, ?)",
                ("Porcentaje: concepto esencial",
                 "Porcentaje es fracción con denominador 100. 25% = 25/100 = 0.25.", 1, now))
    # fetch ids
    cur.execute("SELECT id FROM lessons ORDER BY id")
    lesson_rows = cur.fetchall()
    l1 = lesson_rows[0]['id']
    l2 = lesson_rows[1]['id']
    # exercises sample
    exercises = [
        (l1, 'mcq', "¿Cuál es 1/4 + 1/4?", "1/2||1/4||1/8||2/4", "1/2", "Suma numeradores si denominador igual."),
        (l1, 'write', "Escribe 3/4 + 1/4 en forma simplificada", None, "1", "Suma y simplifica."),
        (l2, 'mcq', "¿Qué es 50% como fracción?", "1/2||1/3||1/4||1/5", "1/2", "Convierte porcentaje a fracción con denominador 100."),
        (l2, 'write', "Convierte 25% a decimal", None, "0.25", "Divide por 100."),
    ]
    for ex in exercises:
        cur.execute("INSERT INTO exercises (lesson_id,kind,prompt,choices,answer,hint,created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (ex[0], ex[1], ex[2], ex[3], ex[4], ex[5], now))
    conn.commit()

# -------------------------
# XP and leveling
# -------------------------
def xp_for_correct(kind):
    return {'mcq': 5, 'write': 12}.get(kind, 5)

def level_from_xp(xp):
    # gentle progression
    return int(math.sqrt(xp/30)) + 1

# -------------------------
# Spaced repetition schedule
# -------------------------
SCHEDULE = [1,1,2,4,7,14,30,60,120,240,365]  # days
def days_until_next(mastery):
    idx = min(max(0, mastery), len(SCHEDULE)-1)
    return SCHEDULE[idx]

# -------------------------
# CLI and app logic
# -------------------------
class KhanProto:
    def __init__(self):
        init_db()
        self.conn = get_conn()
        self.user_id = None
        self.username = None

    # -------------
    # User methods
    # -------------
    def create_user(self, name):
        cur = self.conn.cursor()
        now = datetime.datetime.utcnow().isoformat()
        try:
            cur.execute("INSERT INTO users (username,xp,created_at) VALUES (?, ?, ?)", (name, 0, now))
            self.conn.commit()
            print(f"Usuario '{name}' creado.")
        except Exception as e:
            print("Error:", e)

    def select_user(self, name):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (name,))
        row = cur.fetchone()
        if not row:
            print("Usuario no existe.")
            return False
        self.user_id = row['id']
        self.username = row['username']
        print(f"Sesión iniciada: {self.username}")
        return True

    def list_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT username, xp, created_at FROM users ORDER BY username")
        rows = cur.fetchall()
        if not rows:
            print("No hay usuarios.")
            return
        for r in rows:
            print(f"- {r['username']}: XP={r['xp']} creado {r['created_at']}")

    # -------------
    # Lessons/exercises
    # -------------
    def list_lessons(self, level=None):
        cur = self.conn.cursor()
        if level:
            cur.execute("SELECT id, title, level FROM lessons WHERE level=? ORDER BY id", (level,))
        else:
            cur.execute("SELECT id, title, level FROM lessons ORDER BY level, id")
        rows = cur.fetchall()
        for r in rows:
            print(f"[{r['id']}] (L{r['level']}) {r['title']}")

    def show_lesson(self, lesson_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM lessons WHERE id=?", (lesson_id,))
        r = cur.fetchone()
        if not r:
            print("Lección no encontrada.")
            return
        print(f"\n== {r['title']} (Nivel {r['level']}) ==\n")
        print(textwrap.fill(r['content'], 80))
        print("\n-- Ejercicios asociados --")
        cur.execute("SELECT id, kind, prompt FROM exercises WHERE lesson_id=?", (lesson_id,))
        for ex in cur.fetchall():
            print(f"  [{ex['id']}] {ex['kind']} - {ex['prompt'][:60]}...")

    def add_lesson(self, title, content, level=1):
        now = datetime.datetime.utcnow().isoformat()
        cur = self.conn.cursor()
        cur.execute("INSERT INTO lessons (title,content,level,created_at) VALUES (?, ?, ?, ?)", (title, content, level, now))
        self.conn.commit()
        print("Lección añadida.")

    def add_exercise(self, lesson_id, kind, prompt, answer, choices=None, hint=None):
        now = datetime.datetime.utcnow().isoformat()
        cur = self.conn.cursor()
        cur.execute("INSERT INTO exercises (lesson_id,kind,prompt,choices,answer,hint,created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (lesson_id, kind, prompt, choices, answer, hint, now))
        self.conn.commit()
        print("Ejercicio añadido.")

    # -------------
    # Practice flow
    # -------------
    def get_due_exercises(self, limit=10):
        # returns a list of exercise rows that are due for this user
        cur = self.conn.cursor()
        # all exercises left-join progress
        cur.execute("""
            SELECT e.*, p.mastery, p.next_due, p.correct_count, p.incorrect_count, p.id as progress_id
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
        # simple prioritization: lower mastery first
        random.shuffle(due)
        due.sort(key=lambda x: (x['mastery'] if x['mastery'] is not None else 0))
        return due[:limit]

    def practice_session(self, n=10):
        if not self.user_id:
            print("Selecciona un usuario antes de practicar.")
            return
        due = self.get_due_exercises(limit=n)
        if not due:
            print("No hay ejercicios programados para hoy. ¡Buen trabajo!")
            return
        print(f"Iniciando sesión de práctica: {len(due)} ejercicios")
        for ex in due:
            self.present_exercise(ex)

    def present_exercise(self, ex):
        print("\n--- EJERCICIO ---")
        print(f"ID: {ex['id']} | Tipo: {ex['kind']}")
        print(textwrap.fill(ex['prompt'], 80))
        if ex['kind'] == 'mcq' and ex['choices']:
            choices = ex['choices'].split('||')
            random.shuffle(choices)
            for i, c in enumerate(choices, 1):
                print(f"  {i}. {c}")
            ans = input("Elige número (o escribe tu respuesta): ").strip()
            try:
                idx = int(ans) - 1
                user_resp = choices[idx].strip().lower()
            except:
                user_resp = ans.strip().lower()
            correct = user_resp == ex['answer'].strip().lower()
        elif ex['kind'] == 'write':
            user_resp = input("Escribe tu respuesta: ").strip().lower()
            # normalize whitespace/punctuation minimal
            def norm(s): return " ".join(s.lower().split())
            correct = norm(user_resp) == norm(ex['answer'])
        else:
            print("Tipo de ejercicio no soportado.")
            return
        # feedback
        if correct:
            print("✓ Correcto!")
            self.on_correct(ex)
        else:
            print("✗ Incorrecto.")
            print("Respuesta correcta:", ex['answer'])
            if ex['hint']:
                print("Pista:", ex['hint'])
            self.on_incorrect(ex)
        # small pause
        # update user stats in DB
        self.update_user_stats()

    def on_correct(self, ex):
        cur = self.conn.cursor()
        # ensure progress row exists
        cur.execute("SELECT * FROM progress WHERE user_id=? AND exercise_id=?", (self.user_id, ex['id']))
        row = cur.fetchone()
        now = datetime.datetime.utcnow().isoformat()
        if row is None:
            cur.execute("INSERT INTO progress (user_id,exercise_id,mastery,last_seen,next_due,correct_count,incorrect_count) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (self.user_id, ex['id'], 1, now, (datetime.date.today() + datetime.timedelta(days=days_until_next(1))).isoformat(), 1, 0))
            mastery = 1
        else:
            mastery = min(10, row['mastery'] + 1)
            ndays = days_until_next(mastery)
            next_due = (datetime.date.today() + datetime.timedelta(days=ndays)).isoformat()
            cur.execute("UPDATE progress SET mastery=?, last_seen=?, next_due=?, correct_count=correct_count+1 WHERE id=?", (mastery, now, next_due, row['id']))
        # award xp
        xp = xp_for_correct(ex['kind'])
        cur.execute("UPDATE users SET xp = xp + ? WHERE id = ?", (xp, self.user_id))
        self.conn.commit()
        print(f"Has ganado {xp} XP. Mastery ahora {mastery}")

    def on_incorrect(self, ex):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM progress WHERE user_id=? AND exercise_id=?", (self.user_id, ex['id']))
        row = cur.fetchone()
        now = datetime.datetime.utcnow().isoformat()
        if row is None:
            # create with mastery 0 and next due tomorrow
            cur.execute("INSERT INTO progress (user_id,exercise_id,mastery,last_seen,next_due,correct_count,incorrect_count) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (self.user_id, ex['id'], 0, now, (datetime.date.today() + datetime.timedelta(days=1)).isoformat(), 0, 1))
            mastery = 0
        else:
            mastery = max(0, row['mastery'] - 1)
            ndays = days_until_next(mastery)
            next_due = (datetime.date.today() + datetime.timedelta(days=ndays)).isoformat()
            cur.execute("UPDATE progress SET mastery=?, last_seen=?, next_due=?, incorrect_count=incorrect_count+1 WHERE id=?", (mastery, now, next_due, row['id']))
        self.conn.commit()
        print(f"Mastery ajustado a {mastery}. Volverás a ver este ejercicio pronto.")

    # -------------
    # Progress / stats
    # -------------
    def show_stats(self):
        if not self.user_id:
            print("Selecciona un usuario.")
            return
        cur = self.conn.cursor()
        cur.execute("SELECT username, xp, created_at FROM users WHERE id=?", (self.user_id,))
        u = cur.fetchone()
        level = level_from_xp(u['xp'])
        print(f"Usuario: {u['username']} | XP: {u['xp']} | Nivel estimado: {level} | Creado: {u['created_at']}\n")
        # mastery summary
        cur.execute("SELECT COUNT(*) as total FROM exercises")
        total = cur.fetchone()['total']
        cur.execute("SELECT COUNT(*) as mstr FROM progress WHERE user_id=? AND mastery>=5", (self.user_id,))
        mastered = cur.fetchone()['mstr']
        cur.execute("SELECT COUNT(*) as due FROM progress WHERE user_id=? AND next_due<=?", (self.user_id, datetime.date.today().isoformat()))
        due = cur.fetchone()['due']
        print(f"Ejercicios totales: {total} | Dominados (>=5): {mastered} | Debidos hoy: {due}")

    def export_progress(self, filename=None):
        if not self.user_id:
            print("Selecciona un usuario.")
            return
        if not filename:
            filename = f"{self.username}_progress.txt"
        cur = self.conn.cursor()
        cur.execute("SELECT e.id as eid, e.prompt, p.mastery, p.next_due, p.correct_count, p.incorrect_count FROM exercises e LEFT JOIN progress p ON e.id=p.exercise_id AND p.user_id=? ORDER BY p.mastery DESC NULLS LAST", (self.user_id,))
        rows = cur.fetchall()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Progreso de {self.username}\n\n")
            for r in rows:
                f.write(f"Ex {r['eid']}: mastery={r['mastery']} next={r['next_due']} correct={r['correct_count']} incorrect={r['incorrect_count']}\nPrompt: {r['prompt']}\n\n")
        print(f"Exportado a {filename}")

    # -------------
    # Admin utilities
    # -------------
    def quick_seed_more(self):
        cur = self.conn.cursor()
        now = datetime.datetime.utcnow().isoformat()
        # small set: algebra basics
        cur.execute("INSERT INTO lessons (title,content,level,created_at) VALUES (?, ?, ?, ?)",
                    ("Ecuaciones lineales: idea", "Resolver ax + b = c. Aisla x restando y dividiendo.", 1, now))
        lid = cur.lastrowid
        exs = [
            (lid, 'mcq', "Resuelve: 2x + 3 = 7. ¿x = ?", "1||2||3||4", "2", "Resta 3 y divide por 2."),
            (lid, 'write', "Resuelve: 5x - 5 = 0 => x = ?", None, "1", "Suma 5 luego divide por 5."),
        ]
        for e in exs:
            cur.execute("INSERT INTO exercises (lesson_id,kind,prompt,choices,answer,hint,created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (e[0], e[1], e[2], e[3], e[4], e[5], now))
        self.conn.commit()
        print("Añadido seed extra (álgebra).")

    # -------------
    # CLI main loop
    # -------------
    def repl(self):
        print("Khan-proto (consola) — micro-lecciones y práctica adaptativa")
        print("Escribe 'help' para ver comandos.")
        while True:
            cmd = input("khan> ").strip().split()
            if not cmd:
                continue
            c = cmd[0].lower()
            try:
                if c == 'help':
                    self.print_help()
                elif c == 'quit' or c == 'exit':
                    print("Saliendo.")
                    break
                elif c == 'users':
                    self.list_users()
                elif c == 'create':
                    name = input("Nombre usuario: ").strip()
                    if name:
                        self.create_user(name)
                elif c == 'select':
                    name = input("Usuario a seleccionar: ").strip()
                    if name:
                        self.select_user(name)
                elif c == 'lessons':
                    lvl = None
                    if len(cmd) > 1:
                        try: lvl = int(cmd[1])
                        except: lvl=None
                    self.list_lessons(level=lvl)
                elif c == 'lesson':
                    if len(cmd) < 2:
                        print("Uso: lesson <id>")
                        continue
                    self.show_lesson(int(cmd[1]))
                elif c == 'study':
                    if len(cmd) < 2:
                        print("Uso: study <lesson_id>")
                        continue
                    self.show_lesson(int(cmd[1]))
                    ok = input("¿Deseas practicar los ejercicios de esta lección ahora? (y/n) ").strip().lower()
                    if ok.startswith('y'):
                        # fetch exercises for lesson
                        cur = self.conn.cursor()
                        cur.execute("SELECT * FROM exercises WHERE lesson_id=?", (int(cmd[1]),))
                        rows = cur.fetchall()
                        for ex in rows:
                            self.present_exercise(ex)
                elif c == 'practice':
                    n = 10
                    if len(cmd) > 1:
                        try: n = int(cmd[1])
                        except: n = 10
                    self.practice_session(n=n)
                elif c == 'stats':
                    self.show_stats()
                elif c == 'export':
                    fn = None
                    if len(cmd) > 1: fn = cmd[1]
                    self.export_progress(fn)
                elif c == 'addlesson':
                    title = input("Título: ").strip()
                    content = input("Contenido (micro-lección): ").strip()
                    lvl = input("Nivel (número): ").strip()
                    try: lvl = int(lvl)
                    except: lvl = 1
                    self.add_lesson(title, content, level=lvl)
                elif c == 'addex':
                    lid = int(input("Lesson id: ").strip())
                    kind = input("Tipo (mcq/write): ").strip()
                    prompt = input("Prompt: ").strip()
                    choices = None
                    if kind == 'mcq':
                        choices = input("Choices (separate with ||): ").strip()
                    answer = input("Respuesta canonical: ").strip()
                    hint = input("Hint (opcional): ").strip()
                    self.add_exercise(lid, kind, prompt, answer, choices=choices, hint=hint)
                elif c == 'seed':
                    self.quick_seed_more()
                else:
                    print("Comando no reconocido. Escribe 'help'.")
            except Exception as e:
                print("Error:", e)

    def print_help(self):
        print("""
Comandos disponibles:
 help                : muestra esta ayuda
 users               : lista usuarios
 create              : crear usuario nuevo
 select              : seleccionar usuario activo
 lessons [level]     : listar lecciones (opcional filtrar por nivel)
 lesson <id>         : mostrar micro-lección y ejercicios asociados
 study <lesson_id>   : ver lección y practicar sus ejercicios
 practice [n]        : practicar hasta n ejercicios debidos (por defecto 10)
 stats               : ver progreso del usuario seleccionado
 export [file]       : exportar progreso a texto
 addlesson           : agregar lección manualmente (admin)
 addex               : agregar ejercicio a lección (admin)
 seed                : añadir contenido de ejemplo adicional
 quit / exit         : salir
""")

# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    app = KhanProto()
    app.repl()
