# 🚨 How to Open and Read using "with"

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# 🚨 ou

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# 🚨 open and insert

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# 🚨 open and write

# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text.")

# 🚨 if file is on Desktop

# with open("/Users/joao_/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# 🚨 if file is on Desktop and we are on other folder

# with open("../../Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)