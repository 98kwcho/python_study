def checkKeys(dic, inputNum):
    for i in dic:
        if i == inputNum:
            return True
    
    return False


dic_1 = { 1: 10, 2:20, 3:30, 4:40, 5:50 , 6:60}

inputN = int(input("키 입력"))

if checkKeys(dic_1, inputN):
    print("키가 있다.")
else:
    print("키가 없다")