'''
This module is used to load single stock data into BigQuery.
'''

from google.cloud import bigquery
from StockIntelligence.get_stock_data import GetStockData
from StockIntelligence.db_utility.big_query_setup import create_big_query_client_full_load, create_big_query_client_append
from StockIntelligence.db_utility.logger import log_function

class LoadStockData():
    '''
    Create a loader with single stock data.
    '''
    def __init__(self, name, load_period, project, dataset):
        self.name = name
        self.load_period = load_period
        self.project = project
        self.dataset = dataset
    
    @log_function
    def load_stock_data_to_big_query(self,logger,table_name):
        '''
        This function reads and loads the dataset of a single stock into BigQuery.
        Load mode is full load, meaning it will overwrite the existing table.
        '''
        dataset = GetStockData(self.name, self.load_period).read_daily_data()
        table_id = f'{self.project}.{self.dataset}.{table_name}'
        client, job_config = create_big_query_client_full_load()
        client.load_table_from_dataframe(dataset, table_id, job_config=job_config)
        logger.info(f'Data load to big query {table_id} successfully!')
    
    @log_function
    def load_stock_data_to_big_query_incremental(self,logger,table_name):
        '''
        This function reads and loads the dataset of a single stock into BigQuery.
        Load mode is incremental load, which only loads the latest daily data to the dataset.
        '''
        # fetch the last row of data frame for append
        dataset = GetStockData(self.name, self.load_period).read_daily_data().tail(1)
        table_id = f'{self.project}.{self.dataset}.{table_name}'
        # use job config for append data load in big query
        client, job_config = create_big_query_client_append()
        client.load_table_from_dataframe(dataset, table_id, job_config=job_config)
        logger.info(f'Data load to big query {table_id} successfully! Number of loaded rows: {len(dataset)}...')
