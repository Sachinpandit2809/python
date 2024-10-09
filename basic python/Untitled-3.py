def printstar(n):
    printer=1
    for i in range(1,n+1):
        # print("the value of i=",i)
        for j in range(1,i+1):
            print(printer,end=" ")
            printer+=1
        print()    
printstar(5)            
            