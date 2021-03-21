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
        self.level = 1

    def scoreboard(self):
        self.goto(-280,250)
        self.write(f'Level: {self.level}',align='left',font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.scoreboard()


    def thunderdome(self):
        self.goto(x=280, y=0)
        self.write(f'gang shit only',align='right', font=['Courier', 8])

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f'game over.',align='right', font=['Courier', 8])

