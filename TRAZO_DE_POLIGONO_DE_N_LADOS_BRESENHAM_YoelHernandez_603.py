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
    
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    p= (2 * dy) - dx

    t.color("white")
    t.setx(dx)
    t.sety(dy)
    t.color("black")

    t.pensize("5")
    n=int(input("INDICA EL NUMERO DE LADOS DEL POLIGONO: "))
    ang=180-(((n-2)/n)*180)#CALCULAMOS EL ANGULO DE GIRO
    for i in range(n):
        t.left(ang)
        x1=x1+1
        if p < 0:
            p = p + (2 * dy)
        else:
            p = p + (2 * dy) - (2 * dx)
            y1=y1+1
        print(x1, ',', y1)
        t.fd(p)

if __name__== '__main__':
    main()