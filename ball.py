import random
from paddle1 import Paddle1
from paddle2 import Paddle2
from turtle import Turtle, Screen

STARTING_POSITION = (0, 0)
pad_coordinates = [0, 0]
#I plan to pass coordinates from pads to the ball
#to make the ball movement stop for 1 ms when
# pad coordinates will change


class Ball(Paddle1, Paddle2):
    def __init__(self):
        super(Ball).__init__()
        self.screen = Screen()
        self.ball_x = 0
        self.ball_y = 0
        self.ball = []
        # screen.ontimer(self.move_ball, 10)  # Start the ball movement
        self.game_on = True

    def create_ball(self):
        new_segment = Turtle('circle')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(x=0, y=0)
        self.ball.append(new_segment)
        self.ball_start()

    def ball_start(self):
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
        self.screen.tracer(2)
        angle = random.randint(180, 225)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x > -260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(0.04)
        print(f'pad at {pad_coordinates}')
        return ball_x, ball_y, angle

    def top_left(self):
        self.screen.tracer(2)
        angle = random.randint(145, 180)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x > -260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(0.04)
        return ball_x, ball_y, angle

    def top_right(self):
        self.screen.tracer(2)
        angle = random.randint(0, 30)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x < 260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(0.04)

        return ball_x, ball_y, angle

    def bottom_right(self):
        self.screen.tracer(2)
        angle = random.randint(320, 360)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x < 260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(0.04)
        return ball_x, ball_y, angle


