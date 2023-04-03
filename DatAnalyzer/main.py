from pipeline.cleaners import CleanData
from pipeline.regression import RegressionModel
from pipeline.formatters import Data_Formating
import os

file_path = os.path.abspath(__file__)
data_house_path = f"{file_path}/../../ressources/raw_data/housing/housing.data"
data_house_access = Data_Formating(data_house_path)
data_white_wine_path = f"{file_path}/../../ressources/raw_data/wine/winequality-white.csv"
data_white_wine_access = Data_Formating(data_white_wine_path)
data_red_wine_path = f"{file_path}/../../ressources/raw_data/wine/winequality-red.csv"
data_red_wine_access = Data_Formating(data_red_wine_path)


column_name = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
data_house = data_house_access.import_data(columns_name=column_name)
data_white_wine = data_white_wine_access.import_data()
data_red_wine = data_red_wine_access.import_data()


# Clean the DATA
data = CleanData().drop_duplicated()


# Split the Data
X_train, X_test, y_train, y_test = RegressionModel().train_test_split(data, random_state="X", test_size=0.3)

# Make the Regression
type_of_regression = RegressionModel().regression("MODEL")

type_of_regression.fit(X_train, y_train)

type_of_regression.score(X_train, y_train)
