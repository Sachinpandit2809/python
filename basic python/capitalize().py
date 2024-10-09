str1=input ("enter a string ")
print("original string :",str1)
str2=" "
x=str1.split()
for a in x:
    str2=str2+a.capitalize()+ " "
    
print(str2)    