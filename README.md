
# 📋 StockIntelligence

Enables technical analysis and dashboarding using yfinance library in the background to fetch stock data.

Load data method to Google BigQuery availiable.

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/zhenxiay/StockIntelligence.git
cd StockIntelligence
```

## 📦 Installation Options

You can install this libary either with pip or uv. Choose the option that best suits your needs.

### Option 1: Install with pip install

Install using pip install:

```bash
pip install https://github.com/zhenxiay/StockIntelligence.git
```

### Option 2: Install with uv

#### Create a new directory for our project

⚙️ To add this libary to an existing uv project, pls skip the first 2 steps

```bash
uv init StockIntelligence
cd StockIntelligence
```

#### Create virtual environment and activate it

```bash
uv venv
source .venv/bin/activate
```

#### Install dependencies
```bash
uv add https://github.com/zhenxiay/StockIntelligence.git
```

## 🚀 Example load single stock data

```python
from StockIntelligence.get_stock_data import GetStockData

from StockIntelligence.load_stock_data import LoadStockData

GetStockData('MSFT', '5y').read_daily_data()  # availiable periods: ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

dataset = LoadStockData('MSFT',"5y","your_gcp_project","StockIntelligence")

dataset.load_stock_data_to_big_query('MSFT')
```

## 🚀 Example load multi stock data

```python
from StockIntelligence.load_multi_stock_data import LoadMultiStockData

stock_list = ['MSFT','ASML']


load_object = LoadMultiStockData(stock_list,
                                 "3mo",
                                 "your_gcp_project",
                                 "StockIntelligence")

                                 
load_object.load_multi_stock_data_to_big_query('Table_name')
```
