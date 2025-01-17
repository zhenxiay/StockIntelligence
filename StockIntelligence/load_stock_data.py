from google.cloud import bigquery
from StockIntelligence.get_stock_data import GetStockData

class LoadStockData(GetStockData):
    def __init__(self, name, load_period, project, dataset):
        super().__init__(name=name, load_period=load_period)
        self.project = project
        self.dataset = dataset

    @staticmethod
    def create_big_query_client_full_load():
        client = bigquery.Client()
        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
        return client, job_config

    @staticmethod
    def create_big_query_client_append():
        client = bigquery.Client()
        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
        return client, job_config

    def load_stock_data_to_big_query(self,table_name):
        dataset = GetStockData(self.name, self.load_period).read_daily_data()
        table_id = f'{self.project}.{self.dataset}.{table_name}'
        client, job_config = self.create_big_query_client_full_load()
        client.load_table_from_dataframe(dataset, table_id, job_config=job_config)
        print(f'Data load to big query {table_id} successfully!')

    def load_stock_data_to_big_query_incremental(self,table_name):
        # fetch the last row of data frame for append
        dataset = GetStockData(self.name, self.load_period).read_daily_data().tail(1)
        table_id = f'{self.project}.{self.dataset}.{table_name}'
        # use job config for append data load in big query
        client, job_config = self.create_big_query_client_append()
        client.load_table_from_dataframe(dataset, table_id, job_config=job_config)
        print(f'Data load to big query {table_id} successfully! Number of loaded rows: {len(dataset)}...')
