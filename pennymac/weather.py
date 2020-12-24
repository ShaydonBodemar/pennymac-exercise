"""
Perform tasks related to the weather data.

Author:
    Shaydon Bodemar

Date:
    23 December 2020
"""


import pandas
import re
import os


class Weather:
    """
    The Weather object can be used to maintain the data read from the specified file,
    and perform desired tasks on this data.

    Attributes:
        data (pandas DataFrame): data structure for maintaing weather data read from file
    """


    def __init__(self, filename):
        """
        Constructor for the Weather class.
        Reads file's data into the internal data structure, a pandas DataFrame. 

        Args:
            filename (string): name of file to be read for weather data
        """
        temp_data = []
        all_data = []
        columns = None
        with open("pennymac/data/" + filename) as f:
            for line in f:
                temp_data = line.split()
                if len(temp_data) > 4:
                    if not columns:
                        columns = temp_data
                    else:
                        all_data.append(temp_data)
        for i in range(len(all_data)):
            while len(all_data[i]) < len(columns):
                all_data[i].append(None)
        # NOTE: missing data causes misalignment later in the table, must be solved to use that data effectively
        self.__data = pandas.DataFrame(all_data, columns=columns)


    def get_minimum_temp_spread_day(self):
        """
        Determines and returns the minimum temperature spread from the days in the data.

        Returns:
            day (int): the day number with this minimum temp difference
        """
        min_temp = float(re.sub("[^0-9][\\.[0-9]*]*", "", self.__data["MnT"][0]))
        max_temp = float(re.sub("[^0-9][\\.[0-9]*]*", "", self.__data["MxT"][0]))
        min_spread = max_temp - min_temp
        min_spread_day = self.__data["Dy"][0]
        for _, row in self.__data.iterrows():
            min_temp = float(re.sub("[^0-9][\\.[0-9]*]*", "", row["MnT"]))
            max_temp = float(re.sub("[^0-9][\\.[0-9]*]*", "", row["MxT"]))
            temp_spread = max_temp - min_temp
            if temp_spread < min_spread:
                min_spread = temp_spread
                min_spread_day = row["Dy"]
        return min_spread_day
