# Vẽ đa giác
import turtle
n = turtle.Turtle()
dodaicanh = int(input("Nhập độ dài canh: "))
socanh = int(input ("Nhập số cạnh của đa giác: "))
count = 1
while count <= socanh:
    count = count + 1
    n.fd(dodaicanh)
    n.lt(360/socanh)
turtle.done    



