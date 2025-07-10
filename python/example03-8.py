def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b 
    return a

inputNum = int(input("정수를 입력하시오"))

for i in range(inputNum):
	print(fib(i)) 
     