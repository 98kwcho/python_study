r = float(input("원의 반지름 입력"))

if r >= 0:
    print("원의 지름은", round(3.14 *(r ** 2))*2, "입니다.")

else:
    print("잘못된 값입니다.")