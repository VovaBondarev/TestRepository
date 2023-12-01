import turtle

a = turtle.Turtle()
color = input()
r1 = int(input())
r2 = int(input())
n = int(input())
p = 3.1416
a.color(color)
for i in range(n):
    a.circle(r2)
    a.lt(360 / n)
    a.fd(2 * p * r1 / n)
a.hideturtle()
turtle.done()

# magenta
# 20
# 150
# 36
