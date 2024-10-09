import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()
turtle.Screen().bgcolor("black")
t1.pencolor("red")
t2.pencolor("blue")
t1.pensize(2)
t2.pensize(2)

t1.fd(100)
t1.lt(90)
t1.fd(100)

t2.left(180)
t2.fd(100)
t2.rt(90) 
t2.fd(100)

t1.clear()
t2.reset()
turtle.Screen().exitonclick()