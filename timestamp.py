def format_time_stamp(year, month, day, hour=0, minute=0, second=0, tz='-04'):
    if 0 <= hour < 10:
        hour = '0' + str(hour)
    if 0 <= minute < 10:
        minute = '0' + str(minute)
    if 0 <= second < 10:
        second = '0' + str(second)
    if 0 <= month < 10:
        month = '0' + str(month)
    if 0 <= day < 10:
        day = '0' + str(day)

    # Example timestamp string: '2016-06-22 19:10:25-04'
    # With leading zeroes just in case
    result = '' + str(year) + '-' + str(month) + '-' + str(day) + ' ' + str(hour) + ':' + str(minute) + ':' + str(
        second) + tz
    return result
