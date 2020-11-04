from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators import (StageJsonToRedshiftOperator, StageCSVToRedshiftOperator, PythonOperator)
from helpers import SqlQueries



s3_bucket = 'sammcint-capstone-bucket'
country_s3_key = "CapstoneData/country_names.json"
glt_by_country_s3_key = "CapstoneData/GlobalLandTemperaturesByCountry.csv"
glt_by_state_s3_key = "CapstoneData/GlobalLandTemperaturesByState.csv"
happiness_by_country_s3_key = "CapstoneData/HappinessRanksByCountry2019.csv"



def create_table(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    queries =  open("/home/workspace/airflow/capstone_create_tables.sql", "r").read()
    redshift_hook.run(queries)        
    return


default_args = {
    'owner': 'udacity',
    'start_date': datetime(2020, 10, 30),
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
          schedule_interval='0 * * * *'
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

stage_countrynames_to_redshift = StageJsonToRedshiftOperator(
    task_id='country_names',
    dag=dag,
    table="CountryNames",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket = s3_bucket,
    s3_key = country_s3_key,
    copy_json_option='auto'
)

stage_glt_by_country_to_redshift = StageCSVToRedshiftOperator(
    task_id='glt_by_country',
    dag=dag,
    table="GlobalLandTemperaturesByCountry",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket = s3_bucket,
    s3_key = glt_by_country_s3_key

)



start_operator >> stage_countrynames_to_redshift
start_operator >> stage_glt_by_country_to_redshift