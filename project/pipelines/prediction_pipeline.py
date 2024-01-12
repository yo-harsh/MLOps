import pandas as pd
from zenml import pipeline,get_pipeline_context
from zenml import ModelVersion
from steps.prediction_04 import predict

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


@pipeline(
    model_version=ModelVersion(
        name="rfc_model",
        # Using the production stage
    ),
)
def predict_pipeline(data):
    # model_name and model_version derived from pipeline context
    model_version = get_pipeline_context().model_version

    predict(
        # Here, we load in the `trained_model` from a trainer step
        data=data,
        model=model_version.get_model_artifact("rfc_model"),
    )
