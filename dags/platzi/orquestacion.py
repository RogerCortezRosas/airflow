from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG (dag_id="bashOperator2", description="Bash Operator DAG", start_date=datetime(2025, 1, 25),end_date = datetime(2025,2,25), schedule="@daily",
          default_args={"depends_on_past":True} ,max_active_runs=1) as dag:
    # depends_on_past True mean that the task wil not run if the previous task has not been completed
    #max_active_runs = 1 means that only will run all the task per day
    # schedule = minute hour day month day_of_week -> 5 4 * * 1 means “At 04:05 on Monday. sintaxis chrome

    t1 = BashOperator(task_id='taskBash', bash_command='sleep 5 && echo "Tarea 1 "')
    
    t2 = BashOperator(task_id='taskBash2', bash_command='sleep 5 && echo "Tarea 2 "')
    
    t3 = BashOperator(task_id='taskBash3', bash_command='sleep 5 && echo "Tarea 3 "')
    
    t4 = BashOperator(task_id='taskBash4', bash_command='sleep 5 && echo "Tarea 4 "')


    t1 >> [t2,t3] >> t4
    #