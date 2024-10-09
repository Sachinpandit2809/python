'''Sample dates: (2022, 10, 2), (2022, 10, 23) 
Expected output: 21 days 
''' 
import datetime
date_1=datetime.date(2022, 10, 2)
date_2=datetime.date(2022, 10, 23) 
diffrence= date_2-date_1
print("current difference of days are =",diffrence)