

GOOD HOMBRES PROJECT 

We used these data sets as sources 

https://www.kaggle.com/neuromusic/avocado-prices 
https://www.kaggle.com/mczielinski/bitcoin-historical-data 
https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
https://www.kaggle.com/roshansharma/sanfranciso-crime-dataset 
https://www.kaggle.com/lachhebo/distrowatch-page-hit-ranking-distro-popularity 

The data sets were chosed becuase of high "useability" on kaggle. 
We were asked to use 2 datasets but decided to "go overboard" and load 5. 
There was no suggestion to use "related" datasets anywhere so we fairly randomly chose 5 datasets. 
We assumed that each data set might produce it's own ETC challenges to solve. 
The assignment question did not ask for us to create a scenario or a front end. 
We decided that the best approach was to extract , transform and load the data. 
We decided to use a mongoDB database and also a postgres database to practice using different types of databases. 
with no scenario in mind we decided the best approach was to collate the data into 2 databases and clean them up so that they could be easily searched. Because no use was asked for we decided that the best approach was to perform minimal translations on the data. 
In some instances some columns were removed and rows populated with nulls were discarded. 4 of the data sources were loaded into one mongoDB database. These were unrelated data sources so there was no need to perform a great deal of transformation. 
The 5th data set was extracted , transformed and loaded into a postgres database. 
Specific details about the process are included below. The mongoDB schema is called "etlProject". The data sets used are stored in the /data directory on github. Python files and jupyter notebooks are included here which perform the ETL for each dataset. 




### ETL Project



### Extraction Process for SanFrancisco dataset

Before joining the team had already settled on using datasets from Kaggle. So as part of the initial extraction process was to install the kaggle library using the Anaconda environment. Kaggle provided the data source for the San Francisco which contain geomapping for crime occuring in the city this project.

- Install Kaggle using conda environemt
   1. `➜pip install kaggle`

- Download the San Francisco Crime dataset

    2. `➜kaggle datasets download -d roshansharma/sanfranciso-crime-dataset`
-

### Transformation Process

In order to store this dataset, a database was created during this phase using Postgresql. Use the pandas library to rename and manipulate columns so that the data could loaded in Postgresql.
This process included making a copy of the datafram, renaming columns, and dropping columns that were not needed in pandas

1. making copy
 ```new_sfpd_report_df = sfpd_report_df[['IncidntNum','Category', 'Descript', 'DayOfWeek', 'Date', 'Time', 'PdDistrict','Resolution', 'Address', 'X', 'Y', 'Location', 'PdId']].copy()```

2. renaming ```new_sfpd_report_df= new_sfpd_report_df.rename(
    columns={"IncidntNum": "id", "Category": "category", "Descript": "descript", "Date": "date", "Time":"time", "X": "x", "Y":"y", "Location": "loc"})```

3. dropping columns   ```new_sfpd_report_df= new_sfpd_report_df.drop(columns={'DayOfWeek', 'PdDistrict', 'Resolution', 'Address', 'PdId' new_sfpd_report_df.head()```

### Loading Process

As described in the extraction process that a database was created using Postgresql. In this phase for the data to loaded properly it needed to be accurately specified in sql and match precisely otherwise this loading process will fail. The actions outlined below go over the steps that are necessary to load the dataset content to a sql database.

1. Connect to a local database: ```rds_connection_string = "<insert user name>:<insert password>@localhost:5432/customer_db"
engine = create_engine(f'postgresql://{rds_connection_string}')```

2. Verify the table(s) are identified: ```engine.table_names()```

3. Load the dataframe into the database: ```new_sfpd_report_df.to_sql(name='crime_table', con=engine, if_exists='append', index=False)```


Extraction process for linux distribution data 

# ETL 🚀
**For this project, we had to perform extraction, transformation, and loading on a dataset.**
## Extract
We used the Kaggle website to find the following data source on Linux distributions: https://www.kaggle.com/lachhebo/distrowatch-page-hit-ranking-distro-popularity/version/1. It's one CSV file.

## Transform
First, we used the pandas library to read the CSV and make it a DataFrame. Next, we cleaned it up by dropping an unnamed column. Then, we renamed the columns so that they were more grammatically correct and easier to read/identify.  
We wanted to convert it to a JSON file, so we used the *json.loads* (json library) and *to_json* (pandas library) functions to convert said DataFrame to JSON. The *records* orient makes it into a list of dictionaries. We printed it to verify it's format.

