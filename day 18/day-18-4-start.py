# 🚨 Exemplo

import turtle as t
import random

tim = t.Turtle()

colours = ["medium aquamarine", "green yellow", "medium spring green", "deep pink", "tomato", "brown", "wheat",
          "dark magenta", "gold", "forest green"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))





