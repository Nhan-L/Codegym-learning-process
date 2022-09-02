import turtle
import math
n=turtle.Turtle()
n.speed(0)
vitridau = [0,0]
khoangcach = int(input('Nhập vào khoảng cách ban đầu: '))
distance = 0.1
angle = 15
i = 0
while True:
    n.fd(distance + i)
    n.left(angle + 15)
    i = i + 1
    if i > khoangcach:
        break
    