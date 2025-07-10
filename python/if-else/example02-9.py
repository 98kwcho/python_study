import random

# random.random()
# random.randrange(0, 5)
# random.randint(0, 10)

operator = ["+", "-", "*", "/"]
choiesOperator = random.randint(0, 3)
ranNum1 = random.randint(1, 100)
ranNum2 = random.randint(1, 100)

print(f"{ranNum1}{operator[choiesOperator]}{ranNum2} = ?")

inputRes = input("답")

if choiesOperator == 0:
    if(int(inputRes) == (ranNum1 + ranNum2) ):
        print("정답")

    else :
        print("오답")

elif choiesOperator == 1:
    if(int(inputRes) == (ranNum1 - ranNum2) ):
        print("정답")

    else :
        print("오답")

elif choiesOperator == 2:
    if(int(inputRes) == (ranNum1 * ranNum2) ):
        print("정답")

    else :
        print("오답")

else :
    if(float(inputRes) == (ranNum1 / ranNum2) or ((ranNum1 / ranNum2)-float(inputRes)) < 0.01):
        print("정답")

    else :
        print("오답")

# 3.10 이후 버전에서 사용하는 match case 
'''match choiesOperator:   
    case 0:
        if(int(inputRes) == (ranNum1 + ranNum2) ):
            print("정답")

        else :
            print("오답")
    case 1:
        if(int(inputRes) == (ranNum1 - ranNum2) ):
            print("정답")

        else :
            print("오답")
    case 2:
        if(int(inputRes) == (ranNum1 * ranNum2) ):
            print("정답")

        else :
            print("오답")                     
    case 3:
        if(float(inputRes) == (ranNum1 / ranNum2) or ((ranNum1 / ranNum2)-float(inputRes)) < 0.01):
          print("정답")

        else :
            print("오답")'''