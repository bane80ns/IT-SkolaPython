import re

with open("logs/errors.log", "r") as error_log:

    pattern_time = r"\d{2}:\d{2}:\d{2}" #Sablon za vreme xx:xx:xx

    for error in error_log.readlines():
        match = re.search(pattern_time, error)
        print(match)

