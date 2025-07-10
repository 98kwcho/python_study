import random
gameRule = ["가위", "바위", "보"]

inputGame = input("가위 바위 보 중 하나 택")
comGame = gameRule[random.randint(0,2)]

if inputGame == "가위":
    if comGame == inputGame:
        print("비겼음.")
    elif comGame == "바위":
        print("졌음.")
    else:
        print("이겼음")

elif inputGame == "바위":
    if comGame == inputGame:
        print("비겼음.")
    elif comGame == "가위":
        print("졌음.")
    else:
        print("이겼음")

elif inputGame == "보":
    if comGame == inputGame:
        print("비겼음.")
    elif comGame == "바위":
        print("졌음.")
    else:
        print("이겼음")

else :
    print("잘못된 입력입니다.")