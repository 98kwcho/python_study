height = int(input("키를 입력해 주세요."))
weight = int(input("몸무게를 입력해 주세요."))

avr_weight = (height - 100) * 0.9

if weight > avr_weight:
    print("과체중입니다.")

elif weight == avr_weight:
    print("표준 체중입니다.")

else :
    print("저체중입니다.")

