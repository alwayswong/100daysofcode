from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)
def move_backwards():
    timmy.back(10)
def reset():
    timmy.reset()
def turn_right():
    timmy.right(10)
def turn_left():
    timmy.left(10)

timmy.pensize(2)
timmy.color('red')
timmy.shape('turtle')
screen.listen()
#when using function as an input, dont call it because its waiting for the onkey
#using function as input is basically doing a nested function aka higher order function
screen.onkey(fun=move_forwards,key='w')
screen.onkey(fun=move_backwards,key='s')
screen.onkey(fun=reset,key='c')
screen.onkey(fun=turn_right,key='d')
screen.onkey(fun=turn_left,key='a')

#screen.onkey(move_backwards(),'s')

screen.exitonclick()
