import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    song_data = input_data + "song_data/*/*/*/*.json"

    print("Song data variable successfully created")
    # read song data file
    df = spark.read.json(song_data).dropDuplicates()
    print("Song data schema:") 
    df.printSchema() #can delete
    print("Total records in song data is: ") #can delete
    print(df.count()) #can delete
    df.createOrReplaceTempView("songs_table_DF")
    # extract columns to create songs table
    songs_table = spark.sql("""
        SELECT song_id, title, artist_id, year, duration, artist_name
        FROM songs_table_DF
        ORDER BY song_id
    """)

    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.partitionBy("year", "artist_name").mode("overwrite").parquet("songs.parquet")
    
    # extract columns to create artists table
    artists_table = df_song.withColumn("artist_id",col("artist_id")).where(col("artist_id").isNotNull())
    
    # write artists table to parquet files
    artists_table.write.mode("overwrite").parquet("artists.parquet")


def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data = "s3a://udacity-dend/log-data/*/*/*.json"

    # read log data file
    df = spark.read.format("json").load(log_data)
    
    # filter by actions for song plays
    df_log = df.filter(df.page == "NextSong")

    # extract columns for users table    

    users_table = users_table.drop_duplicates(subset=['userId'])
    
    # write users table to parquet files
    users_table.write.mode("overwrite").parquet("users.parquet")

    # create timestamp column from original timestamp column
    get_timestamp = F.udf(lambda x: datetime.fromtimestamp( (x/1000.0) ), T.TimestampType()) 
    df = df.withColumn("timestamp", get_timestamp(df.ts))
    
    # create datetime column from original timestamp column
    get_datetime = F.udf(lambda x: datetime.fromtimestamp(int(x)),T.DateType())
    df = df.withColumn("datetime", get_timestamp(df.ts))
    
    # extract columns to create time table
    time_table = df.select("ts","datetime","timestamp",
                           year(df.datetime).alias("year"),
                           month(df.datetime).alias("month")
                          ).dropDuplicates()
    
    # write time table to parquet files partitioned by year and month
    time_table.write.partitionBy("year", "month").mode("overwrite").parquet("time_table.parquet")

    # read in song data to use for songplays table
    song_data = input_data + "song_data/*/*/*/*.json"
    song_df = spark.read.format("json").load(song_data)
    songplays_table = df.join(song_df, (df.song == song_df.title) & (df.artist == song_df.artist_name) & (df.length == song_df.duration), 'left_outer')\
        .select(
            df.start_time,
            col("userId").alias('user_id'),
            df.level,
            song_df.song_id,
            song_df.artist_id,
            col("sessionId").alias("session_id"),
            df.location,
            col("useragent").alias("user_agent"),
            year('datetime').alias('year'),
            month('datetime').alias('month')
        )
    # extract columns from joined song and log datasets to create songplays table
    '''
    songplays_table = df.join(song_df, (df.song == song_df.title) & (df.artist == song_df.artist_name) & (df.length == song_df.duration), "inner")\
        .select(
            df.timestamp,
            col("userId").alias("user_id"),
            df.level,
            song_df.song_id,
            song_df.artist_id,
            col("sessionId").alias("session_id"),
            df.location,
            col("useragent").alias("user_agent"),
            time_table.year.alias("year"),
            time_table.month.alias("month")
        )
'''
    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.partitionBy("year", "month").parquet(os.path.join(output_data,'songplay_parquet'),mode = 'overwrite')


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/song-data/"
    output_data = "s3a://udacity-dend/log-data/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
