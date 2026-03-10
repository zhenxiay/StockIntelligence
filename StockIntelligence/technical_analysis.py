'''
This module contains functions for calculating technical indicators using the `ta` library.
It includes functions to calculate the Relative Strength Index (RSI) for given stock data.
'''

from ta.momentum import rsi, williams_r

def calc_rsi(df_input, rsi_window):
    '''
    This function calculates the Relative Strength Index (RSI) for given stock data.

    Args:

    df_input (DataFrame): Input DataFrame containing stock data with a 'Close' column.
    rsi_window (list): List of integers representing the RSI calculation windows.
    '''
    for window in rsi_window:
        rsi_series = rsi(
            close= df_input["Close"],
            window= window,
            fillna= False
        )

        df_input = df_input.assign(**{f'rsi_{window}': rsi_series})

    return df_input

def calc_williams_r(df_input):
    '''
    Calculate Williams %R for given stock data.

    Args:

    df_input (DataFrame): Input DataFrame containing stock data with a 'Close' column.
    '''

    williams_r_series = williams_r(
        high=df_input["High"],
        low=df_input["Low"],
        close=df_input["Close"],
        fillna=False
    )

    df_input = df_input.assign(
        williams_r=williams_r_series
        )

    return df_input
