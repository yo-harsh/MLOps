import logging
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class ModelStrategy(ABC):
    """
    Strategy for model training
    """

    @abstractmethod
    def train_model(self, x_train:pd.DataFrame, y_train:pd.Series,):
        """
        Define a blueprint for model training
        """
        pass

class RandomForestClassifierModel(ModelStrategy):
    """
    Preparing random forest classifier
    """
    try:
        def train_model(self, x_train: pd.DataFrame, y_train: pd.Series, *kwargs):
            rfc = RandomForestClassifier(*kwargs)
            rfc.fit(x_train,y_train)
            logging.info('Model prepared')
            return rfc
    except Exception as e:
        logging.error(f'Error while preparing model {e}')
        raise e


