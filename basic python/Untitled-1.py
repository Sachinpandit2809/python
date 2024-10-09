u=float(input("enter the unit"))
if (u<=150):
    print("electric bill=",u*1.25)
elif(u>150 and u<=250):
    print("electric bill=",(150*1.25  +(u-150)*1.50))   
elif(u>250 and u<=350):
    print("electric bill=",(150*1.25 + 100*1.50 + (u-250)*1.75)) 
else:
    print("electric bill=",150*1.25 + 100*1.50 + 100*1.75 + (u-350)* 2)
             
