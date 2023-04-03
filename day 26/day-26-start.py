# List Comprehension

# 🚨 escrever no python console:

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]


# 🚨 escrever no python console:

# name = "Joao"
# letters_list = [letter for letter in name]


# 🚨 escrever no python console:

# range_list = [num * 2 for num in range(1,5)]


# 🚨 escrever no python console:

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(nane) < 5]

# long_names = [name.upper() for name in names if len(name) > 5]


# 🚨 Feito pela prof

# #For Loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# #List Comprehension
# new_list = [n + 1 for n in numbers]
#
# #String as List
# name = "Angela"
# letters_list = [letter for letter in name]
#
# #Range as List
# range_list = [n * 2 for n in range(1, 5)]
#
# #Conditional List Comprenhension
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
#
# upper_case_names = [name.upper() for name in names if len(name) > 4]
#
# #Dictionary Comprehension
# import random
# student_grades = {name: random.randint(1, 100) for name in names}
# print(student_grades)
#
# passed_students = {
#     student: grade
#     for (student, grade) in student_grades.items() if grade >= 60
# }
# print(passed_students)


# 🚨 Exercicio 26.3 Data Overlap

with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

# Write your code above 👆

print(result)
# fim exercicio

# 🚨 Exercicio 26.4 Dictionary Comprehension 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word:len(word) for word in sentence.split()}

print(result)
# fim exercicio

# 🚨 Exercicio 26.5 Dictionary Comprehension 2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
# fim exercicio


# Looping through dictionaries:
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    if row.student == "Angela":
        print(row.score)