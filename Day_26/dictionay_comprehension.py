# # region passing students
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# student_scores = {student: random.randint(1, 100) for student in names}
#
# passing_students = {student: score for (student, score) in student_scores.items() if score >= 60}
#
# print(passing_students)
# # endregion
#
#
# # region string_split and convert to dictionary
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence_list = sentence.split(" ")
# result = {word: len(word) for (word) in sentence_list}
#
# print(result)
# # endregion
#
#
# # region exercise
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {week: (degree * 9 / 5) + 32 for (week, degree) in weather_c.items()}
#
# print(weather_f)
# # endregion

# region pandas - iterate data_frames row-wise
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
import pandas

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

for (index, data) in student_data_frame.iterrows():
    print(index)
    print(data)
    print(data.student)
    print(data.score)
# endregion
