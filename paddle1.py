from turtle import Turtle
STARTING_POSITIONS = [(280, 20), (280, 0), (280, -20)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle1:
    def __init__(self):
        self.snake = []
        self.create_pad1()
        self.head = self.snake[0]

    def create_pad1(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

