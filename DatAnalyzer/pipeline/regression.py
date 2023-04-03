from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier


class RegressionModel(train_test_split, LinearRegression, DecisionTreeClassifier):
    def __init__(self):
        super().__init__()

    def split_data(self, data, dependant_variable_column, random_state, test_size):
        X = data.drop(columns=[dependant_variable_column])
        y = data[dependant_variable_column]
        X_train_data, X_test_data, y_train_data, y_test_data = train_test_split(X, y, random_state=random_state, test_size=0.3)
        return X_train_data, X_test_data, y_train_data, y_test_data

    def regression(self, model):
        if model == "LinearRegression":
            return self.LinearRegression()
        elif model == "DecisionTreeClassifier":
            return self.DecisionTreeClassifier()
        else:
            raise ValueError("This type of regression is not supported")

    def fit(self, X_train, y_train):
        return self.fit(X_train, y_train)

    def score(self, X_train, y_train):
        return self.score
