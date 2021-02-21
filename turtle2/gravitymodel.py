import turtle as t
import math


t.speed(0)
t.shape('turtle')
x = 0
y = 0
alpha = 60
t.left(alpha)
V = 50
ay = -5
k = -0.05
Vx = V*math.cos(3.14/3)
Vy = V*math.sin(3.14/3)
dt = 0.1
for i in range(10000):
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    ax = k * Vx
    Vx += ax*dt
    t.goto(x, y)
    if y < 0:
        y = 0
        Vy = - Vy * 0.7
        Vx = Vx*0.7
