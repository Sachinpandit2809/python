import pyautogui as pg 
import time 
time.sleep(10)
i=1
j=1
k=0
while j<=3:
    while i<=10:
     k=k+1
    if i==1:
         pg.write (str(k)+" "+" s1 hii vidhi ")
    if i==2:
         pg.write (str(k)+" "+" s2 hii vidhi ")
    if i==3:
         pg.write (str(k)+" "+" s3 hii vidhi ")
    if i==4:
         pg.write (str(k)+" "+" s4 hii vidhi ") 
    if i==5:
         pg.write (str(k)+" "+" s5 hii vidhi ")
    if i==6:
         pg.write (str(k)+" "+" s6 hii vidhi ")
    if i==7:
         pg.write (str(k)+" "+" s7 hii vidhi ")
    if i==8:
         pg.write (str(k)+" "+" s8 hii vidhi ")
    if i==9:
         pg.write (str(k)+" "+" s9 hii vidhi ")
    if i==10:
         pg.write (str(k)+" "+" s9 hii vidhi ")  
    i=i+1
    pg.press("enter")
   