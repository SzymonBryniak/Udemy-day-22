from turtle import Turtle, Screen
import ball
from paddle_collision import PadCollision
# from screen import coordinates # circular import error
STARTING_POSITIONS = [(280, 20), (280, 0), (280, -20)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FORWARD = 30

# PAD1_COORDINATES = [0, 0, 0, 0]


class Paddle1:
    def __init__(self, dict_coordinates):
        self.dict_coordinates = dict_coordinates
        self.ball = ball
        self.screen = Screen()
        self.p1ux = 0
        self.p1uy = 0
        self.p1dx = 0
        self.p1dy = 0
        self.pad1 = []
        self.create_pad1()
        self.collision = PadCollision()

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
        self.screen.tracer(2)
        self.pad1[0].setheading(UP)
        self.pad1[0].forward(FORWARD)
        self.pad1[1].setheading(UP)
        self.pad1[1].forward(FORWARD)
        self.pad1[2].setheading(UP)
        self.pad1[2].forward(FORWARD)
        self.p1ux = self.pad1[0].xcor()
        self.p1uy = self.pad1[0].ycor()
        self.dict_coordinates['pad1_x'] = self.p1ux
        self.dict_coordinates['pad1_y'] = self.p1uy

        print(self.p1ux, self.p1uy)
        return

    def down(self):
        self.screen.tracer(2)
        self.pad1[0].setheading(DOWN)
        self.pad1[0].forward(FORWARD)
        self.pad1[1].setheading(DOWN)
        self.pad1[1].forward(FORWARD)
        self.pad1[2].setheading(DOWN)
        self.pad1[2].forward(FORWARD)
        self.p1dx = self.pad1[0].xcor()
        self.p1dy = self.pad1[0].ycor()
        self.dict_coordinates['pad1_x'] = self.p1dx
        self.dict_coordinates['pad1_y'] = self.p1dy

        print(self.p1dx, self.p1dy)
        return


