from zenml import pipeline

from steps.data_cleaning_02 import clean_data
from steps.data_ingestion_01 import ingest_data
from steps.model_trainer_03 import train_model
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

@pipeline(model_version=Model)
def train_pipeline(data_path:str):
    """
    Train pipeline for ml model
    """
    df = ingest_data(data_path)
    x_train, x_test, y_train, y_test = clean_data(df)
    train_model(x_train, y_train)
