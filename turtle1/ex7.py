import turtle as t

t.shape('turtle')
f = 0.1
for i in range(360):
    t.forward(f)
    t.left(5)
    f += 0.01
