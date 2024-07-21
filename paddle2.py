from turtle import Turtle, Screen
from threading import Thread
STARTING_POSITIONS2 = [(-280, 20), (-280, 0), (-280, -20)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FORWARD = 10
FORWARD_while = 0.01
PADDLE_TRACER = 31
ts = 10000


class Paddle2(Thread):
    def __init__(self, more_coordinates):
        super().__init__()
        self.more_coordinates = more_coordinates
        self.screen = Screen()
        self.pad2 = []
        self.create_pad2()

        # self.screen = Screen()
        # self.screen.onkeypress(self.up, "w")
        # self.screen.onkeypress(self.down, "s")

    def reset_pad2(self):
        val = 0
        for position in STARTING_POSITIONS2:
            self.pad2[val].goto(position)
            val += 1

    def create_pad2(self):
        for position in STARTING_POSITIONS2:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        new_segment.turtlesize(1)
        self.pad2.append(new_segment)

    def pad2_coordinates(self):
        self.more_coordinates['pad2']['p2x'] = self.pad2[0].xcor()
        self.more_coordinates['pad2']['p2y'] = self.pad2[0].ycor()
        self.more_coordinates['pad2']['p2x1'] = self.pad2[1].xcor()
        self.more_coordinates['pad2']['p2y1'] = self.pad2[1].ycor()
        self.more_coordinates['pad2']['p2x2'] = self.pad2[2].xcor()
        self.more_coordinates['pad2']['p2y2'] = self.pad2[2].ycor()

    def up(self):  # I may use the ball movement mechanism to control pads
        # self.screen.listen()
        self.screen.tracer(PADDLE_TRACER)
        self.pad2[0].speed(ts)
        self.pad2[0].setheading(UP)
        self.pad2[0].forward(FORWARD)
        self.pad2[1].speed(ts)
        self.pad2[1].setheading(UP)
        self.pad2[1].forward(FORWARD)
        self.pad2[2].speed(ts)
        self.pad2[2].setheading(UP)
        self.pad2[2].forward(FORWARD)

        self.more_coordinates['pad2']['p2x'] = self.pad2[0].xcor()
        self.more_coordinates['pad2']['p2y'] = self.pad2[0].ycor()
        self.more_coordinates['pad2']['p2x1'] = self.pad2[1].xcor()
        self.more_coordinates['pad2']['p2y1'] = self.pad2[1].ycor()
        self.more_coordinates['pad2']['p2x2'] = self.pad2[2].xcor()
        self.more_coordinates['pad2']['p2y2'] = self.pad2[2].ycor()
        # print(self.pad2[0].xcor(), self.pad2[0].ycor())
        return

    def down(self):
        # self.screen.listen()
        self.screen.tracer(PADDLE_TRACER)
        self.pad2[0].setheading(DOWN)
        self.pad2[0].speed(ts)
        self.pad2[0].forward(FORWARD)
        self.pad2[1].speed(ts)
        self.pad2[1].setheading(DOWN)
        self.pad2[1].forward(FORWARD)
        self.pad2[2].speed(ts)
        self.pad2[2].setheading(DOWN)
        self.pad2[2].forward(FORWARD)
        self.more_coordinates['pad2']['p2x'] = self.pad2[0].xcor()
        self.more_coordinates['pad2']['p2y'] = self.pad2[0].ycor()
        self.more_coordinates['pad2']['p2x1'] = self.pad2[1].xcor()
        self.more_coordinates['pad2']['p2y1'] = self.pad2[1].ycor()
        self.more_coordinates['pad2']['p2x2'] = self.pad2[2].xcor()
        self.more_coordinates['pad2']['p2y2'] = self.pad2[2].ycor()
        # print(self.pad2[0].xcor(), self.pad2[0].ycor())
        return

    def up_while(self, stop_val=1):
        self.screen.tracer(PADDLE_TRACER)
        self.pad2[0].setheading(UP)
        self.pad2[1].setheading(UP)
        self.pad2[2].setheading(UP)
        move_to = int(self.pad2[0].ycor() + 20)
        while self.pad2[0].ycor() < move_to:

            self.pad2[0].forward(FORWARD_while)
            self.pad2[1].forward(FORWARD_while)
            self.pad2[2].forward(FORWARD_while)
            self.pad2_coordinates()
            # if stop_val == 0:
            #     return
        return

    # turtle.onkey(fun, key)
    # turtle.onkeyrelease(fun, key)¶

