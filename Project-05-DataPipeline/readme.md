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

# Add Airflow Connections 

Here, we'll use Airflow's UI to configure AWS credentials and connection to Redshift

1. Click on the **Admin** tab and select **Connections**
![](https://github.com/sammcint/Data-Engineer-Nanodegree-Projects-Udacity/blob/master/images/AirflowConnection1.PNG)

1. Under **Connections**, select **Create**
![](https://github.com/sammcint/Data-Engineer-Nanodegree-Projects-Udacity/blob/master/images/AirflowConnection2.PNG)

1. On the create connection page, enter the following values
* **Conn Id:** Enter aws_credentials
* **Conn Type:** Enter Amazon Web Services
* **Login:** Enter your **Access key ID** from the IAM User credentials
* **Password:** Enter your Secret access key from the IAM User credentials 

Once you've entered these values, select **Save and Add Another**

![](https://github.com/sammcint/Data-Engineer-Nanodegree-Projects-Udacity/blob/master/images/AirflowConnection3.PNG)

1. On the next create connection page, enter the following values:
* **Conn Id:** Enter redshift
* **Conn Type:** Enter Postgres
* **Host:** Enter the endpoint of your Redshift cluster, excluding the port at the end. You can find this by selecting your cluster in the **Clusters** page of the Amazon Redshift console. See where this is located in the screenshot below. IMPORTANT: Make sure to **NOT** include the port at the end of the Redshift endpoint string.
* **Schema:** Enter dev. This is the Redshift database you want to connect to.
* **Login:** Enter awsuser 
* **Password:** Enter the password you created when launching your Redshift cluster.
* **Port:** Enter 5439

Once you've entered these values, select **Save**

![](https://github.com/sammcint/Data-Engineer-Nanodegree-Projects-Udacity/blob/master/images/AirflowConnection4.PNG)

![](https://github.com/sammcint/Data-Engineer-Nanodegree-Projects-Udacity/blob/master/images/AirflowConnection5.PNG)

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
