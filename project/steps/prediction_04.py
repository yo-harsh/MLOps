import json
import pandas as pd
from zenml import step
from zenml import ModelVersion
from sklearn.base import ClassifierMixin

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

# IMPORTANT: Cache needs to be disabled to avoid unexpected behavior
@step(enable_cache=False, model_version=Model)
def predict(
    data,
    model:ClassifierMixin
):
    data = json.loads(data)
    # print(data)
    # data.pop("columns")
    # data.pop("index")
    columns_for_df = ['CustomerID', 'Tenure', 'PreferredLoginDevice', 'CityTier',
       'WarehouseToHome', 'Gender', 'HourSpendOnApp',
       'NumberOfDeviceRegistered', 'SatisfactionScore', 'MaritalStatus',
       'NumberOfAddress', 'Complain', 'OrderAmountHikeFromlastYear',
       'CouponUsed', 'OrderCount', 'DaySinceLastOrder', 'CashbackAmount',
       'PreferredPaymentMode_Credit Card', 'PreferredPaymentMode_Debit Card',
       'PreferredPaymentMode_E wallet', 'PreferredPaymentMode_UPI',
       'PreferedOrderCat_Grocery', 'PreferedOrderCat_Laptop & Accessory',
       'PreferedOrderCat_Mobile', 'PreferedOrderCat_Others']

    df = pd.DataFrame([data.values()], columns=columns_for_df)
    # json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
    # data = json_list
    predictions = model.predict(df)
    return {"predictions": predictions}

