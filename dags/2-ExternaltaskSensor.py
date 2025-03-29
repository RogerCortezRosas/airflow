from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(dag_id="ExternalSensor2",description="Este DAG al finalizar  ExternalSenor se ejecuta",start_date=datetime(2025, 1, 25),end_date = datetime(2025,2,25),schedule="@daily",
          default_args={"depends_on_past":False} ,max_active_runs=1) as dag:
    

    t1 = ExternalTaskSensor(task_id='waiting_DAG', external_dag_id="ExternalSensor", 
                            external_task_id="taskBash",
                           # execution_delta=None,
                            #timeout=600,
                            poke_interval=5,# cada cuanto tiempo se revisa si el DAG ha terminado
                            #mode='poke',# 
                            #soft_fail=False
                            )
    
    t2 = BashOperator(task_id='taskBash2', bash_command='sleep 5 && echo "DAG 2 finalizado con exito "')
   
   
    t1 >> t2
    