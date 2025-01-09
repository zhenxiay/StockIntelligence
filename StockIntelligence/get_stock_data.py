import yfinance as yf
from StockIntelligence.stock_data_abstract import StockDataStructure
from StockIntelligence.technical_analysis import calc_rsi

#Define class for getting and displaying stock data
class GetStockData(StockDataStructure):
    
    def __init__(self, name, load_period):
        self.name = name
        # availiable periods: ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.load_period = load_period
        self.analysis_periods = [7, 14, 30]
        self.rsi_window = [14, 21]
          
    def read_daily_data(self):
        
        df_asset = yf.download(self.name, 
                               period = self.load_period)
        
        def convert_multi_index(X, Ticker):
            
            X = X.droplevel(1, axis=1)
            X = X.reset_index()
            X = X.rename_axis(None, axis=1)
            X['Ticker'] = Ticker
            
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
