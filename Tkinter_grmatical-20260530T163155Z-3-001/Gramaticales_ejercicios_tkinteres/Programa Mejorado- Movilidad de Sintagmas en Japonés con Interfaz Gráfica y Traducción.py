import random
import tkinter as tk
from tkinter import messagebox

# Oraciones predeterminadas en japonés con múltiples sintagmas
oraciones_japones = [
    {
        "original": "SN:老人が SV:ドアを開けました GAdv:慎重に",
        "reordenada": "老人が慎重にドアを開けました",
        "traduccion": "El anciano abrió la puerta con cuidado."
    },
    {
        "original": "SN:子供たちが SV:サッカーをしました SPrep:公園で",
        "reordenada": "子供たちが公園でサッカーをしました",
        "traduccion": "Los niños jugaron fútbol en el parque."
    },
    {
        "original": "SPrep:朝に SN:マリアが SV:コーヒーを淹れました SPrep:お母さんに",
        "reordenada": "マリアが朝にお母さんにコーヒーを淹れました",
        "traduccion": "María preparó café para su madre por la mañana."
    },
    {
        "original": "SN:シェフが SV:夕食を作りました GAdv:速く SPrep:お客様に",
        "reordenada": "シェフが速くお客様に夕食を作りました",
        "traduccion": "El chef preparó rápidamente la cena para los invitados."
    },
    {
        "original": "GAdv:熱心に SN:学生たちが SV:コンテストに参加しました",
        "reordenada": "学生たちが熱心にコンテストに参加しました",
        "traduccion": "Los estudiantes participaron con entusiasmo en el concurso."
    }
]

# Sintagmas disponibles en japonés
sintagmas_japones = {
    "SN": ["老人が", "子供たちが", "マリアが", "シェフが", "学生たちが"],
    "SV": ["ドアを開けました", "サッカーをしました", "コーヒーを淹れました", "夕食を作りました", "コンテストに参加しました"],
    "CD": ["ドアを", "サッカーを", "コーヒーを", "夕食を", "コンテストに"],
    "GAdv": ["慎重に", "速く", "熱心に"],
    "SPrep": ["公園で", "お母さんに", "お客様に", "朝に"]
}

# Función para validar si la oración tiene sentido
def validar_semantica(oracion):
    # Validación básica: verificar que la oración contenga un sujeto y un verbo
    if "が" in oracion and "を" in oracion:
        return True
    return False

# Función para practicar la reordenación de oraciones
def practicar_reordenacion():
    oracion = random.choice(oraciones_japones)
    print(f"\n分解された文 (日本語): {oracion['original']}")
    respuesta = input(f"文を並べ替えてください（または「終了」と入力してメニューに戻ります）: ")

    if respuesta.lower() == "終了":
        return

    if respuesta.strip() == oracion["reordenada"]:
        print("正解です！文を正しく並べ替えました。")
    else:
        print(f"不正解です。正しい答えは: {oracion['reordenada']}")

# Función para mostrar ejemplos de movilidad sintáctica
def mostrar_ejemplos():
    print("\n--- 日本語での構文の柔軟性の例 ---")
    for i, oracion in enumerate(oraciones_japones, start=1):
        print(f"{i}. 分解された文: {oracion['original']}")
        print(f"   並べ替えた文: {oracion['reordenada']}")
        print(f"   翻訳: {oracion['traduccion']}")
        print()

