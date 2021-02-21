import turtle as t


def circle():
    for i in range(180):
        t.forward(2)
        t.left(2)


t.shape('turtle')
circle()
t.left(180)
circle()
t.left(45)
circle()
t.left(180)
circle()
t.right(90)
circle()
t.left(180)
circle()
input()
