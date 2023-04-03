# class User:
#     pass
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Joao"
#
# print(user_1.username)

print("\n")

class User:
    def __init__(self):
        print("new user being created...")

user_1 = User()
user_1.id = "001"
user_1.username = "Joao"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Borrega"

print(user_2.username)

print("\n")

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "Joao")

print(user_1.username)
print(user_1.id)
print(user_1.followers)

print("\n")
user_2 = User("002", "Borrega")

print(user_2.username)
print(user_2.id)
print(user_2.followers)

print("\n")

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Joao")
user_2 = User("002", "Borrega")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)