from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook



class StageJsonToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    sql_template_json = """
        COPY {}
        FROM '{}'
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        FORMAT AS JSON '{}' 
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credentials_id="",
                 table="",
                 s3_bucket="",
                 s3_key="",
                 copy_json_option="auto",
                 *args, **kwargs):

        super(StageJsonToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id
        self.table = table
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.copy_json_option = copy_json_option        


    def execute(self, context):
        # AWS connection
        self.log.info("Connecting to S3")
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        s3_path = "s3://{}/{}".format(
            self.s3_bucket,
            self.s3_key
        )

        # Redshift Conn
        self.log.info("Connecting to Redshift")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        # Clear existing data from Redshift staging table
        clear_msg = "Deleting old records in table {} from redshift"
        self.log.info(clear_msg.format(self.table))
        redshift.run("DELETE FROM {}".format(self.table))

        # Copy data from S3 to Redshift
        self.log.info("Copying specified data to table")
        copy_data_sql = StageJsonToRedshiftOperator.sql_template_json.format(
            self.table,
            s3_path,
            credentials.access_key,
            credentials.secret_key,
            self.copy_json_option            
        )

        redshift.run(copy_data_sql)
        self.log.info("Copying to table complete")
        
        
