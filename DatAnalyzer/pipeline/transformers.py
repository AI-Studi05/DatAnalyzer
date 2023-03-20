from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, PolynomialFeatures

class SmoothData(StandardScaler,MinMaxScaler,PolynomialFeatures):
    def __init__(self,smooth_type):
        self.smooth_type=smooth_type

    def type_of_preprocess(self):
        if self.smooth_type == "min-max scaling":
            scaler=MinMaxScaler()
        elif self.smooth_type == "z-normalisation":
            scaler=StandardScaler()
        elif self.smooth_type == "polynomial features":
            scaler=PolynomialFeatures()
        else:
            raise ValueError("The preprocessing method is not supported")
        return scaler

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        return self.transform(X)
