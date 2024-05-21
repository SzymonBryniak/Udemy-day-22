import turtle
from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
import ball
import threading
from paddle_collision import PadCollision
import threading


middle = Turtle()
screen = Screen()
################

screen.setup(width=600, height=600)
screen.bgcolor("black")
middle.hideturtle()
middle.color('green')
middle.setpos(x=0, y=300)
middle.goto(x=0, y=-300)
pad1 = Paddle1()
pad2 = Paddle2()
ball = ball.Ball
# pad_col = PadCollision()
# ball = Ball()

screen.onkeypress(pad1.up, key='Up')
screen.onkeypress(pad1.down, key='Down')
screen.onkeypress(pad2.up, key='w')
screen.onkeypress(pad2.down, key='s')
# pad_col.pad_collision(coordinate)
# screen.ontimer(self.move_ball, 10)  # Start the ball movement


screen.listen()
turtle.mainloop()  # Main loop is required for the .ontimer to work
screen.exitonclick()

'''
screen.listen()
screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
'''
