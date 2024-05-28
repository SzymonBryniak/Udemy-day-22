# .pos(), tuple(map(int, turtle.pos()))

class PadCollision:

    def __int__(self, ):
        self.cor = 0
        self.instructions = {}
# I may reorganise nested loops below into list comprehension if possible

    def bounce(self, range_start, range_end, ball_cor):
        default_angle = 60
        for i in range(range_start, range_end):
            default_angle -= 1
            if i == ball_cor:
                return default_angle

        ### xcor 260 = angle 0 - 60
        return

    def game_over(self, coordinates):
        game_on = 1
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])

        if coordinates['ball']['ball_x'] == -260:
            range_end = int(coordinates['pad2']['p2y'])
            range_start = int(coordinates['pad2']['p2y2'])
            for i in range(range_start, range_end):
                if coordinates['ball']['ball_y'] == i:
                    self.bounce(range_start, range_end, i)
                    return print('collision') ### I will determine the bounce angle here
                                              # will return pad_collision function
            print('game over')

        elif coordinates['ball']['ball_x'] == 260:
            range_start = int(coordinates['pad1']['p1y'])
            range_end = int(coordinates['pad1']['p2y2'])
            for i in range(range_start, range_end):
                if coordinates['ball']['ball_y'] == i:
                    return print('collision') ### I will determine the bounce angle here
                                                # will return pad_collision function
            print('game_over')

####################################################






### angle to change depending on segment collided with

#pad1seg1 =