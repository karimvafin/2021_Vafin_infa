import turtle as t


def star(n):
    if n % 4 == 0:
        x = 360
    elif n % 2 != 0:
        x = 180
    else:
        for i in range(n):
            t.forward(50)
            t.right(180 - 360/n)
            t.forward(50)
            t.left(360/n)
        return
    for i in range(n):
        t.forward(150)
        t.right(180 - x/n)


t.shape('turtle')
star(3)
input()

