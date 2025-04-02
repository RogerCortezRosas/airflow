from airflow.models import BaseOperator

class WriteFileOperator(BaseOperator):
    def __init__(self, file_path: str, content: str, **kwargs):
        super().__init__(**kwargs)
        self.file_path = file_path
        self.content = content

    def execute(self, context):
        with open(self.file_path, 'w') as f:
            f.write(self.content)
        self.log.info(f"File written to {self.file_path} the message {self.content}" )