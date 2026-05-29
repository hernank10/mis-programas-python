import random

def 识别含义():
    单词表 = {"correr": "快速移动", "brillante": "反射很多光"}
    词, 含义 = random.choice(list(单词表.items()))
    选项 = [含义, "错误选项 1", "错误选项 2"]
    random.shuffle(选项)
    print(f"‘{词}’ 的正确含义是什么？")
    for i, 选项项 in enumerate(选项, 1):
        print(f"{i}. {选项项}")
    答案 = int(input("请选择正确答案: "))
    print("正确！" if 选项[答案 - 1] == 含义 else "错误")

def 同义词_反义词():
    同义词 = {"feliz": "alegre", "rápido": "veloz"}
    反义词 = {"feliz": "triste", "rápido": "lento"}
    词 = random.choice(list(同义词.keys()))
    print(f"请写出‘{词}’的一个同义词或反义词：")
    答案 = input().strip()
    if 答案 in (同义词[词], 反义词[词]):
        print("正确！")
    else:
        print(f"错误。正确答案: 同义词‘{同义词[词]}’，反义词‘{反义词[词]}’")

def 填空():
    句子表 = {"brillante": "太阳今天非常 ______ 。"}
    词, 句子 = random.choice(list(句子表.items()))
    print(句子)
    答案 = input("请填写正确的单词: ").strip()
    if 答案 == 词:
        print("正确！")
    else:
        print(f"错误，正确答案是‘{词}’")

def 词汇分类():
    词汇类别 = {"científico": "技术", "pintoresco": "文学"}
    词, 类别 = random.choice(list(词汇类别.items()))
    print(f"‘{词}’属于哪个语境？")
    答案 = input("请选择：技术、口语、文学: ").strip().lower()
    if 答案 == 类别:
        print("正确！")
    else:
        print(f"错误，正确类别是‘{类别}’")

def 解释单词():
    词 = "correr"
    print(f"请写出‘{词}’的定义：")
    input()
    print("感谢您的回答！正确定义是：快速移动。")

def 菜单():
    while True:
        print("\n单词练习菜单")
        print("1. 识别单词含义")
        print("2. 同义词与反义词练习")
        print("3. 句子填空")
        print("4. 词汇语境分类")
        print("5. 词语定义")
        print("6. 退出")
        选项 = input("请选择一个选项: ")
        if 选项 == "1":
            识别含义()
        elif 选项 == "2":
            同义词_反义词()
        elif 选项 == "3":
            填空()
        elif 选项 == "4":
            词汇分类()
        elif 选项 == "5":
            解释单词()
        elif 选项 == "6":
            print("再见！")
            break
        else:
            print("无效选项，请重试。")

菜单()
