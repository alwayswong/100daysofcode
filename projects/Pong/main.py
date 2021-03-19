from turtle import Turtle,Screen,distance
import time
import paddle
import ball
import score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = paddle.Paddle((380,0))
l_paddle = paddle.Paddle((-380,0))
ball = ball.Ball()
welcome = score.Scoreboard()
welcome.thunderdome()
scoreboard = score.Scoreboard()
scoreboard.update_scoreboard()




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
    if (ball.distance(r_paddle) < 20 and ball.xcor() > 320) or (ball.distance(l_paddle) < 20 and ball.xcor() < -320):
        ball.paddle_bounce()

    if ball.xcor() > 400:
    #     # score for the left guy
        ball.reset_position()
        scoreboard.left_tally()
        scoreboard.update_scoreboard()
    if ball.xcor() < -400:
    #     #score for the right guy
        ball.reset_position()
        scoreboard.right_tally()
        scoreboard.update_scoreboard()



screen.exitonclick()