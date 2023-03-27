import pytest
from DatAnalyzer.pipeline.formatters import Data_Formating
from DatAnalyzer.pipeline.transformers import SmoothData


def test_import_data_with_wrong_extension():
    path = "test_data.txt"
    data_format = Data_Formating(path)
    with pytest.raises(ValueError):
        data_format.import_data()


def test_preprocessing_with_wrong_preprocessed_method():
    method = "log scaling"
    data_format = SmoothData(method)
    with pytest.raises(ValueError):
        data_format.type_of_preprocess()
