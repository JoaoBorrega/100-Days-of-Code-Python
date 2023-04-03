print("Hello")
num_char = len("Hello")
print(num_char)

print("\n")

# inicio exemplo
def my_func():
  print("Hello")
  print("Bye")

my_func()
# fim exemplo

print("\n")

# 🚨 Exercicio Reeborg's World Hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

jump()
jump()
jump()
jump()
jump()
jump()
# ou em vez de escrever jump() 6 vezes
# usar:
# for step in range(6):
#    jump()
# Fim exercicio Hurdle 1

print("\n")

# 🚨 Exercicio Reeborg's World Hurdle 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    jump()
  # Fim exercicio Hurdle 2

print("\n")

# 🚨 Exercicio Reeborg's World Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
# Fim exercicio Hurdle 3

print("\n")

# 🚨 Exercicio Reeborg's World Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
# Fim exercicio Hurdle 4

print("\n")

# 🚨 Exercicio Reeborg's World Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
# Fim exercicio Maze