# .pos(), tuple(map(int, turtle.pos()))

class PadCollision:

    def __init__(self, coordinates):
        self.angle_pad1 = 0
        self.angle_pad2 = 0
        self.coordinates = coordinates

    def bounce_1(self, range_start, range_end, ball_cor): #generates the angle value for pad2
        # print(f'bounce 1 function range:{range_start}, {range_end}')
        default_angle = 300
        print(f'pad2 start:{range_start}, pad2 end:{range_end}')

        for i in range(range_start, range_end + 1):
            if default_angle == 360:
                default_angle = 0
            elif i == ball_cor:
                # print(f'ball coordinates pad2 = {i}, angle: {default_angle}')
                return default_angle
            default_angle += 1.8
        print('point for pad1')
        self.coordinates['score']['pad1'] += 1

    def bounce_2(self, range_start, range_end, ball_cor): #generates the angle value for pad1
        # print(f'bounce 2 function range: {range_start}, {range_end}')
        default_angle = 230
        print(f'pad1 start:{range_start}, pad1 end:{range_end}')

        for i in range(range_start, range_end + 1):
            if i == ball_cor:
                # print(f'ball coordinates pad2 = {i}, angle: {default_angle}')
                return default_angle
            else:
                default_angle -= 1.8

        print('point for pad2')
        self.coordinates['score']['pad2'] += 1


    def core_bounce(self, coordinates): ### the core_bounce function may be
        # print('core_bounce function start')
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])
        # print(coordinates['ball']['ball_y'])
        if coordinates['ball']['ball_x'] <= -260:  # pad2
            # print('core_bounce if statement pad2')
            range_start = int(coordinates['pad2']['p2y2'] - 15)
            range_end = int(coordinates['pad2']['p2y'] + 15)
            self.angle_pad2 = self.bounce_1(range_start, range_end, coordinates['ball']['ball_y'])
            return self.angle_pad2
        elif coordinates['ball']['ball_x'] >= 260:  #pad1
            # print('core_bounce if statement pad1')
            range_start = int(coordinates['pad1']['p1y2'] - 15)
            range_end = int(coordinates['pad1']['p1y'] + 15)
            self.angle_pad1 = self.bounce_2(range_start, range_end, coordinates['ball']['ball_y'])
            return self.angle_pad1
