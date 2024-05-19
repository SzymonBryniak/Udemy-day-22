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
import multiprocessing
from paddle_collision import PadCollision


def worker0(num):
    middle = Turtle()
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    middle.hideturtle()
    middle.color('green')
    middle.setpos(x=0, y=300)
    middle.goto(x=0, y=-300)
    screen.exitonclick()


def worker1(num):
    """Function to be run in a separate process."""
    ball = Ball()
    print(f'Worker: {num}')


def worker2(num):
    pad1 = Paddle1()


def worker3(num):
    pad2 = Paddle2()


if __name__ == '__main__':
    processes = []

    # Create 5 worker processes
    for i in range(4):
        if i == 0:
            p0 = multiprocessing.Process(target=worker0, args=(i,))
            processes.append(p0)
            p0.start()
        elif i == 1:
            p1 = multiprocessing.Process(target=worker1, args=(i,))
            processes.append(p1)
            p1.start()
        elif i == 2:
            p2 = multiprocessing.Process(target=worker2, args=(i,))
            processes.append(p2)
            p2.start()
        elif i == 3:
            p3 = multiprocessing.Process(target=worker3, args=(i,))
            processes.append(p3)
            p3.start()
    # Ensure all of the processes have finished
    # for p in processes:
    #     p.join()

    print('Main process ends')





# pad1 = Paddle1()
# pad2 = Paddle2()
# ball = Ball()



