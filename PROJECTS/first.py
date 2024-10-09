import turtle
turtle.bgcolor('black')
t= turtle.Turtle()
c=['red','darkred']
for n in range(400):
    t.forward (n+1)
    t.right(89)
    t.pencolor(c[n%2])
    turtle.done()