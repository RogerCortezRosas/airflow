from airflow.models.baseoperator import BaseOperator
import os
import pandas as pd


class ETL_Space(BaseOperator):
    def __init__(self,path:str,**kwargs):
        super().__init__(**kwargs)
        self.path = path

    def execute(self,context):
        #Check if file exists
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File {self.path} does not exist")

        #Read json file
        df = pd.read_json(self.path,lines=False)

        #obtener el valor de la clave article en la columna links
        df['Links'] = df['links'].apply(lambda x: x['article'] if x['article'] else None)

        df.drop(columns=['links'], inplace=True)

        #Check if the is not a duplicade rows and if there is aduplicated rows , drop them
        if df.duplicated().any():
            df = df.drop_duplicates()


        return 'Etl completado'    




