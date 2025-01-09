from ta.momentum import rsi

def calc_rsi(X, rsi_window):
    X['rsi'] = rsi(close= X["Close"], 
                 window= rsi_window, 
                 fillna= False)
    return X
