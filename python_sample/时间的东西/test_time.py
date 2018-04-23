# encoding=utf8
import datetime
now = datetime.datetime.now()
print now
import time
time.sleep(5)
now2 = datetime.datetime.now()
time2 = datetime.datetime.strptime("01:00:00",'%H:%M:%S')
print (now2 - now) > datetime.timedelta(hours=1)
now = now + datetime.timedelta(days=-30)
print now.strftime('%Y%m')

d1 = datetime.datetime.now()
print d1
# 当前时间加上半小时
d2 = d1 + datetime.timedelta(hours=0.5)
#another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)

def first_day_of_month():
  '''
  获取本月第一天
  :return:
  '''
  # now_date = datetime.datetime.now()
  # return (now_date + datetime.timedelta(days=-now_date.day + 1)).replace(hour=0, minute=0, second=0,
  # microsecond=0)
  return datetime.date.today() - datetime.timedelta(days=datetime.datetime.now().day - 1)
def first_day_of_week():
  '''
  获取本周第一天
  :return:
  '''
  return datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())

def strtoint(str1):
  return int(str1)
test  = ['201610','201510','201711']
print sorted(test,key=strtoint)

hehe = {}
print len({'fa':'fad','fdas':'fdasf'})
'''
def gen_double_diff(nowmonth):
  year = nowmonth[:4]
  month = nowmonth[4:]
  premonth = ''
  nextmonth = ''
  
  if month == '01':
    premonth = str(int(nowmonth)-89)
    nextmonth = str(int(nowmonth)+1)
  elif month == '12':
    premonth = str(int(nowmonth)-1)
    nextmonth = str(int(nowmonth)+89)
  else:
    premonth = str(int(nowmonth)-1)
    nextmonth = str(int(nowmonth)+1)
  
  print premonth,nextmonth

def nowtime():
  now_time = datetime.datetime.now()
  now_time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
  print now_time_str
  print now_time.weekday()
  print now_time

nowtime()
def test2():
  day1 = "2014-12-29" 
  day2 = "2017-09-01"
  day3 = "2017-09-04"
  now = datetime.datetime.now()
  time_a = datetime.datetime.strptime(day2,'%Y-%m-%d')
  time_b = datetime.datetime.strptime(day3,'%Y-%m-%d')
  print (time_b - now).days
test2()
'''
day2 = "2018-02-28"
datetime.datetime.strptime(day2,'%Y-%m-%d')
'''
%a Abbreviated weekday name   
%A Full weekday name   
%b Abbreviated month name   
%B Full month name   
%c Date and time representation appropriate for locale   
%d Day of month as decimal number (01 - 31)   
%H Hour in 24-hour format (00 - 23)   
%I Hour in 12-hour format (01 - 12)   
%j Day of year as decimal number (001 - 366)   
%m Month as decimal number (01 - 12)   
%M Minute as decimal number (00 - 59)   
%p Current locale's A.M./P.M. indicator for 12-hour clock   
%S Second as decimal number (00 - 59)   
%U Week of year as decimal number, with Sunday as first day of week (00 - 51)   
%w Weekday as decimal number (0 - 6; Sunday is 0)   
%W Week of year as decimal number, with Monday as first day of week (00 - 51)   
%x Date representation for current locale   
%X Time representation for current locale   
%y Year without century, as decimal number (00 - 99)   
%Y Year with century, as decimal number   
%z, %Z Time-zone name or abbreviation; no characters if time zone is unknown   
%% Percent sign
'''
'''
from dateutil import rrule  
import datetime  
  
def workdays(start, end, holidays=0, days_off=None):  
    if days_off is None:  
        days_off = 5,6  
    workdays = [x for x in range(7) if x not in days_off]  
    days = rrule.rrule(rrule.DAILY, dtstart=start, until=end,byweekday=workdays)  
    return days.count() - holidays -1 
  
print workdays(datetime.date(2017,9,15),datetime.date(2017,9,19),0)


'''

print ','.join([]).encode('utf-8')
for i in range(100):
    print i