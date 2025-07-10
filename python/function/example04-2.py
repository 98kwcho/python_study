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

print(get_add(1,2))
print(get_sub(1,2))
print(get_mul(1,2))
print(get_div(1,2))