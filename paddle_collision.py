# .pos(), tuple(map(int, turtle.pos()))

class PadCollision:

    def __init__(self):
        self.angle_pad1 = 0
        self.angle_pad2 = 0

# I may reorganise nested loops below into list comprehension if possible
    def bounce_1(self, range_start, range_end, ball_cor): #generates the angle value for pad2
        print('bounce 1(pad 2)function start')
        print(range_start, range_end)
        default_angle = 320
        #while default_angle < 361:
        for i in range(range_start, range_end):
            if default_angle == 360:
                default_angle = 0
                print('b10')
            elif i == ball_cor:
                print(f'{i}b11')
                print(f'b1: {default_angle} returned')
                return default_angle
            print('b13')
            default_angle += 2
        return print('return b111')

    def bounce_2(self, range_start, range_end, ball_cor): #generates the angle value for pad1
        print('bounce 2 (pad1) function start')
        print(range_start, range_end)
        default_angle = 240
        #while default_angle > 120:
        for i in range(range_start, range_end):
            if i == ball_cor:
                print(f'{i}b21')
                print(f'b2: {default_angle} returned')
                return default_angle
            else:
                print('b24')
                default_angle -= 2
        return print('return 211')

    def core_bounce(self, coordinates): ### the core_bounce function may be
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])

        if coordinates['ball']['ball_x'] == -260:  # pad2
            range_end = int(coordinates['pad2']['p2y'])
            range_start = int(coordinates['pad2']['p2y2'])
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y'] or i == 0:
                    self.angle_pad2 = self.bounce_1(range_start, range_end, i)
                    print(range_start, range_end, i)
                    print('collision 1 ')
                    return self.angle_pad2 #self.bounce_1(range_start, range_end, i)

            print('game over 1')
            return print('1')

        elif coordinates['ball']['ball_x'] == 260:  #pad1
            range_start = int(coordinates['pad1']['p1y2'])
            range_end = int(coordinates['pad1']['p1y'])
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y'] or i == 0:
                    self.angle_pad1 = self.bounce_2(range_start, range_end, i)
                    print('collision 3 ')
                    return self.angle_pad1 #self.bounce_2(range_start, range_end, i) ### changed bounce_1 to bounce_2

            print('game_over 2')
            return print('1')

####################################################






### angle to change depending on segment collided with

#pad1seg1 =