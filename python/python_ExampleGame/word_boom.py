# 랜덤으로 주어지는 한글 단어를 2초 안에 입력
# 2초안에 입력하면 점수가 가산되고, 2초가 넘으면 생명이 감소
# 생명이 없으면 게임 종료

import time as t
import random as r

def checkAnswer(quiz, answer):
    for i in range(min(len(quiz), len(answer))):

        # 문자씩으로 비교 중 다르면 오답처리
        if quiz[i] != answer[i]:
            return False
                
        # for문의 마지막까지 오답이 검출되지 않으면 정답 출력 및 스코어 +1
        elif i == min(len(quiz), len(answer)) - 1:
            return True
        
def calTime(startTime, endTime):
    return endTime - startTime

def gameStart():
    print("한글 단어 폭탄 게임!!!")
    input("아무 키나 누르면 스타트합니다.")

def gameEnd(life, Score):    
    if life <= 0:
        print(f"GAME OVER\n라이프가 전부 감소하여 게임이 종료되었습니다.\nScore : {Score}")

    else : 
        print(f"게임 결과 발표!!\nScore : {Score}")

def mainGame(life, maxScore, Score):
    
    gameStart()

    while life > 0 and Score < maxScore:

        randomWord = KoreanList[r.randint(0, len(KoreanList) - 1)]

        print(f"단어 : {randomWord} ")
        
        startTime = t.time()

        inputText = input("단어를 빠르게 입력하세요.")

        endTime = t.time()

        if checkAnswer(randomWord, inputText):
            print("정답!!")
            Score+=1

        elif(calTime(startTime, endTime) > 2):
            print("시간 초과로 라이프 감소!!")
            life -= 1

        else :
            print("오답으로 인해 점수 감소!!")
            Score -= 1


    gameEnd(life, Score)


KoreanList = [
"사과","바나나","오렌지","딸기",
"포도","수박","멜론","배",
"복숭아","자두","체리","키위",
"망고","파인애플","감","석류","무화과",
"블루베리","라즈베리","블랙베리","레몬","라임",
"자몽","아보카도","코코넛","패션프루트","리치",
"용과","두리안","람부탄"
]

life = 3
score = 0
maxScore = 20

mainGame(life, maxScore, score)