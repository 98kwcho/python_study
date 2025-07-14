def makeDict(list1, list2):
    res_dic = {}
    for i in range(min(len(list1), len(list2))):
        res_dic[list1[i]] = list2[i]
    
    return res_dic


list_1 =[1,2,3,4,5,6,7,8,9]
list_2 =[10,20,30,40,50,60,70,80,90]

print(makeDict(list_1, list_2))