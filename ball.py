import random
import paddle1
import paddle2
import threading
from turtle import Turtle, Screen
import threading
STARTING_POSITION = (0, 0)
pad_coordinates = [0, 0]
#I plan to pass coordinates from pads to the ball
#to make the ball movement stop for 1 ms when
# pad coordinates will change


class Ball:
    def __init__(self):
        self.pad1 = paddle1
        self.pad2 = paddle2
        self.pad2 = paddle2
        self.ball_x = 0
        self.ball_y = 0
        self.ball = []
        self.create_ball()
        self.screen = Screen()
        # screen.ontimer(self.move_ball, 10)  # Start the ball movement
        self.game_on = True

        #self.dict_to = {'left_x': random.randint(-300, 0),
                        #'left_y': random.randint(0, -300)}
                        #'left_y': random.randint(0, -300)}
    def get_pad_coordinates(self):
        old_pad1_coordinate = self.pad1.PAD1_COORDINATES
        old_pad2_coordinate = self.pad2.PAD2_COORDINATES
        return old_pad1_coordinate, old_pad2_coordinate

    def create_ball(self):
        new_segment = Turtle('circle')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(x=0, y=0)
        self.ball.append(new_segment)
        self.top_left()
        # self.screen.ontimer(self.top_left())

    def forward_ball(self):
        self.ball[0].forward(200)

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

    def bottom_left(self):
        left_y = random.randint(-300, 0)
        self.ball[0].goto(x=-260, y=left_y)

        return [-260, int(left_y)]

    def top_left(self):

        angle = random.randint(145, 180)
        #self.ball[0].goto(x=-260, y=right_y)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)

        self.screen.ontimer()
        while ball_x > -260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(1)

        return ball_x, ball_y, angle

    def top_right(self):
        left_y = random.randint(0, 300)
        self.ball[0]._delay(150)
        self.ball[0].goto(x=260, y=left_y)

        return [260, int(left_y)]

    def bottom_right(self):
        right_y = random.randint(-300, 0)
        self.ball[0].goto(x=260, y=right_y)

        return [260, int(right_y)]


