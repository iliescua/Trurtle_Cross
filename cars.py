from turtle import Turtle, colormode
import random as rand

STRETCH_WIDTH = 1
STRETCH_HEIGHT = 2
LEFT = 180
RGB = 255
Y_BORDER = 250
X_BORDER = 300
SPEED = 5


class Cars:

    def __init__(self):
        self.total_cars = []
        self.move_amnt = SPEED

    def generate_car(self):
        '''Generate one car and add it to the total cars list'''
        if rand.randint(1, 6) == 1:
            colormode(RGB)
            car = Turtle("square")
            car.pu()
            car.color(self.rand_color())
            car.shapesize(STRETCH_WIDTH, STRETCH_HEIGHT)
            car.setheading(LEFT)
            car.goto(X_BORDER, rand.randint(-Y_BORDER, Y_BORDER))
            self.total_cars.append(car)

    def rand_color(self):
        '''Generate a random rgb tuple and return it'''
        r = rand.randint(0, RGB)
        g = rand.randint(0, RGB)
        b = rand.randint(0, RGB)
        return (r, g, b)

    def move(self):
        '''Move all the cars in total cars'''
        for car in self.total_cars:
            car.forward(self.move_amnt)

    def update_speed(self):
        '''Update the speed of the car by a constant value'''
        self.move_amnt += SPEED
