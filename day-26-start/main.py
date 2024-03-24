import random
import pandas

# Dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}



# Iterating over a pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Looping through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a dara frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    # Access student value in the row
    # print(row.student)
    # print(row.score)
