def findCommonDivisor():
    num1 = int(input("첫번째 수 입력 :"))
    num2 = int(input("두번째 수 입력 :"))
    max_div = 0
    for i in range(1, num1+1):
        if num1 % i == 0:
            for j in range(1, num2+1):
                if num2 % j == 0 and i == j:
                    max_div = i 

    return max_div


res = findCommonDivisor()
print("최대 공약수는", res)