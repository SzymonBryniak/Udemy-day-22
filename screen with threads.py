from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
import threading
from threading import Thread

from wall_collision import Wall

more_coordinates = {'object': False, 'score': {'pad1': 1, 'pad2': 0}, 'ball': {'ball_x': 0, 'ball_y': 0, 'ball_s': 0},
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
game_on = False
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()
prompt = Screen()


# while not more_coordinates['game_on']:
#     print('press the "UP" key to start the game')
#     screen.onkeypress(ball.on(more_coordinates), key='Up')


class Game:
    def __init__(self):
        self.th = threading
        self.pad1 = Paddle1(more_coordinates)
        self.pad2 = Paddle2(more_coordinates)
        self.coordinates = more_coordinates
        self.ball = Ball(more_coordinates)
        self.text1 = Turtle()
        self.text2 = Turtle()
        self.text1.color('green')
        self.text1.hideturtle()
        self.text1.penup()
        self.text2.color('green')
        self.text2.hideturtle()
        self.text2.penup()
        self.middle = Turtle()
        self.middle.hideturtle()
        self.middle.color('green')
        self.middle.setpos(x=0, y=300)
        self.middle.goto(x=0, y=-300)
        self.mid = self.middle

    def settings(self):

        return

    def middle(self):
        self.middle.hideturtle()
        self.middle.setpos(x=0, y=300)
        self.middle.goto(x=0, y=-300)
        pass

    def update_score(self, val):
        self.text1.clear()
        self.text2.clear()
        self.text1.setpos(x=-56, y=200)
        self.text2.setpos(x=0, y=200)
        self.text1.write(val[0], move=True, align="left", font=("Verdana", 70, "normal",))
        self.text2.write(val[1], move=True, align="left", font=("Verdana", 70, "normal",))

    def restart(self, ini_val):
        self.update_score(ini_val)
        self.middle.setpos(x=0, y=300)
        self.middle.goto(x=0, y=-300)
        screen.update()
        # user_input = prompt.textinput("NIM", "Would you like to continue?: ")
        user_input = input("Would you like to continue?: ")
        if user_input == 'Yes':
            self.ball.ball[0].reset()
            self.pad1.reset_pad1()
            self.pad2.reset_pad2()
            # screen.update()  # ? was not disabled
            val = self.ball.create_ball()
            print(f' ball returned: {val}')
            self.restart(val)
        else:
            print('Game Over')
            return

    def start(self):
        coordinates = more_coordinates
        pad1 = Paddle1(more_coordinates)
        pad2 = Paddle2(more_coordinates)
        ball = Ball(more_coordinates)
        val = [0, 0]
        self.update_score(val)
        screen.onkeypress(pad1.up, key='Up')
        screen.onkeypress(pad1.down, key='Down')
        screen.onkeypress(pad2.up, key='w')
        screen.onkeypress(pad2.down, key='s')
        val = ball.create_ball()
        print(f' ball returned: {val}')
        print(f'Start return value is: {val}')
        self.update_score(list(val))
        screen.update()
        self.restart(list(val))

    def start2(self):
        val = [0, 0]
        self.update_score(val)
        th01 = threading.Thread(target=self.pad_thread())
        th01.start()
        # screen.onkeypress(self.pad1.up, key='Up')
        # screen.onkeypress(self.pad1.down, key='Down')
        # screen.onkeypress(self.pad2.up_while, key='w')
        # screen.onkeypress(self.pad2.down, key='s')
        # self.pad_thread()
        # ball = self.ball.create_ball
        th02 = threading.Thread(target=self.ball.create_ball())
        th02.start()
        print(f' ball returned: {val}')
        print(f'Start return value is: {val}')
        self.update_score(list(val))
        # th03 = threading.Thread(target=self.update_score(list(val)))
        screen.update()
        self.restart(list(val))

    def pad_thread(self):
        screen.onkeypress(self.pad1.up, key='Up')
        screen.onkeypress(self.pad1.down, key='Down')
        screen.onkeypress(self.pad2.up_while, key='w')
        screen.onkeypress(self.pad2.down, key='s')
        return


game = Game()
game.start()  # change to start() to run the closest to working as it should code.

# To try more:
# How objects from the outside scope interact with objects from the inside scope.
