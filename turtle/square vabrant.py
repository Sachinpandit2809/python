import turtle
t=turtle.Turtle()
turtle.title("sachinpandit")
turtle.Screen().bgcolor("black")
turtle.colormode(255)
t.speed(0)
r=5
b=5
g=250
x=4
for i in range (254):
    
    t.pencolor((r,g,b))
    t.pensize(1)
    for i in range(1,5):
       t.fd(x)
       t.left(90)
    g=g-1
    b=b+1
    r=r+1
    x=x+1
    t.rt(5)


turtle.Screen().exitonclick()