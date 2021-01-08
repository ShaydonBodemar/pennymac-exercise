"""
Perform tasks related to the soccer data.

Author:
    Shaydon Bodemar

Date:
    23 December 2020
"""


import pandas


class Soccer:
    """
    The Soccer object can be used to maintain the data read from the specified file,
    and perform desired tasks on this data.

    Attributes:
        data (pandas DataFrame): data structure for maintaing soccer data read from file
    """


    def __init__(self, filename):
        """
        Constructor for the Soccer class.
        Reads file's data into the internal data structure, a pandas DataFrame. 

        Args:
            filename (string): name of file to be read for soccer data
        """
        temp_data = []
        all_data = []
        columns = None

        with open("pennymac/data/" + filename) as f:
            for line in f:
                temp_data = line.split()
                if len(temp_data) > 1:
                    if not columns:
                        columns = temp_data
                    else:
                        all_data.append(temp_data)

        for data in all_data:
            del data[-3]
            del data[0]
        # NOTE: no missing data appears in example file, but still worth noting that missing data is unhandled, could cause errors
        self.__data = pandas.DataFrame(all_data, columns=columns)


    def get_minimum_diff_for_against_team(self):
        """
        Determines and returns the team with the minimum difference between goals scored for and against.

        Returns:
            team (string): name of the team with minimum for/against difference
        """
        for_goals = int(self.__data["F"][0])
        against_goals = int(self.__data["A"][0])
        min_difference = abs(for_goals - against_goals)
        min_difference_team = self.__data["Team"][0]
        for _, row in self.__data.iterrows():
            for_goals = int(row["F"])
            against_goals = int(row["A"])
            difference = abs(for_goals - against_goals)
            if difference < min_difference:
                min_difference = difference
                min_difference_team = row["Team"]
        return min_difference_team
