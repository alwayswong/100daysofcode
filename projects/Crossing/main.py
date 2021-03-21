import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Welcome to the Thunderdome!')
# turtle off the tracer so that it doesnt look weird
screen.tracer(0)

# Scoreboard
egg = Scoreboard()
egg.thunderdome()

# turtles
timmy = Player()

# buttons to play with
screen.listen()
screen.onkey(timmy.go_up,'Up')





#game_is_on = True
while True:
    time.sleep(0.1)
    screen.update()
