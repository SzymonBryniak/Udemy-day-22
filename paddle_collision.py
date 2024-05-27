

class PadCollision:

    def __int__(self):
        self.cor = 0
        self.game_on = True
        self.instructions = {}

    def game_over(self, coordinates):
        while self.game_on:
            for key, value in coordinates['pad1'].items():
                if coordinates['ball_y'] != value:
                    print('game over')
            for key, value in coordinates['pad2'].items():
                if coordinates['ball_y'] != value:
                    print('game over')
####################################################

    def pad_collision(self, coordinates):
        while self.game_on:
            if coordinates['ball_x'] == -260:
                # if coordinates['ball_y'] < 0:
                for key, value in coordinates['pad2'].items():
                    for i in range(90, 270): ## pad 1 range

                        return
            elif coordinates['ball_x'] == 260:
                # if coordinates['ball_y'] < 0:
                for key, value in coordinates['pad1'].items():
                    for i in range(0, 90):
                        return
                    for ii in range(270, 360):
                        return

    def ball_bounce(self):

        return





### angle to change depending on segment collided with

#pad1seg1 =