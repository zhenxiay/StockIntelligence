### StockIntelligence

Enables technical analysis and dashboarding using yfinance library in the background to fetch stock data.

Load data method to Google BigQuery availiable.

#### Example load single stock data
from StockIntelligence.get_stock_data import GetStockData

 from StockIntelligence.load_stock_data import LoadStockData

GetStockData('MSFT', '5y').read_daily_data()  -> availiable periods: ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

dataset = LoadStockData('MSFT',"5y","bq_project_dummy","StockIntelligence")

dataset.load_stock_data_to_big_query('MSFT')

#### Example load multi stock data
from StockIntelligence.load_multi_stock_data import LoadMultiStockData

stock_list = ['MSFT','ASML']


load_object = LoadMultiStockData(stock_list,
                                 "3mo",
                                 "bq_project_dummy",
                                 "StockIntelligence")

                                 
load_object.load_multi_stock_data_to_big_query()
