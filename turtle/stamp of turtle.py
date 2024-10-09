import turtle
t=turtle.Turtle()
turtle.Screen().bgcolor("black")
t.pencolor("red")
t.pensize(2)
for i in range(6):
    x=t.stamp()
    t.fd(100)
    t.lt(60)
    x=t.stamp()
    t.clearstamp(x)
    
turtle.Screen().exitonclick()