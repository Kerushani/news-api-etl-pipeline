# News ETL Pipeline

## Overview

This project implements an ETL pipeline that extracts news articles from the News API, filters for articles related to Uber, and loads the processed data into an Amazon S3 bucket.

## Workflow

- **Extract**: Retrieves news articles from the [News API](https://newsapi.org).
- **Transform**: Filters and structures the data, retaining only articles related to Uber.
- **Load**: Saves the filtered data as a CSV file and uploads it to an S3 bucket.




![etl_diagram drawio](https://github.com/user-attachments/assets/279c4e82-1ec2-4367-87dd-fc658fd1edb0)


####Airflow on the EC2 instance
<img width="1501" alt="Screenshot 2025-05-13 at 8 49 55 PM" src="https://github.com/user-attachments/assets/5a9a60f2-fc44-4efe-a44d-f7e3909286a1" />

####Uploaded file to the S3 bucket
![Screenshot 2025-05-13 at 8 52 29 PM](https://github.com/user-attachments/assets/29b8679f-2b0e-4734-9b84-9dbc504749c5)

## Used

- Python  
- pandas  
- News API
- Airflow   
- EC2, S3 
