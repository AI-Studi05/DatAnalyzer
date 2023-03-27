import pytest
from DatAnalyzer.pipeline.formatters import Data_Formating


def test_import_data_with_wrong_extension():
    path = "test_data.txt"
    data_format = Data_Formating(path)
    with pytest.raises(ValueError):
        data_format.import_data()
