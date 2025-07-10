def get_add(num1, num2):
    return num1 + num2

def get_sub(num1, num2):
    return num1 - num2

def get_mul(num1, num2):
    return num1*num2

def get_div(num1, num2):
    if num1==0 or num2 ==0:
        print("입력값 오류 ")
    else :
        return num1/num2

def calc(num1, num2):
    print("덧셈은", get_add(num1,num2))
    print("뺄셈는", get_sub(num1,num2))
    print("곱셈은", get_mul(num1,num2))
    print("나눗셈은", get_div(num1,num2))

calc(5,76)