def checkPass(p):
    inNum = False
    inAlpha = False
    isCapital = False

    while True:

        for i in p:
            if i.isdigit():
                inNum = True
                break

        for i in p:
            if i.isalpha():
                inAlpha = True
                break

        for i in p:
            if i.isupper():
                isCapital = True   
                break     

        if len(p) < 8:
            print("비밀번호는 8글자 이상이어야 합니다.")
        elif not inAlpha:
            print("비밀번호엔 영어를 사용해야 합니다.")
        elif not isCapital:
            print("적어도 한 문자는 대문자여야 합니다.")
        elif not inNum:
            print("비밀번호엔 숫자를 사용해야 합니다.")
        else:
            print("비밀번호가 안전합니다.")
            return p  

        p = input("비밀번호를 다시 입력하시오: ")

passWord = input("비밀번호를 입력하시오: ")
checkPass(passWord)