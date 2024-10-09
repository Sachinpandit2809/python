import turtle
t=turtle.Turtle()
turtle.title("sachinpandit")
turtle.Screen().bgcolor("black")
turtle.colormode(255)
t.pencolor("red")
t.pensize(2)
x=206


#upper saffron
t.begin_fill()
t.fillcolor((255,140,0))
t.pencolor((255,140,0))
t.penup()
t.goto(624,104)
t.pendown()
t.goto(624,310)
t.goto(-624,310)
t.goto(-624,104)
t.goto(624,104)
t.end_fill()


#middle white
t.begin_fill()
t.fillcolor(("white"))
t.pencolor("white")
t.penup()
t.goto(624,-104)
t.pendown()
t.goto(624,310-x)
t.goto(-624,310-x)
t.goto(-624,104-x)
t.goto(624,104-x)
t.end_fill()

#down green
t.begin_fill()
t.fillcolor((34,139,34))
t.pencolor((34,139,34))
t.penup()
t.goto(624,-104-x)
t.pendown()
t.goto(624,310-2*x)
t.goto(-624,310-2*x)
t.goto(-624,104-2*x)
t.goto(624,104-2*x)
t.end_fill()
#chakra

t.penup()
t.goto(0,-x/2)
t.pensize(4)
t.pencolor("blue")
t.pendown()
t.circle(103)
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(1)
t.pencolor("blue")
t.fillcolor("blue")
for i in range(1,25):
    t.begin_fill()
    t.fd(103)
    t.rt(90)
    t.fd(14)
    t.goto(0,0)
    t.left(165)
    t.end_fill()
    



turtle.exitonclick()
