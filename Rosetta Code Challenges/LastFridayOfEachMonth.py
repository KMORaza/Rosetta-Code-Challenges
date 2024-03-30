# Last Friday of each month
import calendar
def last_friday_of_month(year, month):
    last_day = calendar.monthrange(year, month)[1]
    last_day_of_month = datetime.date(year, month, last_day)
    while last_day_of_month.weekday() != 4:
        last_day_of_month -= datetime.timedelta(days=1)
    return last_day_of_month
year = 2022
month = 10
print("📆 Last Friday:", last_friday_of_month(year, month))