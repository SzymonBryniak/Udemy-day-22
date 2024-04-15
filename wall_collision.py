from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball


class Wall(Paddle1, Paddle2, Ball):

    def __int__(self):
        super().__init__()

    def init_wall(self):
        pass

    def return_cor(self):
        pass


