def printMonth(monthNum):
    month_dic = {1 :"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8: "August", 9:"September", 10:"October", 11 : "November", 12 : "December"}

    for i in month_dic:
        if i == monthNum:
            print(month_dic[i])
            

printMonth(int(input("1~12 입력")))