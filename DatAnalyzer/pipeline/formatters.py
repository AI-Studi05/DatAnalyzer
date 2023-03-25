import pandas as pd
import os
import numpy as np


class Data_Formating:
    """
    This class is used to format the data
    """

    def __init__(self, path):
        """
        With the provided string, extract the path and the extension.

        :param str path: Path to the data
        """
        self.path = path
        self.extension = os.path.splitext(path)[1]

    def import_data(self, columns_name=None):
        """
        Import the data from the path provided in the constructor.

        :param list columns_name: List of the columns name

        :return: Dataframe with the data

        :rtype: pandas.DataFrame

        :raises ValueError: If the extension is not .csv or .data
        """

        print(f"File extension: {self.extension}")
        if self.extension == ".csv":
            data = pd.read_csv(self.path, sep=";", usecols=columns_name)
        elif self.extension == ".data":
            with open(self.path, "r") as f:
                for index, lines in enumerate(f):
                    values = np.array(lines.split())
                    if index == 0:
                        data = values
                    else:
                        data = np.vstack((data, values))
            data = pd.DataFrame(data, columns=columns_name)
        else:
            print(self.extension)
            raise ValueError("We can not import this type of Data")
        return data
