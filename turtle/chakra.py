import turtle
turtle.Screen().bgcolor("black")
t=turtle.Turtle()
turtle.hideturtle()
t.pensize(2)
t.pencolor("blue")
for i in range(20):
    t.fd(100)
    t.left(70)
    t.fd(20)
    t.left(110)
    # t.fd(100)
    t.goto(0,0)
    t.right(160)
    # t.fd(100)
    # t.hideturtle()






turtle.Screen().exitonclick()
