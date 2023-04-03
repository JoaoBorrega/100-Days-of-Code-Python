fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

print("\n")

# 🚨 Exercicio 5.1 Average Height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above 👆
#Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height = total_height + height
# print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students = number_of_students + 1
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)
# Fim exercicio 5.1

print("\n")

# 🚨 Exercicio 5.2 High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above 👆
#Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
# Fim exercicio 5.2

print("\n")

for number in range(1, 11):
  print(number)

print("\n")

for numbers in range(1, 11, 3):
  print(numbers)

print("\n")

total = 0
for number in range(1, 101):
  total += number
print(total)

print("\n")

# 🚨 Exercicio 5.3 Adding Even Numbers
total = 0
for number in range(2, 101, 2):
    total += number
print(total)
# Fim exercicio 5.3
# Outra forma
total2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total2 += number
print(total2)
# Fim

print("\n")

# 🚨 Exercicio 5.4 FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
# Fim exercicio 5.4