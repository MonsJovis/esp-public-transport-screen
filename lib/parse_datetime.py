
def parse_datetime(datetime_string):
    # Split the date and time
    splitted_datetime = datetime_string.split(' ')

    date_part = splitted_datetime[0]
    time_part = splitted_datetime[1]

    # Split the date into year, month, and day
    year, month, day = map(int, date_part.split('-'))

    # Split the time into hour, minute, and second
    hour, minute, second = map(int, time_part.split(':'))

    # Create a tuple in the format (year, month, day, hour, minute, second, weekday, yearday)
    # Note: weekday and yearday are set to 0 as they are not used here
    time_tuple = (year, month, day, hour, minute, second, 0, 0)

    return time_tuple
