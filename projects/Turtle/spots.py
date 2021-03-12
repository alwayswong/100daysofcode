import colorgram

#find colors
# colors = colorgram.extract('image.jpeg',30)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb.append(new_color)
#
#
# print(rgb)
dots = [(253, 251, 248), (254, 250, 252), (231, 251, 242), (198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 247, 252), (244, 33, 165), (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), (222, 160, 8), (10, 98, 61), (17, 18, 43), (47, 214, 232), (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169), (78, 234, 201), (50, 234, 244), (3, 66, 40)]

import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.penup()
timmy.back(250)
timmy.right(90)
timmy.forward(250)
timmy.left(90)
timmy.speed('fastest')
timmy.hideturtle()
for i in range(10):
    for j in range(10):
        timmy.dot(20, random.choice(dots))
        timmy.forward(50)
    timmy.back(500)
    timmy.right(270)
    timmy.forward(50)
    timmy.right(90)
