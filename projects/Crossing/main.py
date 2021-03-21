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
egg = Scoreboard()
egg.thunderdome()

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
    random_chance = random.randint(1,6)
    if random_chance == 1:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move()
        if timmy.distance(car) < 20:
            message = Scoreboard()
            message.game_over()
            #check for collision
            screen.exitonclick()