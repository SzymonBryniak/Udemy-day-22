from turtle import Screen, Turtle
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
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
middle = Turtle()
text1 = Turtle()
text2 = Turtle()
pad1 = Paddle1(more_coordinates)
pad2 = Paddle2(more_coordinates)
ball = Ball(more_coordinates)
score1 = ball.pad1_score
score2 = more_coordinates['score']['pad2']

# while not more_coordinates['game_on']:
#     print('press the "UP" key to start the game')
#     screen.onkeypress(ball.on(more_coordinates), key='Up')


text1.color('green')
text1.hideturtle()
text1.penup()
text1.setpos(x=-56, y=200)
text1.write(score1, move=True, align="left", font=("Verdana", 70, "normal",))
text2.color('green')
text2.hideturtle()
text2.penup()
text2.setpos(x=0, y=200)
text2.write(score2, move=True, align="left", font=("Verdana", 70, "normal",))
middle.hideturtle()
middle.color('green')
middle.setpos(x=0, y=300)
middle.goto(x=0, y=-300)


def start(self):
    self.screen.textinput("NIM", "Would you like to continue?: ")
    print(self.ball[0])
    self.create_ball()
    return


class Game:
    def __init__(self):
        # screen.onkeypress(pad1.up, key='Up')
        # screen.onkeypress(pad1.down, key='Down')
        # screen.onkeypress(pad2.up, key='w')
        # screen.onkeypress(pad2.down, key='s')
        pass

    def restart(self):
        # user_input = prompt.textinput("NIM", "Would you like to continue?: ")
        user_input = input("Would you like to continue?: ")
        if user_input == 'Yes':
            print(' restart function working')
            ball.ball[0].reset()
            ball.create_ball()
            self.restart()
        else:
            print('Game Over')
            return

    def start(self):
        to_restart = 0
        screen.onkeypress(pad1.up, key='Up')
        screen.onkeypress(pad1.down, key='Down')
        screen.onkeypress(pad2.up, key='w')
        screen.onkeypress(pad2.down, key='s')
        ball.create_ball()
        self.restart()


game = Game()
game.start()


'''
Collision evaluation
'''
######
# wall = Wall(more_coordinates)
# wall.wall_bounce_off_1()
# screen.exitonclick()

'''
screen.listen()
screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
'''
