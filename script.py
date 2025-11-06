import time
from datetime import datetime
t = datetime.now()
print("date and time:", t)
print("year:",t.year)
print("month:",t.month)
print("week no:",time.strftime("%u"))
print("weekday:",t.strftime("%A"))
print("day of year:", t.strftime("%j"))
print("day of month:", t.day)
print("day of week:", t.strftime("%w"))
