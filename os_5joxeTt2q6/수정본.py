#헷갈려서 변수명들을 조금 변경 했습니다 ^^
#사용자한테 입력받는 값은 랩의 퍼센트, 숙제 퍼센트, 시험 퍼센트
#큰 부분은 아닌데 점수랑 퍼센트랑 용어를 혼동되게 제가 설명 드려서 다시 바로 잡았어요.
#
#한가지 전제조건을 제가 잘못 설명했었네요 ㅠ ㅠ
#만약에 하나의 과목(랩, 숙제, 시험 중 하나)의 시험을 아직 치지 않았으면 -1을 입력 하고 이것은 최종 계산할 때 제외가 되네요.
#목적이 현재까지 진행 3과목에 대한 점수와 학점을 보는건데... 만약 아직 시험을 치지 않았다면.. -1을 입력 하고 분모에서 해당 과목을 제외하라고 하네요
#예를 들어 '랩'과 '숙제'만 퍼센테이지가 나왔고 '시험'은 아직 안본 상태라면 시험은 -1을 입력 할꺼고, 나중에 학점을 구할 때
# 랩 퍼센테이지 + 숙제 퍼센테이지만 하고.. 나누기 할 때도 /3이 아닌 /2로 하는거네요. 현재까지 진행된 과목만으로 학점을 구하는게 목적이네요
# 만약 3과목 퍼센테이지를 -1이 아니라 다 넣으면 나누기 할 때는 /3이 될테고.. 만약 한과목만 퍼센테이지가 나왔으면 /1이 되겠네요.


#Input percentage
percentage_of_lab = int(input("What is your lab percent so far(-1 if no labs yet)? "))
percentage_of_assignment = int(input("What is your assignment percent so far(-1 if no assignment yet)? "))
percentage_of_exam = int(input("What is your exam percent so far(-1 if no exams yet)? "))

#module
def getscore():
    # Get weight
    if percentage_of_lab == -1:
        weight_of_lab = 0
    else:
        weight_of_lab = 20

    if percentage_of_assignment == -1:
        weight_of_assignment = 0
    else:
        weight_of_assignment = 10

    if percentage_of_exam == -1:
        weight_of_exam = 0
    else:
        weight_of_exam = 70

    # Calculate scoreß
    score_of_lab = weight_of_lab * percentage_of_lab
    score_of_assignment = weight_of_assignment * percentage_of_assignment
    score_of_exam = weight_of_exam * percentage_of_exam

    overallweight = weight_of_lab + weight_of_assignment + weight_of_exam
    earnedpercent = score_of_lab + score_of_assignment + score_of_exam

    # Catch exception (division by zero)
    if overallweight == 0:
        return 0
    else:
        return earnedpercent / overallweight

result_of_score = getscore()


# Calculate Grade
def CalculateGrade(result_of_score):
    if (result_of_score >= 90):
        result_of_grade = "A"
    elif (result_of_score >= 75):
        result_of_grade = "B"
    elif (result_of_score >= 60):
        result_of_grade = "C"
    elif (result_of_score >= 50):
        result_of_grade = "D"
    else:
        result_of_grade = "F"
    return result_of_grade

result_of_grade = CalculateGrade(result_of_score)

print("If things keep going the way they are you should get a " + str(round(result_of_score, 1)) + "% in the course, which is a " + result_of_grade + ".")