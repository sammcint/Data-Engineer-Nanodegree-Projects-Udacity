from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 sql_statement = "",
                 truncate=True,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.sql_statement = sql_statement
        self.redshift_conn_id = redshift_conn_id
        self.truncate = truncate


    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.truncate:
            redshift.run(f"TRUNCATE TABLE {self.table}")
            sql_statement = (f"INSERT INTO {self.table}{self.sql_statement}")
            redshift.run(sql_statement)
            self.log.info(f"Success: {self.task_id}")
        else:
            sql_statement = (f"INSERT INTO {self.table}{self.sql_statement}")
            redshift.run(sql_statement)        
            self.log.info(f"Success: {self.task_id}")
