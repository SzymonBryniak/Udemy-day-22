from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
from paddle_collision import PadCollision
import threading


class ScreenAnimator(threading.Thread):
    def __init__(self, thread):
        threading.Thread.__init__(self)
        self.t1 = thread

    def run(self):


        # while True:
        #     self.t.forward(150 * random())
        #     self.t.left(-180 + 360 * random())


screen = Screen()
pad1 = Paddle1()
pad2 = Paddle2()
ball = Ball()
thread1 = ScreenAnimator(screen)


