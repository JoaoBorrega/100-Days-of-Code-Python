programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

# Retriving items from the dictionary
print(programming_dictionary["Bug"])

print("\n")

# Adding new items from dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

print("\n")

# # Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

print("\n")

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

print("\n")

# Loop through a dictionary
for thing in programming_dictionary:
  print(thing)

print("\n")

for key in programming_dictionary:
  # print(key)
  print(programming_dictionary[key])

print("\n")

# 🚨 Exercicio 9.1 Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
# Don't change the code below 👇
print(student_grades)
# Fim exercicio 9.1

print("\n")

# Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lile", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary
travel_log_1 = {
  "France": {"cities_visited": ["Paris", "Lile", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting a Dictionary in a List
travel_log_2 = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lile", "Dijon"],
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  }
]

# 🚨 Exercicio 9.2 Dictionary in List
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# Do NOT change the code above
# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
# Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
# Fim exercicio 9.2

print("\n")