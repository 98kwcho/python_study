def getIntRange(a, b, msg):
    inputNum = int(input(msg))

    while a > inputNum or b < inputNum:
            inputNum = int(input("잘못된 입력입니다." + msg))

    return inputNum

month = getIntRange(1,12, "월을 입력하시오(1부터 12사이의 값)")
day = getIntRange(1,31, "일을 입력하시오(1부터 31사이의 값)")

print(f"{month}월/{day}일")