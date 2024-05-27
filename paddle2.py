from turtle import Turtle, Screen
import ball
STARTING_POSITIONS = [(-280, 20), (-280, 0), (-280, -20)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FORWARD = 30


class Paddle2:
    def __init__(self, more_coordinates):
        self.more_coordinates = more_coordinates
        self.ball = ball
        self.screen = Screen()
        self.pad2 = []
        self.create_pad2()

        # self.screen = Screen()
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
        # self.screen.listen()
        self.screen.tracer(2)
        self.pad2[0].setheading(UP)
        self.pad2[0].forward(FORWARD)
        self.pad2[1].setheading(UP)
        self.pad2[1].forward(FORWARD)
        self.pad2[2].setheading(UP)
        self.pad2[2].forward(FORWARD)
        self.more_coordinates['pad2']['p2ux'] = self.pad2[0].xcor()
        self.more_coordinates['pad2']['p2uy'] = self.pad2[0].ycor()
        self.more_coordinates['pad2']['p2ux1'] = self.pad2[1].xcor()
        self.more_coordinates['pad2']['p2uy1'] = self.pad2[1].ycor()
        self.more_coordinates['pad2']['p2ux2'] = self.pad2[2].xcor()
        self.more_coordinates['pad2']['p2uy2'] = self.pad2[2].ycor()
        print(self.pad2[0].xcor(), self.pad2[0].ycor())
        return

    def down(self):
        # self.screen.listen()
        self.screen.tracer(2)
        self.pad2[0].setheading(DOWN)
        self.pad2[0].forward(FORWARD)
        self.pad2[1].setheading(DOWN)
        self.pad2[1].forward(FORWARD)
        self.pad2[2].setheading(DOWN)
        self.pad2[2].forward(FORWARD)
        self.more_coordinates['pad2']['p2dx'] = self.pad2[0].xcor()
        self.more_coordinates['pad2']['p2dy'] = self.pad2[0].ycor()
        self.more_coordinates['pad2']['p2dx1'] = self.pad2[1].xcor()
        self.more_coordinates['pad2']['p2dy1'] = self.pad2[1].ycor()
        self.more_coordinates['pad2']['p2dx2'] = self.pad2[2].xcor()
        self.more_coordinates['pad2']['p2dy2'] = self.pad2[2].ycor()
        print(self.pad2[0].xcor(), self.pad2[0].ycor())
        return
