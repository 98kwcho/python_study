def getMoneyText(amount):
    korText = ["", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    digitText =["", "십", "백", "천"]

    if amount <= 0 or amount > 1000:
        return "잘못된 입력입니다. 다시 확인하세요."

    result = ""
    str_amount = str(amount)

    for char in range(len(str_amount)):
        digit = int(str_amount[char])
        if digit != 0:
            result = result + korText[digit - 1] + digitText[len(str_amount) - char - 1]

    return result

amount = 909
print(f"{amount}만원 => {getMoneyText(amount)}만원이다.")