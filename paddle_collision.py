from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball


class PadCollision(Paddle1, Paddle2, Ball):

    def __int__(self):
        super(PadCollision).__init__()
        self.cor = 0

    def pad_collision(self, ball_coordinate, pad1_cor, pad2_cor):

        return



### angle to change depending on segment collided with

#pad1seg1 =