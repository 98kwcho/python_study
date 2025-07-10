for i in range(2, 21):
    for j in range(1,i+1):
        if j != 1 and j != i:
            if i % j == 0:
                break           
        elif i == j:
            print(j , end=" ")


# while 문으로 구현한 2 ~ 20에서 소수 찾기
#maxNum = 20
#number = 2
#count = 2

#while number <maxNum:
#    divisor  =2
#    prime = True
#
#    while divisor < number:
#        if number % divisor == 0:
#            prime = False
#            break
#        divisor += 1
#    
#    if prime:
#        count += 1
#        print(number, end=" ")
#    number+=1