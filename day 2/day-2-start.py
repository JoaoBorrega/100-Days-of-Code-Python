#Data Types
print("Hello"[0])

print("\n")

print("Hello"[2])

print("\n")

print("123" + "456")

print("\n")

print(123 + 456)

print("\n")

print(123_456_789)

print("\n")

# Float 3.14159
# Boolean True or False

# Exercicio
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " charecters.")
# fim exercicio
print("\n")

a = 123
print(type(a))
b = str(123)
print(type(b))
c = float(123)
print(type(c))
print(70 + float("100.5"))
print(str(70) + str(100))
print('\n')

# 🚨 Exercicio 2.1
# Num 87 -> 8+7 =15
two_digit_number = input("Type a two digit number: ")

# print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)
# fim exercicio 2.1

print("\n")

# 🚨 Exercicio 2.2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

result = float(weight) / float(height)**2
final_result = int(result)
print(final_result)
# fim exercicio 2.2

print("\n")

print(round(2.666666677777, 2))

print("\n")

result = 4 / 2
result /= 2
print(result)

print("\n")

# f-string
score = 0
height = 1.91
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

print("\n")

# 🚨 Exercicio 2.3
age = input("What is your current age? ")

years = 90 - int(age)
weeks = int(years) * 52
months = int(years) * 12
days = int(years) * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
# Fim exercicio 2.3

print("\n")

# 🚨 Projeto aula 2
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
total_bill = 150
num_people = 5
tip = 12
print("Welcome to the tip calculator")
input("What is the total bill? ")
input("What percentage tip would you like to give? ")
input("How many people to split the bill? ")
result = (total_bill / num_people) * 1.12
print(result)
# 🚨 fim projeto aula 2

# outra forma:
print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount}$")