from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime,date
from airflow.sensors.filesystem import FileSensor
from ETL_Space_X import ETL_Space
from datosPlatzi import DatosPlatzi
from ETL_platzi import ETL_Platzi
from airflow.utils.trigger_rule import TriggerRule


def getPath(ti):
    #Recupera el path que devuelve DatosPlatzi
    path = ti.xcom_pull(task_ids="DatosPlatzi")
    return path




with DAG(dag_id='ProyectoEspacial',description='Este es un proyecto espacial',schedule='@daily',
         start_date=datetime(2023,1,1),end_date=datetime(2023,2,1),max_active_runs=1) as dag:
    
    #Definicion de tareas

    VoBo = BashOperator(task_id='VoBo_Nasa',bash_command='sleep 20 && echo "VoBo de la NASA" > /tmp/response_{{ds_nodash}}.txt')
    sensor = FileSensor(task_id="file_sensor",filepath="/tmp/response_{{ds_nodash}}.txt",mode="poke")

    getAPI_SpaceX = BashOperator(task_id='getAPI_SpaceX',bash_command = "curl -o /tmp/history.json https://api.spacexdata.com/v4/history")
    ETL_Space_X = ETL_Space(task_id='ETL_Space' , path="/tmp/history.json",depends_on_past=True)

    dataPlatzi = DatosPlatzi(task_id='DatosPlatzi',depends_on_past=True)
    Etl_plati = ETL_Platzi(task_id='ETL_Platzi' , task='DatosPlatzi')

    Space_Success = BashOperator(task_id='Space_Success',bash_command='echo "La data de Space X ya esta disponible"',trigger_rule=TriggerRule.ALL_SUCCESS,
                                 depends_on_past=True)
    Platzi_Success = BashOperator(task_id='Platzi_Success',bash_command='echo "La data de Platzi ya esta disponible"',trigger_rule=TriggerRule.ALL_SUCCESS,
                                  depends_on_past=True)



    VoBo>>sensor>>[getAPI_SpaceX,dataPlatzi]
    getAPI_SpaceX>>ETL_Space_X>>Space_Success
    dataPlatzi>>Etl_plati>>Platzi_Success



