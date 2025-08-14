'''
This module provides functions to create a BigQuery client with full load or append operations.
'''

from google.cloud import bigquery

def create_big_query_client_full_load():
    '''
    This function creates a BigQuery client and configures it for full load operations.
    '''
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    return client, job_config

def create_big_query_client_append():
    '''
    This function creates a BigQuery client and configures it for incremental load operations.
    '''
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    return client, job_config
