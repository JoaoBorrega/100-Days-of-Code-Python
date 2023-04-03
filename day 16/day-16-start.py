from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward((150))

print("\n")

my_screen = Screen()
print(my_screen.canvheight)
# my_screen its object, and canvheight is the attribute
my_screen.exitonclick()

print("\n")

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'

print(table)

