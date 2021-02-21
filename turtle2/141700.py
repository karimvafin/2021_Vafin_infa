import turtle as t
import math


def number(a):
    t.penup()
    for i in range(2):
        t.right(a[2*i])
        t.forward(a[2*i+1])
    t.pendown()
    for i in range(2, len(a)//2):
        t.right(a[2*i])
        t.forward(a[2*i+1])
    move()


def move():
    t.penup()
    t.forward(30)
    t.pendown()


a1 = (90, 50, -90, 0, -45, 50 * math.sqrt(2), 135, 100, 180, 100, 90, 0)
a4 = (0, 0, 0, 0, 90, 50, -90, 50, 90, 50, 180, 100, 90, 0)
a7 = (0, 0, 0, 0, 0, 50, 135, math.sqrt(2) * 50, -45, 50, 180, 50, 45, math.sqrt(2) * 50, 45, 0)
a0 = (0, 0, 0, 0, 0, 50, 90, 100, 90, 50, 90, 100, 90, 50)
a3 = (0, 0, 0, 0, 0, 50, 135, 70.5, -135, 50, 135, 70.5, 180, 70.5, -135, 50, 135, 70.5, 45, 0)
t.speed(10)
t.shape('turtle')
t.penup()
t.goto(-200, 0)
t.pendown()
number(a1)
number(a4)
number(a1)
number(a7)
number(a0)
number(a0)
number(a3)


