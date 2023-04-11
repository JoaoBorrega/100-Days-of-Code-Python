# 🚨 Handling Errors and Exceptions

# # File not found:
# with open("a_file.txt") as file:
#     file.read()

# # Key error:
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

# # Index error:
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # Type error:
# text = "abc"
# print(text + 5)

# 🚨 Catching Exceptions

# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there where no exceptions
# finally: do this no matter what happens

# File not found:

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["jfdjggr"])     # to work, change "jfdjggr" to "key"
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")


# 🚨 Raising Exceptions

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["jfdjggr"])     # to work, change "jfdjggr" to "key"
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeErrorError("This is an error that i made up.")


# 🚨 Raising Exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3m")

bmi = weight / (height ** 2)
print(bmi)


# 🚨 Exercicio 30.1 IndexError Handling

fruits = ["Apple", "Pear", "Orange"]

# To do: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")
make_pie(4)

# Result
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
make_pie(4)

# 🚨 Exercicio 30.2 IndexError Handling

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    total_likes = total_likes + post['Likes']

print(total_likes)

# Result
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0

print(total_likes)