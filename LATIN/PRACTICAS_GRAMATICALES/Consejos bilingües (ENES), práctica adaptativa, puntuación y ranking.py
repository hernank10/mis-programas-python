#!/usr/bin/env python3
# Programa 9: Prototipo offline con SQLite
# Consejos bilingües (EN/ES), práctica adaptativa, puntuación y ranking

import sqlite3
import os
import datetime
import random
from textwrap import fill

DB_PATH = "lms.db"

SEED_TIPS = [
    # (en, es)
    ("Always place adjectives before nouns in English.",
     "Coloca siempre los adjetivos antes de los sustantivos en inglés."),
    ("Learn common adjective order: opinion, size, age, shape, color, origin, material, purpose.",
     "Aprende el orden común de los adjetivos: opinión, tamaño, edad, forma, color, origen, material, propósito."),
    ("Use comparative adjectives to compare two things.",
     "Usa adjetivos comparativos para comparar dos cosas."),
    ("Use superlatives to compare more than two things.",
     "Usa adjetivos superlativos para comparar más de dos cosas."),
    ("Pronouns replace nouns and avoid repetition.",
     "Los pronombres reemplazan a los sustantivos y evitan la repetición."),
    ("Prepositions show relationships of time, place, and movement.",
     "Las preposiciones muestran relaciones de tiempo, lugar y movimiento."),
]

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS tips(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            en TEXT NOT NULL,
            es TEXT NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS attempts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            tip_id INTEGER NOT NULL,
            lang TEXT CHECK(lang IN ('en','es')) NOT NULL,
            typed TEXT NOT NULL,
            correct INTEGER CHECK(correct IN (0,1)) NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(tip_id) REFERENCES tips(id)
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS scores(
            user_id INTEGER PRIMARY KEY,
            points INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
        """)
        con.commit()

def seed_data():
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM tips;")
        count = cur.fetchone()[0]
        if count == 0:
            cur.executemany("INSERT INTO tips(en, es) VALUES(?,?);", SEED_TIPS)
            con.commit()

def get_or_create_user(name):
    name = name.strip()
    if not name:
        raise ValueError("El nombre no puede estar vacío.")
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT id FROM users WHERE name=?;", (name,))
        row = cur.fetchone()
        if row:
            user_id = row[0]
        else:
            cur.execute("INSERT INTO users(name, created_at) VALUES(?,?);",
                        (name, datetime.datetime.utcnow().isoformat()))
            user_id = cur.lastrowid
            cur.execute("INSERT INTO scores(user_id, points) VALUES(?, 0);", (user_id,))
        con.commit()
        return user_id

def add_points(user_id, pts=1):
    with connect() as con:
        cur = con.cursor()
        cur.execute("UPDATE scores SET points = points + ? WHERE user_id=?;", (pts, user_id))
        con.commit()

def record_attempt(user_id, tip_id, lang, typed, correct):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO attempts(user_id, tip_id, lang, typed, correct, created_at)
            VALUES(?,?,?,?,?,?);
        """, (user_id, tip_id, lang, typed, int(correct), datetime.datetime.utcnow().isoformat()))
        con.commit()

def _tip_stats_for_user(user_id):
    """Devuelve dict {tip_id: {'en':(tries,wrong), 'es':(tries,wrong)}}"""
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT tip_id, lang,
                   COUNT(*) AS tries,
                   SUM(CASE WHEN correct=0 THEN 1 ELSE 0 END) AS wrongs
            FROM attempts
            WHERE user_id=?
            GROUP BY tip_id, lang;
        """, (user_id,))
        stats = {}
        for tip_id, lang, tries, wrongs in cur.fetchall():
            stats.setdefault(tip_id, {'en': (0,0), 'es': (0,0)})
            stats[tip_id][lang] = (tries or 0, wrongs or 0)
        return stats

def choose_adaptive_tip(user_id):
    """
    Selección adaptativa: calcula una 'prioridad' por tip = tasa de error media + pequeña aleatoriedad.
    Mayor prioridad = más probable de salir.
    """
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT id, en, es FROM tips;")
        tips = cur.fetchall()

    stats = _tip_stats_for_user(user_id)

    weighted = []
    for tip_id, en, es in tips:
        en_tries, en_wrong = stats.get(tip_id, {}).get('en', (0,0))
        es_tries, es_wrong = stats.get(tip_id, {}).get('es', (0,0))

        def rate(tries, wrong):
            return (wrong + 0.5) / (tries + 1)  # suavizado para evitar 0/0

        # priorizamos donde el usuario falla más; promedio EN/ES
        priority = 0.5 * rate(en_tries, en_wrong) + 0.5 * rate(es_tries, es_wrong)
        # un pequeño ruido para diversidad
        priority += random.uniform(0, 0.1)
        weighted.append((priority, (tip_id, en, es)))

    weighted.sort(reverse=True, key=lambda x: x[0])
    # mayor prioridad primero; entre los top 3, elige uno al azar
    topk = weighted[:min(3, len(weighted))]
    return random.choice(topk)[1]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPresiona ENTER para continuar...")

def wrap(s, width=90):
    return fill(s, width=width)

def practice_tip(user_id):
    tip_id, en, es = choose_adaptive_tip(user_id)
    clear_screen()
    print("=== PRÁCTICA ADAPTATIVA ===")
    print("\nConsejo (EN/ES) para memorizar:\n")
    print("EN:", wrap(en))
    print("ES:", wrap(es))

    print("\n✍️ Reescribe EXACTAMENTE el consejo en INGLÉS:")
    typed_en = input("> ").strip()
    ok_en = (typed_en == en)
    record_attempt(user_id, tip_id, 'en', typed_en, ok_en)
    if ok_en:
        print("✅ Inglés CORRECTO. +1 punto")
        add_points(user_id, 1)
    else:
        print("❌ Inglés INCORRECTO.")
        print("   Correcto:", en)

    print("\n✍️ Reescribe EXACTAMENTE el consejo en ESPAÑOL:")
    typed_es = input("> ").strip()
    ok_es = (typed_es == es)
    record_attempt(user_id, tip_id, 'es', typed_es, ok_es)
    if ok_es:
        print("✅ Español CORRECTO. +1 punto")
        add_points(user_id, 1)
    else:
        print("❌ Español INCORRECTO.")
        print("   Correcto:", es)

    pause()

def show_progress(user_id):
    clear_screen()
    print("=== PROGRESO DEL USUARIO ===\n")
    with connect() as con:
        cur = con.cursor()
        # Puntos
        cur.execute("SELECT points FROM scores WHERE user_id=?;", (user_id,))
        pts = cur.fetchone()
        pts = pts[0] if pts else 0

        # Totales
        cur.execute("""
            SELECT COUNT(*), SUM(CASE WHEN correct=1 THEN 1 ELSE 0 END)
            FROM attempts WHERE user_id=?;
        """, (user_id,))
        total, correct = cur.fetchone()
        total = total or 0
        correct = correct or 0
        acc = (100.0 * correct / total) if total else 0.0

        print(f"Puntos acumulados: {pts}")
        print(f"Intentos totales:  {total}")
        print(f"Aciertos:          {correct}")
        print(f"Precisión global:  {acc:.1f}%\n")

        # Por consejo (resumen breve)
        cur.execute("""
            SELECT t.id, t.en, t.es,
                   SUM(a.correct) AS aciertos,
                   COUNT(a.id) AS intentos
            FROM tips t
            LEFT JOIN attempts a ON a.tip_id=t.id AND a.user_id=?
            GROUP BY t.id
            ORDER BY t.id;
        """, (user_id,))
        rows = cur.fetchall()
        for tip_id, en, es, aciertos, intentos in rows:
            aciertos = aciertos or 0
            intentos = intentos or 0
            acc_tip = (100.0 * aciertos / intentos) if intentos else 0.0
            print(f"[Tip {tip_id:02d}] Intentos: {intentos:3d} | Aciertos: {aciertos:3d} | Precisión: {acc_tip:5.1f}%")
            print("  EN:", wrap(en))
            print("  ES:", wrap(es))
            print()
    pause()

def show_leaderboard():
    clear_screen()
    print("=== RANKING (TOP 10) ===\n")
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT u.name, s.points
            FROM scores s
            JOIN users u ON u.id = s.user_id
            ORDER BY s.points DESC, u.name ASC
            LIMIT 10;
        """)
        rows = cur.fetchall()
        if not rows:
            print("Aún no hay jugadores en el ranking.")
        else:
            for i, (name, pts) in enumerate(rows, start=1):
                print(f"{i:2d}. {name:20s} — {pts} pts")
    pause()

