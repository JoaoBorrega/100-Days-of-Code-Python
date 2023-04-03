# exemplo
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")
    # fim exemplo

print("\n")

# Example rollercoaster
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride")

# == iqual ; != different

print("\n")

# 🚨 Exercicio 3.1
number = int(input("Which number do you want to check? "))

x = number % 2
if x == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
# Fim exercicio 3.1

print("\n")

# outra forma
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
# fim

print("\n")

# Example rollercoaster 1
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5$.")
    elif age <= 18:
        print("Please pay 7$.")
    else:
        print("Please pay 12$.")
else:
    print("Sorry, you have to grow taller before you can ride.")

print("\n")

# 🚨 Exercicio 3.2
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / (height ** 2))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
# Fim exercicio 3.2

print("\n")

# 🚨 Exercicio 3.3 Leap year
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year")
else:
    print("Not leap year")
# Fim exercicio 3.3

print("\n")

# Example rollercoaster 2
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5$.")
    elif age <= 18:
        bill = 7
        print("Youth tickets ara 7$.")
    else:
        bill = 12
        print("Adult tickets are 12$.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3  # ou bill += 3

    print(f"Your final bill is {bill}$")

else:
    print("Sorry, you have to grow taller before you can ride.")
    # Fim exemplo

print("\n")

# 🚨 Exercicio 3.4 Pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

Bill = 0

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = 18
            print("bill 18")
        else:
            bill = 17
            print("bill 17")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = 16
            print("bill 16")
        else:
            bill = 15
            print("bill 15")
if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = 24
            print("bill 24")
        else:
            bill = 23
            print("bill 23")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = 21
            print("bill 21")
        else:
            bill = 20
            print("bill 20")
if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = 29
            print("bill 29")
        else:
            bill = 28
            print("bill 28")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = 26
            print("bill 26")
        else:
            bill = 25
            print("bill 25")
# Fim exercicio
# outra forma
bill = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
# fim exercicio 3.4

print("\n")

# Example rollercoaster 3
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5$.")
    elif age <= 18:
        bill = 7
        print("Youth tickets ara 7$.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us")
    else:
        bill = 12
        print("Adult tickets are 12$.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3  # ou bill += 3

    print(f"Your final bill is {bill}$")

else:
    print("Sorry, you have to grow taller before you can ride.")
    # Fim exemplo

print("\n")

# 🚨 Exercicio 3.5 Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2

lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
# fim exercicio 3.5

print("\n")

# 🚨 Projeto aula 3