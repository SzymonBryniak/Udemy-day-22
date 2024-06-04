# .pos(), tuple(map(int, turtle.pos()))

class PadCollision:

    def __init__(self):
        self.angle_pad1 = 0
        self.angle_pad2 = 0

# The loop runs twice, but it doesn't break the code,  I must fix this later.
    def bounce_1(self, range_start, range_end, ball_cor): #generates the angle value for pad2
        # print('bounce 1(pad 2)function start')
        print(range_start, range_end)
        default_angle = 40 ## might need to be 40 was 340
        #while default_angle < 361:

        for i in range(range_start, range_end):
            if default_angle == 0: #360:
                default_angle = 360
            if default_angle > 40:
                default_angle += 2
            elif i == ball_cor:
                return default_angle
            default_angle -= 2
        return

    def bounce_2(self, range_start, range_end, ball_cor): #generates the angle value for pad1
        # print('bounce 2 (pad1) function start')
        # print(range_start, range_end)
        default_angle = 240
        #while default_angle > 120:
        for i in range(range_start, range_end):
            if i == ball_cor:
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
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y'] or i == 0:
                    # print('pre process collision pad2')
                    self.angle_pad2 = self.bounce_1(range_start, range_end, i) ##
                    # print(range_start, range_end, i)
                    # print('collision pad2 ')
                    return self.angle_pad2  # self.bounce_1(range_start, range_end, i)# return to bounce_off_1
            # print('game over 1')
            return

        elif coordinates['ball']['ball_x'] >= 260:  #pad1
            # print('core_bounce if statement pad1')
            range_start = int(coordinates['pad1']['p1y2'])
            range_end = int(coordinates['pad1']['p1y'])
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y'] or i == 0:
                    # print('pre process collision pad1')
                    self.angle_pad1 = self.bounce_2(range_start, range_end, i)
                    # print('collision pad1 ')
                    return self.angle_pad1 #self.bounce_2(range_start, range_end, i) ### changed bounce_1 to bounce_2# return to bounce_off_2

            print('game_over 2')
            return

####################################################






### angle to change depending on segment collided with

#pad1seg1 =