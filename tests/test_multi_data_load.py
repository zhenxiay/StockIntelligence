from StockIntelligence.get_stock_data import GetStockData
from StockIntelligence.load__multi_stock_data import LoadMultiStockData

def test_read_multi_stock_data():
    dataset = GetStockData('MSFT', '3mo')
    columns_count = len(dataset.read_daily_data().columns)
    assert columns_count == 15

#Test that the an object can be created from the class load stock data
def test_load_stock_data():
    dataset = LoadStockData('MSFT',"3mo","bq_dataset_dummy","StockIntelligence")
    assert dataset.name == 'MSFT'
