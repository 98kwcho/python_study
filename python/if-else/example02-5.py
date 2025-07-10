inputNum1 = int(input("첫 번째 정수 입력"))
inputNum2 = int(input("두 번째 정수 입력"))
inputNum3 = int(input("세 번째 정수 입력"))

if inputNum1 > inputNum2 :
    if inputNum2 > inputNum3:
        print("가장 작은 수는 %d" % inputNum3)

    else:
        print("가장 작은 수는 %d" % inputNum2)

else:
    if inputNum1 > inputNum3:
        print("가장 작은 수는 %d" % inputNum3)

    else:
        print("가장 작은 수는 %d" % inputNum1)    