def add_tip():
    clear_screen()
    print("=== AGREGAR NUEVO CONSEJO ===\n")
    en = input("Escribe el consejo en INGLÉS exactamente:\n> ").strip()
    es = input("Escribe el consejo en ESPAÑOL exactamente:\n> ").strip()
    if not en or not es:
        print("Debe completar ambos campos.")
        pause()
        return
    with connect() as con:
        cur = con.cursor()
        cur.execute("INSERT INTO tips(en, es) VALUES(?,?);", (en, es))
        con.commit()
    print("\n✅ Consejo agregado.")
    pause()

def reset_user_progress(user_id):
    clear_screen()
    print("=== REINICIAR PROGRESO DEL USUARIO ===\n")
    confirm = input("Esto borrará TODOS tus intentos y puntos. Escribe 'SI' para confirmar: ").strip().upper()
    if confirm == "SI":
        with connect() as con:
            cur = con.cursor()
            cur.execute("DELETE FROM attempts WHERE user_id=?;", (user_id,))
            cur.execute("UPDATE scores SET points=0 WHERE user_id=?;", (user_id,))
            con.commit()
        print("✅ Progreso reiniciado.")
    else:
        print("Operación cancelada.")
    pause()

def main_menu(user_id, user_name):
    while True:
        clear_screen()
        print(f"== PROGRAMA 9 · Offline LMS (Usuario: {user_name}) ==")
        print("1) Practicar (adaptativo EN/ES)")
        print("2) Ver progreso")
        print("3) Ranking")
        print("4) Agregar consejo (admin/manual)")
        print("5) Reiniciar mi progreso")
        print("6) Salir")
        opt = input("\nElige una opción: ").strip()
        if opt == "1":
            practice_tip(user_id)
        elif opt == "2":
            show_progress(user_id)
        elif opt == "3":
            show_leaderboard()
        elif opt == "4":
            add_tip()
        elif opt == "5":
            reset_user_progress(user_id)
        elif opt == "6":
            clear_screen()
            print("¡Hasta pronto! 👋 Sigue practicando cada día.")
            break
        else:
            print("Opción no válida.")
            pause()

def boot():
    init_db()
    seed_data()
    clear_screen()
    print("=== PROGRAMA 9 · Inglés Offline con SQLite ===\n")
    name = input("Ingresa tu nombre de usuario: ").strip()
    try:
        user_id = get_or_create_user(name)
    except Exception as e:
        print("Error:", e)
        return
    main_menu(user_id, name)

if __name__ == "__main__":
    boot()
