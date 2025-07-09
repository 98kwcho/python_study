def fibo(n):	
    if n == 1 or n == 2:
        return 1
    else:
    	return fibo(n-1) + fibo(n-2)

inputNum = int(input("정수를 입력하시오"))

for i in range(inputNum):
	print(fibo(i)) 