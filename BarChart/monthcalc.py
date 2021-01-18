from datetime import date
import sys


def twelve_month_apart(date1,date2):
    try:
        d1 = date.fromisoformat(date1)
        d2 = date.fromisoformat(date2)
    except ValueError:
        print('ERROR: Invalid date or incorrect date format. Provide valid dates in YYYY-MM-DD fomat e.g. 2019-04-30.')
        sys.exit(-1)

    if d1 > d2:
        print('ERROR: Second date should be same or later than first date.')
        sys.exit(-1)

    if d2.month == 2 and d2.day == 29:
        d2 = d2.replace(day=28)

    d2_prev_year = d2.replace(year=d2.year-1)

    return True if d2_prev_year >= d1 else False

# example
# twelve_month_apart('2001-02-28', '2002-02-27')
