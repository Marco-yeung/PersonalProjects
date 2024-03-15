"""
1. a program that prompts the user for their date of birth in YYYY-MM-DD format, then show it in minutes
2. for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date
3.  And assume that the current time is also midnight
"""

import datetime
import inflect

def main():
    convert_date(input('Date of Birth: '), 'minutes')

def convert_date(date):
    year, month, day = date.split('-')
    year = int(year)
    month = int(month)
    day = int(day)

    before = datetime.date(year,month,day)
    now = datetime.date.today()

    diff = now - before
    ouput = diff.days*24*60

    p = inflect.engine()
    words = p.number_to_words(ouput)

    return words




if __name__ == "__main__":
    main()