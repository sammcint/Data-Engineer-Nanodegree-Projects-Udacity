from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):
    ui_color = '#F98866'

    @apply_defaults
    def __init__(
        self,
        redshift_conn_id='',
        table_name='',
        sql_statement='',
        append_data = "",
        *args, **kwargs
    ):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table_name = table_name
        self.sql_statement = sql_statement
        self.append_data = append_data
    def execute(self, context):

        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.append_data == True:
            sql_statement = (f"INSERT INTO {self.table_name}{self.sql_statement}")
            redshift.run(sql_statement)
        else:
            sql_statement = (f"DELETE FROM {self.table_name}{self.sql_statement}")
            redshift.run(sql_statement)
        self.log.info('Fact table %s load finished' % self.table_name)
