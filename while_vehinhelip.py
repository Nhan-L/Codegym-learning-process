                                        # hình thứ nhất

# import package - Nhập thư viên turtle
import turtle
 
# method to draw ellipse - phương pháp vẽ hình elipse
def draw(rad):
     
  # rad --> radius of arc - bán kính hình cung
  for i in range(2):
     
    # two arcs - hai hình cung
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)
 
# Main section - CHÍNH
# tilt the shape to negative 45 - Nghiên con trỏ về âm 45 độ
turtle.seth(-45)
 
# calling draw method - chu vi của elipse
draw(100) 

                                        # hình thứ hai

# import package and making object
import turtle
screen = turtle.Screen()
 
# method to draw ellipse
def draw(rad):
     
# rad --> radius for arc
    for i in range(2):
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)
 
# Main Section
# Set screen size
screen.setup(500,500)
 
# Set screen color
screen.bgcolor('black')
 
# Colors
col=['violet','blue','green','yellow',
     'orange','red']
 
# some integers
val=10
ind=0
 
# turtle speed
turtle.speed(100)
 
# loop for multiple ellipse
for i in range(36):
     
    # oriented the ellipse at angle = -val
    turtle.seth(-val)
     
    # color of ellipse
    turtle.color(col[ind])
     
    # to access different color
    if ind==5:
        ind=0
    else:
        ind+=1
     
    # calling method
    draw(80)
     
    # orientation change
    val+=10
 
# for hiding the turtle
turtle.hideturtle()