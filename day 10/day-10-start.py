# Functions with outputs

def format_name(f_name, l_name):
  print(f_name.title())
  print(l_name.title())

format_name("angela", "anGeLA")
# Fim exemplo

print("\n")

# Outro exemplo
def format_name_1(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  print(f"{formated_f_name} {formated_l_name}")

format_name_1("jOaO", "BORREGA")
# fim exemplo

print("\n")

# Outro exemplo
def format_name_2(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  return f"{formated_f_name} {formated_l_name}"

formated_string = format_name_2("jOaO", "BORREGA")
print(formated_string)
# fim exemplo

print("\n")

# Outro exemplo
def format_name_3(f_name, l_name):
  if f_name == "" or l_name == "":
    return
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name_3(input("What is your first name? "), input("what is your last name? ")))
# Fim exemplo

print("\n")

# 🚨 Exercicio 10.1 Days in Month
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
# Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
# Fim exercicio 10.1

print("\n")

# Return as an early exit
def format_name_3(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name"""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"
print(format_name_3(input("What is your first name? "), input("what is your last name? ")))
# Fim exemplo

print("\n")

# Dictionary named operations
# Add
def add(n1, n2):
  return n1 + n2
# Subtract
def subtract(n1, n2):
  return n1 - n2
# Multiply
def multiply(n1, n2):
  return n1 * n2
# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
# Ver exemplo da calculadora

