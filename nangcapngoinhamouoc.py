#Luyện tập các lệnh vẽ, tùy chỉnh bút vẽ trong thư viên turtle
#Khuyến khích học viên thêm ý tưởng, chi tiết, tô màu cho ngôi và khung cảnh cho đẹp hơn.
from cmath import sqrt
import math
import turtle
n = turtle.Turtle()
n.speed(10)

#ngoinha
#ngoinha_hinhvuong
n.penup()
n.goto(-100,0)
n.pendown()

n.fillcolor("pale green")
n.pensize(3)
n.pencolor("blue")
n.begin_fill()
n.fd(200)
n.lt(90)
n.fd(100)
n.lt(90)
n.fd(200)
n.lt(90)
n.fd(100)
n.end_fill()

#ngoinha_Caicua

n.lt(90)
n.fd(75)
n.lt(90)
n.fd(60)
n.rt(90)
n.fd(50)
n.rt(90)
n.fd(60)

n.lt(180)
n.penup()
n.goto(-100,0)
n.pendown()

#ngoinha_mainha

n.fillcolor("yellow")
n.fd(100)
n.begin_fill()
n.rt(60)
n.fd(100)
n.rt(60)
n.fd(100)
n.end_fill()

#ngoinha_ongkhoi
n.fillcolor("green")
n.bk(40)
n.begin_fill()
n.lt(120)
n.fd(30)
n.lt(90)
n.fd(20)
n.lt(90)
n.fd(18)
n.end_fill()

n.penup()
n.bk(40)
n.pendown()
n.bk(20)
n.penup()
n.fd(40)
n.pendown()

n.penup()
n.lt(90)
n.fd(20)
n.lt(90)
n.fd(20)
n.pendown()
n.fd(30)

#Caynho
n.pensize(1)
n.penup()
n.goto(-250,-70)
n.pendown()

#Caynho_goccay

n.fillcolor("gray")
n.begin_fill()
n.rt(10)
n.fd(50)
n.rt(80)
n.fd(20)
n.rt(80)
n.fd(50)
n.rt(100)
n.fd(37)
n.end_fill()

#Caynho_3tamgiaccay

n.penup()
n.goto(-290,-20)
n.pendown()

n.fillcolor("olive drab")
n.begin_fill()
n.bk(117)
n.rt(30)
n.fd(39 * math.sqrt(3))
n.lt(60)
n.fd(39 * math.sqrt(3))
n.bk(39 * math.sqrt(3))
n.end_fill()

n.fillcolor("yellow green")
n.begin_fill()
n.rt(30)
n.fd(50)
n.bk(100)
n.rt(30)
n.fd(100 / math.sqrt(3))
n.lt(60)
n.fd(100 / math.sqrt(3))
n.end_fill()

n.bk(100 / math.sqrt(3))

n.fillcolor("dark sea green")
n.begin_fill()
n.rt(30)
n.fd(30)
n.penup()
n.bk(30)
n.pendown()
n.bk(30)
n.rt(30)
n.fd(20 * math.sqrt(3))
n.lt(60)
n.fd(20 * math.sqrt(3))
n.end_fill()
n.bk(20 * math.sqrt(3))

n.lt(60)
n.lt(180)

#cayto1

n.penup()
n.goto(220,-70)
n.pendown()

#Cayto_goccay

n.fillcolor("gray")
n.begin_fill()
n.rt(10)
n.fd(50)
n.rt(80)
n.fd(20)
n.rt(80)
n.fd(50)
n.rt(100)
n.fd(37)
n.end_fill()

#Cayto_3tamgiaccay

n.penup()
n.goto(180,-20)
n.pendown()

n.fillcolor("olive drab")
n.begin_fill()
n.bk(117)
n.rt(30)
n.fd(39 * math.sqrt(3))
n.lt(60)
n.fd(39 * math.sqrt(3))
n.bk(39 * math.sqrt(3))
n.end_fill()

n.fillcolor("yellow green")
n.begin_fill()
n.rt(30)
n.fd(50)
n.bk(100)
n.rt(30)
n.fd(100 / math.sqrt(3))
n.lt(60)
n.fd(100 / math.sqrt(3))
n.end_fill()

n.bk(100 / math.sqrt(3))

n.fillcolor("dark sea green")
n.begin_fill()
n.rt(30)
n.fd(30)
n.penup()
n.bk(30)
n.pendown()
n.bk(30)
n.rt(30)
n.fd(20 * math.sqrt(3))
n.lt(60)
n.fd(20 * math.sqrt(3))
n.end_fill()
n.bk(20 * math.sqrt(3))

n.lt(60)
n.lt(180)

#cayto2

n.penup()
n.goto(120,-170)
n.pendown()

#Cayto_goccay

n.fillcolor("gray")
n.begin_fill()
n.rt(10)
n.fd(50)
n.rt(80)
n.fd(20)
n.rt(80)
n.fd(50)
n.rt(100)
n.fd(37)
n.end_fill()

#Cayto_3tamgiaccay

n.penup()
n.goto(80,-120)
n.pendown()

