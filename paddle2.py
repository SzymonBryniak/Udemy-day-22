from turtle import Turtle, Screen
import threading
STARTING_POSITIONS = [(-280, 20), (-280, 0), (-280, -20)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FORWARD = 60

PAD2_COORDINATES = []


class Paddle2:
    def __init__(self):
        self.p2ux = 0
        self.p2uy = 0
        self.p2dx = 0
        self.p2dy = 0
        self.pad2 = []
        self.create_pad2()
        self.screen = Screen()
        # self.screen.listen()
        # self.screen.onkeypress(self.up, "w")
        # self.screen.onkeypress(self.down, "s")

    def create_pad2(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.pad2.append(new_segment)

    def up(self):
        self.screen.tracer(0)
        self.pad2[0].setheading(UP)
        self.pad2[0].forward(FORWARD)
        self.pad2[1].setheading(UP)
        self.pad2[1].forward(FORWARD)
        self.pad2[2].setheading(UP)
        self.pad2[2].forward(FORWARD)
        self.screen.update()
        self.p2ux = self.pad2[0].xcor()
        self.p2uy = self.pad2[0].ycor()
        PAD2_COORDINATES[0] = self.p2ux
        PAD2_COORDINATES[1] = self.p2uy
        print(self.p2ux, self.p2uy)

    def down(self):
        self.screen.tracer(0)
        self.pad2[0].setheading(DOWN)
        self.pad2[0].forward(FORWARD)
        self.pad2[1].setheading(DOWN)
        self.pad2[1].forward(FORWARD)
        self.pad2[2].setheading(DOWN)
        self.pad2[2].forward(FORWARD)
        self.screen.update()
        self.p2dx = self.pad2[0].xcor()
        self.p2dy = self.pad2[0].ycor()
        PAD2_COORDINATES[0] = self.p2dx
        PAD2_COORDINATES[1] = self.p2dy
        print(self.p2ux, self.p2uy)
        print(self.p2dx, self.p2dy)
