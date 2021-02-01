#### Overview

The purpose of this project is to provide a public database for stock market analysts to query, analyze, and transform data into actionable insights. The application uses Apache Airflow to kick off jobs(Python ETL scripts) that load data that is stored in JSON and CSV format in a bucket on Amazon S3. The data pipeline utilizes python to read in the data from S3, creates and inserts data into tables hosted on Redshift. The redshift database and tables can be accessed by anyone with appropriate credentials and this is where stock market analysis on the final data can take place. 

#### Technology decisions

Amazon Redshift was chosen as the database host as opposed to another Amazon RDS for this project because Redshift is used primarily for reporting and analytics, whereas Amazon RDS is designed for online-transaction processing (OLTP). OLTP workloads require quickly querying specific information and support for transactions like insert, update, and delete and are best handled by Amazon RDS. Amazon Redshift harnesses the scale and resources of multiple nodes and uses a variety of optimizations to provide order of magnitude improvements over traditional databases for analytic and reporting workloads against very large data sets. Amazon Redshift provides an excellent scale-out option as your data and query complexity grows if you want to prevent your reporting and analytic processing from interfering with the performance of your OLTP workload. Now, with the new Federated Query feature, you can easily query data across your Amazon RDS or Aurora database services with Amazon Redshift.

source: ![When would I use Amazon Redshift vs. Amazon RDS?]


[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

When would I use Amazon Redshift vs. Amazon RDS?

#### **Source Data**
This project draws on historical stock data found on Kaggle. The data consists of daily stock prices for a selection of several thousand stock tickers from NYSE and NASDAQ. Unfortunately, it was not possible to parse the data in a manner that allowed exact decimal calculations, so floating point numbers were provided. You can find the dataset here: https://www.kaggle.com/ehallmar/daily-historical-stock-prices-1970-2018

#### Tools used 
* **Python** is used as one of the programming languases because of its ease-of-use and fexibility 
* **SQL** is used for syntax of the table structure and insertion of records 
* **S3** is used as the data storage for the stock data because of its scalability, and support of multiple file formats 
* **Airflow** is used to orchestrate the steps of the ETL pipeline because of its powerful schedule and monitoring features
* **Redshift** is used to host the data table because of its ease-of-access and ability to handle OLAP for big data 

### Tables 


#### **HistoricalStocks**

* HistoricalStocks table - This table contains information on attributed of the companies, such as sector and industry 
	- *Ticker* - varchar: unique series of letters assigned to a security for trading purposes. This column links with the HistoricalStockPrices table
	- *Exchange* - varchar: The name of the exchange (NYSE, NASDAQ)
	- *Name* - varchar: name of the company
	- *SectorId* - int: sectorid of the company (e.g. Finance, 
	- *IndustryId* - int: Industryid of the company  (e.g. Major Pharmaceuticals, 



#### **HistoricalStockPrices**

* HistoricalStockPrices table - talk about how many records are in the table, how long it dates back to. Those are good things to put here 
	- *Ticker* - varchar: unique series of letters assigned to a security for trading purposes
	- *Open_Price* - float: price at which a security first trades upon the opening of an exchange on a trading day 
	- *Close_Price* - float: price at which a security closes upon the closing of an exchange on a trading day 
	- *Adj_Close* - float: Price that amends a stock\'92s closing price to reflect that stock\'92s value after accounting for any corporate actions
	- *Low* - float: security\'92s intraday low trading price 
	- *High* - float:  security\'92s intraday high trading price 
	- *Volume* - float: Measure of how much of a given financial asset has traded in a period of time 
	- *Date* - date: Date of the trading day 


#### **Sectors**
* Sectors table - Reference table for sectors and their corresponding names
	- *SectorId* int: Id of the sector 
	- *Name* varchar: Name of the Sector

#### **Industries**
* Industries table - Reference table for industries and their corresponding names 
	- *IndustryId* int: Id of the industry
	- *IndustryName* varchar: Name of the Industry 


#### **ERD**
 * Database design is as follows:
![Database Design](https://github.com/sammcint/Data-Engineer-Nanodegree-Projects-Udacity/blob/master/images/Capstone-ERD.png)

#### **Example Queries of Analysis** ####

 * **Which 5 days in January did American Airlines (AAL) have the greatest percentage decrease over the previous day? 

    >>select ticker, date, ROUND(1 - open_price/previousopen,2)"Percent decrease from previous day" FROM  (  
    >>SELECT hsp.ticker, hsp.date, hsp.open_price, hsp.close_price,  
    >>LAG(hsp.close_price) OVER (PARTITION BY hsp.ticker order by hsp.ticker, hsp.date) "previousopen"  
    >>FROM HISTORICALSTOCKSSTAGING HSS  
    >>JOIN HISTORICALSTOCKPRICES HSP on HSP.ticker = hss.ticker  
    >>LEFT JOIN SECTORS S ON UPPER(HSS.Sector) = UPPER(S.Sector)  
    >>LEFT JOIN INDUSTRIES I ON HSS.Industry = I.IndustryName  
    >>where hss.ticker = 'AAL' and hsp.date like '2017%') order by open_price/previousopen asc  LIMIT 5
	
	
#### Potential Scenarios

Eventually the project may have to address these scenarios if it grows and evolves in its use:

**The data was increased by 100** 
	- This would require creating a clutser on redshift that holds more nodes. The more nodes the cluster has, the more data it can store. 

**The pipelines would be run on a daily basis by 7 am each day:**
	- This would require a change to the airflow dag schedule configuration in the capstone_project_dag.py file  
	
		>>dag = DAG('capstone_dag',  
          	>>default_args=default_args,  
          	>>description='Load and transform data in Redshift with Airflow',  
          	>>schedule_interval='0 7 * * *'  
        )

**The database needed to be accessed by 100+ people**
	- This would require making universal IAM, Security Group, and Permission Roles for a set of users in which they would share the password and secret password of the IAM user. A separate user table could also be configured for keeping track of users logging in and out and whenever there is a spike in user activity, additional custers can be initiated
	
	



