import logging
import pandas as pd
from zenml import step
from src.data_cleaning import DataPreprocessingStrategy

from typing import Tuple
from typing_extensions import Annotated


@step
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
