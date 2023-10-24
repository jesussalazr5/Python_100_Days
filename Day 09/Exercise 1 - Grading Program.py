# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for i in student_scores:
    if student_scores[i] > 90:
        student_grades.update({i:"Outstanding"})
    elif student_scores[i] > 80: 
        student_grades.update({i:"Exceeds Expectations"})
    elif student_scores[i] > 70: 
        student_grades.update({i:"Acceptable"})
    else:
        student_grades.update({i:"Fail"})


# 🚨 Don't change the code below 👇
print(student_grades)