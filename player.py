from turtle import Turtle

UP = 90
START_X = 0
START_Y = -280
BORDER_BOUNDS = 280
MOVE_AMNT = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.color("cyan")
        self.setheading(UP)
        self.goto(START_X, START_Y)

    def next_level(self):
        '''Check to see if the player made it past the finish line and return True or False'''
        if self.ycor() > BORDER_BOUNDS:
            self.goto(START_X, START_Y)
            return True
        return False

    def up(self):
        '''Move player up the screen'''
        self.forward(MOVE_AMNT)

    def down(self):
        '''Move player down the screen'''
        self.backward(MOVE_AMNT)
