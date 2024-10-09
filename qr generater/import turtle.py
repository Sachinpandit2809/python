import turtle 
import colorsys
s=turtle.getscreen()
s.title("sachin pandit")
turtle.hideturtle()
turtle.Screen().bgcolor("black")
t=turtle.Turtle()
t.speed(0)
r=1
g=0.5
b=0.4
t.fillcolor("green")
t.begin_fill()
for i in range(75):
    c=colorsys.hsv_to_rgb(r,g,b)

    t.pensize(2)
    t.pencolor(c)
    
    #draw any close shape diagram
    t.circle(150)
    
    # g+=0.03
    # b-=0.03
    t.left(5)
    
t.end_fill()
turtle.Screen().exitonclick()