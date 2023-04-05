import pytest
from DatAnalyzer.pipeline.formatters import Data_Formating
from DatAnalyzer.pipeline.transformers import SmoothData


def test_import_data_with_wrong_extension():
    """
    Test if the import_data function raises an error when the extension is not supported
    """
    path = "test_data.txt"
    data_format = Data_Formating(path)
    with pytest.raises(ValueError):
        data_format.import_data()


def test_preprocessing_with_wrong_preprocessed_method():
    """
    Test if the type_of_preprocess function raises an error when the preprocessing method is not supported
    """
    method = "log scaling"
    data_format = SmoothData(method)
    with pytest.raises(ValueError):
        data_format.type_of_preprocess()
