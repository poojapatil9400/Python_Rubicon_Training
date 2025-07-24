#import calender and used all the functions
import calendar 
print(calendar.isleap(2020))  # Output: True (2020 is a leap year)
print(calendar.month(2023, 10))  # Output: October 2023 calendar
print(calendar.weekday(2023, 10, 1))  # Output: 6 (Sunday)
print(calendar.firstweekday())  # Output: 0 (Monday is the first day of the week)
print(calendar.monthrange(2023, 10))  # Output: (6, 31) (October 2023 starts on a Sunday and has 31 days)
print(calendar.calendar(2023))  # Output: Full calendar for the year 2023
print(calendar.setfirstweekday(calendar.SUNDAY))  # Set Sunday as the first day of the week
print(calendar.monthcalendar(2023, 10))  # Output: List of weeks in October 2023
print(calendar.timegm((2023, 10, 1, 0, 0, 0)))  # Output: 1696118400 (Unix timestamp for October 1, 2023)
print(calendar.leapdays(2000, 2023))  # Output: 6 (Number of leap days between 2000 and 2023)

from datetime import datetime
# Get the current date and time 
now = datetime.now()
print(now)  # Output: Current date and time

# Format the current date and time
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_now)  # Output: Current date and time in the specified format

# Parse a date string into a datetime object
date_string = "2023-10-01 12:30:45"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)  # Output: 2023-10-01 12:30:45

# Get the current date  
current_date = datetime.today().date()
print(current_date)  # Output: Current date

# Get the current time
current_time = datetime.now().time()
print(current_time)  # Output: Current time

# Get the day of the week
day_of_week = now.strftime("%A")
print(day_of_week)  # Output: Current day of the week (e.g., "Monday")

# Get the current year, month, and day
current_year = now.year
current_month = now.month
current_day = now.day
print(f"Year: {current_year}, Month: {current_month}, Day: {current_day}")  # Output: Current year, month, and day

# Get the current hour, minute, and second
current_hour = now.hour
current_minute = now.minute
current_second = now.second
print(f"Hour: {current_hour}, Minute: {current_minute}, Second: {current_second}")  # Output: Current hour, minute, and second

#print the calender for the current month
print(calendar.month(now.year, now.month))  # Output: Calendar for the current month
