import turtle as t


def circle(a):
    for i in range(90):
        t.forward(a)
        t.right(2)


t.penup()
t.goto(-200, 0)
t.pendown()
t.shape('turtle')
t.left(90)
for q in range(5):
    circle(3)
    circle(0.5)

