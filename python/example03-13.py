inputNum = int(input("정수를 입력하시오: "))

a, b = 0, 1
for i in range(inputNum+1):
    print(a, end= " ")
    a, b = b, a + b