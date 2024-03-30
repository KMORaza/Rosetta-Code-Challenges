# Date format
from datetime import datetime
def format_date_strings():
    today = datetime.today()
    first_string = today.strftime('%Y-%-m-%-d')
    second_string = today.strftime('%A, %B %-d, %Y')
    return [first_string, second_string]
print(format_date_strings())