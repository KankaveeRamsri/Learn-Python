# grade = [str(i) for i in input("Input: ").split(',') ]

# score_grade = []

# for score in grade :
#     score = score.strip()
#     if score == 'A':
#         score_grade.append(4)
#     elif score == 'B+':
#         score_grade.append(3.5)
#     elif score == 'B':
#         score_grade.append(3)
#     elif score == 'C+':
#         score_grade.append(2.5)
#     elif score == 'C':
#         score_grade.append(2)
#     elif score == 'D+':
#         score_grade.append(1.5)
#     elif score == 'D':
#         score_grade.append(1)
#     elif score == 'E':
#         score_grade.append(0.5)

# def get_average_score(score):
#     sum_score = 0
#     for scores in score :
#         sum_score += scores
    
#     return sum_score/len(score)

# average_score = get_average_score(score_grade)

# def get_average_grade(average_score):
#     if average_score >= 3.75 :
#         return 'A'
#     elif average_score >= 3.25 :
#         return 'B+'
#     elif average_score >= 2.75 :
#         return 'B'
#     elif average_score >= 2.25 :
#         return 'C+'
#     elif average_score >= 1.75 :
#         return 'C'
#     elif average_score >= 1.25 :
#         return 'D+'
#     elif average_score >= 0.75 :
#         return 'D'
#     else :
#         return 'E'

# result = get_average_grade(average_score)
# print("Output: {}".format(result))


print("------------------------------------")

def get_average_grade_points(grades):
    GRADE_POINTS = {
        "A": 4,
        "B+": 3.5,
        "B": 3,
        "C+": 2.5,
        "C": 2,
        "D+": 1.5,
        "D": 1,
        "E": 0.5,
    }

    average_point = sum([GRADE_POINTS.get(g, 0) for g in grades]) / len(grades)
    return average_point


def grading(point):
    grade = "I"
    if point >= 3.75:
        grade = "A"
    elif point >= 3.25:
        grade = "B+"
    elif point >= 2.75:
        grade = "B"
    elif point >= 2.25:
        grade = "C+"
    elif point >= 1.75:
        grade = "C"
    elif point >= 1.25:
        grade = "D+"
    elif point >= 0.75:
        grade = "D"
    else:
        grade = "E"

    return grade


if __name__ == "__main__":
    # input
    grades = [g.strip() for g in input("Input: ").split(",")]

    # process
    points = get_average_grade_points(grades)
    grade = grading(points)

    # output
    print("Output:", grade)
        


