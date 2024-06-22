from turtle import Turtle, Screen
from paddle_collision import PadCollision
# from screen import coordinates # circular import error
STARTING_POSITIONS = [(280, 20), (280, 0), (280, -20)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FORWARD = 20
PADDLE_TRACER = 31
# PAD1_COORDINATES = [0, 0, 0, 0]
ts = 10


class Paddle1:
    def __init__(self, more_coordinates):
        self.screen = Screen()
        self.more_coordinates = more_coordinates
        self.pad1 = []
        self.create_pad1()

    def create_pad1(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.pad1.append(new_segment)

    def up(self):
        # self.screen.listen()
        self.screen.tracer(PADDLE_TRACER)
        self.pad1[0].setheading(UP)
        self.pad1[0].forward(FORWARD)
        self.pad1[0].speed(ts)
        self.pad1[1].setheading(UP)
        self.pad1[1].forward(FORWARD)
        self.pad1[1].speed(ts)
        self.pad1[2].setheading(UP)
        self.pad1[2].forward(FORWARD)
        self.pad1[2].speed(ts)

        self.more_coordinates['pad1']['p1x'] = self.pad1[0].xcor()
        self.more_coordinates['pad1']['p1y'] = self.pad1[0].ycor()
        self.more_coordinates['pad1']['p1x1'] = self.pad1[1].xcor()
        self.more_coordinates['pad1']['p1y1'] = self.pad1[1].ycor()
        self.more_coordinates['pad1']['p1x2'] = self.pad1[2].xcor()
        self.more_coordinates['pad1']['p1y2'] = self.pad1[2].ycor()
        # print(self.pad1[0].xcor(), self.pad1[0].ycor())
        return

    def down(self):
        self.screen.tracer(PADDLE_TRACER)
        self.pad1[0].speed(ts)
        self.pad1[0].setheading(DOWN)
        self.pad1[0].forward(FORWARD)
        self.pad1[1].speed(ts)
        self.pad1[1].setheading(DOWN)
        self.pad1[1].forward(FORWARD)
        self.pad1[2].speed(ts)
        self.pad1[2].setheading(DOWN)
        self.pad1[2].forward(FORWARD)
        self.more_coordinates['pad1']['p1x'] = self.pad1[0].xcor()
        self.more_coordinates['pad1']['p1y'] = self.pad1[0].ycor()
        self.more_coordinates['pad1']['p1x1'] = self.pad1[1].xcor()
        self.more_coordinates['pad1']['p1y1'] = self.pad1[1].ycor()
        self.more_coordinates['pad1']['p1x2'] = self.pad1[2].xcor()
        self.more_coordinates['pad1']['p1y2'] = self.pad1[2].ycor()
        # print(self.pad1[0].xcor(), self.pad1[0].ycor())
        return


