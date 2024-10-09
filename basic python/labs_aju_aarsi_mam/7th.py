'''7.	Write a Python program that accepts an integer
(n) and computes the value of  n+nn+nnn'''
import math
n= int(input("enter integer for computes the value of  n+nn+nnn "))
sum=0
for i in range(1,4):
    sum += math.pow(n,i)
print("the value of  (n+nn+nnn) =",sum)    