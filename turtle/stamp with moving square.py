import turtle
t=turtle.Turtle()
turtle.Screen().bgcolor("black")
t.pencolor("red")
t.pensize(2)
t.penup()
t.goto(200,200)
# t.pendown()
t.shape("square")
t.fillcolor("yellow")
t.shapesize(5,5,3)
t.stamp()
t.goto(-200,200)
t.stamp()
t.goto(-200,-200)
t.stamp()
t.goto(200,-200)
t.stamp()
t.goto(200,200)
    
turtle.Screen().exitonclick()