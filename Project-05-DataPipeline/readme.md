# Introduction

# Project: Data Pipelines with Airflow

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring me onto the project and expect the creation of high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

This project introduced me to the core concepts of Apache Airflow. To complete the project, I created my own custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step.

# Datasets

For this project, I worked with two datasets. Here are the s3 links for each:

- Log data: s3://udacity-dend/log_data
- Song data: s3://udacity-dend/song_data

# Project Template

The project template package contains three major components for the project:

- The dag template has all the imports and task templates in place, but the task dependencies have not been set
- The operators folder with operator templates
- A helper class for the SQL transformations

Configuring the DAG
In the DAG, add default parameters according to these guidelines

- The DAG does not have dependencies on past runs
- On failure, the task are retried 3 times
- Retries happen every 5 minutes
- Catchup is turned off
- Do not email on retry
- In addition, configure the task dependencies so that after the dependencies are set, the graph view follows the flow shown in the image below.

Final DAG:


![](https://github.com/sammcint/Data-Engineer-Nanodegree-Projects-Udacity/blob/master/images/sparkify_dag.PNG)
