from google.cloud import bigquery
import pandas as pd
import sqlite3
import logging
from StockIntelligence.get_stock_data import GetStockData
from StockIntelligence.db_utility.big_query_setup import create_big_query_client_full_load, create_big_query_client_append

class LoadMultiStockData():
    def __init__(self, stock_list, load_period, project, dataset):
        self.stock_list = stock_list
        self.load_period = load_period
        self.project = project
        self.dataset = dataset

    def create_combined_dataset(self, stock_list):
        combined_df = pd.DataFrame()
      
        for stock in self.stock_list:
            temp_df = GetStockData(stock, self.load_period).read_daily_data()
            combined_df = pd.concat([combined_df, temp_df])
            combined_df.reset_index(inplace=True)
          
        return combined_df

    def load_multi_stock_data_to_big_query(self, stock_list, table_name):

        dataset = self.create_combined_dataset(stock_list).drop('level_0', axis=1)
          
        table_id = f'{self.project}.{self.dataset}.{table_name}'
        client, job_config = create_big_query_client_full_load()
        client.load_table_from_dataframe(dataset, 
                                         table_id, 
                                         job_config=job_config)
        
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.info('Ingested rows: {len(dataset)} into {table_id}, table portfolio_analysis')

    def load_multi_stock_data_to_sqlite3(self, db_path, db_name, table_name):
        
        dataset = self.create_combined_dataset(stock_list).drop('level_0', axis=1)
        conn = sqlite3.connect(f'{db_path}/{db_name}')
        
        data.to_sql(
                     table_name,
                     con=conn,
                     if_exists="replace"
                    )

        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.info('Ingested rows: {len(dataset)} into {db_path}/{db_name}, table {table_name}')
        
