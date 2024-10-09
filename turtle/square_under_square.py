import turtle
t=turtle.Turtle()
turtle.Screen().bgcolor("black")


t.penup()
t.goto(200,200)
t.pendown()
t.pencolor("red")
t.fillcolor("lightblue")
t.begin_fill()
t.goto(-200,200)
t.goto(-200,-200)
t.goto(200,-200)
t.goto(200,200)
t.end_fill()

#draw small square
txy=[(150,150,"navy"),(-25,150,"olive"),(-25,-25,"maroon"),(150,-25,"red")]

for xyc in txy:
    x,y,c=xyc
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    t.goto(x-125,y)
    t.goto(x-125,y-125)
    t.goto(x,y-125)
    t.goto(x,y)
    t.end_fill()

turtle.Screen().exitonclick()