n.fillcolor("olive drab")
n.begin_fill()
n.bk(117)
n.rt(30)
n.fd(39 * math.sqrt(3))
n.lt(60)
n.fd(39 * math.sqrt(3))
n.bk(39 * math.sqrt(3))
n.end_fill()

n.fillcolor("yellow green")
n.begin_fill()
n.rt(30)
n.fd(50)
n.bk(100)
n.rt(30)
n.fd(100 / math.sqrt(3))
n.lt(60)
n.fd(100 / math.sqrt(3))
n.end_fill()

n.bk(100 / math.sqrt(3))

n.fillcolor("dark sea green")
n.begin_fill()
n.rt(30)
n.fd(30)
n.penup()
n.bk(30)
n.pendown()
n.bk(30)
n.rt(30)
n.fd(20 * math.sqrt(3))
n.lt(60)
n.fd(20 * math.sqrt(3))
n.end_fill()
n.bk(20 * math.sqrt(3))

n.lt(60)
n.lt(180)

#cayto3

n.penup()
n.goto(20,-170)
n.pendown()

#Cayto_goccay

n.fillcolor("gray")
n.begin_fill()
n.rt(10)
n.fd(50)
n.rt(80)
n.fd(20)
n.rt(80)
n.fd(50)
n.rt(100)
n.fd(37)
n.end_fill()

#Cayto_3tamgiaccay

n.penup()
n.goto(-20,-120)
n.pendown()

n.fillcolor("olive drab")
n.begin_fill()
n.bk(117)
n.rt(30)
n.fd(39 * math.sqrt(3))
n.lt(60)
n.fd(39 * math.sqrt(3))
n.bk(39 * math.sqrt(3))
n.end_fill()

n.fillcolor("yellow green")
n.begin_fill()
n.rt(30)
n.fd(50)
n.bk(100)
n.rt(30)
n.fd(100 / math.sqrt(3))
n.lt(60)
n.fd(100 / math.sqrt(3))
n.end_fill()

n.bk(100 / math.sqrt(3))

n.fillcolor("dark sea green")
n.begin_fill()
n.rt(30)
n.fd(30)
n.penup()
n.bk(30)
n.pendown()
n.bk(30)
n.rt(30)
n.fd(20 * math.sqrt(3))
n.lt(60)
n.fd(20 * math.sqrt(3))
n.end_fill()
n.bk(20 * math.sqrt(3))

n.lt(60)
n.lt(180)

#cayto4

n.penup()
n.goto(-80,-170)
n.pendown()

#Cayto_goccay

n.fillcolor("gray")
n.begin_fill()
n.rt(10)
n.fd(50)
n.rt(80)
n.fd(20)
n.rt(80)
n.fd(50)
n.rt(100)
n.fd(37)
n.end_fill()

#Cayto_3tamgiaccay

n.penup()
n.goto(-120,-120)
n.pendown()

n.fillcolor("olive drab")
n.begin_fill()
n.bk(117)
n.rt(30)
n.fd(39 * math.sqrt(3))
n.lt(60)
n.fd(39 * math.sqrt(3))
n.bk(39 * math.sqrt(3))
n.end_fill()

n.fillcolor("yellow green")
n.begin_fill()
n.rt(30)
n.fd(50)
n.bk(100)
n.rt(30)
n.fd(100 / math.sqrt(3))
n.lt(60)
n.fd(100 / math.sqrt(3))
n.end_fill()

n.bk(100 / math.sqrt(3))

n.fillcolor("dark sea green")
n.begin_fill()
n.rt(30)
n.fd(30)
n.penup()
n.bk(30)
n.pendown()
n.bk(30)
n.rt(30)
n.fd(20 * math.sqrt(3))
n.lt(60)
n.fd(20 * math.sqrt(3))
n.end_fill()
n.bk(20 * math.sqrt(3))

n.lt(60)
n.lt(180)

#cayto5

n.penup()
n.goto(-180,-170)
n.pendown()

#Cayto_goccay

n.fillcolor("gray")
n.begin_fill()
n.rt(10)
n.fd(50)
n.rt(80)
n.fd(20)
n.rt(80)
n.fd(50)
n.rt(100)
n.fd(37)
n.end_fill()

#Cayto_3tamgiaccay

n.penup()
n.goto(-220,-120)
n.pendown()

n.fillcolor("olive drab")
n.begin_fill()
n.bk(117)
n.rt(30)
n.fd(39 * math.sqrt(3))
n.lt(60)
n.fd(39 * math.sqrt(3))
n.bk(39 * math.sqrt(3))
n.end_fill()

n.fillcolor("yellow green")
n.begin_fill()
n.rt(30)
n.fd(50)
n.bk(100)
n.rt(30)
n.fd(100 / math.sqrt(3))
n.lt(60)
n.fd(100 / math.sqrt(3))
n.end_fill()

n.bk(100 / math.sqrt(3))

n.fillcolor("dark sea green")
n.begin_fill()
n.rt(30)
n.fd(30)
n.penup()
n.bk(30)
n.pendown()
n.bk(30)
n.rt(30)
n.fd(20 * math.sqrt(3))
n.lt(60)
n.fd(20 * math.sqrt(3))
n.end_fill()
n.bk(20 * math.sqrt(3))

n.lt(60)
n.lt(180)

turtle.done()