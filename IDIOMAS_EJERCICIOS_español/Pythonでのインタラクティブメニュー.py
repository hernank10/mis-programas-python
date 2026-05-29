import random

def 意味決定():
    辞書 = {"correr": "速く歩く", "brillante": "光を強く反射する"}
    単語, 意味 = random.choice(list(辞書.items()))
    選択肢 = [意味, "間違った選択肢1", "間違った選択肢2"]
    random.shuffle(選択肢)
    print(f"単語‘{単語}’の意味は何ですか？")
    for i, 選択肢 in enumerate(選択肢, 1):
        print(f"{i}. {選択肢}")
    回答 = int(input("正しい答えを選んでください: "))
    print("正解！" if 選択肢[回答 - 1] == 意味 else "不正解")

def 類義語_対義語():
    類義語 = {"feliz": "alegre", "rápido": "veloz"}
    対義語 = {"feliz": "triste", "rápido": "lento"}
    単語 = random.choice(list(類義語.keys()))
    print(f"単語‘{単語}’の類義語または対義語を入力してください: ")
    回答 = input().strip()
    if 回答 in (類義語[単語], 対義語[単語]):
        print("正解！")
    else:
        print(f"不正解。正しい答え: 類義語‘{類義語[単語]}’、対義語‘{対義語[単語]}’")

def 空欄補充():
    文 = {"brillante": "今日は太陽がとても______です。"}
    単語, 文 = random.choice(list(文.items()))
    print(文)
    回答 = input("正しい単語を入力してください: ").strip()
    if 回答 == 単語:
        print("正解！")
    else:
        print(f"不正解、正しい答え: ‘{単語}’")

def 単語分類():
    カテゴリー = {"científico": "技術", "pintoresco": "文学的"}
    単語, カテゴリー名 = random.choice(list(カテゴリー.items()))
    print(f"単語‘{単語}’はどのカテゴリーに属しますか？")
    回答 = input("選択: 技術、口語、文学的: ").strip().lower()
    if 回答 == カテゴリー名:
        print("正解！")
    else:
        print(f"不正解、正しいカテゴリー: ‘{カテゴリー名}’")

def 単語説明():
    単語 = "correr"
    print(f"単語‘{単語}’の定義を書いてください: ")
    input()
    print("ありがとう！正しい定義: 速く歩く。")

def メニュー():
    while True:
        print("\n単語練習メニュー")
        print("1. 単語の意味を決定")
        print("2. 類義語と対義語")
        print("3. 空欄補充")
        print("4. 単語分類")
        print("5. 単語説明")
        print("6. 終了")
        選択 = input("オプションを選択してください: ")
        if 選択 == "1":
            意味決定()
        elif 選択 == "2":
            類義語_対義語()
        elif 選択 == "3":
            空欄補充()
        elif 選択 == "4":
            単語分類()
        elif 選択 == "5":
            単語説明()
        elif 選択 == "6":
            print("さようなら！")
            break
        else:
            print("無効な入力です。もう一度試してください。")

メニュー()
