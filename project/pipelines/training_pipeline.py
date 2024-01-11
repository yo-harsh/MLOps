from zenml import pipeline

from steps.data_cleaning_02 import clean_data
from steps.data_ingestion_01 import ingest_data
from steps.model_trainer_03 import train_model


@pipeline
def train_pipeline(data_path:str):
    """
    Train pipeline for ml model
    """
    df = ingest_data(data_path)
    x_train, x_test, y_train, y_test = clean_data(df)
    train_model(x_train, y_train)
