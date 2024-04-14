from turtle import Turtle, Screen

STARTING_POSITIONS = [(280, 20), (280, 0), (280, -20)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FORWARD = 60


class Paddle1:
    def __init__(self):
        self.ux = 0
        self.uy = 0
        self.dx = 0
        self.dy = 0
        self.screen = Screen()
        self.pad = []
        self.create_pad1()

    def create_pad1(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.pad.append(new_segment)

    def up(self):
        self.screen.tracer(0)
        self.pad[0].setheading(UP)
        self.pad[0].forward(FORWARD)
        self.pad[1].setheading(UP)
        self.pad[1].forward(FORWARD)
        self.pad[2].setheading(UP)
        self.pad[2].forward(FORWARD)
        self.screen.update()
        self.ux = self.pad[0].xcor()
        self.uy = self.pad[0].ycor()
        print(self.ux, self.uy)

    def down(self):
        self.screen.tracer(0)
        self.pad[0].setheading(DOWN)
        self.pad[0].forward(FORWARD)
        self.pad[1].setheading(DOWN)
        self.pad[1].forward(FORWARD)
        self.pad[2].setheading(DOWN)
        self.pad[2].forward(FORWARD)
        self.screen.update()
        self.dx = self.pad[0].xcor()
        self.dy = self.pad[0].ycor()
        print(self.dx, self.dy)



