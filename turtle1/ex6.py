import turtle as t

n = 12
N = 360/n

t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.stamp()
    t.back(100)
    t.left(N)
