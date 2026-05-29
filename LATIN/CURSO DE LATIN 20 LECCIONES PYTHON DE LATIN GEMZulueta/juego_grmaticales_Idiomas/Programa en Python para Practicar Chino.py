import random
import speech_recognition as sr

# Ejercicio 1: Asociación de imágenes con palabras en chino
def asociacion_imagenes_palabras():
    print("\n--- 练习 1: 图片与词汇关联 ---")
    imagenes_palabras = {
        "苹果": "🍎",  # Manzana
        "狗": "🐕",    # Perro
        "太阳": "☀️",  # Sol
        "房子": "🏠",  # Casa
        "树": "🌳"     # Árbol
    }
    
    for palabra, imagen in imagenes_palabras.items():
        print(f"这张图片对应的词是什么？ {imagen}")
        respuesta = input("写出这个词: ").strip()
        if respuesta == palabra:
            print("正确！🎉\n")
        else:
            print(f"错误。正确答案是: {palabra}\n")

# Ejercicio 2: Dictado Interactivo en chino
def dictado_interactivo():
    print("\n--- 练习 2: 互动听写 ---")
    oraciones = [
        "太阳在天空中闪耀。",  # El sol brilla en el cielo.
        "狗在公园里玩耍。",    # El perro juega en el parque.
        "苹果又红又甜。",      # La manzana es roja y dulce.
        "房子有一个大花园。",  # La casa tiene un jardín grande.
        "树在夏天提供阴凉。"   # El árbol da sombra en verano.
    ]
    oracion = random.choice(oraciones)
    print(f"写出以下句子: '{oracion}'")
    respuesta = input("你的答案: ").strip()
    
    if respuesta == oracion:
        print("完美！没有错误。🎉\n")
    else:
        print(f"有一些错误。正确的句子是: {oracion}\n")

# Ejercicio 3: Ordenar Palabras en chino
def ordenar_palabras():
    print("\n--- 练习 3: 词语排序 ---")
    oraciones_desordenadas = [
        ["玩耍", "在", "公园", "里", "狗", "的"],
        ["闪耀", "天空", "在", "中", "太阳", "的"],
        ["又红", "又甜", "苹果", "是", "的"],
        ["大", "花园", "一个", "有", "房子", "的"],
        ["阴凉", "提供", "树", "夏天", "在", "的"]
    ]
    palabras = random.choice(oraciones_desordenadas)
    print(f"将以下词语排序成句子: {', '.join(palabras)}")
    respuesta = input("你的答案: ").strip()
    
    oracion_correcta = "".join(palabras)
    if respuesta == oracion_correcta:
        print("正确！句子排序正确。🎉\n")
    else:
        print(f"错误。正确的句子是: {oracion_correcta}\n")

# Ejercicio 4: Rellenar Espacios en Blanco en chino
def rellenar_espacios():
    print("\n--- 练习 4: 填空 ---")
    oraciones = [
        "太阳在___中闪耀。",  # El sol brilla en el cielo.
        "狗在___里玩耍。",    # El perro juega en el parque.
        "苹果又___又甜。",    # La manzana es roja y dulce.
        "房子有一个___花园。", # La casa tiene un jardín grande.
        "树在夏天提供___。"   # El árbol da sombra en verano.
    ]
    respuestas_correctas = ["天空", "公园", "红", "大", "阴凉"]
    
    oracion = random.choice(oraciones)
    print(f"完成句子: {oracion}")
    respuesta = input("你的答案: ").strip()
    
    indice = oraciones.index(oracion)
    if respuesta == respuestas_correctas[indice]:
        print("正确！🎉\n")
    else:
        print(f"错误。正确答案是: {respuestas_correctas[indice]}\n")

# Ejercicio 5: Lectura en Voz Alta en chino
def lectura_voz_alta():
    print("\n--- 练习 5: 朗读 ---")
    oraciones = [
        "太阳在天空中闪耀。",  # El sol brilla en el cielo.
        "狗在公园里玩耍。",    # El perro juega en el parque.
        "苹果又红又甜。",      # La manzana es roja y dulce.
        "房子有一个大花园。",  # La casa tiene un jardín grande.
        "树在夏天提供阴凉。"   # El árbol da sombra en verano.
    ]
    oracion = random.choice(oraciones)
    print(f"朗读以下句子: '{oracion}'")
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("正在听...")
        audio = recognizer.listen(source)
        
        try:
            texto_reconocido = recognizer.recognize_google(audio, language="zh-CN")
            print(f"你说的是: {texto_reconocido}")
            if texto_reconocido == oracion:
                print("完美！你读得正确。🎉\n")
            else:
                print(f"有一些错误。正确的句子是: {oracion}\n")
        except sr.UnknownValueError:
            print("无法理解你说的话。请再试一次。\n")
        except sr.RequestError:
            print("语音识别服务出错。\n")

# Menú principal
def main():
    while True:
        print("欢迎使用中文学习应用")
        print("1. 图片与词汇关联")
        print("2. 互动听写")
        print("3. 词语排序")
        print("4. 填空")
        print("5. 朗读")
        print("6. 退出")
        opcion = input("选择一个选项 (1-6): ").strip()
        
        if opcion == "1":
            asociacion_imagenes_palabras()
        elif opcion == "2":
            dictado_interactivo()
        elif opcion == "3":
            ordenar_palabras()
        elif opcion == "4":
            rellenar_espacios()
        elif opcion == "5":
            lectura_voz_alta()
        elif opcion == "6":
            print("感谢使用本应用！再见。👋")
            break
        else:
            print("无效选项。请重试。\n")

if __name__ == "__main__":
    main()
