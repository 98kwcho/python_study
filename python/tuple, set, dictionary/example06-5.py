def shopping(dic):
    sum = 0
    for i in dic.values():
        sum += i

    return sum

my_dic = {"옷" :  100, "컴퓨터" : 2000 , "모니터" : 320}
print(shopping(my_dic))