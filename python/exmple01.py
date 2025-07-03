num1 =int(input("첫 번째 정수를 받습니다."))
num2 = int(input("두 번째 정수를 받습니다."))

print("합은 %d\n차는 %d\n곱은 %d\n평균은 %0.1f\n큰 수는 %d\n작은 수는 %d 입니다" %
       (num1+num2, num1-num2, num1*num2, (num1+num2)/2, max(num1, num2), min(num1, num2)))