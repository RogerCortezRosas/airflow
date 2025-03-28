from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import  PythonOperator


def funcion(variable):
    print(f"Tarea {variable}")

with DAG(dag_id = 'dagDependency',description='Este DAG tiene 4 tareas una dependiendo de la otra', start_date=datetime(2025,3,27),schedule='@once') as dag:
    # Definicion de tareas

    t1 = PythonOperator(task_id = 'tarea1',python_callable = funcion,op_args = ['1'])
    t2 = BashOperator(task_id = 'tarea2',bash_command = 'echo "Tarea 2"')
    t3 = PythonOperator(task_id = 'tarea3',python_callable = funcion,op_args = ['3'])
    t4 = BashOperator(task_id = 'tarea4',bash_command = 'echo "Tarea 4"')

    t1.set_downstream(t2)
    t2.set_downstream([t3,t4])

# t1 >> t2 >> [t3,t4]