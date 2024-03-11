"""
1. implement a function called 'convert' expects a string either 12-hour or 24-hour format(9:00 to 17:00)
2. expect AM and PM will be capitalized


corner case
- raise ValueErrorif either time or format is invalid

"""

import re
import sys


def main():
    print(convert(input("Hours: ")))


# def convert(s):
#     start, end = s.split("to")
#     start = start.strip()
#     start_time = int(start.split()[0])
#     end = end.strip()
#     if "PM" in end:
#         end_time = int(end.split()[0]) + 12
#     else:
#         print('no')

#     return print(f"{start_time:02}:00 to {end_time:02}:00")
    

def convert(s):
    start, end = s.split("to")

    if ":" and "PM" in start:
        start_hour, start_minutes = start.replace("PM", "").strip().split(":")
        start_hour = int(start_hour) + 12
    elif ":" and "AM" in start:
        start_hour, start_minutes = start.replace("AM", "").strip().split(":")
        
    if ":" and "PM" in end:
        end_hour, end_minutes = end.replace("PM", "").strip().split(":")
        end_hour = int(end_hour) + 12
    elif ":" and "AM" in end:
        end_hour, end_minutes = end.replace("AM", "").strip().split(":")

    return print(f"{start_hour:02}:{start_minutes:02} to {end_hour:02}:{end_minutes:02}")





if __name__ == "__main__":
    main()