Results
=======

This is a summary of the results.
The data below are the yield of a run of some machine learning to the datasets Wine Quality and Housing Price.

.. note::
    This is a toy project to test the building of a reproducible research project.
    Therefore, the results are not the primary focus

That said, the results are not bad.
Different models were tested on the three datasets and different preprocessing methods were applied, as well as evaluation metrics.

For each dataset, three different preprocessing methods were tested: min-max scaling, z-normalisation and polynomial features.

Then the following models were tested: Linear Regression and Decision Tree Classifier.

The evaluation metrics used were: explained variance, r2, mean absolute error, mean squared error and root mean squared error.

The results are summarized in the following tables and all the details are available when running the code (see :ref:`_quick_start-label`):

.. table:: Red_wine Dataset model for Random_State_3

    +------------------+------------+------------+------------+------------+------------+
    |                  | Expl Var   | r2         | MAE        | MSE        | RMSE       |
    +==================+============+============+============+============+============+
    | min-max_scaling  |            |            |            |            |            |
    | Linear_Regression| 0.360000   | 0.360000   | 0.520000   | 0.460000   | 0.680000   |
    | Decision_Tree_Cla| -0.470000  | -0.490000  | 0.780000   | 1.060000   | 1.030000   |
    +------------------+------------+------------+------------+------------+------------+
    | z-normalisation  |            |            |            |            |            |
    | Linear_Regression| 0.360000   | 0.360000   | 0.530000   | 0.460000   | 0.680000   |
    | Decision_Tree_Cla| -0.280000  | -0.280000  | 0.660000   | 0.910000   | 0.950000   |
    +------------------+------------+------------+------------+------------+------------+
    | polynomial_featur|            |            |            |            |            |
    | Linear_Regression| 0.290000   | 0.290000   | 0.550000   | 0.500000   | 0.710000   |
    | Decision_Tree_Cla| -0.210000  | -0.210000  | 0.640000   | 0.860000   | 0.930000   |
    +------------------+------------+------------+------------+------------+------------+

.. table:: White_wine Dataset model for Random_State_3

    +------------------+------------+------------+------------+------------+------------+
    |                  | Expl Var   | r2         | MAE        | MSE        | RMSE       |
    +==================+============+============+============+============+============+
    | min-max_scaling  |            |            |            |            |            |
    | Linear_Regression| 0.200000   | -0.570000  | 0.900000   | 1.200000   | 1.100000   |
    | Decision_Tree_Cla| -0.820000  | -0.890000  | 0.860000   | 1.440000   | 1.200000   |
    +------------------+------------+------------+------------+------------+------------+
    | z-normalisation  |            |            |            |            |            |
    | Linear_Regression| 0.290000   | 0.290000   | 0.570000   | 0.540000   | 0.740000   |
    | Decision_Tree_Cla| -0.290000  | -0.290000  | 0.670000   | 0.980000   | 0.990000   |
    +------------------+------------+------------+------------+------------+------------+
    | polynomial_featur|            |            |            |            |            |
    | Linear_Regression| 0.250000   | 0.250000   | 0.560000   | 0.570000   | 0.760000   |
    | Decision_Tree_Cla| -0.320000  | -0.330000  | 0.690000   | 1.010000   | 1.010000   |
    +------------------+------------+------------+------------+------------+------------+

.. table:: House Dataset model for Random_State_3

    +------------------+------------+------------+------------+------------+------------+
    |                  | Expl Var   | r2         | MAE        | MSE        | RMSE       |
    +==================+============+============+============+============+============+
    | min-max_scaling  |            |            |            |            |            |
    | Linear_Regression| 0.600000   | 0.600000   | 3.970000   | 33.430000  | 5.780000   |
    | Decision_Tree_Cla| 0.670000   | 0.660000   | 3.730000   | 28.020000  | 5.290000   |
    +------------------+------------+------------+------------+------------+------------+
    | z-normalisation  |            |            |            |            |            |
    | Linear_Regression| 0.630000   | 0.620000   | 3.750000   | 31.150000  | 5.580000   |
    | Decision_Tree_Cla| 0.460000   | 0.450000   | 4.720000   | 45.290000  | 6.730000   |
    +------------------+------------+------------+------------+------------+------------+
    | polynomial_featur|            |            |            |            |            |
    | Linear_Regression| 0.720000   | 0.720000   | 2.910000   | 23.090000  | 4.800000   |
    | Decision_Tree_Cla| 0.660000   | 0.650000   | 3.700000   | 29.180000  | 5.400000   |
    +------------------+------------+------------+------------+------------+------------+
