from google.cloud import bigquery

def create_big_query_client_full_load():
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    return client, job_config
  
def create_big_query_client_append():
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    return client, job_config
