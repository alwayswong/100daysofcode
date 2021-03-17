from turtle import Turtle

# again take from Turtle
class Counter(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        #self.write(f'Score: {self.counter}',align='center',font=['Courier',8])
        self.tally()

    def tally(self):
        self.counter = self.counter + 1
        self.clear()
        self.write(f'Score: {self.counter}', align='center',font=['Courier',8])

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f'GAME OVER', align='center',font=['Courier',8])