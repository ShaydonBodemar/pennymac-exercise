"""
Run the PennyMac exercise, with options to run one at a time,
as well as user-input for other data files.

Author:
    Shaydon Bodemar

Date:
    23 December 2020
"""


from pennymac import weather


weatherdata = weather.Weather("w_data.dat")
min_spread = weatherdata.get_minimum_temp_spread_day()