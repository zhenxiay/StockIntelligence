from StockIntelligence.get_stock_data import GetStockData
from StockIntelligence.load_multi_stock_data import LoadMultiStockData

stock_list = ['MSFT','ASML']
load_object = LoadMultiStockData(stock_list,
                                 "3mo",
                                 "bq_dataset_dummy",
                                 "StockIntelligence")

#Test that the an object can be created from the class load stock data
def test_read_multi_stock_data():

    dataset = load_object.create_combined_dataset()
    distinct_count = dataset['Ticker'].nunique()
    assert distinct_count == len(stock_list)

def test_load_multi_stock_data():
    load_object.load_multi_stock_data_to_sqlite3(db_path= '.',
                                                 db_name= 'stock_db',
                                                 table_name= 'test')
