import turtle
from math import cos, radians, sin

archimed = turtle.Turtle()
c = input()
d = int(input())
a = int(input())
b = int(input())
archimed.color(c)
for phi in range(0, 360, 360 // d):
    for teta in range(0, 360, 10):
        r = a + b * radians(teta)
        x = r * cos(radians(teta + phi))
        y = r * sin(radians(teta + phi))
        archimed.pu()
        archimed.goto(x, y)
        archimed.pd()
        archimed.dot()
turtle.done()