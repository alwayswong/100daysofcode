from turtle import Turtle

MOVE_AMOUNT = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('pink')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.speed(4)
        self.x_move = MOVE_AMOUNT
        self.y_move = MOVE_AMOUNT

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move = self.y_move * -1

    def paddle_bounce(self):
        self.x_move = self.x_move * -1