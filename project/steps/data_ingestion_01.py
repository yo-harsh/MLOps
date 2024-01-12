import logging
import pandas as pd
from zenml import step
from zenml import ModelVersion

Model = ModelVersion(
    # The name uniquely identifies this model
    # It usually represents the business use case
    name="rfc",
    # The version specifies the version
    # If None or an unseen version is specified, it will be created
    # Otherwise, a version will be fetched.
    version=None,
    # Some other properties may be specified
    license="Apache 2.0",
    description="A classification model for the churn dataset.",
)



class DataIngestion:
    """
    Ingest the data from source
    """

    def __init__(self, data_path:str):
        self.data_path = data_path

    def get_df(self):
        logging.info(f"Throwing data from {self.data_path}")
        return pd.read_excel(self.data_path,sheet_name=1)

@step(model_version=Model)
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