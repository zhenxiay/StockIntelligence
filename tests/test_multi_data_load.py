from StockIntelligence.get_stock_data import GetStockData
from StockIntelligence.load_multi_stock_data import LoadMultiStockData

#Test that the an object can be created from the class load stock data
def test_load_multi_stock_data():
    stock_list = ['MSFT','ASML']
    
    load_object = LoadMultiStockData(stock_list,
                                 "3mo",
                                 "bq_dataset_dummy",
                                 "StockIntelligence")

    dataset = load_object.create_combined_dataset(stock_list)
    distinct_count = dataset['Ticker'].nunique()
    assert distinct_count == len(stock_list)
