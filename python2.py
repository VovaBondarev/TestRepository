from turtle import *
from math import sin

ostrov = Turtle()
ostrov.pu()
ostrov.goto(-150, 0)
ostrov.pd()
ostrov.color("gold")
ostrov.begin_fill()
for x in range(-150, 150, 5):
    y = (150 ** 2 - x ** 2) ** 0.5
    ostrov.goto(x, y)
ostrov.end_fill()
ostrov.pu()
ostrov.goto(-350, -300)
ostrov.pd()
ostrov.color("cornflowerblue")
ostrov.begin_fill()
for x in range(-350, 350, 5):
    y = 10 * sin(0.144 * x) + 10
    ostrov.goto(x, y)
ostrov.goto(350, -300)
ostrov.end_fill()
ostrov.pu()
ostrov.goto(-100, -105)
ostrov.pd()
ostrov.color("goldenrod")
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
ostrov.color("sienna")
ostrov.begin_fill()
for x in range(-8, 80, 1):
    y = 80 * ((80 - x) ** 0.3) - 100
    ostrov.goto(x, y)
ostrov.pu()
ostrov.goto(-8, 206)
ostrov.pd()
for x in range(30, -8, -1):
    y = 50 * ((30 - x) ** 0.5) - 100
    ostrov.goto(x, y)
ostrov.end_fill()
done()
