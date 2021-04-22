import math
a, b = input().split(" ")
c, d = input().split(" ")
x1 = float(a)
y1 = float(b)
x2 = float(c)
y2 = float(d)
distance = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
print("{:.4f}".format(distance))