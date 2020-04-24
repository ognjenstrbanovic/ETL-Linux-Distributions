# ETL 🚀
**For this project, we had to perform extraction, transformation, and loading on a dataset.**
## Extract
We used the Kaggle website to find the following data source on Linux distributions: https://www.kaggle.com/lachhebo/distrowatch-page-hit-ranking-distro-popularity/version/1. It's one CSV file.

## Transform
First, we used the pandas library to read the CSV and make it a DataFrame. Next, we cleaned it up by dropping an unnamed column. Then, we renamed the columns so that they were more grammatically correct and easier to read/identify.__ We wanted to convert it to a JSON file, so we used the *json.loads* (json library) and *to_json* (pandas library) functions to convert the said DataFrame to JSON. The *records* orient makes it into a list of dictionaries. We printed it to verify it's format.

## Load
We had two options here: to load into a PostgreSQL database, or a MongoDB database. We chose the latter.__
First, we made a connection to the local host and the database, which was *etlProject*. We dropped a collection (if it existed in the database), as this is standard practice, and then inserted the collection *json_loads*. We printed the count of the rows to make sure that it was the same as in the pandas DataFrame. Once again, to verify, we printed 10 objects; the output was what we had expected it to be.__ 
Finally, we were finished, and had congratulated each other on some great teamwork!
