class CleanData:
    def __init__(self, X):
        self.X = X

    def drop_duplicated(self):
        self.nb_duplicate = self.X.duplicated().sum()
        return self

    def missing_data(self, ascending=False):
        self.missingdata = self.isnull().sum().sort_values(ascending)
        return self.missingdata