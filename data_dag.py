from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from data_etl import run_news_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now() - timedelta(days=1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    "news_dag",
    default_args=default_args,
    description="etl code for news api"
)

run_etl = PythonOperator(
    task_id="complete_news_api",
    python_callable=run_news_etl,
    dag=dag
)

run_etl