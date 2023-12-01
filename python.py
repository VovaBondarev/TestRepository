from turtle import *

col1 = input()
col2 = input()
size = int(input())
flower = Turtle()
flower.color(col1)
flower.pu()
flower.goto(-60, 100)
flower.pd()
flower.begin_fill()
for x in range(-60, 60):
    y = -0.0278 * x ** 2 + 200
    flower.goto(x, y)
for x in range(60, 29, -1):
    y = -0.045 * (x - 45) ** 2 + 110
    flower.goto(x, y)
for x in range(30, -1, -1):
    y = -0.045 * (x - 15) ** 2 + 110
    flower.goto(x, y)
for x in range(0, -31, -1):
    y = -0.045 * (x + 15) ** 2 + 110
    flower.goto(x, y)
for x in range(-30, -61, -1):
    y = -0.045 * (x + 45) ** 2 + 110
    flower.goto(x, y)
flower.end_fill()
flower.color(col2)
flower.pensize(size)
flower.pu()
flower.goto(0, 200)
flower.pd()
for x in range(0, 200):
    y = -0.025 * x ** 2 + 3 * x + 200
    flower.goto(x, y)
done()

# deeppink
# forestgreen
# 4
