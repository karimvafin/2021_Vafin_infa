import turtle as t
import random as r


t.shape('turtle')
for i in range(10000):
    t.forward(r.randint(5, 40))
    t.left(r.randint(0, 360))
