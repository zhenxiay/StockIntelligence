'''
This module is used to load multiple stock data into BigQuery or SQLite3.
It combines data from multiple stocks, processes it, and loads it into the specified database.
'''

from google.cloud import bigquery
import pandas as pd
import sqlite3
from StockIntelligence.get_stock_data import GetStockData
from StockIntelligence.db_utility.logger import log_function
from StockIntelligence.db_utility.big_query_setup import create_big_query_client_full_load, create_big_query_client_append

class LoadMultiStockData():
    '''
    Create a loader with multiple stock data.
    This class is used to load multiple stock data into BigQuery or SQLite3.
    '''
    def __init__(self, stock_list, load_period, project, dataset):
        self.stock_list = stock_list
        self.load_period = load_period
        self.project = project
        self.dataset = dataset

    @log_function
    def create_combined_dataset(self, logger):
        '''
        Crete a combined dataset from multiple stock data.
        '''
        combined_df = pd.DataFrame()

        for stock in self.stock_list:
            temp_df = GetStockData(stock, self.load_period).read_daily_data()
            combined_df = pd.concat([combined_df, temp_df])
            combined_df.reset_index(drop=True)

        logger.info(f'Dataframe created for {self.stock_list} with {len(combined_df)} rows...')

        return combined_df

    @log_function
    def load_multi_stock_data_to_big_query(self, logger, table_name):
        '''
        This function loads the combined dataset into BigQuery.
        '''
        dataset = self.create_combined_dataset()

        table_id = f'{self.project}.{self.dataset}.{table_name}'
        client, job_config = create_big_query_client_full_load()
        client.load_table_from_dataframe(dataset, 
                                         table_id, 
                                         job_config=job_config)

        logger.info(f'Ingested rows: {len(dataset)} into {table_id}, table {table_name}')

    @log_function
    def load_multi_stock_data_to_sqlite3(self, logger, db_path, db_name, table_name):
        '''
        This function loads the combined dataset into a sqlite db.
        '''

        conn = sqlite3.connect(f'{db_path}/{db_name}')

        dataset = self.create_combined_dataset()

        dataset.to_sql(
                     table_name,
                     con=conn,
                     if_exists="replace"
                    )

        logger.info(f'Ingested rows: {len(dataset)} into {db_path}/{db_name}, table {table_name}')
