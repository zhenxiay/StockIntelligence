### StockIntelligence

Enables technical analysis and dashboarding using yfinance library in the background to fetch stock data.

Load data method to Google BigQuery availiable.

#### Examples

GetStockData('MSFT', '5y').read_daily_data()  -> availiable periods: ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
