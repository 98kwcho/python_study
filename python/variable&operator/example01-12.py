inputNumber = int(input("100000에서 999999사이의 수를 입력해주세요."))
resNumber = str(inputNumber // 1000)  +',' + str(inputNumber % 1000)
#inputNumber = input("100000에서 999999사이의 수를 입력해주세요.")
#resNumber = inputNumber[:3] +',' + inputNumber[3:]

print(resNumber)

"""inNum =int(input("100000에서 999999사이의 수를 입력해주세요."))

if inNum >= 100000 and inNum< 1000000:
    moreT = inNum//1000
    lessT = inNum%1000
    print(f"{moreT},{lessT}")"""