# .pos(), tuple(map(int, turtle.pos()))

class PadCollision:

    def __int__(self, ):
        self.cor = 0
        self.instructions = {}
# I may reorganise nested loops below into list comprehension if possible

    def bounce(self, range_start, range_end, ball_cor):
        default_angle = 60
        while default_angle < 330:
            for i in range(range_start, range_end):
                if i == ball_cor:
                    return print(default_angle)
                elif default_angle == 0:
                    default_angle = 360

                default_angle -= 2

        return

    def game_over(self, coordinates):
        game_on = 1
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])

        if coordinates['ball']['ball_x'] == -260:
            range_end = int(coordinates['pad2']['p2y'])
            range_start = int(coordinates['pad2']['p2y2'])
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y']:
                    self.bounce(range_start, range_end, i)
                    return print('collision'), self.bounce(range_start, range_end, i)

            print('game over')

        elif coordinates['ball']['ball_x'] == 260:
            range_start = int(coordinates['pad1']['p1y'])
            range_end = int(coordinates['pad1']['p2y2'])
            for i in range(range_start, range_end):
                if coordinates['ball']['ball_y'] == i:
                    return print('collision') ### I will determine the bounce angle here
                                                # will return bounce function
            print('game_over')

####################################################






### angle to change depending on segment collided with

#pad1seg1 =