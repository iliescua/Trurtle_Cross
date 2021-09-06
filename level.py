from player import START_X, START_Y
from turtle import Turtle

START_X = -220
START_Y = 270
ALIGN = "center"
FONT = ("Courier", 16, "normal")

class Level:


    def __init__(self):
        self.level = Turtle()
        self.level.hideturtle()
        self.level.pu()
        self.level.color("white")
        self.level.goto(START_X, START_Y)
        self.score = 1
        self.level.write(f"Level: {self.score}", align=ALIGN, font=FONT)

    
    def write_level(self):
        '''Update the level count on the top left of the screen'''
        self.level.clear()
        self.score += 1
        self.level.write(f"Level: {self.score}", align=ALIGN, font=FONT)


    def game_over(self):
        '''Print game over in the middle of the screen'''
        self.level.goto(0, 0)
        self.level.write("GAME OVER", align=ALIGN, font=FONT)