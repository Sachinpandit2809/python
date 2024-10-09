#write a python program to enter time in minute and calcute hour and remaining minutes
time = int (input("enter time "))
hour=int(time/60)
min=time%60
print("hour=",hour)
print("min=",min)