#!/usr/bin/env python3
"""
Ejercicios "Entonces" - Programa de consola para crear, memorizar, editar y guardar ejemplos.
Archivo: ejercicios_entonces_app.py
Descripción: Permite añadir ejemplos en español con traducciones en inglés y francés,
clasificarlos por categoría (temporal, consecuencial, discursivo), buscarlos, editarlos,
borrarlos, exportarlos e iniciar un modo de estudio/quiz para memorizar.

Uso: python3 ejercicios_entonces_app.py
Requiere: Python 3.8+

El programa guarda los datos en 'examples.json' en el mismo directorio.

Funciones principales:
 - Añadir ejemplo
 - Listar ejemplos (con filtros)
 - Buscar por texto
 - Editar / Eliminar
 - Exportar a CSV
 - Modo Quiz (comprobar traducciones)
 - Pre-cargar 100 ejemplos de muestra (opcional)

Hecho por: ChatGPT (Generador de recursos educativos)
"""

from __future__ import annotations
import json
import os
import sys
import csv
import datetime
import textwrap
from typing import List, Dict, Optional

DB_FILENAME = "examples.json"

# -----------------------------
# ESTRUCTURA DE UN EJEMPLO
# -----------------------------
# {
#   "id": int,
#   "spanish": "...",
#   "english": "...",
#   "french": "...",
#   "category": "temporal" | "consecuencial" | "discursivo",
#   "notes": "...",
#   "created_at": "ISO",
#   "updated_at": "ISO"
# }


def now_iso() -> str:
    return datetime.datetime.now().isoformat()


def load_db(filename: str = DB_FILENAME) -> List[Dict]:
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
        except json.JSONDecodeError:
            print("Advertencia: archivo JSON corrupto. Se cargará una lista vacía.")
            return []


def save_db(data: List[Dict], filename: str = DB_FILENAME) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def next_id(data: List[Dict]) -> int:
    if not data:
        return 1
    return max(item.get("id", 0) for item in data) + 1


# -----------------------------
# UTILIDADES DE FORMATEO
# -----------------------------

def print_line():
    print("-" * 60)


def input_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("No puede estar vacío. Intenta de nuevo.")


def choose_category(prompt: str = "Categoría (temporal/consecuencial/discursivo): ") -> str:
    choices = {"temporal", "consecuencial", "discursivo"}
    while True:
        c = input(prompt).strip().lower()
        if c in choices:
            return c
        print("Categoría inválida. Escribe 'temporal', 'consecuencial' o 'discursivo'.")


# -----------------------------
# OPERACIONES CRUD
# -----------------------------


