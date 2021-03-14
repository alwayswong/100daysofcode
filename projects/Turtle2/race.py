from turtle import Turtle,Screen
import random

# separate instances of the same object
# timmy = Turtle()
# jacob = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
guess = screen.textinput(title="Make your bet",prompt="Which color turtle will win?").strip().lower()
colors = ['red','orange','yellow','green','blue','purple']
turts = []

for inx, turtle in enumerate(colors):
    turtle = Turtle()
    turtle.speed('fastest')
    turts.append(turtle)
    turtle.color(colors[inx])
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-200,-125+(inx*50))

while True:
    for timmy in turts:
        move = random.randint(0,10)
        timmy.forward(move)
        if timmy.xcor() > 200:
            winner = timmy.pencolor()
            if winner == guess:
                print(f'You guessed correct, {timmy.pencolor()} wins!')
                quit()
            else:
                print(f'You guessed wrong, {timmy.pencolor()} wins!')
                quit()


screen.exitonclick()