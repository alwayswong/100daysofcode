import random
from turtle import Turtle,Screen,distance
import time
from snake import Snake
from food import Food
from counter import Counter

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('sssssssnake')
# need to call update if you turn the tracer off
screen.tracer(0)

snake = Snake()
food = Food()
score = Counter()
game_over = Counter()
screen.listen()
screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.left,key='Left')
screen.onkey(fun=snake.right,key='Right')



while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        #generate new food spot
        food.new_loc()
        # snake extends
        snake.extend()
        #add to the food score
        score.tally()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over.game_over()
        break

    for segment in snake.segments:
        # dont want to collide with itself
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            break
            game_over.game_over()







screen.exitonclick()