from turtle import Turtle,Screen,distance
import time
import paddle
import ball

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = paddle.Paddle((380,0))
l_paddle = paddle.Paddle((-380,0))
ball = ball.Ball()



# buttons
screen.listen()
screen.onkey(r_paddle.go_up,'o')
screen.onkey(r_paddle.go_down,'k')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'d')

while True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # make the ycor the opposite
        ball.bounce()

    # ball check with paddle
    if (ball.distance(r_paddle) < 20 and ball.xcor() > 320) or (ball.distance(r_paddle) < 20 and ball.xcor() < -320):
        ball.paddle_bounce()



screen.exitonclick()