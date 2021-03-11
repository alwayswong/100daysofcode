import turtle
import random

timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('red')

colors = ['lavender','medium spring green','orange']
turtle.colormode(255)
direction = [0,90,180,270]
turtle.speed('fastest')
# for i in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# draw a bunch of shapes within each other
# for i in range(3,11):
#     timmy.color(random.choice(colors))
#     for j in range(i):
#         angle = 360 / i
#         timmy.right(angle)
#         timmy.forward(100)

while True:
    timmy.pensize(10)
    timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    timmy.right(random.choice(direction))
    timmy.forward(20)

# random walk


screen = Screen()


