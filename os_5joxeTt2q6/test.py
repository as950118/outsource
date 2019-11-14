#Calculate Grade
def CalculateGrade(result_of_score):
    if result_of_score >= 90:
        result_of_grade = "A"
    elif(result_of_score >= 75):
        result_of_grade = "B"
    elif(result_of_score >= 60):
        result_of_grade = "C"
    elif(result_of_score >= 50):
        result_of_grade = "D"
    else:
        result_of_grade = "F"
    return result_of_grade
    result_of_grade = CalculateGrade(result_of_score)

#Input score
score_of_labs = int(input("What is your lab percent so far(-1 if no labs yet)? "))
score_of_assignment = int(input("What is your assignment percent so far(-1 if no assignment yet)? "))
score_of_exams = int(input("What is your exam percent so far(-1 if no exams yet)? "))

#Set weight
if score_of_labs == -1:
    weight_of_labs = 0
else:
    weight_of_labs = 20

if score_of_assignment == -1:
    weight_of_assignment = 0
else:
    weight_of_assignment = 10

if score_of_exams == -1:
    weight_of_exams = 0
else:
    weight_of_exams = 70

#Calculate worth
worth_of_labs = weight_of_labs * score_of_labs
worth_of_assignment = weight_of_assignment * score_of_assignment
worth_of_exams = weight_of_exams * score_of_exams

#Calculate Score
sum_of_worth = worth_of_labs + worth_of_assignment + worth_of_exams
sum_of_weight = weight_of_labs + weight_of_assignment + weight_of_exams
result_of_score = sum_of_worth / sum_of_weight


print("If things keep going the way they are you should get a ", result_of_score, "in ther course, which is a ", result_of_score)
