import pandas as pd
import json
from datetime import datetime
import s3fs
import boto3
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

s3 = s3fs.S3FileSystem(anon=False)

session = boto3.Session()
s3 = s3fs.S3FileSystem(session=session)

def run_news_etl():
    endpoint = "https://newsapi.org/v2/everything"


    query_params = {
        "q": "Uber",
        "sortBy": "popularity",
        "apiKey": API_KEY,
    }

    response = requests.get(endpoint, params=query_params)

    data = response.json()
    articles = data.get("articles", [])

    cleaned_articles_list = []

    for article in articles:
        title = article.get("title", "No Title")
        description = article.get("description", "No description")
        published_at = article.get("publishedAt", "No date")
        url = article.get("url", "")
        cleaned_articles_list.append({"title": title, "description": description, "published_at": published_at, "url": url})

    df = pd.DataFrame(cleaned_articles_list)
    df.to_csv("s3://news-etl-project/uber_news_articles.csv")