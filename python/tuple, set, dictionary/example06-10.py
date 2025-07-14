def commonCheck(str1, str2):
    res_1 = set(str1)
    res_2 = set(str2)

    return res_1.intersection(res_2)

input1 = input("첫번째")
input2 = input("두번째")

print(commonCheck(input1, input2))