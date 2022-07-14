import time, datetime
now = time.gmtime(time.time())
y, m, d, h, min = now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min
dd = datetime.datetime.now()
ddd = str(dd.year) + '_' + str(dd.month) + '_' + str(dd.day) + '_' + str(dd.hour) + '_' + str(dd.minute) 
print(time.ctime())