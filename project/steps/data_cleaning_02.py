import logging
import pandas as pd
from zenml import step
from src.data_cleaning import DataPreprocessingStrategy

from typing import Tuple
from typing_extensions import Annotated
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


@step(model_version=Model)
def clean_data(df:pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, 'x_train'],
    Annotated[pd.DataFrame, 'x_test'],
    Annotated[pd.Series, 'y_train'],
    Annotated[pd.Series, 'y_test'],
]:
    """
    Clean the data using the df

    Returns x_train, x_test, y_train, y_test
    """
    try:
        data_preprocessed = DataPreprocessingStrategy()
        x_train, x_test, y_train, y_test = data_preprocessed.handle_data(df)
        logging.info('data cleaning completed')
        return x_train, x_test, y_train, y_test

    except Exception as e:
        logging.error(f'Error while cleaning_01 data {e}')
        raise e
