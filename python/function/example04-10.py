def testPrime(n):
    for i in range(1,n+1):
        if i != 1 and i != n:
            if n % i == 0:
                break           
        elif n == i:
            print(n , end=" ")


for i in range(2, 100):
    testPrime(i)
