import turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(STARTING_POSITION)
        self.right(270)


    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(),y=new_y)
