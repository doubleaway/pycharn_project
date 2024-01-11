#숫자 맞추기 게임 만들기
# 1 ~100까지의 임의의 수 생성 후 숫자를 입력받아 높은지 낮은지 정답인지 알려주고 맞히는 게임
# .random() 0.0 ~ 0.999999 사이 실수 반환
# .uniform(a,b) a, b사이의 실수 반환
# .randrange(a, b, step) a, b 사이의 정수값 반환, 인자가 하나일 경우 0 ~ a 사이의 정수 값, step값은 생략 가능
# .randint(a,b) a, b 사이의 정수 값 반환
import random

random_number = random.randint(1, 100)
#몇번 만에 맞췄는지
game_count = 1

while True:
    try:
        my_number = int(input("1 ~ 100사이의 숫자를 입력하세요."))
        if my_number > random_number:
            print("Down")
        elif my_number < random_number:
            print("Up")
        elif my_number == random_number:
            print(f"축하드립니다. {game_count}회 만에 맞췄습니다.")
            break
        game_count += 1
        #잘못된 값이 들어올 시 프로그램 종료
    except:
        print("1 ~ 100가지 숫자만 입력하실 수 있습니다. 다시 시도해주세요.")
