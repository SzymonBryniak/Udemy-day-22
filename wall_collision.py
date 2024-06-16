import ball


class Wall:
    def __init__(self, ball_coordinate):
        self.ball = [ball_coordinate]
        self.angle_wall1 = 0
        self.angle_wall2 = 0

    def wall_bounce_off_1(self, direction, last_angle):
        print('wall_collision.py, pad1 side angle')
        # 150 = 30
        if direction == -280:
            print(f'last angle:{last_angle}')
            return 150
        elif direction == 280:
            print(f'last angle:{last_angle}')
            return 210

    def wall_bounce_off_2(self, direction):  # generates the angle value for pad2
        print('wall_collision.py, pad2 side angle')
        if direction == -280:
            return 40
        elif direction == 280:
            return 330
############################################################################################ I want to adjust the below functions to generate more varied angles for bounce offs from the walls
############################################################################################
    def bounce_1(self, range_start, range_end, ball_cor):  # generates the angle value for pad2
        print(f'bounce 1 function range:{range_start}, {range_end}')
        default_angle = 300

        for i in range(range_start, range_end + 1):
            if default_angle == 360:
                default_angle = 0
            elif i == ball_cor:
                print(f'ball coordinates pad2 = {i}, angle: {default_angle}')
                return default_angle
            default_angle += 2
        print('game over')
        return

    ## I need to consider negative y coordinates of paddles

    def bounce_2(self, range_start, range_end, ball_cor):  # generates the angle value for pad1
        print(f'bounce 2 function range: {range_start}, {range_end}')
        default_angle = 250
        for i in range(range_start, range_end + 1):
            if i == ball_cor:
                print(f'ball coordinates pad2 = {i}, angle: {default_angle}')
                return default_angle
            else:
                default_angle -= 2
        print('game over')
        return
