# ETL 🚀
<figure class="image">
 <img src="https://github.com/ognjenstrbanovic/ETL-Linux-Distributions/blob/master/Ognjen%20Strbanovic/Tux.png?raw=true" height="33%" width="33%">
 <figcaption>Tux is very cute!</figcaption>
</figure>

## <ins>We call ourselves the *"Good Hombres"*, and for this project, we had to perform extraction, transformation, and loading on a dataset.</ins>

## Extract
We used the Kaggle website to find the following data source on Linux distributions: https://www.kaggle.com/lachhebo/distrowatch-page-hit-ranking-distro-popularity/version/1. It's one CSV file, and it was ranked as having "high useability".  
The database chosen was MongoDB, because we didn't have datasets that were related at all. The schema was called `etlProject`.

## Transform
First, we used the pandas library to read the CSV and make it a DataFrame. Next, we cleaned it up by dropping an unnamed column. Then, we renamed the columns so that they were more grammatically correct and easier to read/identify.  
We wanted to convert it to a JSON file, so we used the *json.loads* (json library) and *to_json* (pandas library) functions to convert said DataFrame to JSON. The *records* orient makes it into a list of dictionaries. We printed it to verify it's format.

## Load
We had two options here: to load into a PostgreSQL database, or a MongoDB database. We chose the latter.__
First, we made a connection to the local host and the database, which was *etlProject*. We dropped a collection (if it existed in the database), as this is standard practice, and then inserted the collection *json_loads*. We printed the count of the rows to make sure that it was the same as in the pandas DataFrame. Once again, to verify, we printed 10 objects; the output was what we had expected it to be.  
As an aside, you may find my Jupyter notebook by clicking on the following link: https://github.com/ognjenstrbanovic/etlproject/blob/master/Ognjen%20Strbanovic/Import%20Linux%20Distro%20CSV%20to%20MongoDB.ipynb.  
Finally, we were finished, and had congratulated each other on some great teamwork!!

# Guidelines (Met)

> Team Effort  
> Due to the short timeline, teamwork will be crucial to the success of this project! Work closely with your team through all phases of the project to ensure that there are no surprises at the end of the week. Working in a group enables you to tackle more difficult problems than you'd be able to working alone. In other words, working in a group allows you to work smart and dream big. Take advantage of it!  

> Project Proposal  
> Before you start writing any code, remember that you only have one week to complete this project. View this project as a typical assignment from work. Imagine a bunch of data came in and you and your team are tasked with migrating it to a production data base. Take advantage of your Instructor and TA support during office hours and class project work time. They are a valuable resource and can help you stay on track.  

> Finding Data  
> Your project must use 2 or more sources of data.  

> Data Cleanup & Analysis  
> Once you have identified your datasets, perform ETL on the data. Make sure to plan and document the following:  
> - The sources of data that you will extract from.  
> - The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).  
> - The type of final production database to load the data into (relational or non-relational).  
> - The final tables or collections that will be used in the production database.  
> - You will be required to submit a final technical report with the above information and steps required to reproduce your ETL process.  

> Project Report  
> At the end of the week, your team will submit a Final Report that describes the following:  
> - Extract: your original data sources and how the data was formatted (CSV, JSON, pgAdmin 4, etc).  
> - Transform: what data cleaning or transformation was required.  
> - Load: the final database, tables/collections, and why this was chosen.  
