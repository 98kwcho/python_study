num = int(input("4자리 정수를 입력"))

res = (num // 1000) + ((num % 1000) // 100) + ((num % 100) // 10) + (num % 10)

print("각 자리 수의 합은 ", res)