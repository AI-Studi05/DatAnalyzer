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

        Parameters
        ----------
        path : str
        """
        self.path = path
        self.extension = os.path.splitext(path)[1]

    def import_data(self, columns_name=None):
        """
        Import the data from the path provided in the constructor.

        Parameters
        ----------
        columns_name : list
            List of the columns name. If None, the columns name will be
            the default one.

        Returns
        -------
        data : pandas.DataFrame
            Dataframe containing the data.

        Raises
        ------
        ValueError
            If the extension is not .csv or .data

        Examples
        --------
        >>> data = Data_Formating("data.csv")
        >>> data.import_data()

        >>> data = Data_Formating("data.data")
        >>> data.import_data()

        >>> data = Data_Formating("data.txt")
        >>> data.import_data()
        Traceback (most recent call last):
        ...
        ValueError: We can not import this type of Data

        >>> data = Data_Formating("data.csv")
        >>> data.import_data(columns_name=["a", "b", "c"])
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
