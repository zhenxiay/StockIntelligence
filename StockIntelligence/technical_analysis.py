from ta.momentum import rsi

def calc_rsi(X, rsi_window):
    for window in rsi_window:
        X[f'rsi_{window}'] = rsi(close= X["Close"], 
                                 window= window, 
                                 fillna= False)
    return X
