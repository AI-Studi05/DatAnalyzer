from sklearn.preprocessing import MinMaxScaler, StandardScaler, PolynomialFeatures

PPREPROCESS_PROTOCSOLS = ["min-max scaling", "z-normalisation", "polynomial features"]


class SmoothData(StandardScaler, MinMaxScaler, PolynomialFeatures):
    """
    This class is used to smooth the data using different methods
    """

    def __init__(self, smooth_type):
        """
        With the provided string, extract the path and the extension.

        :param smooth_type: Type of smoothing
        :type smooth_type: str
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
        :type X: numpy.ndarray

        :param y: Target
        :type y: numpy.ndarray

        :return: self
        :rtype: SmoothData
        """
        return self

    def transform(self, X):
        """
        Transform the data

        :param X: Data to transform
        :type X: numpy.ndarray

        :return: Transformed data
        :rtype: numpy.ndarray
        """
        return self.transform(X)
