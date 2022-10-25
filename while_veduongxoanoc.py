#[Bài tập] Vẽ đường xoắn ốc
import math
import turtle
n = turtle.Turtle()
n.speed(10)
n.setpos(0,0)
distance = 1 
angle = 5
for i in range (0,120,1):
    n.forward(distance + i) 
    n.left(angle + 15)

