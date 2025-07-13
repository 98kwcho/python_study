import random
import time

'''
ReadMe:

1. 게임이 시작 될 때 필요한 부분들을 생성.
    - 폭탄리스트, 매 판 새로운 순서-> 셔플로 리스트 재생성, 생명, 타이머 생성,
      생명체크(생명 0이면 False 로 반복문 종료시키도록),

2. while을 함수로 만들면 안의 내용도 집어 넣어야 하고
    받아서 사용하는 인자들이 많아지므로 while은 밖에서 만든다.

3. 게임 시작 멘트나 멘트들을 모아두는 함수를 생성 -> 상수로 변경되고 -> list로 변경되었음
      
### 추가 구현 기록
# 게임의 난이도 조정 1번째 맞추는 개수 생성 -( 이후 추가: 난이도 조절에서 시간을 줄이는 구현 예정 )
# 유저 생명력 default 값 부여 - ( 이후 추가 : 난이도 조절에서 라이프 개수를 줄이는 방법도 구현 예정)


# 리드미에 순서도를 만들어서 적어두고 구현을 순서대로 하면 편했을것 같은데..
# 함수로 추가 내용들과 아이디어가 생기니까 이슈발생
# 다음부터는 순서도를 만들고 구현을 완료한 뒤 추가 내용을 생성하고
# 함수의 분리는 코드가 완성되고 나서 실행해도 괜찮을 것 같다


'''


BOOM_LIST = [
    "참외", "수박", "토끼", "의자", "컴퓨터", 
    "자동차", "사자", "초콜릿", "연필", "강아지",
    "노트북", "냉장고", "포도", "커피", "바나나",
    "비행기", "바다", "펜", "신발", "달력"
]


GAME_START_MSG_MENT = "게임을 시작합니다"
GAME_START_MSG_C_THREE = "3"
GAME_START_MSG_C_TWO = "2"
GAME_START_MSG_C_ONE = "1"
GAME_START_MSG_C_START = "START"
TIME_ONE_SEC = 1
TIME_TWO_SEC = 2
LIFE_DIFAULT_VALUE = 3

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

# 유저에게 단어를 받는 인풋
def input_user_word():
    global user_input # 전역 변수임을 명시
    user_input = input().split()

# 유저에게 인풋 받기 
import threading
def input_timeOut_elapsed(TIME_TWO_SEC):    
    # 누적 시간을 계산하기 위한 전역변수 세팅
    global elapsed_time
    global remaining_time
    # 함수 객체 자체를 의미하므로 실행하지 않고 바라보고 있다는 의미 / 함수() 는 즉시 실행해버림
    input_thread = threading.Thread(target=input_user_word)

    # 스레드 시작(비동기적으로 get_user_input() 실행)
    input_thread.start()
    
    # timeout초 동안 기다림 -> 직접 구현함
    # input_thread.join(timeout=TIME_TWO_SEC) 
    start_time = time.time()
    # 스레드 실행중일때 True이면 계속 돌아감
    while input_thread.is_alive():
        elapsed_time = time.time() - start_time

        # 시간 초과인지 아닌지 판단
        # if input_thread.is_alive():
        if elapsed_time >= TIME_TWO_SEC:    
            print("⏰ 시간 초과! 입력 실패")
            return None, elapsed_time
    
    # 입력 완료시 스레드 종료하고 리턴함
    end_time = time.time()
    total_time = end_time - start_time
    return user_input, total_time

# 유저에게 몇 레벨로 플레이할지 물어보는 인풋
def input_user_lever():
    print("플레이 할 단계를 선택하세요")
    print("1. LV1")
    print("2. LV2")
    print("2. LV3")
    return input()


# 랜덤 단어를 출력
def random_output(boom_list):
    return random.choice(boom_list)

# 랜덤 문장의 출력 순서를 변경해줌
def random_shuffle(boom_list):
    random.shuffle(boom_list)

# 생명 생성
def generate_life_default(n):
     return n

# 생명이 0인지 체크
def check_life_zoro(life):
    if life == 0:
        return True
    return False

# 폭탄단어와 유저입력이 같은지 체크
def check_boomAndInput(boom,userInput):
    if boom == userInput:
        return True
    return False

# 타이머
def time_two_second(n):
    timeout = n # 60에 1분
    start = time.time()
    while time.time() - start < timeout:
	    pass

# 순서대로 메시지를 뱉아내도록 생성 
def game_star_msg():
    for msg in range(GAME_START_SEQUENCE[:-1]):
        print(msg)
        time_two_second(TIME_ONE_SEC)

# 게임의 난이도 조정 1번째 맞추는 개수 생성 -( 이후 추가: 난이도 조절에서 시간을 줄이는 구현 예정 )
def choice_game_level(input_level):
    return 10 * input_level

# 목숨을 깎는 함수..!
# 본문에서 lamdba human_life : hu_life -1로 사용
def decrease_life(human_life):
    return human_life -1




# ---------------------------아래는 게임의 영역 ------------------




# 게임 시작시 순서를 섞어줌
random_shuffle(BOOM_LIST)

# 레벨 물어보는 것 부터 생성
# -> 레벨에 맞춰서 아래의 휴먼 라이프에 오버라이딩해서
# if문으로 인자 하나 더 받는 함수 사용
# genrate_life_default(LIFE_DIFAULT_VALUE,level)
level = choice_game_level(input_user_lever())

# 유저 생명력 default 값 부여 - ( 이후 추가 : 난이도 조절에서 라이프 개수를 줄이는 방법도 구현 예정)
human_life = generate_life_default(LIFE_DIFAULT_VALUE)

#
correct = 0


# 중복 허용 여부 True면 word_list에 깊은 복사
allow_duplicates = ALLOW_DUPLICATES_TRUE
word_list = BOOM_LIST if allow_duplicates else BOOM_LIST[:]

i = 0

while i < level and word_list:
    # 붐 단어를 뽑아옴 생성
    boom = random_output(word_list)
    print(boom)
    i += 1
    # False이면  값을 복사해서 공간이 확보된 상황 -> 줄여주는 방향으로
    if not allow_duplicates:
        word_list.remove(boom)

    # 유저 입력 경과시간과 흐른시간 판단
    # + if 문에서 None,False,"",[],{}빈 딕셔너리 빈 리스트 빈 문자열 등이면 조건 False
    # + 나머지는 다 True로 적용

    # None인지 인풋인지 / 경과시간
    result, elapsed_time = input_timeOut_elapsed(TIME_TWO_SEC)

    # 남은 시간
    remaining_time += elapsed_time
    
    #
    if remaining_time >= LIMIT_TIME:
        print("모든 시간 다 사용함")
        break

    if result == boom:
        correct += 1
        print(f"남은 시간: {LIMIT_TIME - remaining_time}")
    else:
        human_life -= 1
        print(f"남은 시간: {LIMIT_TIME - remaining_time}")
    
    if human_life == 0:
        print("목숨을 다 사용했습니다.")
        break

print(f"맞춘 개수: {correct}")
if human_life:
    print(f"남은 생명력: {human_life}")
print(f"경과 시간: {remaining_time}")

        
            

        


    











