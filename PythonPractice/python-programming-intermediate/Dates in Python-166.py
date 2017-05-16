## 1. The Time Module ##

import time

current_time = time.time()

print (current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()

current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

## 3. UTC ##

from datetime import datetime
current_datetime = datetime.now()
print (current_datetime)

current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime

today = datetime.datetime.now()

diff = datetime.timedelta(days =1)

tomorrow = today + diff
yesterday = today - diff


## 5. Formatting Dates ##

import datetime

mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print (mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")

print (mystery_date)

## 8. Reformatting Our Data ##

import datetime

for row in posts:
    datetime_object = datetime.datetime.fromtimestamp(float(row[2]))
    row[2] = datetime_object

## 9. Counting Posts from March ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1

## 10. Counting Posts from Any Month ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1
        
def monthcounter(month):
    month_count = 0
    for row in posts:
        if row[2].month == month:
            month_count += 1
    return month_count

feb_count = monthcounter(2)
aug_count = monthcounter(8)