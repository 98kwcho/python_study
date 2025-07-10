import random
import time

Texts = [
"인생은 용기 있는 모험이거나 아무것도 아니다.",
"행복은 태도가 결정한다.",
"성공은 작은 노력들이 모여 이루어진다.",
"가장 큰 영광은 넘어지지 않는 것이 아니라 넘어질 때마다 일어서는 것이다.",
"오늘 읽는 것이 내일의 리더를 만든다.",
"변화는 유일한 상수이다.",
"꿈을 꿔라, 그리고 실현시켜라.",
"자신을 믿어라, 그러면 무엇이든 가능하다.",
"인생은 짧다, 순간을 즐겨라.",
"배움은 끝이 없다.",
"말이 아닌 행동으로 보여줘라.",
"실수는 경험의 다른 이름이다.",
"친절은 결코 헛되지 않는다.",
"두려움은 환상일 뿐이다.",
"사랑은 모든 것을 이겨낸다.",
"단순함이 최고의 미덕이다.",
"과거는 잊고 현재에 집중하라.",
"작은 시작이 큰 결과를 낳는다.",
"모든 것을 포기할 때가 아닌, 더 열심히 할 때이다.",
"인생은 우리가 만드는 것이다."
]

print("타자 속도 게임입니다!")
input("엔터를 누르면 문장이 나옵니다.")

text_Asset = random.choice(Texts)

start_time = time.time()

print(text_Asset)

while True:

    inputText = input("\n텍스트 입력 :")

    end_time = time.time()
    elapsed_time = end_time - start_time

    correct = 0
    incorrect = 0

    for i in range(min(len(text_Asset), len(inputText))):
        if text_Asset[i] == inputText[i]:
            correct += 1
        else:
            incorrect += 1

    if correct == len(text_Asset):
        break


accuracy = correct / max(len(text_Asset),len(inputText)) * 100 

#per minutec
typeSpeed = (len(inputText) / elapsed_time ) * 60

print(f"오타 횟수 : {incorrect}번")
#print(f"정확도 : {accuracy:.2f}% 분당 속도 : {typeSpeed:.2f}타")