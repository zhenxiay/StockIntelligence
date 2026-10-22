'''
Main API module for the FastAPI application.
Provides endpoints for root and item retrieval.
'''
import os
import sys
from fastapi import FastAPI

from StockIntelligence.get_stock_data import GetStockData

# Create fastapi app
app = FastAPI()

# Define endpoints
@app.get("/")
def read_root():
    '''
    Root endpoint that returns a simple greeting.
    '''
    return {"Hello": "World"}

@app.get("/stock/daily/{ticker}")
def get_stock_daily(
    ticker: str = "MSFT",
    range: str = "5d",
    ):
    '''
    Endpoint to retrieve daily stock data for a specific ticker.

    Args:
        ticker (str, optional): Stock ticker symbol. Defaults to "MSFT".

    Returns:
        dict: Dictionary representation of the daily stock data.
    '''
    dataset = GetStockData(name=ticker, load_period=range)
    df = dataset.read_daily_data().fillna('')

    return df.to_dict()

def run_api():
    '''
    Function to run the FastAPI application using Uvicorn.
    '''
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run_api()