from turtle import Turtle
import subprocess

def main():
    subprocess.call(["cmd.exe","/C","cls"])
    t=Turtle()
    t.hideturtle()
    x1= int(input('INGRESA X1:\n'))
    y1= int(input('INGRESA Y1:\n'))
    x2= int(input('INGRESA X2:\n'))
    y2= int(input('INGRESA Y2:\n'))
    
    x=0
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    if dx > dy:
        steps= dx
    else:
        steps= dy

    incx= dx/steps
    incy= dy/steps

    t.color("white")
    t.setx(dx)
    t.sety(dy)
    t.color("black")

    t.pensize("5")
    n=int(input("INDICA EL NUMERO DE LADOS DEL POLIGONO: "))
    ang=180-(((n-2)/n)*180)#CALCULAMOS EL ANGULO DE GIRO
    for i in range(n):
        t.left(ang)
        x1=x1+incx
        y1=y1+incy
        print(x1, ',', y1)
        t.fd(steps)

if __name__== '__main__':
    main()

    