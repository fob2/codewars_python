""" Write a function, which takes a non-negative integer (seconds) as input
and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59) """

import math

def make_readable(seconds):
    hours = str(math.floor(seconds / 3600))
    minutes = str(math.floor(seconds % 3600 / 60))
    secs = str(math.floor(seconds % 3600 % 60))
    if len(hours) == 1:
        hours = '0' + hours
    if len(minutes) == 1:
        minutes = '0' + minutes
    if len(secs) == 1:
        secs = '0' + secs
    return f'{hours}:{minutes}:{secs}'