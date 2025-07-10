import random

def makeProblem(num1, num2):
    operator = ["+", "-", "*", "/"]
    operator_choose = random.randint(0, 3)

    print(f"{num1} {operator[operator_choose]} {num2} =? ")

inputNum1, inputNum2 = int(input("첫번째 정수 입력")), int(input("두번째 정수 입력"))
makeProblem(inputNum1, inputNum2)