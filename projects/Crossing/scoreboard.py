import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()

    def thunderdome(self):
        self.goto(x=280, y=0)
        self.write(f'gang shit only',align='right', font=['Courier', 8])

