# controls all the food (dots)
from turtle import Turtle
import random

# this makes it inherit all the attributes from the Turtle class
class Food(Turtle):
    #init gets called any time you call this class
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # stretch is a way to compress the default turtle object which is too big for food
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.new_loc()
    def new_loc(self):
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(rand_x,rand_y)
        