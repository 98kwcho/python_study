import secrets
import qrcode
from IPython.display import display

def generate_lotto_numbers():
    numbers = set()
    while len(numbers) < 6:
        number = secrets.randbelow(45) + 1  # 1~45까지의 랜덤 숫자
        numbers.add(number)
    return sorted(numbers)

# 사용자 입력 및 로또 추첨
try:
    count = int(input("로또 세트 개수를 입력하세요 (예: 1~5): "))
    if count < 1:
        print("1 이상의 숫자를 입력하세요.")
    else:
        result_text = "===== 로또 번호 추첨 결과 =====\n"
        for i in range(1, count + 1):
            lotto = generate_lotto_numbers()
            result_text += f"{i}세트: {lotto}\n"
        
        print(result_text)

        # QR코드 생성
        qr = qrcode.make(result_text)
        qr.show()
        display(qr)

except ValueError:
    print("숫자만 입력해주세요.")