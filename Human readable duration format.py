import math


def format_duration(seconds):
    time = ''
    year = 31536000
    day = 86400
    hour = 3600
    minute = 60
    if seconds == 0:
        time = 'now'
    if seconds >= 2 * year:
        time += str(seconds // year) + ' years'
        seconds = seconds % year
        if seconds > 0:
            time += ', '

    if seconds >= year:
        time += str(seconds // year) + ' year'
        seconds = seconds % year
        if seconds > 0:
            time += ', '

    if seconds >= 2 * day:
        time += str(seconds // day) + ' days'
        seconds = seconds % day
        if seconds > 0:
            time += ', '

    if seconds >= day:
        time += str(seconds // day) + ' day'
        seconds = seconds % day
        if seconds > 0:
            time += ', '

    if seconds >= 2 * hour:
        time += str(seconds // hour) + ' hours'
        seconds = seconds % hour
        if seconds > 0 and seconds % minute != 0:
            time += ', '
        else:
            time += ' '

    if seconds >= hour:
        time += str(seconds // hour) + ' hour'
        seconds = seconds % hour
        if seconds > 0:
            time += ', '

    if seconds >= 2 * minute:
        if seconds % minute == 0 and time is not '':
            time += 'and '
        time += str(seconds // minute) + ' minutes'
        seconds = seconds % minute
        if seconds > 0:
            time += ' '

    if seconds >= minute:
        if seconds % minute == 0 and time is not '':
            time += 'and '
        time += str(seconds // minute) + ' minute'
        seconds = seconds % minute
        if seconds > 0:
            time += ' '

    if seconds >= 2:
        if time != '':
            time += 'and '
        time += str(seconds) + ' seconds'

    if seconds == 1:
        if time != '':
            time += 'and '
        time += str(seconds) + ' second'
    return time

x=format_duration(132030240)
print(x)


