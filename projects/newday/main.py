import random
from turtle import Turtle,Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('sssssssnake')
# need to call update if you turn the tracer off
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.left,key='Left')
screen.onkey(fun=snake.right,key='Right')



while True:
    screen.update()
    time.sleep(0.1)
    # for part in parts:
    #     part.forward(10)
    snake.move()








screen.exitonclick()