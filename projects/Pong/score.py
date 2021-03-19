from turtle import Turtle

# again take from Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()

    def thunderdome(self):
        self.goto(x=0, y=280)
        self.write(f'Welcome to the Thunderdome :)',align='center', font=['Courier', 16])

    def update_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(f'{self.l_score}',align='center',font=['Courier',16])
        self.goto(x=100, y=200)
        self.write(f'{self.r_score}', align='center', font=['Courier', 16])
        # self.left_tally()
        # self.right_tally()

    def left_tally(self):
        self.l_score = self.l_score + 1
        self.clear()

    def right_tally(self):
        self.r_score = self.r_score + 1
        self.clear()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f'GAME OVER', align='center',font=['Courier',8])