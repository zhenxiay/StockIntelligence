from StockIntelligence.load_multi_stock_data import LoadMultiStockData

stock_list = ['MSFT','NVDA','SNOW','TEAM','ASML']

load_object = LoadMultiStockData(stock_list, 
                                 "2y", 
                                 "keen-vial-420113", 
                                 "StockIntelligence")

load_object.load_multi_stock_data_to_big_query(
                                  table_name='portfolio_analysis')