from airflow.models.baseoperator import BaseOperator
import os
import pandas as pd

class DatosPlatzi(BaseOperator):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
    def execute(self,context):

        logical_date = context['logical_date']
        date = context['ds_nodash']

        data = pd.DataFrame({"student": ["Maria Cruz", "Daniel Crema",
                                        "Elon Musk", "Karol Castrejon", "Freddy Vega"],
                            "timestamp": [logical_date,
                                        logical_date, logical_date, logical_date,
                                        logical_date]})
        data.to_csv(f"/tmp/platzi_data{date}.csv",index=False)
        self.log.info(f"Data saved to /tmp/platzi_data{date}.csv")   

        path = f"/tmp/platzi_data{date}.csv"

        context['ti'].xcom_push(key='platzi_data', value=path)

        return path
                 