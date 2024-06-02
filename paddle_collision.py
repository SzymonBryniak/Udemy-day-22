# .pos(), tuple(map(int, turtle.pos()))

class PadCollision:

    def __init__(self):
        self.angle_pad1 = None
        self.angle_pad2 = None

# I may reorganise nested loops below into list comprehension if possible
    def bounce_1(self, range_start, range_end, ball_cor): #generates the angle value for pad2
        default_angle = 320
        while default_angle < 361:
            for i in range(range_start, range_end):
                if default_angle == 360:
                    default_angle = 0
                    print('b10')
                if i == ball_cor:
                    print('b11')
                    print(f'b1: {default_angle} returned')
                    return default_angle
                print('b13')
                default_angle += 2

        return print('return b111')

    def bounce_2(self, range_start, range_end, ball_cor): #generates the angle value for pad1
        default_angle = 240
        while default_angle > 120:
            for i in range(range_start, range_end):
                if i == ball_cor:
                    print('b21')
                    print(f'b2: {default_angle} returned')
                    return default_angle
                else:
                    print('b24')
                    default_angle -= 2
        return print('return 211')

    def game_over(self, coordinates):
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])
        if coordinates['ball']['ball_x'] == -260:  # pad2
            range_end = int(coordinates['pad2']['p2y'])
            range_start = int(coordinates['pad2']['p2y2'])
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y']:
                    self.angle_pad2 = self.bounce_1(range_start, range_end, i)
                    print(f'collision 1 {self.bounce_1(range_start, range_end, i)}')
                    return self.angle_pad2 #self.bounce_1(range_start, range_end, i)
            if coordinates['ball']['ball_y'] == 0:
                print('0 collision 2')
                return 0
            else:
                print('game over 1')
                return 1

        elif coordinates['ball']['ball_x'] == 260:  #pad1
            range_start = int(coordinates['pad1']['p1y2'])
            range_end = int(coordinates['pad1']['p1y'])
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y']:
                    self.angle_pad1 = self.bounce_2(range_start, range_end, i)
                    print(f'collision 3 {self.bounce_2(range_start, range_end, i)}')

                    return self.angle_pad1 #self.bounce_2(range_start, range_end, i) ### changed bounce_1 to bounce_2
            if coordinates['ball']['ball_y'] == 0: ### I need to write code for the "0" exception
                print('0 collision 4')
                return 0
            else:
                print('game_over 2')
                return 1

####################################################






### angle to change depending on segment collided with

#pad1seg1 =