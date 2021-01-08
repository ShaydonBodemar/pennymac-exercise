"""
Run the PennyMac exercise, with options to run one at a time,
as well as user-input for other data files.

Author:
    Shaydon Bodemar

Date:
    23 December 2020
"""


import sys
from pennymac import weather
from pennymac import soccer


if len(sys.argv) > 1 and sys.argv[1] == '-w':
    if len(sys.argv) > 2:
        try:
            weatherdata = weather.Weather(str(sys.argv[2]))
            min_spread = weatherdata.get_minimum_temp_spread_day()
            print("Day of Smallest Temperature Spread: " + min_spread)
        except FileNotFoundError:
            print("Invalid filename provided.")
    else:
        print("No filename specified.")
elif len(sys.argv) > 1 and sys.argv[1] == '-s':
    if len(sys.argv) > 2:
        try:
            soccerdata = soccer.Soccer(str(sys.argv[2]))
            min_diff = soccerdata.get_minimum_diff_for_against_team()
            print("Minimum For/Against Difference Team: " + min_diff)
        except FileNotFoundError:
            print("Invalid filename provided.")
    else:
        print("No filename specified.")
else:
    print("Invalid or missing command line arguments.\nUse -w for weather or -s for soccer, followed by the filename.")
