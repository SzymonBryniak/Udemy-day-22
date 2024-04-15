from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball


class PadCollision(Ball):

    def __int__(self):
        super().__init__()
        self.pad_collision()

    def pad_collision(self):
        print(self.ball_coordinates())



### angle to change depending on segment collided with

#pad1seg1 =