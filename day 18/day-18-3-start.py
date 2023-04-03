# 🚨 Exemplo

from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

colours = ["medium aquamarine", "green yellow", "medium spring green", "deep pink", "tomato", "brown", "wheat",
          "dark magenta", "gold", "forest green"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3, 11):
    timmy_the_turtle.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()