import random

def makeList():
    res_list = []
    list_size = random.randint(1, 100)
    for i in range(list_size):
        res_list.append("a" + str(i))

    return res_list

def chooseIndex(list_for_choose):
    #list_index = random.randint(0, len(list_for_choose))
    list_index = random.choice(list_for_choose)
    return list_for_choose[list_index]

print(chooseIndex(makeList()))   
    