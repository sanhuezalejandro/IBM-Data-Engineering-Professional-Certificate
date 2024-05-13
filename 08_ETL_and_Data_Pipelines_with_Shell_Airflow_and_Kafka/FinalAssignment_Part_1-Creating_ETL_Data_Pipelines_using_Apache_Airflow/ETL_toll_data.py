from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow_user',
   'start_date': datetime.today(),
    'email': 'airflow@example.com',
    'email_on_failure': True,
    'email_on_retry': True,
   'retries': 1,
   'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='ETL_toll_data',
    schedule_interval=timedelta(days=1),  # daily once
    default_args=default_args,
    description='Apache Airflow Final Assignment'
)

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/',
    dag=dag
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1,2,3,4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -f5,6,7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag=dag
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c21-23,24-27 /home/project/airflow/dags/finalassignment/payment-data.txt > /home/project/airflow/dags/finalassignment/fixed_width_data.csv',
    dag=dag
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='''
        paste -d"," /home/project/airflow/dags/finalassignment/csv_data.csv \
               /home/project/airflow/dags/finalassignment/tsv_data.csv \
               /home/project/airflow/dags/finalassignment/fixed_width_data.csv \
               > /home/project/airflow/dags/finalassignment/extracted_data.csv
    ''',
    dag=dag
)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command='tr "[a-z]" "[A-Z]" < /home/project/airflow/dags/finalassignment/extracted_data.csv > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv',
    dag=dag
)

# Define the task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
