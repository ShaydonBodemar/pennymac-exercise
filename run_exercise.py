"""
Run the PennyMac exercise, with options to run one at a time,
as well as user-input for other data files.

Author:
    Shaydon Bodemar

Date:
    23 December 2020
"""


from pennymac import weather
from pennymac import soccer


weatherdata = weather.Weather("w_data.dat")
min_spread = weatherdata.get_minimum_temp_spread_day()
print("Day of Smallest Temperature Spread: " + min_spread)

soccerdata = soccer.Soccer("soccer.dat")
min_diff = soccerdata.get_minimum_diff_for_against_team()
print("Minimum For/Against Difference Team: " + min_diff)