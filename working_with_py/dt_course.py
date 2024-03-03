import datetime as dt
from datetime import timedelta

"""
# DATE & TIME NOW OF THE MACHINE
calnow = dt.datetime.now()
print(calnow)

# DATE TODAY
dtoday = dt.date.today()
print(dtoday)

# CALLING YEAR
nowyy = calnow.year
print(nowyy)

# CALLING TIME
tnow = calnow.time()
print(tnow)

# CREATE OBJECT
inp_date = dt.datetime(2021,1,1)
print (inp_date)
print (inp_date.date().year)

# DATE & TIME FORMATTING
# by using -- strftime --
# TUTORIAL : https://www.w3schools.com/python/python_datetime.asp
# Let's try this formatting : Day, Month Day, Year (Mon, Jan 1, 2021)
print (calnow.strftime("%a, %b %d %Y"))

# DATE & TIME MANIPULATION
# by using -- timedelta --
d3_before = dtoday - timedelta(days=3)
print("3 days before now is ",d3_before)
"""

# SHOWING CALENDAR
import calendar

# YEARLY
#print (calendar.calendar(2023))

# MONTHLY
#print (calendar.month(theyear=2024,themonth=3))
# You could do this as well
yy = 2024
mm = 3
print (calendar.month(yy,mm))