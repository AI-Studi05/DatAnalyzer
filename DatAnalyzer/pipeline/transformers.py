from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


class SmoothData(StandardScaler, MinMaxScaler, PolynomialFeatures):
    """
    This class is used to smooth the data using different methods
    """

    def __init__(self, smooth_type):
        """
        With the provided string, extract the path and the extension.

        :param str smooth_type: Type of smoothing
        """
        self.smooth_type = smooth_type

    def type_of_preprocess(self):
        """
        Return the type of preprocessing

        :return: Type of preprocessing
        :rtype: str
        """
        if self.smooth_type == "min-max scaling":
            scaler = MinMaxScaler()
        elif self.smooth_type == "z-normalisation":
            scaler = StandardScaler()
        elif self.smooth_type == "polynomial features":
            scaler = PolynomialFeatures()
        else:
            raise ValueError("The preprocessing method is not supported")
        return scaler

    def fit(self, X, y=None):
        """
        Fit the data

        :param X: Data to fit
        :param y: Target

        :return: self
        :rtype: SmoothData
        """
        return self

    def transform(self, X):
        """
        Transform the data

        :param X: Data to transform

        :return: Transformed data
        :rtype: numpy.ndarray
        """
        return self.transform(X)
