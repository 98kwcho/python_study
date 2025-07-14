def inputList():
    res_list = list()
    for i in range(5):
        inputNum = int(input("입력"))
        res_list.append(inputNum)

    return res_list

result = inputList()
rm_overlap = set(result)
result = sorted(rm_overlap)

print(result)