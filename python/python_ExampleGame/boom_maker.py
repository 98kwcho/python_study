import random
import time
import threading
import os

BOOM_LIST = [
    "참외", "수박", "토끼", "의자", "컴퓨터", 
    "자동차", "사자", "초콜릿", "연필", "강아지",
    "노트북", "냉장고", "포도", "커피", "바나나",
    "비행기", "바다", "펜", "신발", "달력",
    "책상", "거울", "우산", "고양이", "핸드폰",
    "라디오", "텔레비전", "냄비", "토마토", "양말"
]

GAME_START_MSG_MENT = "게임을 시작합니다"
GAME_START_MSG_C_THREE = "3"
GAME_START_MSG_C_TWO = "2"
GAME_START_MSG_C_ONE = "1"
GAME_START_MSG_C_START = "START"
TIME_ONE_SEC = 1
TIME_TWO_SEC = 2
LIFE_DIFAULT_VALUE = 3

TIME_THREE_SEC = 3
TIME_FOUR_SEC = 4
TIME_FIVE_SEC = 5
TIME_TEN_SEC = 10


GAME_START_SEQUENCE = [
    GAME_START_MSG_C_THREE,
    GAME_START_MSG_C_TWO,
    GAME_START_MSG_C_ONE,
    GAME_START_MSG_C_START
]

ALLOW_DUPLICATES_TRUE = True
ALLOW_DUPLICATES_FLASE = False

LIMIT_TIME = 30

life = 3
score = 0
remaining_time = 0
user_input = None
elapsed_time = 0


def input_user_word():
    global user_input
    user_input = input()
    os.system('cls')

def input_timeOut_elapsed(TIME_TWO_SEC):    
    global elapsed_time
    global remaining_time

    input_thread = threading.Thread(target=input_user_word)
    input_thread.start()
    
    start_time = time.time()
    while input_thread.is_alive():
        elapsed_time = time.time() - start_time

        if elapsed_time >= TIME_TWO_SEC:    
            print("⏰ 시간 초과! 입력 실패")
            print("-----------------------")
            return None, elapsed_time
    
    end_time = time.time()
    total_time = end_time - start_time
    return user_input, total_time

def input_user_level():
    print("플레이 할 단계를 선택하세요")
    print("1. LV1")
    print("2. LV2")
    print("2. LV3")
    return input()

def random_output(boom_list):
    return random.choice(boom_list)

def random_shuffle(boom_list):
    random.shuffle(boom_list)

def generate_life_default(n):
     return n

def check_life_zoro(life):
    if life == 0:
        return True
    return False

def check_boomAndInput(boom,userInput):
    return boom == userInput
  
def time_two_second(n):
    timeout = n
    start = time.time()
    while time.time() - start < timeout:
	    pass

def game_star_msg():
    for msg in GAME_START_SEQUENCE[:-1]:
        print(msg)
        time_two_second(TIME_ONE_SEC)
    print("!!!------"+GAME_START_MSG_C_START+"------!!!")
    print("-----------------------")

def choice_game_level(input_level):
    return 10 * input_level

# ---------------------------아래는 게임의 영역 ------------------
# ------------게임 세팅 -----------------------------------------

random_shuffle(BOOM_LIST)

level = choice_game_level(int(input_user_level()))
print("--------잠시 후 시작 합니다---------")
human_life = generate_life_default(LIFE_DIFAULT_VALUE)

# 중복 허용 여부 True면 word_list에 깊은 복사
allow_duplicates = ALLOW_DUPLICATES_TRUE
word_list = BOOM_LIST if allow_duplicates else BOOM_LIST[:]
correct = 0
i = 0

# ------------게임 시작 -----------------------------------------

game_star_msg()

while i < level:
    boom = random_output(word_list)
    print(boom)
    i += 1

    if not allow_duplicates:
        word_list.remove(boom)

    user_input, elapsed_time = input_timeOut_elapsed(TIME_FIVE_SEC)
    remaining_time += elapsed_time
    print("-----------------------")
    if remaining_time >= LIMIT_TIME:
        print("모든 시간 다 사용함")
        break
    print(f"남은 시간: {LIMIT_TIME - remaining_time:.2f}")
    print("-----------------------")

    if check_boomAndInput(boom,user_input):
        correct += 1
    else:
        human_life -= 1

    if check_life_zoro(human_life):
        print("목숨 끝")
        break


# ------------게임 종료 -----------------------------------------
print("-----------------------")
print("-------go saeng--------")
print("-----------------------")
print("-----------------------")
print(f"맞춘 개수: {correct}")
if human_life:
    print(f"남은 생명력: {human_life}")
print(f"경과 시간: {remaining_time:.2f}")