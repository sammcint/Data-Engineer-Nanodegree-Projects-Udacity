from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 sql = "",
                 append_data = "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.sql = sql
        self.redshift_conn_id = redshift_conn_id
        self.append_data = append_data


    def execute(self, context):
        #self.log.info(f"Load Dimension Table: {self.table}")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.append_data == True:
            sql = (f"INSERT INTO {self.table}{self.sql}")
            redshift.run(sql)
        else:
            sql = (f"DELETE FROM {self.table}{self.sql}")
            redshift.run(sql)
            
