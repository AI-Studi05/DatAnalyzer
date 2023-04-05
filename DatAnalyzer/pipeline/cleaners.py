class CleanData:
    """
    This class is used to clean the data
    """

    def __init__(self, X):
        """
        Set the data to clean

        :param X: Data to clean
        :type X: pandas.DataFrame
        """
        self.X = X

    def drop_duplicated(self):
        """
        Drop duplicated rows

        :return: Data without duplicated rows
        :rtype: pandas.DataFrame
        """
        self.nb_duplicate = self.X.duplicated().sum()
        x_cleaned = self.X.drop_duplicates()
        return x_cleaned

    def missing_data(self, ascending=False):
        """
        Return the number of missing data

        :param ascending: Sort the missing data
        :type ascending: bool

        :return: Missing data
        :rtype: pandas.Series
        """
        self.missingdata = self.isnull().sum().sort_values(ascending)
        return self.missingdata
