import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Welcome to the Thunderdome!')
# turtle off the tracer so that it doesnt look weird
screen.tracer(0)

# Scoreboard
scoreboard = Scoreboard()
scoreboard.scoreboard()


egg = Scoreboard()
egg.thunderdome()

# car manager
car_manager = CarManager()

# turtles
timmy = Player()

# cars
cars = []

# buttons to play with
screen.listen()
screen.onkey(timmy.go_up,'Up')
screen.onkey(timmy.go_down,'Down')


#game_is_on = True
while True:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            message = Scoreboard()
            message.game_over()
            #check for collision
            screen.exitonclick()

    if timmy.ycor() > 300:
        timmy.starting()
        scoreboard.increase_level()
        car_manager.level_up()