from turtle import Turtle, colormode, xcor
import random as rand

STRETCH_WIDTH = 1
STRETCH_HEIGHT = 2
LEFT = 180
RGB = 255
Y_BORDER = 250
X_BORDER = 320
SPEED = 5


class Obstacles:

    def __init__(self):
        self.total_obstacles = []
        self.move_amnt = SPEED

    def generate_obstacle(self):
        '''Generate one obstacle and add it to the total obstacles list'''
        if rand.randint(1, 6) == 1:
            colormode(RGB)
            obs = Turtle("square")
            obs.pu()
            obs.color(self.rand_color())
            obs.shapesize(STRETCH_WIDTH, STRETCH_HEIGHT)
            obs.setheading(LEFT)
            obs.goto(X_BORDER, rand.randint(-Y_BORDER, Y_BORDER))
            self.total_obstacles.append(obs)

    def rand_color(self):
        '''Generate a random rgb tuple and return it'''
        r = rand.randint(0, RGB)
        g = rand.randint(0, RGB)
        b = rand.randint(0, RGB)
        return (r, g, b)

    def move(self):
        '''Move all the obstacles in total obstacles and delete the ones that are off the screen'''
        for obs in self.total_obstacles:
            obs.forward(self.move_amnt)
            if obs.xcor() < -X_BORDER:
                self.total_obstacles.remove(obs)

    def update_speed(self):
        '''Update the speed of the obstacle by a constant value'''
        self.move_amnt += SPEED
