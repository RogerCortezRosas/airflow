from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from airflow.decorators import dag


#Context manager

with DAG (dag_id = "primerdag" , description = "Primer DAG" , start_date = datetime(2025,3,27,12,40), schedule = "@once") as dag:


    t1 = EmptyOperator(task_id = "task1")

# Standar constructor

my_dag = DAG ( dag_id ="dagConstructor", description = "Este es un DAG con el metodo constructor", start_date = datetime(2025,3,27,13,5), schedule = "@once")
op = EmptyOperator(task_id = "taskConstructor", dag = my_dag)

# @dag decorator

"""@dag(
        dag_id = "dagDecorator", 
        description = "Este es un DAG con el decorador", 
        start_date = datetime(2025,3,27,12,50), 
        schedule = "@once",)

def my_decorator():
    op = EmptyOperator(task_id = "taskDecorator")

dag_instance = my_decorator()"""