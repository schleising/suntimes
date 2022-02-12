#! /Users/steve/Downloads/.suntimes_env/bin/python
from datetime import date, datetime
import warnings
import sys

from astral import LocationInfo
from dateparser import parse

from astral.sun import sun

if __name__=='__main__':
    # Filter out a warning from dateparser
    warnings.filterwarnings('ignore', message='The localize method is no longer necessary')

    # Set the city to Brighton UK
    city = LocationInfo('Brighton', 'England', latitude=50.84472625108979, longitude=-0.1414355729975994)

    # Get the input string
    inputString = ' '.join(sys.argv[1:])

    # Parse the input string using dateparser
    sunsetDate = parse(inputString, settings={'PREFER_DATES_FROM': 'future'})

    # If dateparser failed to parse the date, set the date to today
    if sunsetDate is None:
        # If there was no input string silently set the date to today
        if inputString != '':
            # If there was a string but it was erroneous, print an error message
            print('Could not parse date, showing sunset time for today')
        sunsetDate = datetime.today()

    # Assume the date is in the future
    timeInPast = False

    # Find the difference between the requested date and today
    match (sunsetDate.date() - date.today()).days:
        # Today and the requested date are the same
        case 0:
            dayString = 'Today'

        # The requested date is one day into the future (i.e., tomorrow)
        case 1:
            dayString = 'Tomorrow'

        # The requested date is more than a week away, in this case print the day of month and month
        case dayDiff if dayDiff > 6 or dayDiff < 0:
            dayString = sunsetDate.strftime('On %A %d %B %Y')

            # Register that the date is in the past
            if dayDiff < 0:
                timeInPast = True

        # The requested date is in this week, but not today or tomorrow, so just print the day name
        case _:
            dayString = sunsetDate.strftime('On %A')

    # Get the sunset time
    sunset: datetime = sun(city.observer, sunsetDate.date())['sunset']

    # Print the sunset time with the formatted day string
    print()
    print(f'{dayString} the sun {"" if timeInPast else "will "}set at {sunset.hour:02}:{sunset.minute:02}')
    print()
