from turtle import Screen
from player import Player
from level import Level
from obstacles import Obstacles
import time

WIDTH = 600
HEIGHT = 600
WAIT_TIME = 0.1
HIT_BOX = 20

screen = Screen()
screen.title("Turtle Cross")
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer(0)


def start_game():
    screen.reset()
    is_game_on = True
    player = Player()
    level = Level()
    hazards = Obstacles()

    screen.listen()
    screen.onkeypress(player.up, "Up")
    screen.onkeypress(player.down, "Down")
    screen.onkeypress(None, "space")

    while is_game_on:
        time.sleep(WAIT_TIME)
        screen.update()

        hazards.generate_obstacle()
        hazards.move()

        # Detect collision between obstacles and player
        for obs in hazards.total_obstacles:
            if obs.distance(player) < HIT_BOX:
                level.game_over()
                is_game_on = False

        # Detect level increase
        if player.next_level():
            hazards.update_speed()
            level.write_level()

    screen.onkeypress(start_game, "space")


start_game()

screen.exitonclick()