# Función para crear nuevas oraciones reorganizando sintagmas
def crear_nuevas_oraciones():
    print("\n--- 日本語で新しい文を作成する ---")
    print("指示: 文法的に正しい文を作成するために、要素を並べ替えてください。")
    print("利用可能な要素: 主語 (SN), 動詞 (SV), 目的語 (CD), 副詞 (GAdv), 前置詞句 (SPrep).")

    print("\n利用可能な要素:")
    for clave, valores in sintagmas_japones.items():
        print(f"{clave}: {', '.join(valores)}")

    # Solicitar al usuario que cree una oración
    sn = input("主語 (SN) を選んでください: ")
    sv = input("動詞 (SV) を選んでください: ")
    cd = input("目的語 (CD) を選んでください（オプション、Enterを押してスキップ）: ")
    gadv = input("副詞 (GAdv) を選んでください（オプション、Enterを押してスキップ）: ")
    spre = input("前置詞句 (SPrep) を選んでください（オプション、Enterを押してスキップ）: ")

    # Construir la oración
    oracion_creada = " ".join(filter(None, [sn, gadv, cd, spre, sv]))
    print(f"\n作成した文: {oracion_creada}")

    # Validar si la oración es gramaticalmente correcta
    if (sn in sintagmas_japones["SN"] and sv in sintagmas_japones["SV"] and
        (not cd or cd in sintagmas_japones["CD"]) and
        (not gadv or gadv in sintagmas_japones["GAdv"]) and
        (not spre or spre in sintagmas_japones["SPrep"])):
        if validar_semantica(oracion_creada):
            print("正解です！文法的に正しい文を作成しました。")
        else:
            print("文法的には正しいですが、意味が不明確です。")
    else:
        print("不正解です。いくつかの要素が利用可能なオプションと一致しません。")

# Función para traducir oraciones
def traducir_oraciones():
    print("\n--- 日本語からスペイン語への翻訳 ---")
    oracion = random.choice(oraciones_japones)
    print(f"日本語の文: {oracion['reordenada']}")
    respuesta = input("この文をスペイン語に翻訳してください: ")

    if respuesta.strip() == oracion["traduccion"]:
        print("正解です！翻訳が正確です。")
    else:
        print(f"不正解です。正しい翻訳は: {oracion['traduccion']}")

# Interfaz gráfica con Tkinter
def crear_interfaz_grafica():
    ventana = tk.Tk()
    ventana.title("日本語の構文練習")

    def mostrar_mensaje(mensaje):
        messagebox.showinfo("Resultado", mensaje)

    def practicar_reordenacion_gui():
        oracion = random.choice(oraciones_japones)
        respuesta = simpledialog.askstring("Reordenar", f"Oración desglosada:\n{oracion['original']}\nReordena la oración:")
        if respuesta == oracion["reordenada"]:
            mostrar_mensaje("¡Correcto! Has reordenado la oración adecuadamente.")
        else:
            mostrar_mensaje(f"Incorrecto. La respuesta correcta es:\n{oracion['reordenada']}")

    def traducir_oraciones_gui():
        oracion = random.choice(oraciones_japones)
        respuesta = simpledialog.askstring("Traducir", f"Traduce al español:\n{oracion['reordenada']}")
        if respuesta == oracion["traduccion"]:
            mostrar_mensaje("¡Correcto! La traducción es precisa.")
        else:
            mostrar_mensaje(f"Incorrecto. La traducción correcta es:\n{oracion['traduccion']}")

    # Botones de la interfaz
    btn_reordenar = tk.Button(ventana, text="Reordenar Oraciones", command=practicar_reordenacion_gui)
    btn_reordenar.pack(pady=10)

    btn_traducir = tk.Button(ventana, text="Traducir Oraciones", command=traducir_oraciones_gui)
    btn_traducir.pack(pady=10)

    btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
    btn_salir.pack(pady=10)

    ventana.mainloop()

# Función principal
def main():
    while True:
        print("\n--- メインメニュー ---")
        print("1. 日本語で文の並べ替えを練習する")
        print("2. 日本語での構文の柔軟性の例を見る")
        print("3. 新しい文を作成する")
        print("4. 日本語からスペイン語への翻訳を練習する")
        print("5. インターフェースグラフィックを使用する")
        print("6. 終了する")
        opcion = input("オプションを選んでください: ")

        if opcion == "1":
            practicar_reordenacion()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            crear_nuevas_oraciones()
        elif opcion == "4":
            traducir_oraciones()
        elif opcion == "5":
            crear_interfaz_grafica()
        elif opcion == "6":
            print("練習ありがとうございました！さようなら。")
            break
        else:
            print("無効なオプションです。正しいオプションを選んでください。")

if __name__ == "__main__":
    main()
