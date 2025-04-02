from airflow import DAG
from  datetime import datetime
from airflow.operators.bash import BashOperator

with DAG (dag_id="bashOperator", description="Bash Operator DAG", start_date=datetime(2025, 3, 27), schedule="@once") as dag:

    t1 = BashOperator(task_id='taskBash', bash_command='echo "Hello from BashOperator"')

    t1

    