import calendar
from datetime import date,timedelta
today=date.today()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("Yesterday = ",calendar.day_name[yesterday.weekday()])
print("Today = ",calendar.day_name[today.weekday()])
print("Tomorrow = ",calendar.day_name[tomorrow.weekday()])
