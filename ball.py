import random
import paddle1
import paddle2
from turtle import Turtle, Screen
from paddle_collision import PadCollision
import math
from wall_collision import Wall
STARTING_POSITION = (0, 0)

#I plan to pass coordinates from pads to the ball
#to make the ball movement stop for 1 ms when
# pad coordinates will change


class Ball:
    def __init__(self, more_coordinates):
        self.pad_collision = PadCollision()
        self.more_coordinates = more_coordinates
        self.wall = Wall()
        self.screen = Screen()
        self.ball_x = 0
        self.ball_y = 0
        self.ball = []
        self.angle = 0
        self.angle_wall = 0

    def create_ball(self):
        new_segment = Turtle('circle')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(x=0, y=0)
        self.ball.append(new_segment)
        # self.ball_start()
        self.ball_start()

    def bounce_off_2(self, angle): ## paddle2 to paddle1
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        self.screen.tracer(2)
        self.ball[0].setheading(angle)
        print(f'to paddle 2 {self.more_coordinates}')
        while self.ball[0].xcor() < 260: # if ycor == 300 call wall collision function
            ################################################ wall collision tests
            if int(self.ball[0].ycor()) == -280:
                print('bottom wall collision test')
                print(f'to paddle 1 {self.more_coordinates}')
                self.ball[0].setheading(40)
                while self.ball[0].xcor() < 260:
                    self.ball[0].forward(0.04)
            elif int(self.ball[0].ycor()) == 280:
                print('top wall collision test')
                print(f'to paddle 1 {self.more_coordinates}')
                self.ball[0].setheading(330)
                while self.ball[0].xcor() < 260:
                    self.ball[0].forward(0.04)
            self.ball[0].forward(0.04)
            ################################################
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        print('after forward from pad 2')
        print(f'bounce off pad 2{self.more_coordinates}')
        self.bounce_off_1(self.pad_collision.core_bounce(self.more_coordinates))
        return

    def bounce_off_1(self, angle): ## paddle1 to paddle2
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        self.screen.tracer(2)
        print(f'to paddle 2 {self.more_coordinates}')
        self.ball[0].setheading(angle)
        while self.ball[0].xcor() > -260:
            ################################################ wall collision tests
            if int(self.ball[0].ycor()) == -280:
                print('bottom wall collision test')
                print(f'to paddle 2 {self.more_coordinates}')
                self.ball[0].setheading(150)
                while self.ball[0].xcor() > -260:
                    print(self.ball[0].xcor())
                    self.ball[0].forward(0.04)
            elif int(self.ball[0].ycor()) == 280:
                print('top wall collision test')
                print(f'to paddle 2 {self.more_coordinates}')
                self.ball[0].setheading(210)
                while self.ball[0].xcor() < 260: ### the ball continues going forward after 260 for some reason
                    print(self.ball[0].xcor())
                    self.ball[0].forward(0.04)
            ################################################
            self.ball[0].forward(0.04)
        print('after forward from pad1')
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        print(f'bounce off pad 1 {self.more_coordinates}')
        self.bounce_off_2(self.pad_collision.core_bounce(self.more_coordinates))
        return

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
        angle = random.randint(179, 225)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x > -260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(0.04)
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        self.angle = int(self.pad_collision.core_bounce(self.more_coordinates))
        self.bounce_off_2(self.angle)
        return

    def top_left(self):
        self.screen.tracer(2)
        angle = random.randint(145, 179)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x > -260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(0.04)
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        self.angle = int(self.pad_collision.core_bounce(self.more_coordinates))
        self.bounce_off_2(self.angle)
        return

    def top_right(self):
        self.screen.tracer(2)
        angle = random.randint(1, 30)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x < 260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(0.04)
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        self.angle = int(self.pad_collision.core_bounce(self.more_coordinates))
        self.bounce_off_1(self.angle)
        return

    def bottom_right(self):
        self.screen.tracer(2)
        angle = random.randint(320, 359)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x < 260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(0.04)
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        self.angle = int(self.pad_collision.core_bounce(self.more_coordinates))
        self.bounce_off_1(self.angle)
        return

# 0