from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
from paddle_collision import PadCollision


more_coordinates = {'ball': {'ball_x': 0, 'ball_y': 0},
                    'pad1': {
                    'p1x': 0,
                    'p1y': 0,
                    'p1x1': 0,
                    'p1y1': 0,
                    'p1x2': 0,
                    'p1y2': 0,
                    },
                    'pad2': {
                    'p2x': 0,
                    'p2y': 0,
                    'p2x1': 0,
                    'p2y1': 0,
                    'p2x2': 0,
                    'p2y2': 0,
                    }
                    }


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
pad1 = Paddle1(more_coordinates)
pad2 = Paddle2(more_coordinates)
ball = Ball(more_coordinates)
screen.onkeypress(pad1.up, key='Up')
screen.onkeypress(pad1.down, key='Down')
screen.onkeypress(pad2.up, key='w')
screen.onkeypress(pad2.down, key='s')
ball.create_ball()

##### evaluate ball and pad coordinates
# collision.pad_collision(dict_coordinates)
print(more_coordinates)

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
