import pandas as pd
import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock

import StockIntelligence.api as api


@pytest.fixture
def client():
    return TestClient(api.app)


def _install_stock_data_mock(monkeypatch, dataframe):
    dataset = Mock()
    dataset.read_daily_data.return_value = dataframe
    get_stock_data = Mock(return_value=dataset)
    monkeypatch.setattr(api, "GetStockData", get_stock_data)
    return get_stock_data, dataset


def _expected_json(dataframe):
    # DataFrame.to_dict() uses integer row indexes; JSON object keys are strings.
    return {
        column: {str(index): value for index, value in values.items()}
        for column, values in dataframe.fillna("").to_dict().items()
    }


def test_read_root_returns_greeting(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_stock_daily_uses_default_range_and_returns_data(
    client, monkeypatch
):
    dataframe = pd.DataFrame(
        {"Close": [100.5, None], "Volume": [1000, 2000]},
        index=[0, 1],
    )
    get_stock_data, dataset = _install_stock_data_mock(monkeypatch, dataframe)

    response = client.get("/stock/daily/MSFT")

    assert response.status_code == 200
    assert response.json() == _expected_json(dataframe)
    get_stock_data.assert_called_once_with(name="MSFT", load_period="5d")
    dataset.read_daily_data.assert_called_once_with()


def test_get_stock_daily_accepts_custom_range(client, monkeypatch):
    dataframe = pd.DataFrame({"Close": [100.5]}, index=[0])
    get_stock_data, _ = _install_stock_data_mock(monkeypatch, dataframe)

    response = client.get("/stock/daily/MSFT", params={"range": "1mo"})

    assert response.status_code == 200
    assert response.json() == _expected_json(dataframe)
    get_stock_data.assert_called_once_with(name="MSFT", load_period="1mo")
