# .pos(), tuple(map(int, turtle.pos()))
import math

class PadCollision:

    def __init__(self):
        self.angle_pad1 = 0
        self.angle_pad2 = 0

# The loop runs twice, but it doesn't break the code,  I must fix this later.
    def bounce_1(self, range_start, range_end, ball_cor): #generates the angle value for pad2 #  bounce functions must consider the
        # print('bounce 1(pad 2)function start')
        print(range_start, range_end)
        default_angle = 40 ## might need to be 40 was 340
        #while default_angle < 361:
        if ball_cor == 0:
            return 360
        for i in range(range_start, range_end):
            if default_angle == 0: #360:
                default_angle = 360
            elif i == ball_cor:
                print(f'ball coordinates pad2 = {i}, {default_angle}')
                return default_angle
            default_angle -= 2
        return
## I need to consider negative y coordinates of paddles
    def bounce_2(self, range_start, range_end, ball_cor): #generates the angle value for pad1
        # print('bounce 2 (pad1) function start')
        # print(range_start, range_end)
        default_angle = 240
        #while default_angle > 120:
        if ball_cor == 0:
            return 180
        for i in range(range_start, range_end):
            if i == ball_cor:
                print(i, default_angle)
                return default_angle
            else:
                default_angle -= 2
        return

    def core_bounce(self, coordinates): ### the core_bounce function may be
        # print('core_bounce function start')
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])
        # print(coordinates['ball']['ball_y'])
        if coordinates['ball']['ball_x'] <= -260:  # pad2
            # print('core_bounce if statement pad2')
            range_end = int(coordinates['pad2']['p2y'])
            range_start = int(coordinates['pad2']['p2y2'])
            self.angle_pad2 = self.bounce_1(range_start, range_end, math.ceil(coordinates['ball']['ball_y'])) ##
            return self.angle_pad2  # self.bounce_1(range_start, range_end, i)# return to bounce_off_1


            ######## ceil or floor depending on the y coordinate of the paddle
        elif coordinates['ball']['ball_x'] >= 260:  #pad1
            # print('core_bounce if statement pad1')
            range_start = int(coordinates['pad1']['p1y2'])
            range_end = int(coordinates['pad1']['p1y'])

            ######## ceil or floor depending on the y coordinate of the paddle
            self.angle_pad1 = self.bounce_2(range_start, range_end, math.ceil(coordinates['ball']['ball_y']))
            return self.angle_pad1 #self.bounce_2(range_start, range_end, i) ### changed bounce_1 to bounce_2# return to bounce_off_2



####################################################






### angle to change depending on segment collided with

#pad1seg1 =