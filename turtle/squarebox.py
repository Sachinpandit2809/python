import turtle
s=turtle.getscreen()
t=turtle.Turtle()
turtle.Screen().bgcolor("black")

t.pensize(2)
t.pencolor("white")

t.penup()
t.goto(200,200)
t.pendown()
t.goto(-200,200)
t.goto(-200,-200)
t.goto(200,-200)
t.goto(200,200)


t.begin_fill()
#ist quadrant square
t.fillcolor("white")

t.penup()
t.goto(25,25)
t.pendown()
t.pencolor("red")
t.goto(175,25)
t.goto(175,175)
t.goto(25,175)
t.goto(25,25)
t.penup()

#2nd quadrant square

t.goto(-25,25)
t.pendown()
t.pencolor("blue")
t.goto(-175,25)
t.goto(-175,175)
t.goto(-25,175)
t.goto(-25,25)
t.penup()

#3rd quadrant square

t.goto(25,-25)
t.pendown()
t.pencolor("yellow")
t.goto(175,-25)
t.goto(175,-175)
t.goto(25,-175)
t.goto(25,-25)
t.penup()

#4rt quadrant square

t.goto(-25,-25)
t.pendown()
t.pencolor("green")
t.goto(-175,-25)
t.goto(-175,-175)
t.goto(-25,-175)
t.goto(-25,-25)
t.end_fill()




turtle.Screen().exitonclick()