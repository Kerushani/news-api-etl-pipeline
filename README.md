# News ETL Pipeline

## Overview

This project implements an ETL pipeline that extracts news articles from the News API, filters for articles related to Uber, and loads the processed data into an Amazon S3 bucket.

## Workflow

- **Extract**: Retrieves news articles from the [News API](https://newsapi.org).
- **Transform**: Filters and structures the data, retaining only articles related to Uber.
- **Load**: Saves the filtered data as a CSV file and uploads it to an S3 bucket.

## Used![etl_diagam](https://github.com/user-attachments/assets/334d9be2-8d6d-4320-9995-3d9c07d1b6d8)

- Python  
- pandas  
- News API
- Airflow   
- EC2, S3 
