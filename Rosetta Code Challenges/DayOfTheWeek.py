# Day of the week
import datetime
def xmas_sundays(start_year, end_year):
    xmas_sunday_years = []
    for year in range(start_year, end_year + 1):
        xmas_date = datetime.date(year, 12, 25)
        if xmas_date.weekday() == 6:
            xmas_sunday_years.append(year)
    return xmas_sunday_years
start_year = 2022
end_year = 2030
print(xmas_sundays(start_year, end_year))