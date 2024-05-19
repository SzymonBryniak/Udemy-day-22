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


class MainScreen(Screen, Turtle, Ball):
    def __int__(self):
        self.screen = Screen()
        self.middle = Turtle()
        # Paddle1.__init__(self)
        # Paddle2.__init__(self)
        # Ball.__init__(self)

    def screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.middle.hideturtle()
        self.middle.color('green')
        self.middle.setpos(x=0, y=300)
        self.middle.goto(x=0, y=-300)
        self.screen.exitonclick()


MainScreen()




# if __name__ == '__main__':
#     processes = []
#
#     # Create 5 worker processes
#     for i in range(1):
#         if i == 0:
#             p0 = multiprocessing.Process(target=worker0, args=(i,))
#             processes.append(p0)
#             p0.start()

    # Ensure all of the processes have finished
    # for p in processes:
    #     p.join()

    # print('Main process ends')



# pad1 = Paddle1()
# pad2 = Paddle2()
# ball = Ball()



