from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="ExternalSensor",description="Este DAG al finalizar desencadenara el DAG ExternalSenor2",start_date=datetime(2025, 1, 25),end_date = datetime(2025,2,25),schedule="@daily",
          default_args={"depends_on_past":False} ,max_active_runs=1) as dag:
    

    t1 = BashOperator(task_id='taskBash', bash_command='sleep 5 && echo "Tarea 1 "')
    t1

    