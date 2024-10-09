'''8.	Write a Python program to add two positive 
integers without using the '+' operator. '''
def fun(a,b):
    while (b!=0):
        carry=a&b
        a=a^b
        b=carry<<1
    return a
    
n1=5
n2=3
result=fun(n1,n2)
print("sum=",result)    