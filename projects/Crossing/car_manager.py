import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        rand_color = random.choice(COLORS)
        self.color(rand_color)
        self.speed('fastest')
        self.goto(x=300,y=random.randint(-250,250))
        self.x_move = MOVE_INCREMENT

    def move(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x,self.ycor())

