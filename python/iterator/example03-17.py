for i in range(21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end= " ")
    elif i%3 ==0:
        print("Fizz", end= " ")
    elif i%5 == 0:
        print("Buzz", end= " ")
    else:
        print("*", end= " ")

# 위의 if else를 삼항 연산자로 표현
#for i in range(10):
#    print("FizzBuzz"if i % 3 == 0 and i % 5 == 0 else "Fizz" if i%3 ==0 else "Buzz" if i%5 == 0 else "*" , end= " ")
