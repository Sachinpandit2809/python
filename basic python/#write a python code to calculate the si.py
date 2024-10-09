#write a python code to calculate the simple interest

p=int(input("enter the principal amount  "))
r=float(input("enter the rate"))
t=int(input("enter the time "))
intrest=(p*r*t)/100
amount=p+intrest
print("the intrest is =",intrest)
print("amount=",amount)
