# Review:
# Create a function called greet().
def greet():
# Write 3 print statements inside the function.
  print("Hello ")
  print("to ")
  print("all")
# Call the greet() function and run your code.
greet()

print("\n")

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"why they call you {name}?")

greet_with_name("Joao")

print("\n")

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is your location? {location}.")

greet_with("Joao","Portugal")

print("\n")

def greet_with_two(name, location, age):
  print(f"Hello {name}")
  print(f"What is your location? {location}")
  print(f"is your age {age}?")

greet_with_two(age="32", name="Joao", location="Portugal")

print("\n")

# 🚨 Exercicio 8.1 Paint Area Calculator
import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.
# Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
# Fim exercicio 8.1

print("\n")

# 🚨 Exercicio 8.2 Prime Numbers
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
#Write your code above this line 👆
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
# Fim exercicio 8.1

print("\n")