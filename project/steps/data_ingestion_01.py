import logging
import pandas as pd
from zenml import step

class DataIngestion:
    """
    Ingest the data from source
    """

    def __init__(self, data_path:str):
        self.data_path = data_path

    def get_df(self):
        logging.info(f"Throwing data from {self.data_path}")
        return pd.read_excel(self.data_path,sheet_name=1)

@step
def ingest_data(data_path:str) -> pd.DataFrame:
    """
    takes path of data source and returns it
    """
    try:
        ingest_data = DataIngestion(data_path)
        df = ingest_data.get_df()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting the data: {e}")
        raise e