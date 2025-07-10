def getGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

inputScore = int(input("점수를 입력하세요."))

print("해당 학생의 학점은", getGrade(inputScore))