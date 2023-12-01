import turtle
from math import cos, radians, sin

spiral_archimeda = turtle.Turtle()
c = input()
d = int(input())
a = int(input())
b = int(input())
spiral_archimeda.color(c)
for phi in range(0, 360, 360 // d):
    for teta in range(0, 360, 10):
        r = a + b * radians(teta)
        x = r * cos(radians(teta + phi))
        y = r * sin(radians(teta + phi))
        spiral_archimeda.pu()
        spiral_archimeda.goto(x, y)
        spiral_archimeda.pd()
        spiral_archimeda.dot()
turtle.done()

# silver
# 5
# 0
# 40
