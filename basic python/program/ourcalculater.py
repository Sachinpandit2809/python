#our calculater
f=input("enter first number")
s=input("enter second number")
f=float(f)
s=float(s)
print("operation are:- + - * / %")
op=input("enter any operater for doing operation")

if op=="+":
    print(f+s)
elif op=="-":
    print(f-s)
elif op=="*":
    print(f*s)
elif op=="/":
    print(f/s)
elif op=="%":
    print(f%s)
    
else:
    print("invalid operation")