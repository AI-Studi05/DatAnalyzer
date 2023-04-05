from pipeline import cleaners
from pipeline import regression
from pipeline import formatters
from pipeline import transformers
import sys


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
    X_test = smoothing.fit_transform(X_test)

    # train our model and predict
    model = regression.RegressionModel().regression(regression_model)
    model = model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    # Score and result of our model
    result = regression.RegressionModel().regression_results(y_test, y_predict)
    return result


def all():
    """Builds the first table of my report"""
    i = 0
    for name_of_state, state in regression.SPLIT_PROTOCOLS.items():
        for dataset, path in formatters.DATAFILE.items():
            i += 1
            print("\nTable %d: %s Dataset model for %s :" % (i, dataset, name_of_state))
            print(60 * "-")
            print(
                "{:25s}".format(" "),
                "{:25s}".format(" "),
                "{:12s}".format("| Expl Var "),
                "{:12s}".format("| r2"),
                "{:12s}".format("| MAE"),
                "{:12s}".format("| MSE"),
                "{:12s}".format("| RMSE"),
            )

            for preprocess_method in transformers.PPREPROCESS_PROTOCSOLS:
                print(
                    "{:25s}".format(preprocess_method),
                    "{:25s}".format(" "),
                    "{:12s}".format(" "),
                    "{:12s}".format(" "),
                    "{:12s}".format(" "),
                    "{:12s}".format(" "),
                    "{:12s}".format(" "),
                )

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
                        "{:25s}".format(" "),
                        "{:25s}".format(regression_type),
                        "{:12s}".format("| %f" % (result["explained_variance"])),
                        "{:12s}".format("| %f" % (result["r2"])),
                        "{:12s}".format("| %f" % (result["MAE"])),
                        "{:12s}".format("| %f" % (result["MSE"])),
                        "{:12s}".format("| %f" % (result["RMSE"])),
                    )

    return i


def specific(protocol, metadata, scaling, model):
    """Builds the first table of my report"""
    i = 0
    split_protocols = {
        name_state: regression.SPLIT_PROTOCOLS[name_state]
        for name_state in protocol
        if name_state in regression.SPLIT_PROTOCOLS
    }
    datafile = {dataset: formatters.DATAFILE[dataset] for dataset in metadata if dataset in formatters.DATAFILE}
    for name_of_state, state in split_protocols.items():
        for dataset, path in datafile.items():
            i += 1
            print("\nTable %d: %s Dataset model for %s :" % (i, dataset, name_of_state))
            print(60 * "-")
            print(
                "{:25s}".format(" "),
                "{:25s}".format(" "),
                "{:12s}".format("| Expl Var "),
                "{:12s}".format("| r2"),
                "{:12s}".format("| MAE"),
                "{:12s}".format("| MSE"),
                "{:12s}".format("| RMSE"),
            )

            for preprocess_method in scaling:
                print(
                    "{:25s}".format(preprocess_method),
                    "{:25s}".format(" "),
                    "{:12s}".format(" "),
                    "{:12s}".format(" "),
                    "{:12s}".format(" "),
                    "{:12s}".format(" "),
                    "{:12s}".format(" "),
                )

                for regression_type in model:
                    result = process(
                        path,
                        formatters.Y_DATAFILE[dataset],
                        preprocess_method,
                        regression_type,
                        state,
                        column_name=formatters.COLUMN_NAME[dataset],
                    )
                    print(
                        "{:25s}".format(" "),
                        "{:25s}".format(regression_type),
                        "{:12s}".format("| %f" % (result["explained_variance"])),
                        "{:12s}".format("| %f" % (result["r2"])),
                        "{:12s}".format("| %f" % (result["MAE"])),
                        "{:12s}".format("| %f" % (result["MSE"])),
                        "{:12s}".format("| %f" % (result["RMSE"])),
                    )
    return i


def main():
    """Main function to be called from the command-line"""

    import argparse

    example_doc = """\
    examples:
    1. Returns all tables in the original report:
       $ rr-paper
    2. Only prints results for protocol "proto2":
       $ rr-paper --protocol=proto2
    3. Only prints results for protocol "proto1" and combinations of
       variables 3 by 3:
       $ rr-paper --protocol=proto1 --case=3
    """

    parser = argparse.ArgumentParser(
        usage="%(prog)s [options]",
        description="Performs Logistic Regression on Iris Flowers Dataset",
        epilog=example_doc,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-s",
        "--scaling",
        choices=["max_scaling", "z-normalisation", "polynomial_features"],
        nargs="*",
        default=["min-max_scaling", "z-normalisation", "polynomial_features"],
        help="Choose the preprocessing method. If you choose '1', then "
        "you choose the min-max scaling method for your the dataset "
        "If you choose '2', then you chooses the z-normalisation scaling"
        "method for your the dataset. If you choose '3', then you  "
        "chooses the min-max and z-normalisation (Polynomial) scaling "
        "method for  your the dataset. By default, if no specific"
        "method, it prints all methods ",
    )

    parser.add_argument(
        "-p",
        "--protocol",
        choices=["Random_State_1", "Random_State_2", "Random_State_3"],
        nargs="*",
        default=["Random_State_1", "Random_State_2", "Random_State_3"],
        help="Defines which protocol you want to use. We use three different "
        "random state for our result. Random state are 123, 456 and 789."
        "By default, if no specific method, it prints all protocols",
    )

    parser.add_argument(
        "-d",
        "--dataset",
        choices=["House", "White_wine", "Red_wine"],
        nargs="*",
        default=["House", "White_wine", "Red_wine"],
        help="Defines which Dataset you want to perform the regression. "
        "We use three different Dataset. House, which is the price of "
        "the house in Boston according to some criteria. White wine,"
        "which is the quality of wine according to wine criteria."
        "Red wine, which is the quality of wine according to wine criteria"
        "By default, if no specific method, it prints all protocols",
    )

    parser.add_argument(
        "-m",
        "--model",
        choices=["Linear_Regression", "Decision_Tree_Clasifier"],
        nargs="*",
        default=["Linear Regression", "Decision Tree Clasifier"],
        help="Defines with which model you want to apply to your"
        "dataset. Two models are available. Linear Regression"
        "model, and the Decision Tree Classifier.",
    )

    args = parser.parse_args()

    # keeps a nice sequential table number

    if len(sys.argv) > 1:
        specific(args.protocol, args.dataset, args.scaling, args.model)
    else:
        all()


if __name__ == "__main__":
    main()
