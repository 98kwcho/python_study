sum = 0

for i in range(1, 100):
    if i % 3 == 0:
        sum += i

print(f"3의 배수 전체 합은 {sum}")