## Load
We had two options here: to load into a PostgreSQL database, or a MongoDB database. We chose the latter.__
First, we made a connection to the local host and the database, which was *etlProject*. We dropped a collection (if it existed in the database), as this is standard practice, and then inserted the collection *json_loads*. We printed the count of the rows to make sure that it was the same as in the pandas DataFrame. Once again, to verify, we printed 10 objects; the output was what we had expected it to be.  
Finally, we were finished, and had congratulated each other on some great teamwork!

Extraction process of Avocado data and Air BNB DATA 

This was used as the source
https://www.kaggle.com/neuromusic/avocado-prices
It contains a 2D csv of avocado prices.
The file was stored in a mongoDB dictionary
schema is eltProject
database is avocado

sample of data stored :

{'_id': ObjectId('5ea0701c7378791bedb8809a'), 'Date': '2018-01-07', 'AveragePrice': 1.62, 'Total Volume': 17489.58, '4046': 2894.77, '4225': 2356.13, '4770': 224.53, 'Total Bags': 12014.15, 'Small Bags': 11988.14, 'Large Bags': 26.01, 'XLarge Bags': 0.0, 'type': 'organic', 'year': 2018, 'region': 'WestTexNewMexico', 'id': 11}
{'_id': ObjectId('5ea0701c7378791bedb88099'), 'Date': '2018-01-14', 'AveragePrice': 1.93, 'Total Volume': 16205.22, '4046': 1527.63, '4225': 2981.04, '4770': 727.01, 'Total Bags': 10969.54, 'Small Bags': 10919.54, 'Large Bags': 50.0, 'XLarge Bags': 0.0, 'type': 'organic', 'year': 2018, 'region': 'WestTexNewMexico', 'id': 10}
{'_id': ObjectId('5ea0701c7378791bedb88098'), 'Date': '2018-01-21', 'AveragePrice': 1.87, 'Total Volume': 13766.76, '4046': 1191.92, '4225': 2452.79, '4770': 727.94, 'Total Bags': 9394.11, 'Small Bags': 9351.8, 'Large Bags': 42.31, 'XLarge Bags': 0.0, 'type': 'organic', 'year': 2018, 'region': 'WestTexNewMexico', 'id': 9}

It was decided that since the use is unknown nulls would be kept ( in the date column ).
Since use was unknown it was decided that the creation of a relational schema was unnecessary


A similar process was applied to the bitcoin data. 
The 2 datasets where combined into one table. 
We decided to drop nulls because many rolls only hada timestamp and no data. 
It was loaded into mongoDB. 
 

GUIDELINES GIVEN ARE BELOW 










# etlproject

Guidelines for ETL Project
This document contains guidelines, requirements, and suggestions for Project 1.

Team Effort
Due to the short timeline, teamwork will be crucial to the success of this project! Work closely with your team through all phases of the project to ensure that there are no surprises at the end of the week.

Working in a group enables you to tackle more difficult problems than you'd be able to working alone. In other words, working in a group allows you to work smart and dream big. Take advantage of it!

Project Proposal
Before you start writing any code, remember that you only have one week to complete this project. View this project as a typical assignment from work. Imagine a bunch of data came in and you and your team are tasked with migrating it to a production data base.

Take advantage of your Instructor and TA support during office hours and class project work time. They are a valuable resource and can help you stay on track.

Finding Data
Your project must use 2 or more sources of data. We recommend the following sites to use as sources of data:

data.world

Kaggle

You can also use APIs or data scraped from the web. However, get approval from your instructor first. Again, there is only a week to complete this!

Data Cleanup & Analysis
Once you have identified your datasets, perform ETL on the data. Make sure to plan and document the following:

The sources of data that you will extract from.

The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).

The type of final production database to load the data into (relational or non-relational).

The final tables or collections that will be used in the production database.

You will be required to submit a final technical report with the above information and steps required to reproduce your ETL process.

Project Report
At the end of the week, your team will submit a Final Report that describes the following:

Extract: your original data sources and how the data was formatted (CSV, JSON, pgAdmin 4, etc).

Transform: what data cleaning or transformation was required.

Load: the final database, tables/collections, and why this was chosen.

Please upload the report to Github and submit a link to Bootcampspot.






