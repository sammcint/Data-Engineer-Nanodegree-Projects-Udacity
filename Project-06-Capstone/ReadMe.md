#### Overview

The purpose of this project is to provide a public database for stock market analysts to query, analyze, and transform data into actionable insights. The application uses Apache Airflow to kick off jobs(Python ETL scripts) that load data that is stored in JSON and CSV format in a bucket on Amazon S3. The data pipeline reads in the data from S3, creates and inserts data into tables hosted on Redshift. The redshift database and tables can be accessed by anyone with appropriate credentials.


#### **Source Data**
This project draws on historical stock data found on Kaggle. The data consists of daily stock prices for a selection of several thousand stock tickers from NYSE and NASDAQ. Unfortunately, it was not possible to parse the data in a manner that allowed exact decimal calculations, so floating point numbers were provided. ***URL HERE****



#### Tables 


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

![Database Design](https://github.com/sammcint/Data-Engineer-Nanodegree-Projects-Udacity/blob/master/images/Capstone-ERD.png)

#### **Example Queries of Analysis** ####

##### **For each sector find the the worst and best year


Instructions:

Install Airflow
Set up Cluster in Redshift 
Launch Airflow
Set up connections in Airflow
