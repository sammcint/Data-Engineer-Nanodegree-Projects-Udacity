from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators import (StageCSVToRedshiftOperator, PythonOperator, LoadReferenceOperator, StageJsonToRedshiftOperator, LoadHistoricalStocksOperator, DataQualityOperator)
from helpers import SqlQueries



s3_bucket = 'sammcint-capstone-bucket'
historical_stock_prices_s3_key = "CapstoneData/historical_stock_prices.csv"
historical_stocks_s3_key = "CapstoneData/historical_stocks.csv" 
sectors_s3_key = "CapstoneData/Sectors.json"

def create_table(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    queries =  open("/home/workspace/airflow/capstone_create_tables.sql", "r").read()
    redshift_hook.run(queries)        
    return


default_args = {
    'owner': 'udacity',
    'start_date': datetime(2020, 11, 10),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries':0,
    'retry_delay':timedelta(minutes=1),
    'catchup': False
}


dag = DAG('capstone_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval = '@once'
          #schedule_interval='0 * * * *'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

create_tables_in_redshift = PythonOperator(
    task_id = "create_tables_in_redshift",
    redshift_conn_id = "redshift",
    aws_credentials_id="aws_credentials",    
    dag = dag,
    provide_context=True,
    python_callable=create_table
)



stage_historical_stock_prices_to_redshift = StageCSVToRedshiftOperator(
    task_id='historical_stock_prices',
    dag=dag,
    table="HistoricalStockPrices",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket = s3_bucket,
    s3_key = historical_stock_prices_s3_key

)



historical_stocks_staging_to_redshift = StageCSVToRedshiftOperator(
    task_id='historical_stocks_staging',
    dag=dag,
    table="HistoricalStocksStaging",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket = s3_bucket,
    s3_key = historical_stocks_s3_key

)



stage_sectors_to_redshift = StageJsonToRedshiftOperator(
    task_id='Sectors',
    dag=dag,
    table="Sectors",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket = s3_bucket,
    s3_key = sectors_s3_key,
    iam_role = 'arn:aws:iam::280184132493:role/myRedshiftRole'
)



stage_industries_to_redshift = LoadReferenceOperator(
    task_id='Industry',
    table="Industries",
    redshift_conn_id="redshift",
    truncate_table=True,
    aws_credentials_id="aws_credentials",
    sql_statement = SqlQueries.industries_table_insert, 
    dag=dag 
)    


historical_stocks_to_redshift = LoadHistoricalStocksOperator(
    task_id='historical_stocks',
    table="HistoricalStocks",
    redshift_conn_id="redshift",
    truncate_table=True,
    aws_credentials_id="aws_credentials",
    sql_statement = SqlQueries.historical_stocks_insert, 
    dag=dag 
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id="redshift",   
    tables=["historicalstockprices",
            "historicalstocks",
            "industries",
            "sectors"]
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)
    
start_operator >> create_tables_in_redshift
create_tables_in_redshift >> stage_historical_stock_prices_to_redshift
create_tables_in_redshift >> historical_stocks_staging_to_redshift
create_tables_in_redshift >> stage_sectors_to_redshift
create_tables_in_redshift >> stage_industries_to_redshift
historical_stocks_staging_to_redshift >> stage_industries_to_redshift
historical_stocks_staging_to_redshift >> historical_stocks_to_redshift
stage_sectors_to_redshift >> historical_stocks_to_redshift
stage_industries_to_redshift >> historical_stocks_to_redshift
create_tables_in_redshift >> historical_stocks_to_redshift
run_quality_checks << historical_stocks_to_redshift
run_quality_checks << stage_historical_stock_prices_to_redshift
run_quality_checks << stage_sectors_to_redshift
run_quality_checks << stage_industries_to_redshift      