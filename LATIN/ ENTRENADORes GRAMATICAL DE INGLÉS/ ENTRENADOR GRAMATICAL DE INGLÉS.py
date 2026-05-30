# -*- coding: utf-8 -*-
import random
import sys

# =========================
# Datos y reglas
# =========================

REGULAR_NOUNS = [
    "cat", "dog", "book", "car", "table", "chair", "house", "pen", "apple", "banana",
    "bus", "box", "glass", "watch", "dish", "fox", "class", "match",
    "photo", "piano", "toy", "day", "key", "boy", "monkey", "church", "kiss", "hero"
]

# Plurales irregulares comunes
IRREGULAR_PLURALS = {
    "child": "children",
    "man": "men",
    "woman": "women",
    "mouse": "mice",
    "goose": "geese",
    "tooth": "teeth",
    "foot": "feet",
    "person": "people",
    "ox": "oxen",
    "louse": "lice",
    "cactus": "cacti",
    "analysis": "analyses",
    "thesis": "theses",
    "crisis": "crises",
    "phenomenon": "phenomena",
    "basis": "bases"
}

# Adjetivos regulares (pre-calculados para evitar ambigüedades)
# Elegidos para cubrir reglas: +er/est, CVC (doble consonante), -y -> -ier/-iest, termina en e
ADJ_REGULAR = {
    "big": ("bigger", "biggest"),          # CVC, duplica consonante
    "hot": ("hotter", "hottest"),          # CVC
    "sad": ("sadder", "saddest"),          # CVC
    "thin": ("thinner", "thinnest"),       # CVC
    "fat": ("fatter", "fattest"),          # CVC
    "nice": ("nicer", "nicest"),           # termina en e
    "late": ("later", "latest"),           # termina en e
    "happy": ("happier", "happiest"),      # y -> i
    "funny": ("funnier", "funniest"),      # y -> i
    "easy": ("easier", "easiest"),         # y -> i
    "small": ("smaller", "smallest"),      # +er/est
    "fast": ("faster", "fastest"),         # +er/est
    "short": ("shorter", "shortest"),      # +er/est
    "long": ("longer", "longest"),         # +er/est
    # multi-sílaba que usan more/most
    "beautiful": ("more beautiful", "most beautiful"),
    "expensive": ("more expensive", "most expensive"),
    "difficult": ("more difficult", "most difficult"),
    "interesting": ("more interesting", "most interesting"),
    "useful": ("more useful", "most useful"),
}

# Irregulares famosos
ADJ_IRREGULAR = {
    "good": ("better", "best"),
    "well": ("better", "best"),
    "bad": ("worse", "worst"),
    "far": ("farther", "farthest"),  # también "further/furthest"
    "little": ("less", "least"),
    "many": ("more", "most"),
    "much": ("more", "most")
}

# =========================
# Utilidades
# =========================

def is_consonant(ch: str) -> bool:
    return ch.lower() in "bcdfghjklmnpqrstvwxyz"

def rule_plural_and_explain(word: str):
    """
    Forma plural regular + explicación breve de la regla aplicada.
    (No cubre todas las excepciones del inglés; es un entrenador básico.)
    """
    # -s, -sh, -ch, -x, -z -> +es
    if word.endswith(("s", "sh", "ch", "x", "z")):
        return word + "es", "Termina en -s/-sh/-ch/-x/-z → +es"
    # consonant + y -> -ies
    if word.endswith("y") and len(word) >= 2 and is_consonant(word[-2]):
        return word[:-1] + "ies", "Consonante + y → y → ies"
    # palabras en -o: hay irregulares; simplificamos: hero → heroes; photo/piano → +s
    if word.endswith("o"):
        if word in {"hero", "potato", "tomato"}:
            return word + "es", "Algunas en -o → +es (hero→heroes)"
        return word + "s", "Mayoría en -o → +s (photo→photos)"
    # default: +s
    return word + "s", "+s general"

def normalize(s: str) -> str:
    return " ".join(s.strip().lower().split())

def ask(prompt: str) -> str:
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nSaliendo…")
        sys.exit(0)

# =========================
# Módulos de práctica
# =========================

def practice_regular_plurals(rounds=10):
    print("\n=== Plurales REGULARES ===")
    score = 0
    words = random.sample(REGULAR_NOUNS, min(rounds, len(REGULAR_NOUNS)))
    for w in words:
        correct, rule = rule_plural_and_explain(w)
        ans = normalize(ask(f"Plural de '{w}': "))
        if ans == normalize(correct):
            print("✅ Correcto")
            score += 1
        else:
            print(f"❌ Incorrecto. Correcto: {correct}  ({rule})")
        print("-")
    print(f"Puntuación: {score}/{len(words)}")

def practice_irregular_plurals(rounds=10):
    print("\n=== Plurales IRREGULARES ===")
    items = random.sample(list(IRREGULAR_PLURALS.items()), min(rounds, len(IRREGULAR_PLURALS)))
    score = 0
    for singular, plural in items:
        ans = normalize(ask(f"Plural de '{singular}': "))
        if ans == normalize(plural):
            print("✅ Correcto")
            score += 1
        else:
            print(f"❌ Incorrecto. Correcto: {plural} (irregular)")
        print("-")
    print(f"Puntuación: {score}/{len(items)}")

