import turtle as t


def circle(a):
    for i in range(180):
        t.forward(a)
        t.left(2)
    for i in range(180):
        t.forward(a)
        t.right(2)


t.right(90)
t.shape('turtle')
a = 1
for e in range(1, 5):
    circle(a)
    a += 0.2
