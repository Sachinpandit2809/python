from turtle import *
import colorsys
tracer(2)
bgcolor("black")
pensize(1)
h=0.3
for i in range(500):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    rt(20)
    for j in range(5):
        fd(i)
        rt(90)
        fd(i)
        rt(90)
        fd(i)
        rt(90)
        fd(i)
        rt(90)
        
done()        
        
        
     