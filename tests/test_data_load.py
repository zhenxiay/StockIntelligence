from StockIntelligence.get_stock_data import GetStockData

def test_read_team_adv_stats():
    dataset = GetStockData('MSFT', '3mo')
    columns_count = len(dataset.read_daily_data().columns)
    assert columns_count == 14

@pytest.mark.parametrize("column", ['Close', 'Volume', 'rsi'])
def test_column_dtype_is_float(column):
    dataset = GetStockData('MSFT', '1d')
    assert dataset[column].dtype == 'float64', f"Column {column} is not of type float64"
