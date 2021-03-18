from turtle import Turtle,Screen,distance
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Turtle('square')
r_paddle.penup()
r_paddle.speed('fastest')
r_paddle.shapesize(stretch_wid=5,stretch_len=1)

r_paddle.color('white')
r_paddle.goto(x=380,y=0)


def go_up():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(x=r_paddle.xcor(),y=new_y)

def go_down():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(x=r_paddle.xcor(),y=new_y)





screen.listen()
screen.onkey(go_up,'Up')
screen.onkey(go_down,'Down')

while True:
    screen.update()


screen.exitonclick()