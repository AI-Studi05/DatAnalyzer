from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as metrics
import numpy as np

REGRESSION_PROTOCOLS = ["Linear Regression", "Decision Tree Classifier"]
SPLIT_PROTOCOLS = {"Radom state 1": 123, "Radom state 2": 456, "Radom state 3": 789}


class RegressionModel(LinearRegression, DecisionTreeClassifier):
    def __init__(self):
        super().__init__()
        self.linear_regression = LinearRegression()
        self.decision_tree_classifier = DecisionTreeClassifier()

    def split_data(self, data, dependant_variable_column, random_state, test_size):
        X = data.drop(columns=[dependant_variable_column])
        y = data[dependant_variable_column]
        X_train_data, X_test_data, y_train_data, y_test_data = train_test_split(X, y, random_state=random_state, test_size=0.3)
        return X_train_data, X_test_data, y_train_data, y_test_data

    def regression(self, model):
        self.model = model
        if model == "Linear Regression":
            return self.linear_regression
        elif model == "Decision Tree Classifier":
            return self.decision_tree_classifier
        else:
            raise ValueError(f"This type of regression is not supported : {self.model}")

    def fit(self, X_train, y_train):
        return self.fit(X_train, y_train)

    def predict(self, X_test):
        return self.predict(X_test)

    def regression_results(self, y_true, y_pred):
        # Regression metrics
        result = {}
        explained_variance = metrics.explained_variance_score(y_true, y_pred)
        mean_absolute_error = metrics.mean_absolute_error(y_true, y_pred)
        mse = metrics.mean_squared_error(y_true, y_pred)
        mean_squared_log_error = metrics.mean_squared_log_error(y_true, y_pred)
        r2 = metrics.r2_score(y_true, y_pred)
        result["explained_variance"] = round(explained_variance, 4)
        result["mean_squared_log_error"] = round(mean_squared_log_error, 4)
        result["r2"] = round(r2, 4)
        result["MAE"] = round(mean_absolute_error, 4)
        result["MSE"] = round(mse, 4)
        result["RMSE"] = round(np.sqrt(mse), 4)
        return result
