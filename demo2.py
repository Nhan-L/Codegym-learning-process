# Hinh tron dong tam
from turtle import clear, pencolor, penup
khoangcach = 20
chuvi1 = 50
chuvi2 = chuvi1 + khoangcach
chuvi3 = chuvi2 + khoangcach
import turtle
nhan_screen = turtle.Screen()            
nhan_screen = turtle.Turtle()  
nhan_screen.speed(5)

nhan_screen.circle(chuvi1)
nhan_screen.right(90)

nhan_screen.penup()
nhan_screen.goto(0,-20)
nhan_screen.pendown()

nhan_screen.left(90)
nhan_screen.circle(chuvi2)
nhan_screen.right(90)

nhan_screen.penup()
nhan_screen.goto(0,-40)
nhan_screen.pendown()

nhan_screen.left(90)
nhan_screen.circle(chuvi3)

turtle.done
