inputNum = int(input("정수를 입력하시오"))

for i in range(1, inputNum+1):
    if inputNum % i == 0:
        print(i , end=" ")