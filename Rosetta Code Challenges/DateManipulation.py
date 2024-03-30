# Date manipulation
from datetime import datetime, timedelta
import pytz
def add_12_hours_to_est_date(date_str):
    est = pytz.timezone('US/Eastern')
    date_format = "%B %d %Y %I:%M%p"
    est_dt = datetime.strptime(date_str[:-4], date_format)
    est_dt = est.localize(est_dt)
    est_dt += timedelta(hours=12)
    updated_date_str = est_dt.strftime(date_format + " %Z")
    return updated_date_str
input_date = "March 6 2009 7:30pm EST"
output_date = add_12_hours_to_est_date(input_date)
print("Input:", input_date)
print("Output:", output_date)