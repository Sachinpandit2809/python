#

sum =0
n= int (input ("how many terms :"))
for a in range(2,n+2):
    term =0
    for b in range(1,a):
        term=term+b
    print("term",a-1,':',term)    
    sum = sum+term
print("sum of ",n,"term is :",sum )    