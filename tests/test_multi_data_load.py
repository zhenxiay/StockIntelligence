from StockIntelligence.get_stock_data import GetStockData
from StockIntelligence.load_multi_stock_data import LoadMultiStockData

#Test that the an object can be created from the class load stock data
def test_load_multi_stock_data():
    stock_list = ['MSFT','ASML']
    
    load_object = LoadMultiStockData(stock_list,
                                 "3mo",
                                 "bq_dataset_dummy",
                                 "StockIntelligence")

    dataset = load_object.reate_combinded_dataset(self, stock_list)
    assert dataset.name == 'MSFT'
