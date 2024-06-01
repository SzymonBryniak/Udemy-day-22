# .pos(), tuple(map(int, turtle.pos()))

class PadCollision:

    def __int__(self, ):
        self.cor = 0
        self.instructions = {}
# I may reorganise nested loops below into list comprehension if possible

    def bounce(self, range_start, range_end, ball_cor):
        default_angle = 320
        while default_angle < 361:
            for i in range(range_start, range_end):
                if default_angle == 360:
                    default_angle = 0
                if i == ball_cor:
                    print(default_angle)
                    return default_angle
                if default_angle < 360:
                    default_angle += 2
                else:
                    default_angle -= 2
        return

    def game_over(self, coordinates):
        game_on = 1
        coordinates['ball']['ball_x'] = int(coordinates['ball']['ball_x'])
        coordinates['ball']['ball_y'] = int(coordinates['ball']['ball_y'])
        count = 0
        if coordinates['ball']['ball_x'] == -260:
            range_end = int(coordinates['pad2']['p2y'])
            range_start = int(coordinates['pad2']['p2y2'])
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y']:
                    print('collision'),
                    return self.bounce(range_start, range_end, i)
            if coordinates['ball']['ball_y'] == 0:
                print('collision')
                return 0
            else:
                print('game over')
                return 1

        elif coordinates['ball']['ball_x'] == 260:
            range_start = int(coordinates['pad1']['p1y2'])
            range_end = int(coordinates['pad1']['p1y'])
            for i in range(range_start, range_end):
                if i == coordinates['ball']['ball_y']:
                    print('collision')
                    return self.bounce(range_start, range_end, i)
            if coordinates['ball']['ball_y'] == 0: ### I need to write code for the "0" exception
                print('collision')
                return 0
            else:
                print('game_over')
                return 1

####################################################






### angle to change depending on segment collided with

#pad1seg1 =