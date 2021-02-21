import turtle as t
import math as m


def figure(n):
    alpha = 180 - (n - 2) * 180 / n
    r = 10*(n+1) / (2*m.sin(2*3.1415/(2*(n+1)))) - 10*n / (2*m.sin(2*3.1415/(2*n)))
    t.left((180 - alpha) / 2)
    for i in range(n):
        t.left(alpha)
        t.forward(n*10)
    t.right((180 - alpha) / 2)
    t.penup()
    t.forward(r)
    t.pendown()


t.shape('turtle')
for r in range(3, 10):
    figure(r)

