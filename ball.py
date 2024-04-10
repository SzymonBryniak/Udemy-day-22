import random
from turtle import Turtle
STARTING_POSITION = (0,0)


class Ball:
    def __init__(self):
        self.ball = []
        self.create_ball()
        self.turtle = Turtle


    def create_ball(self):
        new_segment = Turtle('circle')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(x=0, y=0)
        self.ball.append(new_segment)

