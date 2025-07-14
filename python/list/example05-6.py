def findSame(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return True
        
    return False

list_1 = [1,2,3,4,5,6,7,8,9, 0]
list_2 = [1,3,5,7,9, 11, 13, 15, 17 ,19]

print(findSame(list_1, list_2))