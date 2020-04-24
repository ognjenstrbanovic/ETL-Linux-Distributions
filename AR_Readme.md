### ETL Project



### Extraction Process

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

