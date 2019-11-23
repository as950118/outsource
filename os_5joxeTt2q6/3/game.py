import random

# 처음 이름 입력받는 것에 대한 함수
def inputname():
    name = str(input("Welcome to my game, what is your first name? "))
    print("")
    while not name.isalpha():
        # 올바르지 못할경우 sorry 출력 후 반복
        print("Iʼm sorry {0}, names are only allowed to contain letters.".format(name))
        name = str(input("Please re-enter your name: "))
    return name

# 패턴에 관한 함수들
# all is same
def is_same(dices):
    for i in range(1, 5):
        if dices[i-1] != dices[i]:
            # 같은게 하나라도 없다면 틀린 경우이다
            return False
    return True
# sum is prime
def is_prime(number):
    counter = 2
    if number == 1:
        return False
    while counter < number:
        if number % counter == 0:
            return False
        counter += 1
    return True
# 3 is same
def three_same(dices):
    for i in range(5-2):
        # 같은 숫자를 센다
        num_of_same = 0
        for j in range(i+1,5):
            if dices[i] == dices[j]:
                num_of_same += 1
        # 같은 숫자가 3개라면 맞는 경우이다
        if num_of_same == 3:
            return True
    return False
# all is diffrent
def is_diff(dices):
    # set으로 타입을 변경하면 중복되는 값은 사라진다
    # 만약 중복되는 값이 없어서 set(dices)의 길이가 5라면
    # 모두 다른 값이라고 생각할 수 있다
    if len(set(dices)) == 5:
        return True
    return False
# get pattern
def getpattern(dices):
    if is_same(dices):
        return "all 5 dice have the same value", 100
    if is_prime(sum(dices)):
        return "all 5 dice add up to a prime number", 50
    if three_same(dices):
        return "3 of 5 dice have the same value", 30
    if is_diff(dices):
        return "all different values", 25
    return "nothing", 0

# 패턴 점수와 총합 점수에 대한 함수
def getpoint(dices):
    #패턴 종류와 점수
    pattern_name, pattern_point = getpattern(dices)
    while True:
        y_n = str(input(("Would you like to score the pattern points for {0} ({1} points)? [y/n] "
                         .format(pattern_name, pattern_point))))
        # 패턴 점수를 얻을 경우
        if y_n.lower() == 'y':
            # 패턴 점수를 반환하고 종료
            return pattern_point
        # 패턴 점수를 얻지 않을 경우
        elif y_n.lower() == 'n':
            # 계속 진행
            break
        else:
            # y, n 외의 다른값이 들어올 경우 다시 반복
            print("Iʼm sorry, {0} is not a valid choice, please enter y or n".format(y_n))
    print("")
    #총합 점수
    sum_point = sum(dices)
    while True:
        y_n = str(input(("Would you like to score the sum of the dice ({0} points)? [y/n] "
                         .format(sum_point))))
        # 총합 점수를 얻을 경우
        if y_n.lower() == 'y':
            # 총합 점수를 반환하고 종료
            return sum_point
        # 총합 점수를 얻지 않을 경우
        elif y_n.lower() == 'n':
            # 계속 진행
            break
        else:
            # y, n 외의 다른값이 들어올 경우 다시 반복
            print("Iʼm sorry, {0} is not a valid choice, please enter y or n".format(y_n))
    print("")
    # 둘다 선택하지 않을 경우에는
    # -1을 반환하고 종료한다
    return -1


# 하나의 turn에 대한 함수
def turn():
    dices = [random.randint(1, 7) for i in range(5)]
    print("You rolled 5 dice. Their values are {0},{1},{2},{3},{4}"
          .format(dices[0], dices[1], dices[2], dices[3], dices[4]))
    # 첫번째 경우에서 얻은 포인트
    first_point = getpoint(dices)
    # 첫번째 경우에서 얻은 포인트가 -1이 아니라면,
    # 즉 포인트를 얻었다면 해당 turn은 종료한다.
    if first_point != -1:
        return first_point

    # 포인트를 얻지 않았다면 최대 2번까지 반복한다.

    #다시 던지는 행위는 최대 2번까지
    for rerolled in range(2):
        # 다시 던지는 경우 조사
        rerolled_dices = list()
        for i in range(5):
            while True:
                y_n = str(input("Would you like to reroll die {0}? [y/n] ".format(i + 1)))
                # 다시 던질 경우에는
                if y_n.lower() == 'y':
                    # 랜덤값
                    rerolled_dices.append(random.randint(1, 7))
                    break
                # 다시 안던질 경우에는
                elif y_n.lower() == 'n':
                    # 기존값
                    rerolled_dices.append(dices[i])
                    break
                else:
                    # y, n 외의 다른값이 들어올 경우 다시 반복
                    print("Iʼm sorry, {0} is not a valid choice, please enter y or n".format(y_n))
        print("")
        # 다시 던진 결과와
        print("You rerolled some dice and the new values are {0},{1},{2},{3},{4}"
          .format(rerolled_dices[0], rerolled_dices[1], rerolled_dices[2], rerolled_dices[3], rerolled_dices[4]))
        print("")
        # 그에 따른 점수를 보여주고 점수를 얻을지 말지 결정한다
        rerolled_point = getpoint(rerolled_dices)
        # 마찬가지로 얻은 포인트가 -1이 아니라면,
        # 즉 포인트를 얻었다면 해당 turn은 종료한다
        if rerolled_point != -1:
            return rerolled_point

    # 2번을 했는데도 점수가 없다면
    # 마지막 경우에서 얻을 수 있는 점수를 반환한다.
    # 이 경우에는 총합 혹은 패턴 점수 중 높은 점수를 반환한다.
    return max(getpattern(rerolled_dices)[1], sum(rerolled_dices))


def main():
    # 첫번째 출력
    print("Programming Fundamentals 201935, 이름, 학번")
    print("")
    # 이름 입력받기
    # 첫번째만 대문자로, 즉 캐피탈라이즈 해준다
    name = inputname().capitalize()
    print("")
    #### 게임 시작
    print("Thank you {0}, you start off with 0 points, letʼs play!".format(name))
    print("")
    ret_point = 0 # 최종 포인트
    for i in range(1,11):
        print("Turn {0}:".format(i))
        ret_point += turn()
        print("Your score is now {0} points. Taking points ended your turn.\nEnd of turn {1}."
              .format(ret_point, i))
        print("\n\n\n\n\n")
    #### 게임 종료
    # 최종 포인트와 멘트
    # 400점 초과
    if ret_point > 400:
        ret_ment = "this is a good score"
    # 200점 초과
    elif ret_point >= 200:
        ret_ment = "this is a average score"
    # 200점 미만
    else:
        while True:
            y_n = str(input("do you like to play again? [y/n] "))
            # 다시 하겠다고 하는 경우
            if y_n.lower() == 'y':
                # 게임 재시작
                return main()
            # 종료하겠다고 하는경우
            elif y_n.lower() == 'n':
                # 종료
                return
            else:
                # y, n 외의 다른값이 들어올 경우 다시 반복
                print("Iʼm sorry, {0} is not a valid choice, please enter y or n".format(y_n))

    # 종료하기
    print("Your total score is {0} and {1}".format(ret_point))
    return

# 게임 실행
main()