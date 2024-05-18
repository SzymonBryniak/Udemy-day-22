from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
from paddle_collision import PadCollision
import threading
middle = Turtle()
screen = Screen()


ball = Ball()

ball.create_ball()
################

screen.setup(width=600, height=600)
screen.bgcolor("black")

middle.hideturtle()
middle.color('green')
middle.setpos(x=0, y=300)
middle.goto(x=0, y=-300)
pad1 = Paddle1()
pad2 = Paddle2()
screen.listen()
screen.onkeypress(pad1.up, "Up")
screen.onkeypress(pad1.down, "Down")
screen.onkeypress(pad2.up, "w")
screen.onkeypress(pad2.down, "s")


ball.top_left()
pad_col = PadCollision()
# pad_col.pad_collision(coordinate)


screen.exitonclick()

'''
screen.listen()
screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
'''