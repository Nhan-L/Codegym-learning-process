from cmath import sqrt
import math
import turtle
turtle.bgcolor("deep sky blue")
n = turtle.Turtle()
n.speed(10)

#Sun
n.penup()
n.goto(180,130)
n.pendown()

n.fillcolor("yellow")
n.begin_fill()
n.circle(40)
n.end_fill()

n.rt(90)
n.fd(40)

n.penup()
n.goto(180,210)
n.pendown()

n.rt(180)
n.fd(40)

n.penup()
n.goto(220,170)
n.pendown()

n.rt(90)
n.fd(40)

n.penup()
n.goto(140,170)
n.pendown()

n.rt(180)
n.fd(40)

n.penup()
n.goto(146,194)
n.pendown()

n.rt(45)
n.fd(30)

n.penup()
n.goto(146,146)
n.pendown()

n.lt(90)
n.fd(30)

n.penup()
n.goto(214,146)
n.pendown()

n.lt(90)
n.fd(30)

n.penup()
n.goto(214,194)
n.pendown()

n.lt(90)
n.fd(30)

#tree

n.penup()
n.home()
n.pendown()

n.penup()
n.goto(200,-200)
n.pendown()

#goc cay

n.fillcolor("brown")
n.begin_fill()
n.fd(30)
n.lt(90)
n.fd(50)
n.lt(90)
n.fd(30)
n.lt(90)
n.fd(50)
n.end_fill()

#3 tam giac cay

n.penup()
n.goto(130,-150)
n.pendown()

n.fillcolor("pale green")
n.begin_fill()
n.lt(90)
n.fd(170)
n.lt(135)
n.fd(65 / math.cos(45))
n.lt(90)
n.fd(65 / math.cos(45))
n.end_fill()

n.penup()
n.home()
n.pendown()

n.penup()
n.goto(140,-62)
n.pendown()

n.fillcolor("pale green")
n.begin_fill()
n.fd(150)
n.lt(135)
n.fd(55 / math.cos(45))
n.lt(90)
n.fd(55 / math.cos(45))
n.end_fill()

n.penup()
n.home()
n.pendown()

n.penup()
n.goto(165,12)
n.pendown()

n.fillcolor("pale green")
n.begin_fill()
n.fd(100)
n.lt(135)
n.fd(39 / math.cos(45))
n.lt(90)
n.fd(39 / math.cos(45))
n.end_fill()

n.penup()
n.home()
n.pendown()

#ve ngoi nha

n.penup()
n.goto(-300,-150)
n.pendown()

#hinh vuong nha

n.fillcolor("blue")
n.begin_fill()
n.fd(100)
n.lt(90)
n.fd(120)
n.lt(90)
n.fd(100)
n.lt(90)
n.fd(120)
n.end_fill()

n.penup()
n.goto(-270,-150)
n.pendown()

n.fillcolor("pale green")
n.begin_fill()
n.lt(90)
n.fd(40)
n.lt(90)
n.fd(60)
n.lt(90)
n.fd(40)
n.lt(90)
n.fd(60)
n.end_fill()

n.penup()
n.goto(-300,-30)
n.pendown()

n.fillcolor("pink")
n.begin_fill()
n.lt(150)
n.fd(100)
n.rt(120)
n.fd(100)
n.end_fill()

n.fillcolor("yellow")
n.begin_fill()
n.lt(90)
n.fd(100)
n.rt(120)
n.fd(120)
n.rt(60)
n.fd(100)
n.rt(120)
n.end_fill()

n.fillcolor("orange")
n.begin_fill()
n.fd(120)
n.rt(60)
n.fd(100)
n.lt(90)
n.fd(100)
n.lt(90)
n.fd(100)
n.lt(90)
n.fd(100)
n.end_fill()

n.fillcolor("brown")
n.begin_fill()
n.lt(90)
n.penup()
n.goto(-160,-50)
n.pendown()
n.fd(30)
n.rt(120)
n.fd(40)
n.rt(60)
n.fd(30)
n.rt(120)
n.fd(40)
n.end_fill()

turtle.done