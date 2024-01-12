import logging
import pandas as pd
from zenml import step
from typing_extensions import Annotated
from src.model import RandomForestClassifierModel
from sklearn.base import ClassifierMixin
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
def train_model(x_train:pd.DataFrame,y_train:pd.Series) -> Annotated[ClassifierMixin, "rfc_model"]:
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