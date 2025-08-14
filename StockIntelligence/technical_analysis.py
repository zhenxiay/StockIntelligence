'''
This module contains functions for calculating technical indicators using the `ta` library.
It includes functions to calculate the Relative Strength Index (RSI) for given stock data.
'''

from ta.momentum import rsi

def calc_rsi(df_input, rsi_window):
    '''
    This function calculates the Relative Strength Index (RSI) for given stock data.

    Args:

    df_input (DataFrame): Input DataFrame containing stock data with a 'Close' column.
    rsi_window (list): List of integers representing the RSI calculation windows.
    '''
    for window in rsi_window:
        df_input[f'rsi_{window}'] = rsi(close= X["Close"],
                                 window= window,
                                 fillna= False)
    return df_input
