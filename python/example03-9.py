for i in range(2, 20):
    for j in range(1,i+1):
        if j != 1 and j != i:
            if i % j == 0:
                break           
        elif i == j:
            print(j , end=" ")

