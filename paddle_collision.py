

class PadCollision:

    def __int__(self, coordinates1):
        self.cor = 0

    def game_over(self, coordinates):
        if coordinates['ball_y']:

            return

    def pad_collision(self, coordinates):
        if coordinates['ball_x'] == -260:
            if coordinates['ball_y'] < 0:
                return
            elif coordinates['ball_y'] > 0:

                return
        elif coordinates['ball_x'] == 260:
            if coordinates['ball_y'] < 0:
                return
            elif coordinates['ball_y'] > 0:
                return

    def ball_bounce(self):

        return





### angle to change depending on segment collided with

#pad1seg1 =