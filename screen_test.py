# from turtle import Screen, Turtle
# from paddle1 import Paddle1
# from paddle2 import Paddle2
# from ball import Ball
# from paddle_collision import PadCollision
# import threading
#
#

#
#
#         # while True:
#         #     self.t.forward(150 * random())
#         #     self.t.left(-180 + 360 * random())
#
#
# screen = Screen()
# pad1 = Paddle1()
# pad2 = Paddle2()
# ball = Ball()
# thread1 = ScreenAnimator(screen)

#############################################################

from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
# import threading
from paddle_collision import PadCollision


# class ScreenAnimator(threading.Thread):
#     def __init__(self, thread_id, name):
#         threading.Thread.__init__(self)
#         self.t1 = name
#         self.thread_id = thread_id
#
#     def run(self):
#         return


middle = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

middle.hideturtle()
middle.color('green')
middle.setpos(x=0, y=300)
middle.goto(x=0, y=-300)

pad1 = Paddle1()
pad2 = Paddle2()
ball = Ball()


screen.exitonclick()
