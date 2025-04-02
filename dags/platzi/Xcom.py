from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime



"""En Apache Airflow, los XComs (abreviatura de "Cross Communications") son una herramienta que permite a las tareas intercambiar mensajes o compartir datos entre sí dentro de un DAG (Directed Acyclic Graph). Los XComs son útiles para pasar información de una tarea a otra, lo que permite una mayor flexibilidad y modularidad en los flujos de trabajo de Airflow."""

default_args = {"depends_on_past":True}

def my_function(ti):

    valor = int(ti.xcom_pull(task_ids="task1") )#Recupera el valor de task1
    return valor*valor

with DAG( dag_id = "Xcom" , description="Probando xcom",schedule="@daily",start_date=datetime(2025,1,1),default_args=default_args,max_active_runs=1) as dag:
   
    task1 = BashOperator(
        task_id="task1",
        bash_command="sleep 5 && echo $((3 * 8))",
        do_xcom_push=True,#La salida se guardara em Xcom
    )

    task2 = BashOperator(
        task_id="task2",
        bash_command="echo '{{ task_instance.xcom_pull(task_ids='task1') }}'",
        do_xcom_push=False,
    )

    task3 = PythonOperator(
        task_id="task3",
        python_callable=my_function,
        do_xcom_push=False,
    )

    task1 >> [task2, task3]  # Set dependencies