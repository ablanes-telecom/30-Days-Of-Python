# Day 16 - 30DaysOfPython Challenge
#Datetime
"""
import datetime
print(dir(datetime))#With dir or help built-in commands it is possible to know the available functions in a certain module. 

#Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now)                      # 2026-02-17 16:39:57.303342
day = now.day                   # 17 
month = now.month               #  2
year = now.year                 # 2026
hour = now.hour                 # 16
minute = now.minute             # 39
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 17/2/2026, 16:39

#Formatting Date Output Using strftime
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           # time: 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)        # time one: 06/28/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)        # time two: 28/06/2022, 18:21:40

#String to Time Using strptime
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)     # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2019-12-05 00:00:00

#Using date from datetime
from datetime import date
d = date(2020, 1, 1)
print(d)        # 2020-01-01
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5

#Time Objects to Represent Time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555

#Difference Between Two Points in Time Using
from datetime import date, datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

#Difference Between Two Points in Time Using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
"""

#EJERCICIOS
from datetime import datetime 
from datetime import date
from datetime import time 
ahora=datetime.now()
print(ahora.strftime("%m/%d/%Y, %H:%M:%S"))
timestamp=ahora.timestamp()
print(timestamp)
today= '5 December, 2019'
mejor=datetime.strptime(today,"%d %B, %Y")
print(mejor)

ahora=date(2026,2,17)
new_year=date(2027,1,1)
print('Quedan',new_year-ahora,'para que se acaba este año')
longlongago=date(1970,1,1)
print(ahora-longlongago)

