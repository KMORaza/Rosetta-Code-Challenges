# CUSIP
import re
def is_valid_cusip(cusip):
    pattern = r'^[a-zA-Z0-9]{6}[0-9]{1}[a-zA-Z0-9]{2}$'
    if re.match(pattern, cusip):
        return True
    else:
        return False
cusip = "037833100"
print(is_valid_cusip(cusip))
cusip = "03783310"
print(is_valid_cusip(cusip))  