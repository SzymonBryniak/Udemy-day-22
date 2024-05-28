# .pos(), tuple(map(int, turtle.pos()))

class PadCollision:

    def __int__(self, ):
        self.cor = 0
        self.instructions = {}
# I may reorganise nested loops below into list comprehension if possible

    def game_over(self, coordinates):
        game_on = 1
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])

        if coordinates['ball']['ball_x'] == -260:
            range_end = int(coordinates['pad2']['p2y'])
            range_start = int(coordinates['pad2']['p2y2'])
            for i in range(range_start, range_end):
                if coordinates['ball']['ball_y'] == i:
                    return print('collision') ### I will determin the bounce angle here

        elif coordinates['ball']['ball_x'] == 260:
            range_start = int(coordinates['pad1']['p1y'])
            range_end = int(coordinates['pad1']['p2y2'])
            for i in range(range_start, range_end):
                if coordinates['ball']['ball_y'] == i:
                    return print('collision') ### I will determine the bounce angle here
            # for key, value in coordinates['pad1'].items():
            #     if coordinates['ball_y'] != value:

            print('game_over')

####################################################

    def pad_collision(self, coordinates):
        game_on = 1
        while game_on:
            if coordinates['ball_x'] == -260:
                # if coordinates['ball_y'] < 0:
                # for key, value in coordinates['pad2'].items():
                #     for vertical in range(-260, 260):
                        #### I want to define angles here

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