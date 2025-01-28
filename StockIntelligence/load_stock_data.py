from google.cloud import bigquery
from StockIntelligence.get_stock_data import GetStockData

class LoadStockData(GetStockData):
    def __init__(self, name, load_period, project, dataset_name):
        super().__init__(name=name, load_period=load_period)
        self.project = project
        self.dataset_name = dataset_name

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

    @staticmethod
    def data_ingestion_big_query_client_full_load(self,dataset,table_name) -> None:
        table_id = f'{self.project}.{self.dataset_name}.{table_name}'
        client, job_config = self.create_big_query_client_full_load()
        client.load_table_from_dataframe(dataset, table_id, job_config=job_config)
        print(f'Data load to big query {table_id} successfully!')        

    @staticmethod
    def data_ingestion_big_query_client_append(self,dataset,table_name) -> None:
        table_id = f'{self.project}.{self.dataset_name}.{table_name}'
        client, job_config = self.create_big_query_client_append()
        client.load_table_from_dataframe(dataset, table_id, job_config=job_config)
        print(f'Data load to big query {table_id} successfully! Number of loaded rows: {len(dataset)}...')
    
    ############ Methods of loading single ticker into a dedicated table ######################
    def load_stock_data_to_big_query(self,table_name):
        dataset = GetStockData(self.name, self.load_period).read_daily_data()
        self.data_ingestion_big_query_client_full_load(dataset,table_name)

    def load_stock_data_to_big_query_incremental(self,table_name):
        # fetch the last row of data frame for append
        dataset = GetStockData(self.name, self.load_period).read_daily_data().tail(1)
        # use append method to do incremental load in big query
        self.data_ingestion_big_query_client_append(dataset,table_name)
        
