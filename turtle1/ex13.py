import turtle as t


def circle(a):
    for i in range(180):
        t.forward(a)
        t.left(2)


def arc1(a, phi):
    for i in range(phi):
        t.forward(a)
        t.left(2)


def arc2(a, phi):
    for i in range(phi):
        t.forward(a)
        t.right(2)


def tp(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


t.shape('turtle')
tp(0, -60)
t.begin_fill()
circle(5)
t.color('Yellow')
t.end_fill()

t.color('Black')
tp(-60, 100)

t.begin_fill()
circle(1)
t.color('Red')
t.end_fill()

t.color('Black')
tp(-60, 120)

t.begin_fill()
circle(0.2)
t.end_fill()

t.color('Black')
tp(60, 100)

t.begin_fill()
circle(1)
t.color('Red')
t.end_fill()

t.color('Black')
tp(60, 120)

t.begin_fill()
circle(0.2)
t.end_fill()

tp(-77, 40)
t.begin_fill()
t.width(10)
t.color('Red')
t.forward(160)

t.right(90)
arc2(2.8, 90)
t.color('White')
t.end_fill()
tp(-100, -100)

tp(170, 10)
t.right(90)
t.begin_fill()
t.color('Black')
t.width(2)
t.forward(20)
t.right(90)
t.forward(120)
t.right(90)
t.forward(60)
t.right(90)

t.forward(20)
t.right(90)
t.forward(50)
t.back(50)
t.left(90)

t.forward(20)
t.right(90)
t.forward(50)
t.back(50)
t.left(90)

t.forward(20)
t.right(90)
t.forward(50)
t.back(50)
t.left(90)

t.forward(20)
t.right(90)
t.forward(50)
t.back(10)
t.left(90)
t.forward(40)
t.color('Yellow')
t.end_fill()

tp(-100, -100)

input()
