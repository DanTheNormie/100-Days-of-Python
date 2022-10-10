# 🚨 Don't change the code below 👇
import random

student_heights = list()
for n in range(0,5):
  student_heights.append(random.randint(100,200))

#for n in range(0, len(student_heights)):
# student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

  

#Write your code below this row 👇

sum_of_heights = 0
no_of_students = 0

for n in student_heights:
  sum_of_heights += n
  no_of_students += 1
  

avg_height = sum_of_heights/no_of_students

print(f"The student heights are : \n\n {student_heights} \n")


print(f"The avg height of the students is : {avg_height}")