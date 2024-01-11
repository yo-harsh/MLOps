import logging
from abc import ABC, abstractmethod
import pandas as pd
from typing import Union

from sklearn.model_selection import train_test_split


class DataStrategy(ABC):
    """
    Abstract class
    """

    @abstractmethod

    def handle_data(self, data:pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        """
        Define the blueprint
        """
    pass


class DataPreprocessingStrategy(DataStrategy):
    """
    Strategy for preprocessing
    """

    def replace_values(self, data:pd.DataFrame):
        try:
            data['PreferredLoginDevice'].replace(['Mobile Phone', 'Phone', 'Computer'], [0,0,1], inplace=True)
            data['PreferredPaymentMode'].replace(['Debit Card', 'UPI', 'CC', 'Cash on Delivery', 'E wallet', 'COD', 'Credit Card'], ['Debit Card', 'UPI', 'Credit Card', 'Cash on Delivery', 'E wallet', 'Cash on Delivery', 'Credit Card'], inplace=True)
            data['Gender'].replace(['Female', 'Male'], [0,1], inplace=True)
            data['PreferedOrderCat'].replace(['Laptop & Accessory', 'Mobile', 'Mobile Phone', 'Others', 'Fashion', 'Grocery'], ['Laptop & Accessory', 'Mobile', 'Mobile', 'Others', 'Fashion', 'Grocery'], inplace=True)
            data['MaritalStatus'].replace(['Single', 'Divorced', 'Married'], [1,0,2], inplace=True)
            return data
        except Exception as e:
            logging.error(f"Error while replacing values {e}")
            raise e

    def one_hot_encoding(self, data:pd.DataFrame):
        try:
            col_to_encode = ['PreferredPaymentMode', 'PreferedOrderCat']
            df_encoded = pd.get_dummies(data, col_to_encode, drop_first=True)
            return df_encoded

        except Exception as e:
            logging.error(f'Error while encoding {e}')
            raise e

    def to_numeric(self, data:pd.DataFrame):
        try:
            data = data.astype(float)
            return data

        except Exception as e:
            logging.error(f'Error while converting dtypes {e}')
            raise e

    def remove_null(self, data:pd.DataFrame):
        try:
            # Get columns with null values
            columns_with_null = data.columns[data.isnull().any()].tolist()
            print(columns_with_null)
            data.dropna(how='all', inplace=True)
            # fill null values
            for column in columns_with_null:
                data.fillna(data[column].median(), inplace=True, axis=0)
            return data

        except Exception as e:
            logging.error(f"Error while removing null data: {e}")
            raise e

    def handle_data(self, data:pd.DataFrame):
        try:
            data_obj = DataPreprocessingStrategy()
            replaced_data = data_obj.replace_values(data)
            encoded_data = data_obj.one_hot_encoding(replaced_data)
            numeric_data = data_obj.to_numeric(encoded_data)
            clean_data = data_obj.remove_null(numeric_data)
            x_train, x_test, y_train, y_test = train_test_split(clean_data.drop('Churn', axis=1), clean_data['Churn'], test_size=0.25, stratify=clean_data['Churn'], random_state=42)
            return x_train, x_test, y_train, y_test

        except Exception as e:
            logging.error(f'Error while handling data {e}')
            raise e

