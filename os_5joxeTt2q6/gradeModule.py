#gradeModule
def gradeModule():
    #Input score
    def InputScore(sentence):
        score_of_thing = int(input(sentence))
        return score_of_thing
    score_of_labs = InputScore("What is your lab percent so far(-1 if no labs yet)? ")
    score_of_assignment = InputScore("What is your assignment percent so far(-1 if no assignment yet)? ")
    score_of_exams = InputScore("What is your exam percent so far(-1 if no exams yet)? ")

    #Set weight
    def CheckScore(score, weight):
        if score == -1:
            return 0
        else:
            return weight
    weight_of_labs = CheckScore(score_of_labs, 20)
    weight_of_assignment = CheckScore(score_of_assignment, 10)
    weight_of_exams = CheckScore(score_of_exams, 70)

    #Calculate worth
    def CalculateWorth(score, weight):
        worth = score * weight
        return worth
    worth_of_labs = CalculateWorth(score_of_labs, weight_of_labs)
    worth_of_assignment = CalculateWorth(score_of_assignment, weight_of_assignment)
    worth_of_exams = CalculateWorth(score_of_exams, weight_of_exams)

    #Sum worth and weight
    def SumThings(first, second, third):
        sum_of_things = first + second + third
        return sum_of_things
    sum_of_worth = SumThings(worth_of_labs, worth_of_assignment, worth_of_exams)
    sum_of_weight = SumThings(weight_of_labs, weight_of_assignment, weight_of_exams)

    #Calculate score
    def CalculateScore(worth, weight):
        score = worth / weight
        return score
    result_of_score = CalculateScore(sum_of_worth, sum_of_weight)

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

    #Display Score and Grade
    def DisplayScoreAndGrade(result_of_score, result_of_grade):
        result_of_sentence = "If things keep going the way they are you should get a {0}% in the course, which is a {1}.".format(round(result_of_score, 1), result_of_grade)
        return result_of_sentence
    print(DisplayScoreAndGrade(result_of_score, result_of_grade))
gradeModule()