#! python3
# Count the number of Sundays that fell on the first of the month in the 20th century (1 Jan 1901 - 31 Dec 2000)

import logging
logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')

day = 6
month = 1
year = 1901

end_day = 31
end_month = 12
end_year = 2000

ndays = 31
nsundays = 0

while year <= end_year and month <= end_month and day <= end_day:
    day = day + 7
    if day > ndays:
        day = day % ndays
        month += 1
        if month > 12:
            month = month % 12
            year = year + 1
        if month in (4, 6, 9, 11):
            ndays = 30
        elif month == 2:
            if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
                ndays = 29
            else:
                ndays = 28
        else:
            ndays = 31
    assert day <= ndays
    assert month <= 12
    if day == 1:
        nsundays += 1

print('There were %d Sundays in the 20th century' % nsundays)