def practice_regular_comparatives(rounds=10):
    print("\n=== Comparativos/Superlativos REGULARES ===")
    items = random.sample(list(ADJ_REGULAR.items()), min(rounds, len(ADJ_REGULAR)))
    score = 0
    for adj, (comp, sup) in items:
        mode = random.choice(["comp", "sup"])
        if mode == "comp":
            ans = normalize(ask(f"Comparativo de '{adj}': "))
            if ans == normalize(comp):
                print("✅ Correcto")
                score += 1
            else:
                print(f"❌ Incorrecto. Correcto: {comp}")
        else:
            ans = normalize(ask(f"Superlativo de '{adj}': "))
            if ans == normalize(sup):
                print("✅ Correcto")
                score += 1
            else:
                print(f"❌ Incorrecto. Correcto: {sup}")
        print("-")
    print(f"Puntuación: {score}/{len(items)}")

def practice_irregular_comparatives(rounds=10):
    print("\n=== Comparativos/Superlativos IRREGULARES ===")
    items = random.sample(list(ADJ_IRREGULAR.items()), min(rounds, len(ADJ_IRREGULAR)))
    score = 0
    for adj, (comp, sup) in items:
        mode = random.choice(["comp", "sup"])
        if mode == "comp":
            ans = normalize(ask(f"Comparativo de '{adj}': "))
            if ans == normalize(comp):
                print("✅ Correcto")
                score += 1
            else:
                print(f"❌ Incorrecto. Correcto: {comp}")
        else:
            ans = normalize(ask(f"Superlativo de '{adj}': "))
            if ans == normalize(sup):
                print("✅ Correcto")
                score += 1
            else:
                print(f"❌ Incorrecto. Correcto: {sup}")
        print("-")
    print(f"Puntuación: {score}/{len(items)}")

def practice_mixed(rounds=12):
    """
    Mezcla los 4 tipos anteriores.
    """
    print("\n=== Ejercicios MIXTOS ===")
    score = 0
    tasks = []
    tasks += [("plural_reg", w) for w in random.sample(REGULAR_NOUNS, min(rounds//4, len(REGULAR_NOUNS)))]
    tasks += [("plural_irreg", w) for w in random.sample(list(IRREGULAR_PLURALS.keys()), min(rounds//4, len(IRREGULAR_PLURALS)))]
    tasks += [("adj_reg", w) for w in random.sample(list(ADJ_REGULAR.keys()), min(rounds//4, len(ADJ_REGULAR)))]
    tasks += [("adj_irreg", w) for w in random.sample(list(ADJ_IRREGULAR.keys()), min(rounds - len(tasks), len(ADJ_IRREGULAR)))]
    random.shuffle(tasks)

    for typ, token in tasks:
        if typ == "plural_reg":
            correct, rule = rule_plural_and_explain(token)
            ans = normalize(ask(f"(Plural regular) '{token}' → "))
            if ans == normalize(correct):
                print("✅ Correcto")
                score += 1
            else:
                print(f"❌ Incorrecto. Correcto: {correct}  ({rule})")

        elif typ == "plural_irreg":
            correct = IRREGULAR_PLURALS[token]
            ans = normalize(ask(f"(Plural irregular) '{token}' → "))
            if ans == normalize(correct):
                print("✅ Correcto")
                score += 1
            else:
                print(f"❌ Incorrecto. Correcto: {correct}")

        elif typ == "adj_reg":
            comp, sup = ADJ_REGULAR[token]
            mode = random.choice(["comp", "sup"])
            if mode == "comp":
                ans = normalize(ask(f"(Adj regular) Comparativo de '{token}': "))
                if ans == normalize(comp):
                    print("✅ Correcto")
                    score += 1
                else:
                    print(f"❌ Incorrecto. Correcto: {comp}")
            else:
                ans = normalize(ask(f"(Adj regular) Superlativo de '{token}': "))
                if ans == normalize(sup):
                    print("✅ Correcto")
                    score += 1
                else:
                    print(f"❌ Incorrecto. Correcto: {sup}")

        else:  # adj_irreg
            comp, sup = ADJ_IRREGULAR[token]
            mode = random.choice(["comp", "sup"])
            if mode == "comp":
                ans = normalize(ask(f"(Adj irregular) Comparativo de '{token}': "))
                if ans == normalize(comp):
                    print("✅ Correcto")
                    score += 1
                else:
                    print(f"❌ Incorrecto. Correcto: {comp}")
            else:
                ans = normalize(ask(f"(Adj irregular) Superlativo de '{token}': "))
                if ans == normalize(sup):
                    print("✅ Correcto")
                    score += 1
                else:
                    print(f"❌ Incorrecto. Correcto: {sup}")
        print("-")
    print(f"Puntuación: {score}/{len(tasks)}")

# =========================
# Menú
# =========================

def menu():
    while True:
        print("\n=== ENTRENADOR GRAMATICAL DE INGLÉS ===")
        print("1) Plurales regulares")
        print("2) Plurales irregulares")
        print("3) Comparativos/Superlativos regulares")
        print("4) Comparativos/Superlativos irregulares")
        print("5) Ejercicios mixtos")
        print("6) Salir")
        op = ask("Elige una opción: ").strip()

        if op == "1":
            practice_regular_plurals()
        elif op == "2":
            practice_irregular_plurals()
        elif op == "3":
            practice_regular_comparatives()
        elif op == "4":
            practice_irregular_comparatives()
        elif op == "5":
            practice_mixed()
        elif op == "6":
            print("¡Hasta la próxima! 👋")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
