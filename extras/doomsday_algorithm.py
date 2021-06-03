from random import randint
from calendar import calendar

year = randint(0,99)
print(year)
def even():
    if year % 2 == 0:
        return True

if year is even:
    year = year / 2
    if year is even:
        year = year % 7
        day = 7 - year
        print(year, day)

else:
    year += 11
    year = year / 2
    if year is not even:
        year += 11
        year = year % 7
        day = 7 - year
        print(year, day)



 