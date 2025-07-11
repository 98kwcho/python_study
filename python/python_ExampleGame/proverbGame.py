import random

def checkAnswer(num1, num2):
    for i in range(min(len(num1), len(num2))):

        # 문자씩으로 비교 중 다르면 오답처리
        if num1[i] != num2[i]:
            print("오답!")
            return False
                
        # for문의 마지막까지 오답이 검출되지 않으면 정답 출력 및 스코어 +1
        elif i == min(len(num1), len(num2)) - 1:
            print("정답!")
            return True


# 게임에 사용할 속담을 튜블에 이중 리스트로 저장
proverbList = [
("가는 말이 고와야", "오는 말이 곱다"),
("등잔 밑이", "어둡다"),
("고생 끝에", "낙이 온다"),
("도둑이", "제 발 저리다"),
("누워서", "떡 먹기"),
("개구리 올챙이 적", "생각 못 한다"),
("말 한마디로", "천 냥 빚 갚는다"),
("백지장도", "맞들면 낫다"),
("산 넘어", "산"),
("호랑이도", "제 말하면 온다"),
("우물 안", "개구리"),
("아는 길도", "물어가라")
]

gameCount = 0                   # 게임 시도 횟수
correct = 0                     # 맞힌 횟수

#lastQuiz1, lastReply1 = "", ""  while 문으로 중복처리 시 사용한 변수
#lastQuiz2, lastReply2 = "", ""

print("속담 맞추기 게임입니다!")
input("엔터를 누르면 속담이 나옵니다.")

while gameCount < 5:

    # 속담의 앞말을 가릴지 뒷말을 가릴지 고르기 위한 랜덤 함수
    quizType = random.randint(0,1)

    # 뒷말을 가리는 경우
    if quizType == 0:
        quiz, reply = random.choice(proverbList)

        #list의 remove 함수를 이용해 랜덤함수에서 고른 요소를 제거하여 후의 중복을 방지
        proverbList.remove((quiz, reply))

        #while을 이용한 랜덤으로 뽑은 값의 중복 제거
        #while lastQuiz1 != quiz and lastReply1 != reply :
        #    quiz, reply = random.choice(proverbList)

            #if lastQuiz1 != quiz and lastReply1 != reply :
            #    lastQuiz1 = quiz
            #    lastReply1 = reply

        # 가리는 말 초기화
        blank = ""
        hint = ""

        # 가리는 문자열을 만들기 위해 띄어쓰기를 제외한 문자에 _를 추가
        for i in range(len(reply)):
            if reply[i] != " ":
                blank += "_"

                if i == 0:
                    hint += reply[i]
                else :
                    hint += "_"

            else :
                blank += " "
                hint += " "

        print(f"문제 : {quiz} {blank} ?")

        for i in range(2):
            if i == 1:
                print(f"문제 힌트 : {quiz} {hint} ?")

            inputText = input("텍스트 입력 : ").strip()

            # 정답 비교를 위한 for문
            if checkAnswer(inputText,reply):
                correct+=1
                break

    # 앞말을 가리는 경우    
    elif quizType == 1:

        reply, quiz = random.choice(proverbList)

        #list의 remove 함수를 이용해 랜덤함수에서 고른 요소를 제거하여 후의 중복을 방지
        proverbList.remove((reply, quiz))

        #while을 이용한 랜덤으로 뽑은 값의 중복 제거
        #while lastQuiz2 != quiz and lastReply2 != reply :
        #    reply, quiz = random.choice(proverbList)
            
            #if lastQuiz2 != quiz and lastReply2 != reply :
            #    lastQuiz2 = quiz
            #    lastReply2 = reply
        
        # 가리는 말 초기화
        blank = ""
        hint = ""

        # 가리는 문자열을 만들기 위해 띄어쓰기를 제외한 문자에 _를 추가
        for i in range(len(reply)):
            if reply[i] != " ":
                blank += "_"

                if i == 0:
                    hint += reply[i]
                else :
                    hint += "_"

            else :
                blank += " "
                hint += " "

        print(f"문제 : {blank} {quiz} ?")


        for i in range(2):
            if i == 1:
                print(f"문제 힌트 : {hint}{quiz} ?")

            inputText = input("텍스트 입력 : ").strip()

            # 정답 비교를 위한 for문
            if checkAnswer(inputText,reply):
                correct+=1                
                break
    
    # 게임 시도 증가
    gameCount += 1

# 게임 결과 출력
print(f"게임 종료!\b결과 발표! 맞힌 개수 : {correct} 틀린 개수 : {gameCount - correct}")
