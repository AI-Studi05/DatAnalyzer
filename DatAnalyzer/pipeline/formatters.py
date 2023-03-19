import pandas as pd
import os
import numpy as np


class Data_Formating():
    def __init__(self, directory):
        self.directory = directory
        self.extension = os.path.splitext(directory)[1]

    def import_data(self, columns_name=None):
        print(f"File extension: {self.extension}")
        if self.extension == ".csv":
            data = pd.read_csv(self.directory, sep=";", usecols=columns_name)
        elif self.extension == ".data":
            with open(self.directory, "r") as f:
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
