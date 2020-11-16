from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 aws_credentials_id="",
                 redshift_conn_id="",
                 tables=[],
                 sql_query="",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)

        self.aws_credentials_id = aws_credentials_id
        self.redshift_conn_id = redshift_conn_id
        self.tables = tables
        self.sql_query = sql_query

    def execute(self, context): 
        redshift_hook = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        for tables in self.tables:  
            self.log.info(f"Starting data quality validation on tables : {tables}")
            records = redshift_hook.get_records(f"select count(*) from {tables};")
            if len(records) < 1 or len(records[0]) < 1 or records[0][0] < 1:
                self.log.error(f"Data Quality validated failed for tables: {tables}")
            else:
                self.log.info(f"Data Quality Validated Passed on Tables : {tables}")
