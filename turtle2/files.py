import turtle as t


def number(a):
    t.penup()
    for i in range(2):
        t.right(a[2*i])
        t.forward(a[2*i+1])
    t.pendown()
    for i in range(2, len(a)//2):
        t.right(a[2*i])
        t.forward(a[2*i+1])
    move()


def move():
    t.penup()
    t.forward(30)
    t.pendown()


def unpack(b):
    b = b.replace(',', '')
    b = b.split()
    for i in range(len(b)):
        b[i] = float(b[i])


corteges = open('file.txt')
t.penup()
t.goto(-250, 0)
t.pendown()
a = corteges.readlines()
for i in range(len(a)):
    a[i] = a[i].replace(',', '')
    a[i] = a[i].split()
    for j in range(len(a[i])):
        a[i][j] = float(a[i][j])
for i in range(3, 10):
    number(a[i])


corteges.close()
