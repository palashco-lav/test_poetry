from io import StringIO
from pathlib import Path
from unittest.mock import MagicMock, Mock, mock_open, patch

import pandas as pd

from src.load_data import read_financial_trans_csv, read_financial_trans_xlsx

BASE_DIR = Path(__file__).resolve().parent.parent


@patch("builtins.open", new_callable=mock_open, read_data="1")
def test_read_financial_trans_csv(mock_read_financial_trans_csv: MagicMock,
                                  test_read_financial_trans_csv_data: str) -> None:

    data = test_read_financial_trans_csv_data

    f = StringIO(data)
    test_df = pd.read_csv(f, sep=";")
    mock = mock_open(read_data=data)
    test_result = test_df.to_dict(orient="records")
    # Мокаем open(file)
    with patch("builtins.open", mock):
        result = read_financial_trans_csv("dummy.csv")
        assert result == test_result  # Работает!


def test_read_financial_trans_xlsx(test_read_financial_trans_xlsx_data: tuple) -> None:
    # Определяю a DF как содержимое файла excel.
    data = pd.DataFrame(test_read_financial_trans_xlsx_data)
    mock_read_financial_trans_xlsx = Mock(return_value=data)
    pd.read_excel = mock_read_financial_trans_xlsx
    assert read_financial_trans_xlsx(f"{BASE_DIR}\\data\\transactions_excel.xlsx") == data.to_dict(orient="records")
