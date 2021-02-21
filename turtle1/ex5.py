import turtle as t


def rect(a):
    for i in range(4):
        t.forward(a)
        t.left(90)


t.shape('turtle')
x = 30
y = 30
a = 5
for i in range(10):
    t.penup()
    t.goto(x, y)
    t.pendown()
    rect(a)
    x -= 5
    y -= 5
    a += 10

