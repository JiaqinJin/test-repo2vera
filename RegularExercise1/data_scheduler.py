"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""


import datetime


def date_passed(todays_date, scheduled_date):
    # Define the format of the date strings
    date_format = '%dth %B'

    # Convert the date strings to datetime objects
    today = datetime.datetime.strptime(todays_date, date_format)
    scheduled = datetime.datetime.strptime(scheduled_date, date_format)

    # Compare the dates
    if today > scheduled:
        return "Scheduled date has passed."
    elif today < scheduled:
        return "Scheduled date is yet to pass."
    else:
        return "Scheduled date is today."

# Test cases
print(date_passed('26th March', '25th March'))  # Expected: Scheduled date has passed
print(date_passed('26th March', '26th March'))  # Expected: Scheduled date is today
print(date_passed('26th March', '27th March'))  # Expected: Scheduled date is yet to pass

# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
