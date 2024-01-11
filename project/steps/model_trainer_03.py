import logging
import pandas as pd
from zenml import step
from src.model import RandomForestClassifierModel
from sklearn.base import ClassifierMixin

@step
def train_model(x_train:pd.DataFrame,y_train:pd.Series) -> ClassifierMixin:
    """
    Train the model using Data-frame
    """
    try:
        model_obj = RandomForestClassifierModel()
        model = model_obj.train_model(x_train,y_train)
        logging.info('Model training complete')
        return model
    except Exception as e:
        logging.error(f'Error while model training')
        raise e