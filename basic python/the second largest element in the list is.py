print("enter the number of element in list ")
n=int (input())
i=0
num=[]
while i<n:
    print("enter the list value")
    num1=int (input ())
    num.append(num1)
    i=i+1
    
    
print("the original list is :",end=" ")
for i in range(n):
    print(num[i],end=" ")
if(num[0]>num[1]):
        m,m2=num[0],num[1]
else:
        m,m2=num[1],num[2] 
        
for x in num[2:] :
    if x>m2:
        if x>m:
            m2,m=m,x
        else:
            m2=x

print()
print("the second largest element in the list is : ",m2)                            