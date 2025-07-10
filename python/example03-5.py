
inputNum  = int(input("정수 값 입력 : "))

for i in range(inputNum):
    for j in range(i+1):
        print("*" , end= " ")
    print("")



#for i in range(num + 1):
#   for j in range(num + 1):
#       if j<=i:
#            print("*", end="")
#   print("\n") 