import pandas as pd
import os
import numpy as np

cwd = os.path.dirname(__file__)

DATAFILE = {
    "House": os.path.abspath(os.path.join(cwd, os.pardir, os.pardir, "ressources/raw_data/housing/housing.data")),
    "White wine": os.path.abspath(os.path.join(cwd, os.pardir, os.pardir, "ressources/raw_data/wine/winequality-white.csv")),
    "Red wine": os.path.abspath(os.path.join(cwd, os.pardir, os.pardir, "ressources/raw_data/wine/winequality-red.csv")),
}

Y_DATAFILE = {
    "House": "MEDV",
    "White wine": "quality",
    "Red wine": "quality",
}

COLUMN_NAME = {
    "House": ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"],
    "White wine": None,
    "Red wine": None,
}
two_dirs_back = os.path.abspath(os.path.join(cwd, os.pardir, os.pardir))


class Data_Formating:
    """
    This class is used to format the data
    """

    def __init__(self, path):
        """
        With the provided string, extract the path and the extension.

        :param path: Path to the data
        :type path: str
        """
        self.path = path
        self.extension = os.path.splitext(path)[1]

    def import_data(self, columns_name=None):
        """
        Import the data from the path provided in the constructor.

        :param columns_name: List of the columns name
        :type columns_name: list

        :return: Dataframe with the data
        :rtype: pandas.DataFrame

        :raises ValueError: If the extension is not .csv or .data
        """

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
            raise ValueError(f"We can not import this type of extension :{self.extension}")
        return data
