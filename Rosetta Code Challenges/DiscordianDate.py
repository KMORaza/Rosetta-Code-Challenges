# Discordian date
import datetime
def gregorian_to_discordian(gregorian_date):
    discordian_epoch = datetime.date(2022, 1, 1)
    delta_days = (gregorian_date - discordian_epoch).days
    leap_years = sum(1 for year in range(discordian_epoch.year, gregorian_date.year + 1) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    delta_days -= leap_years
    discordian_year = 3188 + (delta_days // 365)
    day_of_year = delta_days % 365
    is_leap_year = (gregorian_date.year % 4 == 0 and (gregorian_date.year % 100 != 0 or gregorian_date.year % 400 == 0))
    if day_of_year >= 59 and is_leap_year:
        day_of_year += 1
    discordian_month = day_of_year // 73
    discordian_day = day_of_year % 73
    discordian_months = ['Chaos', 'Discord', 'Confusion', 'Bureaucracy', 'The Aftermath']
    discordian_weekdays = ['Sweetmorn', 'Boomtime', 'Pungenday', 'Prickle-Prickle', 'Setting Orange']
    discordian_apostles = ['Mungday', 'Mojoday', 'Syaday', 'Zaraday', 'Maladay']
    discordian_holidays = ['Chaoflux', 'Discoflux', 'Confuflux', 'Bureflux', 'Afflux']
    discordian_date = "{} {}, {} YOLD".format(discordian_months[discordian_month], discordian_day + 1, discordian_year)
    discordian_weekday = discordian_weekdays[(day_of_year % 5)]
    discordian_apostle = discordian_apostles[(day_of_year % 5)]
    discordian_holiday = discordian_holidays[(day_of_year % 5)]
    return discordian_date, discordian_weekday, discordian_apostle, discordian_holiday
gregorian_date = datetime.date(2024, 3, 29)  # Enter the Gregorian date here
discordian_date, discordian_weekday, discordian_apostle, discordian_holiday = gregorian_to_discordian(gregorian_date)
print("Gregorian Date:", gregorian_date.strftime("%Y-%m-%d"))
print("Discordian Date:", discordian_date)
print("Discordian Weekday:", discordian_weekday)
print("Discordian Apostle:", discordian_apostle)
print("Discordian Holiday:", discordian_holiday)