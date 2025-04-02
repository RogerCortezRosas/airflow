from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator


#If you need access to Airflow context variables (e.g., ds, run_id), you must include **kwargs.
def hello(country): #**kwaargs):
    print(f"Hello {country}")

with DAG (dag_id="pythonOperator", description="Python Operator DAG", start_date=datetime(2025, 3, 27), schedule="@once") as dag:

    t1 = PythonOperator(task_id='taskPython', python_callable=hello,op_args=["Mexico"])

    t2 = PythonOperator(task_id='taskPython2', python_callable=hello,op_kwargs={'countrty':"France"})

# op_args = you can pass a list of arguments to the function. if you have more than one argument you must pass the arguments in order in a list
# op_kwargs = you can pass a dictionary where the keys are the name of the argumnet ant the values are the values you want to pass. if you have more than one argument you can pass them in any order.