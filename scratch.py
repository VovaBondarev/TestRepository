from turtle import *
from math import cos, exp

col = Turtle()
color1 = input()
A0 = int(input())
omega = float(input())
col.pu()
col.goto(-350, A0)
col.color(color1)
t = 1
col.pd()
for k in range(-350, 351, 1):
    a = A0 * exp(-0.005 * t)
    y = a * cos(omega * k)
    col.goto(k, y)
    t += 1
col.hideturtle()
done()

# deeppink
# 200
# 0.072
