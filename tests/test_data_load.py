from StockIntelligence.get_stock_data import GetStockData

def test_read_team_adv_stats():
  
	dataset = GetStockData('MSFT', '1d')
	columns_count = len(dataset.read_daily_data().columns)
	assert columns_count == 13
