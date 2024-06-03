import random
import paddle1
import paddle2
from turtle import Turtle, Screen
from paddle_collision import PadCollision
STARTING_POSITION = (0, 0)

#I plan to pass coordinates from pads to the ball
#to make the ball movement stop for 1 ms when
# pad coordinates will change


class Ball:
    def __init__(self, more_coordinates):
        self.pad_collision = PadCollision()
        self.more_coordinates = more_coordinates
        self.screen = Screen()
        self.ball_x = 0
        self.ball_y = 0
        self.ball = []
        self.angle = 0

        # screen.ontimer(self.move_ball, 10)  # Start the ball movement

### I want to use recursive function call to loop the animation

    def create_ball(self):
        new_segment = Turtle('circle')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(x=0, y=0)
        self.ball.append(new_segment)
        # self.ball_start()
        self.top_left()

    def bounce_off_2(self, angle): ## paddle 2
        print('bounce_off_2 function start')
        print(f'bounce_off_2 angle: {angle}')
        self.screen.tracer(2)
        self.ball[0].setheading(angle)
        while self.ball[0].xcor() < 260:
            self.ball[0].forward(0.04)
            # if self.ball[0].xcor == 260:
        self.more_coordinates['ball']['ball_x'] = self.ball[0].xcor()
        self.more_coordinates['ball']['ball_y'] = self.ball[0].ycor()
        print(f'bounce pad 2{self.more_coordinates}')
        return self.bounce_off_1(int(self.pad_collision.core_bounce(self.more_coordinates)))# get
        ## I must invoke the bounce_off_1 function

    def bounce_off_1(self, angle): ## paddle 1
        print('bounce_off_1 function start')
        print(f'bounce_off_1 angle: {angle}')
        self.screen.tracer(2)
        print(self.more_coordinates)
        self.ball[0].setheading(angle)  # angle was wrong
        while self.ball[0].xcor() > -261:
            self.ball[0].forward(0.04)
            # if self.ball[0].xcor == -260:
        self.more_coordinates['ball']['ball_x'] = self.ball[0].xcor()
        self.more_coordinates['ball']['ball_y'] = self.ball[0].ycor()
        print(f'bounce pad 1 {self.more_coordinates}')
        return self.bounce_off_2(self.pad_collision.core_bounce(self.more_coordinates))

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
        self.more_coordinates['ball']['ball_x'] = self.ball[0].xcor()
        self.more_coordinates['ball']['ball_y'] = self.ball[0].ycor()
        self.bounce_off_2(int(self.pad_collision.core_bounce(self.more_coordinates)))
        return

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
        self.more_coordinates['ball']['ball_x'] = self.ball[0].xcor()
        self.more_coordinates['ball']['ball_y'] = self.ball[0].ycor()
        self.pad_collision.core_bounce(self.more_coordinates)
        self.angle = int(self.pad_collision.core_bounce(self.more_coordinates))
        self.bounce_off_2(self.angle)
        return

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
        self.more_coordinates['ball']['ball_x'] = self.ball[0].xcor()
        self.more_coordinates['ball']['ball_y'] = self.ball[0].ycor()
        self.bounce_off_1(int(self.pad_collision.core_bounce(self.more_coordinates)))
        # self.collision.game_over(self.more_coordinates)
        return

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
        self.more_coordinates['ball']['ball_x'] = self.ball[0].xcor()
        self.more_coordinates['ball']['ball_y'] = self.ball[0].ycor()
        self.bounce_off_1(int(self.pad_collision.core_bounce(self.more_coordinates)))
        return

# 0