from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball

middle = Turtle()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")

middle.hideturtle()
middle.color('green')
middle.setpos(x=0, y=300)
middle.setpos(x=0, y=300)
middle.goto(x=0, y=-300)
pad1 = Paddle1()
pad2 = Paddle2()

ball = Ball()

screen.exitonclick()

