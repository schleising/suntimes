#! /Users/steve/Downloads/.suntimes_env/bin/python
from datetime import date, datetime
from astral import LocationInfo

from astral.sun import sun
from astral.geocoder import database, lookup

if __name__=='__main__':
    city = LocationInfo('Brighton', 'England', latitude=50.84472625108979, longitude=-0.1414355729975994)

    sunset: datetime = sun(city.observer, date.today())['sunset']

    print(f'Today the sun will set at {sunset.hour}:{sunset.minute}')
