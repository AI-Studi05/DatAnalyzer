from pipeline import cleaners
from pipeline import regression
from pipeline import formatters
from pipeline import transformers


def process(data_path, y_column, scaling_method, regression_model, random_state, column_name=None):
    # import the data
    data_access = formatters.Data_Formating(data_path)
    data = data_access.import_data(columns_name=column_name)

    # Clean the data
    data = cleaners.CleanData(data).drop_duplicated()

    # Split the data
    X_train, X_test, y_train, y_test = regression.RegressionModel().split_data(data, y_column, random_state, test_size=0.3)

    # Smooth the data:
    smoothing = transformers.SmoothData(scaling_method).type_of_preprocess()
    X_train = smoothing.fit_transform(X_train)

    # train our model and predict
    model = regression.RegressionModel().regression(regression_model)
    model = model.fit(X_train, y_train)
    y_predict = model.predict(X_test)

    # Score and result of our model
    result = regression.RegressionModel().regression_results(y_test, y_predict)
    return result


def all(tabnum, protocols):
    """Builds the first table of my report"""
    step = 1
    for name_of_state, state in regression.SPLIT_PROTOCOLS.items():
        for dataset, path in formatters.DATAFILE.items():
            for preprocess_method in transformers.PPREPROCESS_PROTOCSOLS:
                print(
                    "\nTable %d: %s Dataset model for %s with %s preprocessing method:"
                    % (step, dataset, name_of_state, preprocess_method)
                )
                print(60 * "-")

                for regression_type in regression.REGRESSION_PROTOCOLS:
                    result = process(
                        path,
                        formatters.Y_DATAFILE[dataset],
                        preprocess_method,
                        regression_type,
                        state,
                        column_name=formatters.COLUMN_NAME[dataset],
                    )
                    print(
                        ("%-15s" % regression_type),
                        "| %f" % (result["explained_variance"]),
                        "| %f" % (result["mean_squared_log_error"]),
                        "| %f" % (result["r2"]),
                        "| %f" % (result["MAE"]),
                        "| %f" % (result["MSE"]),
                        "| %f" % (result["RMSE"]),
                    )

        return len(protocols)


def main():
    return


if __name__ == "__main__":
    main
