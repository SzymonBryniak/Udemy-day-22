import ball


class Wall:
    def __init__(self, ball_coordinate):
        self.ball = [ball_coordinate]
        self.angle_wall1 = 0
        self.angle_wall2 = 0

    def wall_bounce_off_1(self):
        print('wall_collision.py, pad1 side angle')
        return 150

    def wall_bounce_off_2(self):  # generates the angle value for pad2
        print('wall_collision.py, pad2 side angle')
        return 40

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



