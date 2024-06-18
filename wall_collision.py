import ball


class Wall:
    def __init__(self, ball_coordinate):
        self.ball = [ball_coordinate]
        self.angle_wall1 = 0
        self.angle_wall2 = 0
        self.angle = 0

    def wall_bounce_off_1(self, direction, last_angle):
        ## paddle1 to paddle2
        if direction == -280:
            print(f'from pad1 wall_collision.py, bottom angle 150. last angle: {last_angle}')
            # 180 - (270 - last_angle)
            return_angle = 180 - (270 - last_angle)# was 150
            print(f'return angle is {return_angle}')
            return return_angle
        elif direction == 280:
            print(f'from pad1 wall_collision.py, top angle 210. last angle {last_angle}')
            return_angle = 180 + (last_angle - 90)
            print(f'return angle is {return_angle}')
            return return_angle# was 210, last angle 90+
        return self

    def wall_bounce_off_2(self, direction, last_angle):  # generates the angle value for pad2
        ## paddle2 to paddle1
        if direction == -280:
            print(f'from pad2 wall_collision.py, bottom wall angle returned 40 last angle: {last_angle}')
            return_angle = last_angle - 300 # was minus 270
            print(f'return angle is {return_angle}')
            return return_angle #e.g last angle 272 - 270 = 2 # was 40

        elif direction == 280:
            print(f' from pad2 wall_collision.py, top angle returned 330 last angle: last angle {last_angle}')
            return_angle = 360 - last_angle
            print(f'return angle is {return_angle}')
            return return_angle #(last was 90 - 0) # was 330
        return self

########################################################################################## I want to adjust the below functions to generate more varied angles for bounce offs from the walls
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
        return self

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
        return self
