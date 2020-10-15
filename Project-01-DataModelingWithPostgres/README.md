# Data Modeling with Postgres


## Introduction
------------------------------------------------
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. My role was to create a database schema and ETL pipeline for this analysis.

## Project Description
------------------------------------------------
For this project, I applied what I learned on data modeling with Postgres and built an ETL pipeline using Python. I defined fact and dimension tables for a star schema, and wrote an ETL pipeline that transfers data from files in two local directories into tables in Postgres using Python and SQL.

The purpose of creating this database was so that Sparkify could have an easier way of analyzing their data that they have been collecting on songs and user activity in their new music streaming app.Previously, there wasn't an easy way for them to query their data, because it was all stored in JSON logs as well as a directory with JSON metadata. Now, with the creation of the fact and dimension tables, as well as the ETL pipeline that transfers data from files into the new tables, Sparkify will be able to analyze their data at a much greater speed.

## Project Template
------------------------------------------------
For this project, I created a star schema which included a Fact table as well as several dimension tables. The fact table was 'songplays' which included key links to the other dimension tables 
such as start_time, user_id, song_id, artist_id.

Fact Table:
- **Songplays**
    - records in log data associated with song plays i.e. records with page **NextSong**
        - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
        
Dimension Tables:
- **users** 
    - users in music database  
        - user_id, first_name, last_name, gender, level
- **songs** 
    - songs in music database 
        - song_id, title, artist_id, year, duration
- **artists** 
    - artists in music database 
        - artist_id, name, location, latitude, longitude
- **time** 
    - timestamps of records in songplays broken down into specific units 
        - start_time, hour, day, week, month, year, weekday

## Project Structure
------------------------------------------------

Files used for this project:
* **data:** folder nested at the home of the project, where all needed jsons reside.
    * *Song datasets:* all json files are nested in subdirectories under /data/song_data. A sample of this files is:
        >{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
    * *Log datasets:* all json files are nested in subdirectories under /data/log_data. A sample of a single row of each files is:
        >{"artist":"Slipknot","auth":"Logged In","firstName":"Aiden","gender":"M","itemInSession":0,"lastName":"Ramirez","length":192}
* **test.ipynb:** displays the first few rows of each table to let you check your database.
* **create_tables.py:** drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
* **etl.ipynb:** reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
* **etl.py:** reads and processes files from *song_data* and *log_data* and loads them into your tables. You can fill this out based on your work in the ETL notebook.
* **sql_queries.py:** contains all your sql queries, and is imported into the last three files above.
* **README.md:** provides description on the project.

# Project Steps
------------------------------------------------
1. **Created Tables**
    1. Wrote CREATE statements in sql_queries.py to create each table.
    1. Wrote DROP statements in sql_queries.py to drop each table if it already existed.
    1. Ran create_tables.py to create database and tables.
    1. Ran test.ipynb to confirm the creation of tables with the correct columns. 
1. **Built ETL Processes**
    1. Followed instructions in the etl.ipynb notebook to develop ETL processes for each table.
1. **Built ETL Pipeline**
    1. Used what was completed in etl.ipynb to complete etl.py, where entire datasets were processed.
