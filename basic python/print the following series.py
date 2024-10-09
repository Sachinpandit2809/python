# print the following series 
# x^0 + x^1 + x^2 + x^3......x^4

x=float(input("enter the value of x"))
n=int (input("enter the last number of power"))
sum=0
for i in range (n+1):
    sum=sum+x**i
print("sum of first ",n,"terms",sum)    