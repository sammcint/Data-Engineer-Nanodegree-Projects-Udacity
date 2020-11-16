{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 HelveticaNeue-Bold;\f2\fnil\fcharset0 HelveticaNeue;
\f3\fnil\fcharset0 Menlo-Regular;\f4\fnil\fcharset0 HelveticaNeue-Italic;}
{\colortbl;\red255\green255\blue255;\red27\green31\blue34;\red255\green255\blue255;\red87\green96\blue106;
}
{\*\expandedcolortbl;;\cssrgb\c14118\c16078\c18039;\cssrgb\c100000\c100000\c100000;\cssrgb\c41569\c45098\c49020;
}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid201\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid202\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid3}
{\list\listtemplateid4\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid301\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid4}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}{\listoverride\listid4\listoverridecount0\ls4}}
\margl1440\margr1440\vieww16560\viewh13420\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 CapstoneReadMe\
\
#### Overview\
\
The purpose of this project is to provide a public database for stock market analysts to query, analyze, and transform data into actionable insights. The application uses Apache Airflow to kick off jobs(Python ETL scripts) that load data that is stored in JSON and CSV format in a bucket on Amazon S3. The data pipeline reads in the data from S3, creates and inserts data into tables hosted on Redshift. The redshift database and tables can be accessed by anyone with appropriate credentials.\
\
\
#### **Source Data**\
This project draws on historical stock data found on Kaggle. The data consists of daily stock prices for a selection of several thousand stock tickers from NYSE and NASDAQ. Unfortunately, it was not possible to parse the data in a manner that allowed exact decimal calculations, so floating point numbers were provided. ***URL HERE****\
\
\
\
#### Tables \
\
\
#### **HistoricalStocks**\
\
* HistoricalStocks table - This table contains information on attributed of the companies, such as sector and industry \
	- *Ticker* - varchar: unique series of letters assigned to a security for trading purposes. This column links with the HistoricalStockPrices table\
	- *Exchange* - varchar: The name of the exchange (NYSE, NASDAQ)\
	- *Name* - varchar: name of the company\
	- *SectorId* - int: sectorid of the company (e.g. Finance, \
	- *IndustryId* - int: Industryid of the company  (e.g. Major Pharmaceuticals \
\
\
\
#### **HistoricalStockPrices**\
\
* HistoricalStockPrices table - talk about how many records are in the table, how long it dates back to. Those are good things to put here \
	- *Ticker* - varchar: unique series of letters assigned to a security for trading purposes\
	- *Open_Price* - float: price at which a security first trades upon the opening of an exchange on a trading day \
	- *Close_Price* - float: price at which a security closes upon the closing of an exchange on a trading day \
	- *Adj_Close* - float: Price that amends a stock\'92s closing price to reflect that stock\'92s value after accounting for any corporate actions\
	- *Low* - float: security\'92s intraday low trading price \
	- *High* - float:  security\'92s intraday high trading price \
	- *Volume* - float: Measure of how much of a given financial asset has traded in a period of time \
	- *Date* - date: Date of the trading day \
\
\
#### **Sectors**\
	-*SectorId* int: Id of the sector \
	-*Name* varchar: Name of the Sector\
\
#### **Industries**\
	-*IndustryId* int: Id of the industry\
	-*IndustryName* varchar: Name of the Industry \
\
\
#### **ERD**\
\
#### **Example Queries of Analysis** ####\
\
##### **For each sector find the the worst and best year\
\
\
Instructions:\
\
Install Airflow\
Set up Cluster in Redshift \
Launch Airflow\
Set up connections in Airflow\
\
\
\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f1\b\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
Tools\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls1\ilvl0
\fs32 \cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Python
\f2\b0 \'a0is used as the programming language because of its ease-of-use and flexibility\cb1 \
\ls1\ilvl0
\f1\b \cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
S3
\f2\b0 \'a0is used as the input and transform staging area because of its scalability, durability and support of multiple file formats\cb1 \
\ls1\ilvl0
\f1\b \cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Spark
\f2\b0 \'a0(specfically\'a0
\f1\b PySpark
\f2\b0 ) is used to transform the data because of its ability to handle big data sets\cb1 \
\ls1\ilvl0
\f1\b \cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Airflow
\f2\b0 \'a0is used to orchestrate the steps of the ETL data pipeline because of its powerful scheduling and monitoring features\cb1 \
\ls1\ilvl0
\f1\b \cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Redshift
\f2\b0 \'a0is used to host the data warehouse because of its ability to handle OLAP for big data\cb1 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \kerning1\expnd0\expndtw0 \
\
\
\
\
\pard\pardeftab720\sl440\sa320\partightenfactor0

\f1\b\fs36 \cf2 \cb3 \expnd0\expndtw0\kerning0
Purpose\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f2\b0\fs32 \cf2 The purpose of this project is to provide credit risk analysts with a public database they can query to fine tune the rules used to give credit to applicants based on demographics, financial and delinquencies information of current borrowers.\
The following are some questions that can be answered by the data:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls2\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
How many percent of borrowers under 30 years old have have had a serious delinquency?\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
What is the average number of loans and open credit lines for homeowners?\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
How many percent of borrowers with two or more dependents have had a 30-59 days delinquency?\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
What is the average household income of borrowers with a 60-89 days delinquency?\cb1 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls2\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\
\pard\pardeftab720\sl440\sa320\partightenfactor0

\f1\b\fs36 \cf2 \cb3 Setup\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls3\ilvl0
\f2\b0\fs32 \cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Download\'a0
\f3\fs27\fsmilli13600 cs-training.csv
\f2\fs32 \'a0dataset and then upload it to\'a0
\f3\fs27\fsmilli13600 <s3-bucket-name>/input
\f2\fs32 \cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Create\'a0
\f3\fs27\fsmilli13600 <s3-bucket-name>/staging
\f2\fs32 \'a0folder\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Set up a Redshift Cluster with the permission to read from S3\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Set up Apache Airflow\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Set up Spark\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Install Pyspark Python module\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Create the following\'a0
\f3\fs27\fsmilli13600 Connections
\f2\fs32 \'a0in Airflow\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\sl320\partightenfactor0
\ls3\ilvl1
\f3\fs27\fsmilli13600 \cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
redshift
\f2\fs32 \'a0: with the information necessary to connect to a redshift cluster\cb1 \
\ls3\ilvl1
\f3\fs27\fsmilli13600 \cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
aws_credentials
\f2\fs32 \'a0: with the credentials for an IAM user able to read and write to\'a0
\f3\fs27\fsmilli13600 <s3-bucket-name>
\f2\fs32 \cb1 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls3\ilvl0\cf2 \cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Create the following\'a0
\f3\fs27\fsmilli13600 Variables
\f2\fs32 \'a0in Airflow\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\sl320\partightenfactor0
\ls3\ilvl1
\f3\fs27\fsmilli13600 \cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
bucket_name
\f2\fs32 \'a0: with the name of the bucket where the input data is uploaded and the stage data will be written\cb1 \
\ls3\ilvl1
\f3\fs27\fsmilli13600 \cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
number_of_rows
\f2\fs32 : the data quality checks need this variable\cb1 \
\pard\tx720\pardeftab720\sl360\partightenfactor0
\cf2 \
\pard\pardeftab720\sl440\sa320\partightenfactor0

\f1\b\fs36 \cf2 \cb3 Source Data\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f2\b0\fs32 \cf2 This project draws on historical borrower's data provided for a Kaggle competition aiming to build an algorithm predicting the likelihood of a borrower experiencing financial hardship.\'a0{\field{\*\fldinst{HYPERLINK "https://www.kaggle.com/c/GiveMeSomeCredit/overview"}}{\fldrslt Give Me Some Credit}}\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f1\b \cf2 Give Me Some Credit Training Data
\f2\b0 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls4\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Name:\'a0
\f4\i cs-training.csv
\f2\i0 \cb1 \
\ls4\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Location:\'a0{\field{\*\fldinst{HYPERLINK "https://www.kaggle.com/c/GiveMeSomeCredit/data?select=cs-training.csv"}}{\fldrslt cs-training.csv}}\cb1 \
\ls4\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Update frequency: None\cb1 \
\ls4\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Number of rows (as of Sep 27 2020): 150,000\cb1 \
\ls4\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Description: demographic, financial and delinquency information for borrowers including whether or not they experienced a 90 days past due delinquency\cb1 \
\pard\tx720\pardeftab720\sl360\partightenfactor0
\cf2 \
\pard\pardeftab720\sl440\sa320\partightenfactor0

\f1\b\fs36 \cf2 \cb3 Project Structure\
\pard\pardeftab720\sl300\partightenfactor0

\fs30 \cf2 \cb1 \
\pard\pardeftab720\sl360\sa320\partightenfactor0
\cf2 \cb3 Source Code\
\pard\pardeftab720\sl380\partightenfactor0

\f3\b0\fs27\fsmilli13600 \cf2 \uc0\u9500 \u9472 \u9472  README.md - This file.\
\uc0\u9500 \u9472 \u9472  dags\
	\uc0\u9492 \u9472 \u9472  credilitycs.py \cf4 # Python script containing the tasks and depencdencies of the DAG\cf2 \
\uc0\u9500 \u9472 \u9472  plugins\
	\uc0\u9500 \u9472 \u9472  helpers\
		\uc0\u9500 \u9472 \u9472  __init__.py\
		\uc0\u9500 \u9472 \u9472  sql_queries.py \cf4 # Defining prepared and reusable SQL queries\cf2 \
    \uc0\u9500 \u9472 \u9472  operators\
		\uc0\u9500 \u9472 \u9472  __init__.py\
		\uc0\u9500 \u9472 \u9472  data_quality.py \cf4 # with `DataQualityOperator`, running data quality check by passing an array of SQL queries and an expected result as arguments, failing if the result of any query does not match the expected one.\cf2 \
		\uc0\u9500 \u9472 \u9472  load.py \cf4 # with `LoadOperator`, loading a dimension or fact table from data in the stage table.\cf2 \
		\uc0\u9500 \u9472 \u9472  transform.py \cf4 # with `TransformOperator`, loading the original CSV into a DataFrame, appending a UUID to each row and saving the result in parquet format.\cf2 \
		\uc0\u9492 \u9472 \u9472  stage_redshift.py \cf4 # with `StageToRedshiftOperator`, Loading the parquet datd\cf2 \cb1 \
\pard\tx720\pardeftab720\sl360\partightenfactor0

\f2\fs32 \cf2 \
\
}