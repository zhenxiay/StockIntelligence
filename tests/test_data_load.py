from StockIntelligence.get_stock_data import GetStockData
from StockIntelligence.load_stock_data import LoadStockData

def test_read_stock_data():
    dataset = GetStockData('MSFT', '3mo')
    columns_count = len(dataset.read_daily_data().columns)
    assert columns_count == 15

#Test that the an object can be created from the class load stock data
def test_load_stock_data():
    dataset = LoadStockData('MSFT',"3mo","bq_dataset_dummy","StockIntelligence")
    assert dataset.name == 'MSFT'

#@pytest.mark.parametrize("column", ['Close', 'Volume', 'rsi'])
#def test_column_dtype_is_float(column):
#    dataset = GetStockData('MSFT', '1d')
#    assert dataset[column].dtype == 'float64', f"Column {column} is not of type float64"
