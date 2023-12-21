from zenml import pipeline

from steps.data_cleaning import clean_data
from steps.data_ingestion import ingest_data
from steps.model_trainer import train_model
from zenml.config import DockerSettings


@pipeline
def train_pipeline(data_path:str):
    """
    Train pipeline for ml model
    """
    df = ingest_data(data_path)
    clean_data(df)
    train_model(df)
