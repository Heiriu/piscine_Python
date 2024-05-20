import datetime
import time


time = str(round(time.time() * 1000))
myDateTime = datetime.datetime.now()

length = 2
time_dot = ""
for i in time:
    if length % 3 == 0 and length < 12:
        time_dot = time_dot + ","
    elif length == 12:
        time_dot = time_dot + "."
    time_dot = time_dot + i
    length += 1

time = int(myDateTime.strftime('%s'))
print("Seconds since January 1, 1970: ",
      time_dot, "or", format(time, ".1E"), "in scientific notation")

myDate = datetime.date.today()
list_month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
              "Aug", "Sep", "Oct", "Nov", "Dec"]
print(list_month[myDate.month - 1], myDate.day, myDate.year)
