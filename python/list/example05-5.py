def checkListIndex(asset):
    if asset[0] == asset[len(asset) - 1]:
        return True
    
    else :
        return False

def sum_listIndex(list):
    sum = 0
    for i in range(len(list)):
        if checkListIndex(list[i]):
            sum += 1
    
    return sum

stringList = ["aba", "eve", "think", "sure", "depend"]

print(sum_listIndex(stringList))