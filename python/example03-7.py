inputNum = int(input("정수를 입력하시오"))
sum = 0

for i in range(1, inputNum+1):
    sum += i**2

print(f"전체 합은 {sum}입니다.")