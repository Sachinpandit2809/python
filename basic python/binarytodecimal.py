def bintodecimal(binary):
    mynumber=binary
    decimal=0
    power=0
    while (binary>0):
        reminder=binary%10
        decimal=decimal+int(reminder*(2**power))
        power+=1
        binary//=10
        
    print("the decimal value of ",mynumber,"is = ",decimal)
    
val=int (input("enter the binary number"))
bintodecimal(val)         