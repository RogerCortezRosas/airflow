from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

with DAG(dag_id = "file_sensor_dag",
         description = "File Sensor DAG",
         schedule="@daily",
            start_date=datetime(2025,1,1),
            end_date=datetime(2025,2,1),
            max_active_runs=1

         ) as dag:
    
    t1 = BashOperator(task_id="creating_file",bash_command = "sleep 10 && touch /tmp/my_file.txt")

    t2 = FileSensor(task_id="file_sensor",filepath="/tmp/my_file.txt",mode="poke")
    #poke ->in this mode the sensor is active in a wait loop until de file is find, it's useful when you want to wait for a little bit but the disadvantage is that consumes a slot an this can impact in the performance if there are many sensors in the dag
    #reschedule-> the sensor reschedule the task freeing the executor slot while waiting to perform a new check, this is useful when you have many sensors in the dag and you want to avoid the performance impact of having many sensors in poke mode
    t3 = BashOperator(task_id="removing_file",bash_command = "echo 'File exists!'")

    t1 >> t2 >> t3