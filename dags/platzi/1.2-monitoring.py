from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule
import random

def myFunction():
        num = random.uniform (0,0.5)
        if num > 0.4:
            return True
        else:
            raise Exception

default_args = {}
with DAG(dag_id="monitoring2", description="Bash Operator DAG", start_date=datetime(2025, 1, 25),end_date = datetime(2025,2,25), schedule="@daily",
          default_args=default_args, max_active_runs=1) as dag:
    
        t1 = PythonOperator(task_id='casa1', python_callable=myFunction ,
                          trigger_rule = TriggerRule.ALWAYS ,
                          retries=2,#Cantidad de intentos
                          retry_delay=2,#tiempo entre cada intento en segundos
                          depends_on_past = False)
    
        t2 = PythonOperator(task_id='casa2',python_callable=myFunction,
                          retries=2,#Cantidad de intentos
                          retry_delay=5,#tiempo entre cada intento en segundos
                          trigger_rule = TriggerRule.ALWAYS,
                          depends_on_past = False)
        t3 = PythonOperator(task_id='casa3', python_callable=myFunction,
                          retries=2,
                          retry_delay=2,
                          trigger_rule = TriggerRule.ALWAYS,
                          depends_on_past = False)
        
        t4 = BashOperator(task_id='ALARMA_INUNDACION', bash_command='sleep 5 && echo "ALARMA DE INCENDIOS ENCENDIDA"',
                          retries=2,retry_delay=5,trigger_rule = TriggerRule.ALL_FAILED,depends_on_past = False)
        
        t5 = BashOperator(task_id='ALARMA_CAMARA', bash_command='sleep 5 && echo "ALARMA DE CAMARA ENCENDIDA"',
                          retries=2,retry_delay=5,trigger_rule = TriggerRule.ONE_FAILED,depends_on_past = False)
        t6 = BashOperator(task_id='ALARMA_CONTROL', bash_command='sleep 5 && echo "LED EN VERDE"',
                          retries=2,retry_delay=5,trigger_rule = TriggerRule.NONE_FAILED,depends_on_past = False)
        
       
        
       
[t1,t2,t3] >> t4
       
[t1,t2,t3] >> t5
       
[t1,t2,t3] >> t6

"""    t1>> t2 >> t3 >> t4 
        t1 >> t2 >> t3 >> t5
        t1 >> t2 >> t3 >> t6"""