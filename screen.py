from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball

from paddle_collision import PadCollision


coordinates = [0, 0, 0, 0, 0, 0] # coordinates list is updated by ball, and pad classes

collision = PadCollision()
middle = Turtle()
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
middle.hideturtle()
middle.color('green')
middle.setpos(x=0, y=300)
middle.goto(x=0, y=-300)

######
pad1 = Paddle1(coordinates)
pad2 = Paddle2(coordinates)
ball = Ball(coordinates)
screen.onkeypress(pad1.up, key='Up')
screen.onkeypress(pad1.down, key='Down')
screen.onkeypress(pad2.up, key='w')
screen.onkeypress(pad2.down, key='s')
ball.create_ball()

##### evaluate ball and pad coordinates


print(coordinates)

'''

Collision evaluation

'''
######

screen.exitonclick()

'''
screen.listen()
screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
'''