def add_example(db: List[Dict]) -> None:
    print_line()
    print("Añadir nuevo ejemplo")
    spanish = input_non_empty("Español: ")
    english = input_non_empty("Inglés: ")
    french = input_non_empty("Francés: ")
    category = choose_category()
    notes = input("Notas (opcional): ").strip()
    eid = next_id(db)
    item = {
        "id": eid,
        "spanish": spanish,
        "english": english,
        "french": french,
        "category": category,
        "notes": notes,
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    db.append(item)
    save_db(db)
    print(f"Ejemplo añadido con id {eid}.")


def list_examples(db: List[Dict], category: Optional[str] = None, limit: Optional[int] = None) -> None:
    to_show = [e for e in db if (category is None or e.get("category") == category)]
    to_show = sorted(to_show, key=lambda x: x.get("id"))
    if limit:
        to_show = to_show[:limit]
    if not to_show:
        print("No hay ejemplos para mostrar.")
        return
    for e in to_show:
        print_line()
        print(f"ID: {e['id']}  |  Categoría: {e['category']}  |  Actualizado: {e['updated_at']}")
        print(f"ES: {e['spanish']}")
        print(f"EN: {e['english']}")
        print(f"FR: {e['french']}")
        if e.get("notes"):
            print(f"Notas: {e['notes']}")
    print_line()
    print(f"Total: {len(to_show)} ejemplos mostrados.")


def find_by_id(db: List[Dict], eid: int) -> Optional[Dict]:
    for e in db:
        if e.get("id") == eid:
            return e
    return None


def search_db(db: List[Dict], term: str) -> List[Dict]:
    term_l = term.lower()
    out = []
    for e in db:
        if term_l in e.get("spanish", "").lower() or term_l in e.get("english", "").lower() or term_l in e.get("french", "").lower() or term_l in e.get("notes", "").lower():
            out.append(e)
    return out


def edit_example(db: List[Dict]) -> None:
    try:
        eid = int(input_non_empty("ID del ejemplo a editar: "))
    except ValueError:
        print("ID inválido.")
        return
    e = find_by_id(db, eid)
    if not e:
        print("No se encontró el ejemplo.")
        return
    print("Deja en blanco para mantener el valor actual.")
    spanish = input(f"Español [{e['spanish']}]: ").strip()
    english = input(f"Inglés [{e['english']}]: ").strip()
    french = input(f"Francés [{e['french']}]: ").strip()
    category = input(f"Categoría [{e['category']}]: ").strip().lower()
    notes = input(f"Notas [{e.get('notes','')}]: ").strip()
    if spanish:
        e['spanish'] = spanish
    if english:
        e['english'] = english
    if french:
        e['french'] = french
    if category in {"temporal", "consecuencial", "discursivo"}:
        e['category'] = category
    if notes:
        e['notes'] = notes
    e['updated_at'] = now_iso()
    save_db(db)
    print("Ejemplo actualizado.")


def delete_example(db: List[Dict]) -> None:
    try:
        eid = int(input_non_empty("ID del ejemplo a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    e = find_by_id(db, eid)
    if not e:
        print("No se encontró el ejemplo.")
        return
    confirm = input(f"Confirmar eliminación del ejemplo {eid}? (s/n): ").strip().lower()
    if confirm == 's':
        db.remove(e)
        save_db(db)
        print("Ejemplo eliminado.")
    else:
        print("Operación cancelada.")


# -----------------------------
# EXPORT / IMPORT
# -----------------------------


def export_csv(db: List[Dict], filename: str) -> None:
    keys = ["id", "spanish", "english", "french", "category", "notes", "created_at", "updated_at"]
    with open(filename, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for e in db:
            writer.writerow({k: e.get(k, "") for k in keys})
    print(f"Exportado a {filename}")


def import_csv(db: List[Dict], filename: str) -> None:
    if not os.path.exists(filename):
        print("Archivo no encontrado.")
        return
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        added = 0
        for row in reader:
            # assign id if missing
            try:
                rid = int(row.get('id') or 0)
            except ValueError:
                rid = 0
            item = {
                'id': next_id(db),
                'spanish': row.get('spanish', '').strip(),
                'english': row.get('english', '').strip(),
                'french': row.get('french', '').strip(),
                'category': row.get('category', '').strip() or 'temporal',
                'notes': row.get('notes', '').strip(),
                'created_at': row.get('created_at') or now_iso(),
                'updated_at': now_iso(),
            }
            db.append(item)
            added += 1
    save_db(db)
    print(f"Importación finalizada. Agregados {added} ejemplos.")


# -----------------------------
# MODO QUIZ / MEMORIZACIÓN
# -----------------------------


def normalize_answer(s: str) -> str:
    return ''.join(ch for ch in s.lower() if ch.isalnum() or ch.isspace()).strip()


def quiz_mode(db: List[Dict]) -> None:
    if not db:
        print("La base de datos está vacía. Agrega ejemplos primero.")
        return
    print("Modo Quiz: se te mostrará la oración en español. Escribe la traducción en inglés y francés.")
    cat = input("Filtrar por categoría (temporal/consecuencial/discursivo) o ENTER para todas: ").strip().lower()
    pool = [e for e in db if (not cat or e['category'] == cat)]
    if not pool:
        print("No hay ejemplos en esa categoría.")
        return
    import random
    random.shuffle(pool)
    score = 0
    total = 0
    for e in pool:
        total += 1
        print_line()
        print(f"ID {e['id']}  |  Categoría: {e['category']}")
        print(f"ES: {e['spanish']}")
        ans_en = input("Traducción al inglés: ").strip()
        ans_fr = input("Traducción al francés: ").strip()
        correct_en = normalize_answer(e['english'])
        correct_fr = normalize_answer(e['french'])
        if normalize_answer(ans_en) == correct_en and normalize_answer(ans_fr) == correct_fr:
            print("Correcto ✅")
            score += 1
        else:
            print("Incorrecto. Respuestas correctas:")
            print(f"EN → {e['english']}")
            print(f"FR → {e['french']}")
        # opción para detener
        cont = input("Continuar? (s para seguir, otra para salir): ").strip().lower()
        if cont != 's':
            break
    print_line()
    print(f"Quiz finalizado. Puntuación: {score}/{total}")


# -----------------------------
# GENERADOR DE EJEMPLOS DE MUESTRA (100)
# -----------------------------


def preload_100_examples(db: List[Dict]) -> None:
    """Agrega 100 ejemplos de muestra divididos por categoría.
    Estos son ejemplos simples que pueden editarse luego por el usuario.
    """
    if db:
        confirm = input("La base de datos ya contiene ejemplos. ¿Deseas añadir los 100 ejemplos de muestra además de los existentes? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operación cancelada.")
            return
    samples = []
    # 40 temporales
    temporal_sentences = [
        ("Llegamos tarde al cine; entonces, ya había empezado la película.", "We arrived late at the cinema; then the movie had already started.", "Nous sommes arrivés en retard au cinéma; alors le film avait déjà commencé."),
        ("Primero preparó la mesa; entonces sirvió la comida.", "First she set the table; then she served the food.", "D’abord elle a mis la table; alors elle a servi le repas."),
        ("Terminé de leer el libro; entonces me fui a dormir.", "I finished reading the book; then I went to sleep.", "J’ai fini de lire le livre; alors je suis allé dormir."),
        ("Se hizo de noche; entonces encendieron las luces.", "It got dark; then they turned on the lights.", "La nuit est tombée; alors ils ont allumé les lumières."),
        ("Llegó la primavera; entonces los árboles florecieron.", "Spring arrived; then the trees bloomed.", "Le printemps est arrivé; alors les arbres ont fleuri."),
        ("Primero estudió la lección; entonces hizo el examen.", "First he studied the lesson; then he took the exam.", "D’abord il a étudié la leçon; alors il a passé l’examen."),
        ("La película terminó; entonces salimos del cine.", "The movie ended; then we left the cinema.", "Le film s’est terminé; alors nous sommes sortis du cinéma."),
        ("Cerró la puerta; entonces apagó la luz.", "He closed the door; then he turned off the light.", "Il a fermé la porte; alors il a éteint la lumière."),
        ("El tren llegó a la estación; entonces los pasajeros bajaron.", "The train arrived at the station; then the passengers got off.", "Le train est arrivé à la gare; alors les passagers sont descendus."),
        ("Primero cocinó la pasta; entonces añadió la salsa.", "First she cooked the pasta; then she added the sauce.", "D’abord elle a cuit les pâtes; alors elle a ajouté la sauce."),
    ]
    # we'll repeat and modify slightly to reach 40
    for i in range(40):
        base = temporal_sentences[i % len(temporal_sentences)]
        samples.append((base[0] + f" ({i+1})", base[1] + f" ({i+1})", base[2] + f" ({i+1})", 'temporal'))

    # 30 consecuenciales
    consecuential_sentences = [
        ("No trajiste paraguas; entonces te mojarás.", "You didn’t bring an umbrella; so you’ll get wet.", "Tu n’as pas apporté de parapluie; donc tu seras mouillé."),
        ("No hiciste la tarea; entonces no puedes salir a jugar.", "You didn’t do the homework; so you can’t go out to play.", "Tu n’as pas fait les devoirs; donc tu ne peux pas sortir jouer."),
        ("Se rompió la tubería; entonces la casa quedó sin agua.", "The pipe broke; so the house had no water.", "La tuyauterie s’est cassée; donc la maison est restée sans eau."),
        ("Perdió el vuelo; entonces canceló el viaje.", "He missed the flight; so he canceled the trip.", "Il a raté le vol; donc il a annulé le voyage."),
        ("No aprobó el examen; entonces repitió el curso.", "He didn’t pass the exam; so he repeated the course.", "Il n’a pas réussi l’examen; donc il a refait le cours."),
    ]
    for i in range(30):
        base = consecuential_sentences[i % len(consecuential_sentences)]
        samples.append((base[0] + f" ({i+1})", base[1] + f" ({i+1})", base[2] + f" ({i+1})", 'consecuencial'))

    # 30 discursivos
    discursivo_sentences = [
        ("Entonces… ¿qué piensas de mi propuesta?", "So… what do you think of my proposal?", "Alors… qu’est-ce que tu penses de ma proposition ?"),
        ("Entonces, como te decía, el problema es más complejo.", "So, as I was saying, the problem is more complex.", "Alors, comme je te le disais, le problème est plus complexe."),
        ("Entonces, sigamos con el siguiente punto.", "So, let’s move on to the next point.", "Alors, passons au point suivant."),
        ("Entonces… ehm… no estoy seguro.", "So… um… I’m not sure.", "Alors… euh… je ne suis pas sûr."),
        ("Entonces, en resumen, debemos actuar.", "So, in summary, we must act.", "Alors, en résumé, nous devons agir."),
    ]
    for i in range(30):
        base = discursivo_sentences[i % len(discursivo_sentences)]
        samples.append((base[0] + f" ({i+1})", base[1] + f" ({i+1})", base[2] + f" ({i+1})", 'discursivo'))

    # add to db with ids
    for s in samples:
        item = {
            'id': next_id(db),
            'spanish': s[0],
            'english': s[1],
            'french': s[2],
            'category': s[3],
            'notes': '',
            'created_at': now_iso(),
            'updated_at': now_iso(),
        }
        db.append(item)
    save_db(db)
    print(f"Se han añadido {len(samples)} ejemplos de muestra. Total en DB: {len(db)}")


# -----------------------------
# MENU PRINCIPAL
# -----------------------------


def print_menu():
    print_line()
    print("Ejercicios 'Entonces' - Menú principal")
    print("1) Añadir ejemplo")
    print("2) Listar ejemplos (todas)")
    print("3) Listar por categoría")
    print("4) Buscar")
    print("5) Editar ejemplo")
    print("6) Eliminar ejemplo")
    print("7) Exportar a CSV")
    print("8) Importar desde CSV")
    print("9) Modo Quiz (memorizar)")
    print("10) Pre-cargar 100 ejemplos de muestra")
    print("0) Salir")


def main_loop():
    db = load_db()
    while True:
        print_menu()
        choice = input("Elige una opción: ").strip()
        if choice == '1':
            add_example(db)
        elif choice == '2':
            list_examples(db)
        elif choice == '3':
            cat = choose_category("Elige categoría (temporal/consecuencial/discursivo): ")
            list_examples(db, category=cat)
        elif choice == '4':
            term = input_non_empty("Término de búsqueda: ")
            res = search_db(db, term)
            if res:
                list_examples(res)
            else:
                print("No se encontraron coincidencias.")
        elif choice == '5':
            edit_example(db)
        elif choice == '6':
            delete_example(db)
        elif choice == '7':
            fname = input_non_empty("Nombre de archivo CSV a crear (ejemplo: export.csv): ")
            export_csv(db, fname)
        elif choice == '8':
            fname = input_non_empty("Nombre de archivo CSV a importar (ejemplo: import.csv): ")
            import_csv(db, fname)
        elif choice == '9':
            quiz_mode(db)
        elif choice == '10':
            preload_100_examples(db)
        elif choice == '0':
            print("Adiós — los cambios ya están guardados.")
            break
        else:
            print("Opción no reconocida. Intenta otra vez.")


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. Saliendo...")
        sys.exit(0)
