from cmath import sqrt
import math
import turtle
turtle.bgcolor("deep sky blue")
n = turtle.Turtle()
n.speed(10)

#bien_mattroi
duongkinh_sun = 40
toadoX_sun = duongkinh_sun + 140
toadoY_sun = duongkinh_sun + 90
#bien_tree
day_goccay = 30
toadoX_tamgiaccay = 130
toadoY_tamgiaccay = -150
#bien_ngoinha
day_ngoinha = 100
toadoX_ngoinha = -300
toadoY_ngoinha = -150
gocquay_mainha = 60

#Sun
n.penup()
n.goto(toadoX_sun,toadoY_sun)
n.pendown()

n.fillcolor("yellow")
n.begin_fill()
n.circle(duongkinh_sun)
n.end_fill()

n.rt(90)
n.fd(duongkinh_sun)

n.penup()
n.goto(toadoX_sun,toadoY_sun +80)
n.pendown()

n.rt(180)
n.fd(duongkinh_sun)

n.penup()
n.goto(toadoX_sun + 40,toadoY_sun + 40)
n.pendown()

n.rt(90)
n.fd(duongkinh_sun)

n.penup()
n.goto(toadoX_sun - 40,toadoY_sun + 40)
n.pendown()

n.rt(180)
n.fd(duongkinh_sun)

n.penup()
n.goto(toadoX_sun - 34,toadoY_sun + 64)
n.pendown()

n.rt(45)
n.fd(duongkinh_sun-10)

n.penup()
n.goto(toadoX_sun - 34,toadoY_sun + 16)
n.pendown()

n.lt(90)
n.fd(duongkinh_sun-10)

n.penup()
n.goto(toadoX_sun + 34,toadoY_sun + 16)
n.pendown()

n.lt(90)
n.fd(duongkinh_sun-10)

n.penup()
n.goto(toadoX_sun + 34,toadoY_sun + 64)
n.pendown()

n.lt(90)
n.fd(duongkinh_sun-10)

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
n.fd(day_goccay)
n.lt(90)
n.fd(day_goccay+20)
n.lt(90)
n.fd(day_goccay)
n.lt(90)
n.fd(day_goccay+20)
n.end_fill()

#3 tam giac cay

n.penup()
n.goto(toadoX_tamgiaccay,toadoY_tamgiaccay)
n.pendown()

n.fillcolor("pale green")
n.begin_fill()
n.lt(90)
n.fd(toadoX_tamgiaccay+40)
n.lt(135)
n.fd(toadoX_tamgiaccay/2 / math.cos(45))
n.lt(90)
n.fd(toadoX_tamgiaccay/2 / math.cos(45))
n.end_fill()

n.penup()
n.home()
n.pendown()

n.penup()
n.goto(toadoX_tamgiaccay + 10,toadoY_tamgiaccay+88)
n.pendown()

n.fillcolor("pale green")
n.begin_fill()
n.fd(toadoX_tamgiaccay+20)
n.lt(135)
n.fd((toadoX_tamgiaccay-20)/2 / math.cos(45))
n.lt(90)
n.fd((toadoX_tamgiaccay-20)/2 / math.cos(45))
n.end_fill()

n.penup()
n.home()
n.pendown()

n.penup()
n.goto(toadoX_tamgiaccay + 35,toadoY_tamgiaccay+162)
n.pendown()

n.fillcolor("pale green")
n.begin_fill()
n.fd(toadoX_tamgiaccay-30)
n.lt(135)
n.fd((toadoX_tamgiaccay-52)/2 / math.cos(45))
n.lt(90)
n.fd((toadoX_tamgiaccay-52)/2 / math.cos(45))
n.end_fill()

n.penup()
n.home()
n.pendown()

#ve ngoi nha

n.penup()
n.goto(toadoX_ngoinha,toadoY_ngoinha)
n.pendown()

#hinh vuong nha

n.fillcolor("blue")
n.begin_fill()
n.fd(day_ngoinha)
n.lt(90)
n.fd(day_ngoinha+20)
n.lt(90)
n.fd(day_ngoinha)
n.lt(90)
n.fd(day_ngoinha+20)
n.end_fill()

n.penup()
n.goto(toadoX_ngoinha+30,toadoY_ngoinha)
n.pendown()

n.fillcolor("pale green")
n.begin_fill()
n.lt(90)
n.fd(day_ngoinha/2-10)
n.lt(90)
n.fd(day_ngoinha-40)
n.lt(90)
n.fd(day_ngoinha/2-10)
n.lt(90)
n.fd(day_ngoinha-40)
n.end_fill()

n.penup()
n.goto(toadoX_ngoinha,toadoY_ngoinha+120)
n.pendown()

n.fillcolor("pink")
n.begin_fill()
n.lt(gocquay_mainha+90)
n.fd(day_ngoinha)
n.rt(gocquay_mainha+60)
n.fd(day_ngoinha)
n.end_fill()

n.fillcolor("yellow")
n.begin_fill()
n.lt(gocquay_mainha+30)
n.fd(day_ngoinha)
n.rt(120)
n.fd(day_ngoinha+20)
n.rt(60)
n.fd(day_ngoinha)
n.rt(day_ngoinha+20)
n.end_fill()

n.fillcolor("orange")
n.begin_fill()
n.fd(day_ngoinha+20)
n.rt(gocquay_mainha)
n.fd(day_ngoinha)
n.lt(90)
n.fd(day_ngoinha)
n.lt(90)
n.fd(day_ngoinha)
n.lt(90)
n.fd(day_ngoinha)
n.end_fill()

n.fillcolor("brown")
n.begin_fill()
n.lt(90)
n.penup()
n.goto(toadoX_ngoinha+140,toadoY_ngoinha+100)
n.pendown()
n.fd(day_ngoinha-70)
n.rt(120)
n.fd(day_ngoinha-60)
n.rt(60)
n.fd(day_ngoinha-70)
n.rt(120)
n.fd(day_ngoinha-60)
n.end_fill()

turtle.done