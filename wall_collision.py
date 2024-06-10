

class Wall:
    def __init__(self):
        self.angle_wall1 = 0
        self.angle_wall2 = 0

    def wall_bounce_1(self, ball_cor):  # generates the angle value for pad2
        print(f'bounce 1 function range:')
        # default_angle = 300
        # for i in range(range_start, range_end + 1):
        #     if default_angle == 360:
        #         default_angle = 0
        #     elif i == ball_cor:
        #         print(f'ball coordinates pad2 = {i}, angle: {default_angle}')
        #         return default_angle
        #     default_angle += 2
        # print('game over')
        # return
        pass

    def wall_bounce_2(self, ball_cor):  # generates the angle value for pad1
        print(f'bounce 2 function range:')
        # default_angle = 250
        # for i in range(range_start, range_end + 1):
        #     if i == ball_cor:
        #         print(f'ball coordinates pad2 = {i}, angle: {default_angle}')
        #         return default_angle
        #     else:
        #         default_angle -= 1.5
        # print('game over')
        # return
        pass

    def wall_core_bounce(self, coordinates, direction):  ### the core_bounce function may be
        # print('core_bounce function start')
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])
        # print(coordinates['ball']['ball_y'])
        if coordinates['ball']['ball_y'] < 0:  #
            if direction == 1:# to pad2
                return 150
            else:
                return 30
        elif coordinates['ball']['ball_y'] > 0:  #
            if direction == 1:# to pad2
                return 210
            else:
                return 330



