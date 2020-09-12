import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')


# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplays_table_drop = "DROP TABLE IF EXISTS songplays"
users_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artists_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""  CREATE TABLE IF NOT EXISTS staging_events (artist        VARCHAR, 
                                                                              auth          VARCHAR, 
                                                                              firstName     VARCHAR, 
                                                                              gender        VARCHAR, 
                                                                              itemInSession INT,
                                                                              lastName      VARCHAR, 
                                                                              length        FLOAT, 
                                                                              level         VARCHAR,
                                                                              location      VARCHAR, 
                                                                              method        VARCHAR,
                                                                              page          VARCHAR, 
                                                                              registration  FLOAT, 
                                                                              sessionId     INT, 
                                                                              song          VARCHAR,
                                                                              status        INT, 
                                                                              ts            BIGINT, 
                                                                              userAgent     VARCHAR 
                                                                              ,userId       INT)                                 
""")




staging_songs_table_create = (""" CREATE TABLE IF NOT EXISTS staging_songs(num_songs           INTEGER,
                                                                           artist_id           VARCHAR,
                                                                           artist_latitude     NUMERIC,
                                                                           artist_longitude    NUMERIC,
                                                                           artist_location     VARCHAR,
                                                                           artist_name         VARCHAR,
                                                                           song_id             VARCHAR,
                                                                           title               VARCHAR,
                                                                           duration            NUMERIC,
                                                                           year                INTEGER)
""")







songplays_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id INTEGER IDENTITY(0,1) PRIMARY KEY, 
                                                                   start_time  TIMESTAMP NOT NULL, 
                                                                   user_id     INT NOT NULL, 
                                                                   level       VARCHAR, 
                                                                   song_id     VARCHAR, 
                                                                   artist_id   VARCHAR, 
                                                                   session_id  INT, 
                                                                   location    VARCHAR, 
                                                                   user_agent  VARCHAR)""")

users_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id    INT PRIMARY KEY, 
                                                           first_name VARCHAR, 
                                                           last_name  VARCHAR, 
                                                           gender     VARCHAR, 
                                                           level      VARCHAR)""")

songs_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id   VARCHAR PRIMARY KEY, 
                                                           title     VARCHAR, 
                                                           artist_id VARCHAR, 
                                                           year      INT, 
                                                           duration  NUMERIC)""")

artists_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR PRIMARY KEY, 
                                                               name      VARCHAR, 
                                                               location  VARCHAR, 
                                                               latitude  NUMERIC, 
                                                               longitude NUMERIC)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMP PRIMARY KEY, 
                                                         hour       INT, 
                                                         day        INT, 
                                                         week       INT, 
                                                         month      INT, 
                                                         year       INT, 
                                                         weekday    INT)""")



## For COPY : 

staging_events_copy = ("""
                            COPY staging_events
                            FROM {}
                            IAM_ROLE {}
                            REGION 'us-west-2'
                            FORMAT AS JSON {} 
                            TIMEFORMAT 'epochmillisecs';
                      """).format(config['S3']['LOG_DATA'],
                                  config['IAM_ROLE']['ARN'],
                                  config['S3']['LOG_JSONPATH'])
staging_songs_copy = ("""
                           COPY staging_songs
                           FROM {}
                           IAM_ROLE {}
                           REGION 'us-west-2'
                           FORMAT AS JSON 'auto';
                      """).format(config['S3']['SONG_DATA'],
                                  config['IAM_ROLE']['ARN'],)


# FINAL TABLES

songplays_table_insert = ("""INSERT into songplays(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent)
SELECT DISTINCT timestamp 'epoch' + staging_events.ts/1000 * interval '1 second' AS start_time,
staging_events.userId,
staging_events.level,
staging_songs.song_id,
staging_songs.artist_id,
staging_events.sessionId,
staging_events.location,
staging_events.userAgent
FROM staging_events
LEFT JOIN staging_songs
ON (staging_events.artist=staging_songs.artist_name
AND staging_events.song=staging_songs.title)
WHERE staging_events.page='NextSong';
""")

users_table_insert = ("""INSERT INTO users (user_id,first_name, last_name,gender,level)
SELECT DISTINCT userId,firstName,lastName,gender,level
FROM staging_events
WHERE page='NextSong';
""")

songs_table_insert = ("""INSERT INTO songs (song_id,title,artist_id,year,duration)
SELECT DISTINCT song_id,title,artist_id,year,duration
FROM staging_songs
""")

artists_table_insert = ("""INSERT INTO artists (artist_id,name,location,latitude,longitude)
SELECT DISTINCT artist_id, artist_name, artist_location, artist_latitude, artist_longitude
FROM staging_songs
""")

time_table_insert = ("""INSERT INTO time(start_time,hour,day,week,month,year)
SELECT DISTINCT start_time, EXTRACT (hour FROM start_time), 
EXTRACT (day FROM start_time), 
EXTRACT (week FROM start_time),
EXTRACT (month FROM start_time),
EXTRACT (year FROM start_time)
FROM songplays;
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplays_table_create, users_table_create, songs_table_create, artists_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplays_table_drop, users_table_drop, songs_table_drop, artists_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplays_table_insert, users_table_insert, songs_table_insert, artists_table_insert, time_table_insert]


