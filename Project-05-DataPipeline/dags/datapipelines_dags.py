from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators import (StageToRedshiftOperator, 
                                LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator, PythonOperator)
from helpers import SqlQueries


AWS_KEY = os.environ.get('')
AWS_SECRET = os.environ.get('')

s3_bucket = 'udacity-dend'
song_s3_key = "song_data"
log_s3_key = "log_data"
log_json_file = "s3://udacity-dend/log_json_path.json"
#log_json_file = "s3://udacity-dend/song_data/A/A/A"



def create_table(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    queries =  open("/home/workspace/airflow/create_tables.sql", "r").read()
    redshift_hook.run(queries)        
    return


default_args = {
    'owner': 'udacity',
    'start_date': datetime(2020, 9, 9),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries':3,
    'retry_delay':timedelta(minutes=5),
    'catchup': False
}


dag = DAG('sparkify_dag',
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



stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag,
    table="staging_events",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket = s3_bucket,
    s3_key = log_s3_key,
    file_format="JSON",
    log_json_file = log_json_file
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    dag=dag,
    table="staging_songs",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket = s3_bucket,
    s3_key = song_s3_key,
    file_format="JSON"

)

load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    table_name ="songplays",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    sql_statement = SqlQueries.songplay_table_insert, 
    append_data=True,
    dag=dag
)

load_user_dimension_table = LoadDimensionOperator(
    task_id='Load_user_dim_table',
    table="users",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    sql = SqlQueries.user_table_insert, 
    append_data=True,
    dag=dag
)

load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    table="songs",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    sql = SqlQueries.song_table_insert, 
    append_data=True,
    dag=dag
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    table="artists",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    sql = SqlQueries.artist_table_insert, 
    append_data=True,
    dag=dag
)

load_time_dimension_table = LoadDimensionOperator(
    task_id='Load_time_dim_table',
    table="time",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    sql = SqlQueries.time_table_insert, 
    append_data=True,
    dag=dag 
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id="redshift",
    tables=["users",
            "songs",
            "artists",
            "time",
            "songplays"]
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> stage_events_to_redshift
start_operator >> stage_songs_to_redshift
stage_events_to_redshift >> load_songplays_table
stage_songs_to_redshift >> load_songplays_table
load_songplays_table >> load_song_dimension_table 
load_songplays_table >> load_user_dimension_table
load_songplays_table >> load_artist_dimension_table
load_songplays_table >> load_time_dimension_table
run_quality_checks << load_song_dimension_table 
run_quality_checks << load_user_dimension_table
run_quality_checks << load_artist_dimension_table
run_quality_checks <<  load_time_dimension_table
run_quality_checks >> end_operator
