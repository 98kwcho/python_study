def list_sum(user_list):
    sum = 0
    for i in range(len(user_list)):
        sum += user_list[i]

    return sum

testList = []
inputNum = int(input("입력 받을 수를 입력"))
for i in range(inputNum):
    inputIndex = int(input("입력 "))
    testList.append(inputIndex)
res = list_sum(testList)

print(f"리스트의 총 합은 {res}")
