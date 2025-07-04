import random

operator = ["+", "-", "*", "//"]
choiesOperator = random.randint(0, 3)
ranNum1 = random.randint(0, 100)
ranNum2 = random.randint(0, 100)

print(f"{ranNum1}{operator[choiesOperator]}{ranNum2} = ?")

inputRes = int(input("답"))

if choiesOperator == 0:
    if(inputRes == (ranNum1 + ranNum2) ):
        print("정답")

    else :
        print("오답")

elif choiesOperator == 1:
    if(inputRes == (ranNum1 - ranNum2) ):
        print("정답")

    else :
        print("오답")

elif choiesOperator == 2:
    if(inputRes == (ranNum1 * ranNum2) ):
        print("정답")

    else :
        print("오답")

else :
    if(inputRes == (ranNum1 // ranNum2) ):
        print("정답")

    else :
        print("오답")