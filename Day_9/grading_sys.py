student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

for key in student_scores:
  if(student_scores[key] > 90):
    student_grades[key] = "Outstanding"
  elif(student_scores[key] > 80):
    student_grades[key] = "Exceeds expectation"
  elif(student_scores[key] > 70):
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
