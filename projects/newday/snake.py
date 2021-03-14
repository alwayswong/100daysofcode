from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):

        for i in range(3):
            snake = Turtle(shape='square')
            snake.color('white')
            snake.penup()
            snake.goto(x=(-20 + 20 * i), y=0)
            snake.speed('fastest')
            self.parts.append(snake)

    def move(self):
        for i in range(2, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(x=new_x, y=new_y)
        self.parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.parts[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.parts[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.parts[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.parts[0].setheading(RIGHT)