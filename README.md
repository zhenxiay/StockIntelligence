#### StockIntelligence

Enables technical analysis and dashboarding using yfinance library in the background to fetch stock data.

Load data method to Google BigQuery availiable.

##### Examples

GetStockData('MSFT', '5y').read_daily_data()  -> availiable periods: ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

            Close	      High	      Low	        Open	      Volume	  Ticker pct_delta_7_day	pct_delta_14_day	pct_delta_30_day	mavg_7_day	mavg_14_day	mavg_30_day
2025-01-06	427.850006	434.320007	425.480011	428.000000	20545900	MSFT	-2.61%	          -4.34%	          2.97%	            426.392853	434.028569	434.015331
2025-01-07	425.859985	430.649994	425.200012	429.429993	5359226	  MSFT	-2.80%	         -5.70%	            3.15%	            424.642853	432.190711	434.448331
