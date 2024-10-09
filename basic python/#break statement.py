#break statement
#enter number to sum negative number ends list
entry =0
sum=0
print("enter number to sum negative number ends list ")
while True:
    entry =eval(input())
    if entry <0 :
        break
    sum=sum +entry
    
print ("sum=",sum)    
        