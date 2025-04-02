from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime ,date
from airflow.utils.trigger_rule import TriggerRule


default_args = {
    'start_date':datetime(2023,1,1),
    'end_date':datetime(2023,2,1)

}

def choose(**context):

    if context['logical_date'].date()< date(2023,1,15):
        return '14_Enero'
    else:
        return '15_Enero'
    

with DAG (dag_id='Branching',schedule='@daily',default_args=default_args) as dag:

    branching = BranchPythonOperator(task_id = "branch",python_callable = choose)

    finish14 = BashOperator(task_id='14_Enero',bash_command="echo 'Running {{ds}}'")

    start15 = BashOperator(task_id='15_Enero',bash_command="echo 'Running {{ds}}'") 

    task = BashOperator(task_id='task',bash_command="echo 'TAREA CUAQUIERA",trigger_rule=TriggerRule.NONE_FAILED) # TriggerRule.NONE_FAILED: La tarea se ejecuta si no ha fallado ninguna de las tareas anteriores



branching >> [finish14,start15,task] # Set dependencies