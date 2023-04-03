import random

random_integer = random.randint(1,10)
print(random_integer)

# 0.00000 - 0.99999...
random_float = random.random()
print(random_float)

print("\n")

# 🚨 Exercicio 4.1 Heads or Tails
import random

random_size = random.randint(0,1)

if random_size == 1:
    print("Heads")
else:
    print("Tails")
# Fim exercicio 4.1

print("\n")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[1])
print(states_of_america[-1])

print("\n")

states_of_america.append("JoaoBorrega")
print(states_of_america)

print("\n")

states_of_america.extend(["AnaPires", "JoaoEnsinas", "AnaCarolina"])
print(states_of_america)

print("\n")

# 🚨 Exercicio 4.2 Banker Roulette
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above 👆
#Write your code below this line 👇
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")
# Fim exercicio 4.2

print("\n")

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

print("\n")

# 🚨 Exercicio 4.3 Treasure Map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above 👆
#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

#Write your code above this row 👆
# Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
#F Fim exercicio 4.3

print("\n")

