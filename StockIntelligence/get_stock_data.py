'''
Define class for getting and displaying stock data
'''

import yfinance as yf
from curl_cffi import requests
from StockIntelligence.abstract.stock_data_abstract import StockDataStructure
from StockIntelligence.technical_analysis import calc_rsi

class GetStockData(StockDataStructure):
    '''
    Define class for getting stock data from Yahoo Finance using yfinance library.
    This class inherits from StockDataStructure and implements methods to read daily stock data, 
    calculate percentage changes, moving averages, and RSI (Relative Strength Index).
    '''    

    def __init__(self, name, load_period):
        self.name = name
        # availiable periods: ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.load_period = load_period
        self.analysis_periods = [7, 14, 30]
        self.rsi_window = [14, 21]

    def read_daily_data(self):
        """Read daily stock data from Yahoo Finance using yfinance library."""

        df_asset = yf.download(self.name,
                               period = self.load_period)

        def convert_multi_index(X, ticker):

            X = X.droplevel(1, axis=1)
            X = X.reset_index()
            X = X.rename_axis(None, axis=1)
            X['Ticker'] = ticker

            return X

        def calc_pct_delta(X):

            for period in self.analysis_periods:
                X[f'pct_delta_{period}_day'] = X['Close']\
                                               .pct_change(period)
            return X

        def calc_moving_avg(X):

            for period in self.analysis_periods:
                X[f'mavg_{period}_day'] = X['Close']\
                                          .rolling(window=period).mean()

            return X

        df_output = (df_asset
                     .pipe(convert_multi_index, Ticker = self.name)
                     .pipe(calc_pct_delta)
                     .pipe(calc_moving_avg)
                     .pipe(calc_rsi, rsi_window = self.rsi_window)
                    )

        return df_output
