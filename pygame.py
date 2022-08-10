import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor('lightblue')
# player one

player_one = turtle.Turtle()
player_one.color('blue')
player_one.shape('turtle')
# player two

player_two = player_one.clone()
# color of player two

player_two.color('red')

# positioning of players
player_one.penup()
player_one.goto(-300,200)

player_two.penup()
player_two.goto(-300,-200)

# finish line
player_one.goto(250,-250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish', font=20)
player_one.penup()
player_one.color('blue')
player_one.goto(-300,200)
player_one.right(90)

# draw lines when moving

player_one.pendown()
player_two.pendown()

die = [1, 2, 3, 4, 5, 6]

# Game
for i in range(30):
    if player_one.pos() >=(300, 250):
        print("Player one wins the game")
        break
    elif player_two.pos() >=(300, -250):
        print("Player two wins the game")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30 * die_roll)
        time.sleep(.5)
        die_roll2 = random.choice(die)
        player_two.forward(30 * die_roll2)
        time.sleep(.5)





# turtle.done()