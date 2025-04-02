from airflow import DAG
from datetime import datetime
from HelloOperator import hello
from writeFile import WriteFileOperator


with DAG ( dag_id="customOperator",description="Custom Operator DAG",start_date=datetime(2025,3,27),schedule="@once") as dag:

    t1 = hello(task_id='taskHello',name = "Eva")
    t2 = hello(task_id='taskHello2',name = "Violeta")
    t3 = WriteFileOperator(task_id = "taskwrite",file_path="/tmp/hello.txt",content = "Hello from custom operator")

    t1>>t2 >>t3
