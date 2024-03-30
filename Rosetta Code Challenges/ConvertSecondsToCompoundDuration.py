# Convert seconds to compound duration
def format_duration(seconds):
    if seconds == 0:
        return "0 sec"
    weeks = seconds // (7 * 24 * 3600)
    seconds %= (7 * 24 * 3600)
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    duration_parts = []
    if weeks:
        duration_parts.append(f"{weeks} week" if weeks == 1 else f"{weeks} weeks")
    if days:
        duration_parts.append(f"{days} day" if days == 1 else f"{days} days")
    if hours:
        duration_parts.append(f"{hours} hour" if hours == 1 else f"{hours} hours")
    if minutes:
        duration_parts.append(f"{minutes} min" if minutes == 1 else f"{minutes} mins")
    if seconds:
        duration_parts.append(f"{seconds} sec" if seconds == 1 else f"{seconds} secs")
    return ', '.join(duration_parts)
print(format_duration(100))