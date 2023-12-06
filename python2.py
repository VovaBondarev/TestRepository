from turtle import *
from math import sin

ostrov = Turtle()
c1 = input()
c2 = input()
c3 = input()
c4 = input()
c5 = input()
ostrov.pu()
ostrov.goto(-150, 0)
ostrov.pd()
ostrov.color(c1)
ostrov.begin_fill()
for x in range(-150, 151, 5):
    y = (150 ** 2 - x ** 2) ** 0.5
    ostrov.goto(x, y)
ostrov.end_fill()
ostrov.pu()
ostrov.goto(-350, -300)
ostrov.pd()
ostrov.color(c2)
ostrov.begin_fill()
for x in range(-350, 350, 5):
    y = 10 * sin(0.144 * x) + 10
    ostrov.goto(x, y)
ostrov.goto(350, -300)
ostrov.end_fill()
ostrov.pu()
ostrov.goto(-100, -105)
ostrov.pd()
ostrov.color(c3)
ostrov.begin_fill()
for x in range(-100, 200, 5):
    y = - 0.0025 * ((x - 50) ** 2) - 50
    ostrov.goto(x, y)
for x in range(200, -100, -5):
    y = 0.0005 * ((x - 50) ** 2) - 118
    ostrov.goto(x, y)
ostrov.end_fill()
ostrov.pu()
ostrov.goto(-8, 206)
ostrov.pd()
ostrov.color(c4)
ostrov.begin_fill()
for x in range(-8, 81, 1):
    y = 80 * ((80 - x) ** 0.3) - 100
    ostrov.goto(x, y)
for x in range(30, -8, -1):
    y = 50 * ((30 - x) ** 0.5) - 100
    ostrov.goto(x, y)
ostrov.end_fill()
ostrov.pu()
ostrov.goto(-40, 138)
ostrov.pd()
ostrov.color(c5)
ostrov.begin_fill()
for x in range(-40, 20, 1):
    y = 0.002 * ((x + 8) ** 3) + 206
    ostrov.goto(x, y)
for x in range(20, -40, -1):
    y = 2.05 * x + 221
    ostrov.goto(x, y)
ostrov.end_fill()
ostrov.pu()
ostrov.goto(-52, 258)
ostrov.pd()
ostrov.begin_fill()
for x in range(-52, -8, 1):
    y = -0.0195 * ((x + 60) ** 2) + 260
    ostrov.goto(x, y)
for x in range(-8, -52, -1):
    y = 0.02 * (x ** 2) + 205
    ostrov.goto(x, y)
ostrov.end_fill()
done()

# gold
# cornflowerblue
# goldenrod
# sienna
# green
