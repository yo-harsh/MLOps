import json

import streamlit as st
from pipelines.prediction_pipeline import predict_pipeline

# Streamlit app
def main():
    st.title('Prediction App')

    # Create a form for user input
    st.subheader('Enter Data for Prediction:')
    form = st.form(key='prediction_form')

    columnsss = ['CustomerID', 'Tenure', 'PreferredLoginDevice', 'CityTier',
       'WarehouseToHome', 'Gender', 'HourSpendOnApp',
       'NumberOfDeviceRegistered', 'SatisfactionScore', 'MaritalStatus',
       'NumberOfAddress', 'Complain', 'OrderAmountHikeFromlastYear',
       'CouponUsed', 'OrderCount', 'DaySinceLastOrder', 'CashbackAmount',
       'PreferredPaymentMode_Credit Card', 'PreferredPaymentMode_Debit Card',
       'PreferredPaymentMode_E wallet', 'PreferredPaymentMode_UPI',
       'PreferedOrderCat_Grocery', 'PreferedOrderCat_Laptop & Accessory',
       'PreferedOrderCat_Mobile', 'PreferedOrderCat_Others']


    # Input fields for specific columns

    # CustomerID = form.number_input('CustomerID',key = 'CustomerID')
    # Tenure = form.number_input('Tenure',key = 'Tenure')
    # PreferredLoginDevice = form.number_input('PreferredLoginDevice',key = 'PreferredLoginDevice')
    # CityTier = form.number_input('CityTier',key = 'CityTier')
    # WarehouseToHome = form.number_input('WarehouseToHome',key = 'WarehouseToHome')
    # Gender = form.number_input('Gender',key = 'Gender')
    # HourSpendOnApp = form.number_input('HourSpendOnApp',key = 'HourSpendOnApp')
    # NumberOfDeviceRegistered = form.number_input('NumberOfDeviceRegistered',key = 'NumberOfDeviceRegistered')
    # SatisfactionScore = form.number_input('SatisfactionScore',key = 'SatisfactionScore')
    # MaritalStatus = form.number_input('MaritalStatus',key = 'MaritalStatus')
    # NumberOfAddress = form.number_input('NumberOfAddress',key = 'NumberOfAddress')
    # Complain = form.number_input('Complain',key = 'Complain')
    # OrderAmountHikeFromlastYear = form.number_input('OrderAmountHikeFromlastYear',key = 'OrderAmountHikeFromlastYear')
    # CouponUsed = form.number_input('CouponUsed',key = 'CouponUsed')
    # OrderCount = form.number_input('OrderCount',key = 'OrderCount')
    # DaySinceLastOrder = form.number_input('DaySinceLastOrder',key = 'DaySinceLastOrder')
    # CashbackAmount = form.number_input('CashbackAmount',key = 'CashbackAmount')
    # PreferredPaymentMode_Credit_Card = form.number_input('PreferredPaymentMode_Credit Card',key = 'PreferredPaymentMode_Credit_Card')
    # PreferredPaymentMode_Debit_Card = form.number_input('PreferredPaymentMode_Debit Card',key = 'PreferredPaymentMode_Debit_Card')
    # PreferredPaymentMode_E_wallet = form.number_input('PreferredPaymentMode_E wallet',key = 'PreferredPaymentMode_E_wallet')
    # PreferredPaymentMode_UPI = form.number_input('PreferredPaymentMode_UPI',key = 'PreferredPaymentMode_UPI')
    # PreferedOrderCat_Grocery = form.number_input('PreferedOrderCat_Grocery',key = 'PreferedOrderCat_Grocery')
    # PreferedOrderCat_Laptop_Accessory = form.number_input('PreferedOrderCat_Laptop & Accessory',key = 'PreferedOrderCat_Laptop_Accessory')
    # PreferedOrderCat_Mobile = form.number_input('PreferedOrderCat_Mobile',key = 'PreferedOrderCat_Mobile')
    # PreferedOrderCat_Others = form.number_input('PreferedOrderCat_Others',key = 'PreferedOrderCat_Others')

    # Add a predict button to trigger predictions
    user_input = {}

    # Input fields for specific columns
    for i in columnsss:
        user_input[i] = form.number_input(f'{i}', key=f'{i}')

    # Add a predict button to trigger predictions
    submit_button = form.form_submit_button('Predict')

    if submit_button:

        user_input_json = json.dumps(user_input)

        # Make predictions
        predictions = predict_pipeline(user_input_json)
        pred = predictions

        # Display the predictions
        st.subheader('Predictions:')
        st.write(pred)

        # Display the predictions
        st.subheader('Predictions:')
        st.write(predictions)

if __name__ == '__main__':
    main()
