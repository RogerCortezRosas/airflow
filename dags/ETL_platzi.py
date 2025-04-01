from airflow.models.baseoperator import BaseOperator
import os
import pandas as pd


class ETL_Platzi(BaseOperator):
    def __init__(self,task:str,**kwargs):
        super().__init__(**kwargs)
        self.task= task

    def execute(self,context):
        ti = context['ti']
        path = ti.xcom_pull(task_ids=self.task)
        #Check if file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist")

        #Read json file
        df = pd.read_csv(path)

        #Check if the is not a duplicade rows and if there is aduplicated rows , drop them
        if df.duplicated().any():
            df = df.drop_duplicates()


        return 'ETL PLatzi completado'   




