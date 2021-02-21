import numpy


a = '5, 5, 6, 1, 8'
a = a.replace(',', '')
a = a.split()
for i in range(len(a)):
    a[i] = float(a[i])
print(a)

