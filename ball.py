import random
import paddle1
import paddle2
from turtle import Turtle, Screen
from paddle_collision import PadCollision
import math
from wall_collision import Wall
STARTING_POSITION = (0, 0)
BALL_FORWARD = 0.004
BALL_TRACER = 31
#I plan to pass coordinates from pads to the ball
#to make the ball movement stop for 1 ms when
# pad coordinates will change


class Ball:
    def __init__(self, more_coordinates):
        self.more_coordinates = more_coordinates
        self.wall = Wall(more_coordinates)
        self.pad_collision = PadCollision(more_coordinates)
        self.screen = Screen()
        self.ball_x = 0
        self.ball_y = 0
        self.ball = []
        self.ball2 = []
        self.angle = 0
        self.last_angle = 0
        self.pad1_score = 0
        self.pad2_score = 0
        self.score = [self.pad1_score, self.pad2_score]

    def create_ball(self):
        # self.screen.update()
        new_segment = Turtle('circle')
        new_segment.color('green')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(x=0, y=0)
        self.ball.insert(0, new_segment)
        print(self.ball)
        # self.ball_start()
        self.top_left()  # this may need to return something
        return 1

    def pad_score(self, score1=0, score2=0):

        self.more_coordinates['pad1'][0] += score1
        self.more_coordinates['pad2'][0] += score2
        return

    def top_left(self):
        self.screen.tracer(BALL_TRACER)
        angle = random.randint(145, 179)
        ball_x = 0
        ball_y = 0
        self.ball[0].setheading(angle)
        while ball_x > -260:
            ball_x = self.ball[0].xcor()
            ball_y = self.ball[0].ycor()
            self.ball[0].forward(BALL_FORWARD)
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        angle = int(self.pad_collision.core_bounce(self.more_coordinates))
        self.bounce_off_2(angle)  # to return a value for the screen module

    def bounce_off_2(self, angle):  # paddle2 to paddle1
        if angle == 0 or None:

            print('pad2 lost')
            self.pad_score(score1=1, score2=0)
            self.ball[0].clear()
            self.pad1_score += 1
            print('about to return one')
            return 1
            # self.restart()
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        self.screen.tracer(BALL_TRACER)
        self.ball[0].setheading(angle)
        while self.ball[0].xcor() < 260:  # if ycor == 300 call wall collision function
            ################################################

            if int(self.ball[0].ycor()) == -280:
                ################################################
                # print('bottom wall collision test')
                # print(f'to paddle 1 {self.more_coordinates}')
                print(f'from pad2 bottom wall collision test:{angle}')
                angle = self.wall.wall_bounce_off_2(-280, angle)
                self.ball[0].setheading(angle)#40d
                # print(f'self angle test {self.angle}')  # I will use the angle of the last bounce off to generate the angle for the ball bounce off from the wall.
                while self.ball[0].xcor() < 260:
                    self.ball[0].forward(BALL_FORWARD)

            elif int(self.ball[0].ycor()) == 280:
                # print('top wall collision test')
                # print(f'to paddle 1 {self.more_coordinates}')
                angle = self.wall.wall_bounce_off_2(280, angle)
                self.ball[0].setheading(angle)  # 330d
                print(f'from pad2 top wall collision test:{angle}')
                while self.ball[0].xcor() < 260:
                    self.ball[0].forward(BALL_FORWARD)

            self.ball[0].forward(BALL_FORWARD)
        ################################################
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        # print('after forward from pad 2')
        # print(f'bounce off pad 2{self.more_coordinates}')
        self.pad2_score += 1
        print(self.pad2_score)
        self.bounce_off_1(self.pad_collision.core_bounce(self.more_coordinates))
        return

    def bounce_off_1(self, angle):  # paddle1 to paddle2
        # if angle == 0 > end game
        if angle == 0 or None:
            print('pad1 lost')
            self.ball[0].clear()
            self.pad2_score += 1
            # self.restart()
            print(' about to return 1')
            return 1
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())  #  self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        self.screen.tracer(BALL_TRACER)
        # print(f'to paddle 2 {self.more_coordinates}')
        self.ball[0].setheading(angle)
        self.more_coordinates['ball']['ball_s'] = angle
        # print(f' ball_s test print {self.more_coordinates['ball']['ball_s']}') ### test ball_s print
        while self.ball[0].xcor() > -260:

            if int(self.ball[0].ycor()) == -280:
                ################################################
                # print(f'to paddle 2 {self.more_coordinates}')
                print(f'pad1 to pad2 bottom angle:{angle}')
                angle = self.wall.wall_bounce_off_1(-280, angle) #150d
                self.ball[0].setheading(angle)  # 150d
                print(f'from pad1 bottom wall collision test:{angle}')
                while self.ball[0].xcor() > -260:
                    self.ball[0].forward(BALL_FORWARD)
            elif int(self.ball[0].ycor()) == 280:
                # print('top wall collision test')
                # print(f'to paddle 2 {self.more_coordinates}')
                print(f'pad1 to pad2 top angle:{angle}')
                angle = self.wall.wall_bounce_off_1(280, angle)  # 210d
                self.ball[0].setheading(angle)  #
                print(f'from pad1 top wall collision test:{angle}')
                while self.ball[0].xcor() < -260:
                    self.ball[0].forward(BALL_FORWARD)
            self.ball[0].forward(BALL_FORWARD)
            ################################################
        # print('after forward from pad1')
        self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
        self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
        # print(f'bounce off pad 1 {self.more_coordinates}')
        self.pad1_score += 1
        print(self.pad1_score)
        self.bounce_off_2(self.pad_collision.core_bounce(self.more_coordinates))
        return

    # def ball_start(self):
    #     direction = random.randint(1, 4)
    #     if direction == 1:
    #         self.bottom_left()
    #     elif direction == 2:
    #         self.bottom_right()
    #     elif direction == 3:
    #         self.top_left()
    #     elif direction == 4:
    #         self.top_right()

    # def bottom_left(self):
    #     self.screen.tracer(BALL_TRACER)
    #     angle = random.randint(179, 225)
    #     ball_x = 0
    #     ball_y = 0
    #     self.ball[0].setheading(angle)
    #     while ball_x > -260:
    #         ball_x = self.ball[0].xcor()
    #         ball_y = self.ball[0].ycor()
    #         self.ball[0].forward(BALL_FORWARD)
    #     self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
    #     self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
    #     self.angle = int(self.pad_collision.core_bounce(self.more_coordinates))
    #     self.bounce_off_2(self.angle)
    #     return

    # def top_right(self):
    #     self.screen.tracer(BALL_TRACER)
    #     angle = random.randint(1, 30)
    #     ball_x = 0
    #     ball_y = 0
    #     self.ball[0].setheading(angle)
    #     while ball_x < 260:
    #         ball_x = self.ball[0].xcor()
    #         ball_y = self.ball[0].ycor()
    #         self.ball[0].forward(BALL_FORWARD)
    #     self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
    #     self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
    #     self.angle = int(self.pad_collision.core_bounce(self.more_coordinates))
    #     self.bounce_off_1(self.angle)
    #     return
    #
    # def bottom_right(self):
    #     self.screen.tracer(BALL_TRACER)
    #     angle = random.randint(320, 359)
    #     ball_x = 0
    #     ball_y = 0
    #     self.ball[0].setheading(angle)
    #     while ball_x < 260:
    #         ball_x = self.ball[0].xcor()
    #         ball_y = self.ball[0].ycor()
    #         self.ball[0].forward(BALL_FORWARD)
    #     self.more_coordinates['ball']['ball_x'] = math.floor(self.ball[0].xcor())
    #     self.more_coordinates['ball']['ball_y'] = math.floor(self.ball[0].ycor())
    #     self.angle = int(self.pad_collision.core_bounce(self.more_coordinates))
    #     self.bounce_off_1(self.angle)
    #     return

