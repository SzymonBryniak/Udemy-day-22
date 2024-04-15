import random
from turtle import Turtle

STARTING_POSITION = (0, 0)


class Ball:
    def __init__(self):
        self.ball_x = 0
        self.ball_y = 0
        self.ball = []
        self.game_on = True
        #self.dict_to = {'left_x': random.randint(-300, 0),
                        #'left_y': random.randint(0, -300)}

    def create_ball(self):
        new_segment = Turtle('circle')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(x=0, y=0)
        self.ball.append(new_segment)

    def ball_coordinates(self):
        ball_position_x = self.ball_x
        ball_position_y = self.ball_y
        return ball_position_x, ball_position_y

    def ball_start(self):
        self.create_ball()
        direction = random.randint(1, 4)

        if direction == 1:
            self.bottom_left()
        elif direction == 2:
            self.bottom_right()
        elif direction == 3:
            self.top_left()
        elif direction == 4:
            self.top_right()
        self.ball_x = self.ball[0].xcor()
        self.ball_y = self.ball[0].ycor()

    def bottom_left(self):
        left_y = random.randint(-300, 0)
        self.ball[0].goto(x=-260, y=left_y)

    def top_left(self):
        right_y = random.randint(0, 300)
        self.ball[0].goto(x=-260, y=right_y)

    def top_right(self):
        left_y = random.randint(0, 300)
        self.ball[0].goto(x=260, y=left_y)

    def bottom_right(self):
        right_y = random.randint(-300, 0)
        self.ball[0].goto(x=260, y=right_y)

