from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

for i in range(20):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()


