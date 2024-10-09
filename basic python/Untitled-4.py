def decimal_to_binary(decimal):
    mynumber=decimal
    power=0
    binary=0
    while(decimal>0):
        reminder=decimal%2
        binary=binary+ reminder* (pow(10,power))
        power=power+1
        decimal=decimal//2
    print("the binary value of",mynumber,"is = ",binary)
val=int (input("enter the binary value:- "))
decimal_to_binary(val)        