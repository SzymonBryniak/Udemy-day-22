from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball


class MainScreen:

    def __int__(self):

        self.more_coordinates = {'score': {'pad1': 1, 'pad2': 0}, 'ball': {'ball_x': 0, 'ball_y': 0, 'ball_s': 0},
                        'pad1': {
                        'p1x': 0,
                        'p1y': 0,
                        'p1x1': 0,
                        'p1y1': 0,
                        'p1x2': 0,
                        'p1y2': 0,
                        },
                        'pad2': {
                        'p2x': 0,
                        'p2y': 0,
                        'p2x1': 0,
                        'p2y1': 0,
                        'p2x2': 0,
                        'p2y2': 0,
                        }
                        }

        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.middle = Turtle()
        self.text1 = Turtle()
        self.text2 = Turtle()
        self.pad1 = Paddle1(self.more_coordinates)
        self.pad2 = Paddle2(self.more_coordinates)
        self.middle.hideturtle()
        self.middle.color('green')
        self.middle.setpos(x=0, y=300)
        self.middle.goto(x=0, y=-300)

        self.screen.listen()
        self.screen.onkeypress(self.pad1.up, key='Up')
        self.screen.onkeypress(self.pad1.down, key='Down')
        self.screen.onkeypress(self.pad2.up, key='w')
        self.screen.onkeypress(self.pad2.down, key='s')
        self.ball = Ball(self.more_coordinates)
        self.score1 = self.ball.pad1_score
        self.score2 = self.more_coordinates['score']['pad2']
        self.text1.color('green')
        self.text1.hideturtle()
        self.text1.penup()
        self.text1.setpos(x=-56, y=200)
        self.text1.write(self.score1, move=True, align="left", font=("Verdana", 70, "normal",))
        self.text2.color('green')
        self.text2.hideturtle()
        self.text2.penup()
        self.text2.setpos(x=0, y=200)
        self.text2.write(self.score2, move=True, align="left", font=("Verdana", 70, "normal",))
        self.ball.create_ball()


game = MainScreen()
game.ball.create_ball()
