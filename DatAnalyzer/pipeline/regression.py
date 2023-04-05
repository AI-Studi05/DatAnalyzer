from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as metrics
import numpy as np

REGRESSION_PROTOCOLS = ["Linear Regression", "Decision Tree Classifier"]
SPLIT_PROTOCOLS = {"Random state 1": 123, "Random state 2": 456, "Random state 3": 789}


class RegressionModel(LinearRegression, DecisionTreeClassifier):
    """
    This class is used to create a regression model
    """

    def __init__(self):
        """
        Create a regression model
        """
        super().__init__()
        self.linear_regression = LinearRegression()
        self.decision_tree_classifier = DecisionTreeClassifier()

    def split_data(self, data, dependant_variable_column, random_state, test_size):
        """
        Split the data into train and test data

        :param data: Data to split
        :type data: pandas.DataFrame

        :param dependant_variable_column: Name of the dependant variable column
        :type dependant_variable_column: str

        :param random_state: Random state
        :type random_state: int

        :param test_size: Size of the test data
        :type test_size: float

        :return: Train and test data
        :rtype: tuple
        """
        X = data.drop(columns=[dependant_variable_column])
        y = data[dependant_variable_column]
        X_train_data, X_test_data, y_train_data, y_test_data = train_test_split(X, y, random_state=random_state, test_size=0.3)
        return X_train_data, X_test_data, y_train_data, y_test_data

    def regression(self, model):
        """
        Return the regression model

        :param model: Type of regression
        :type model: str

        :return: Regression model
        :rtype: sklearn.linear_model.LinearRegression

        :raise ValueError: If the model is not supported
        """
        self.model = model
        if model == "Linear Regression":
            return self.linear_regression
        elif model == "Decision Tree Classifier":
            return self.decision_tree_classifier
        else:
            raise ValueError(f"This type of regression is not supported : {self.model}")

    def fit(self, X_train, y_train):
        """
        Fit the data

        :param X_train: Train data
        :type X_train: pandas.DataFrame

        :param y_train: Target
        :type y_train: pandas.DataFrame

        :return: self
        :rtype: RegressionModel
        """
        return self.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Predict the data

        :param X_test: Test data
        :type X_test: pandas.DataFrame

        :return: Predicted data
        :rtype: pandas.DataFrame
        """
        return self.predict(X_test)

    def regression_results(self, y_true, y_pred):
        """
        Return the regression metrics

        :param y_true: True values
        :type y_true: pandas.DataFrame

        :param y_pred: Predicted values
        :type y_pred: pandas.DataFrame

        :return: Regression metrics
        :rtype: dict
        """
        result = {}
        explained_variance = metrics.explained_variance_score(y_true, y_pred)
        mean_absolute_error = metrics.mean_absolute_error(y_true, y_pred)
        mse = metrics.mean_squared_error(y_true, y_pred)
        r2 = metrics.r2_score(y_true, y_pred)
        result["explained_variance"] = round(explained_variance, 2)
        result["r2"] = round(r2, 2)
        result["MAE"] = round(mean_absolute_error, 2)
        result["MSE"] = round(mse, 2)
        result["RMSE"] = round(np.sqrt(mse), 2)
        return result
