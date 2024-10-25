import os
import sys
import pandas as pd
import pickle
from dataclasses import dataclass
from sklearn.feature_extraction.text import CountVectorizer
from ..exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self, df: pd.DataFrame, column_name: str = 'tags'):
        try:
            if column_name not in df.columns:
                logging.error(f"Column '{column_name}' does not exist in the DataFrame.")
                raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
            
            # Initialize CountVectorizer
            cv = CountVectorizer(max_features=5000, stop_words='english')
            vectorized_data = cv.fit_transform(df[column_name]).toarray()

            # Save the CountVectorizer object to a pickle file
            os.makedirs(os.path.dirname(self.data_transformation_config.preprocessor_obj_file_path), exist_ok=True)
            with open(self.data_transformation_config.preprocessor_obj_file_path, 'wb') as f:
                pickle.dump(cv, f)

            logging.info(f"Data transformed successfully with CountVectorizer for column '{column_name}'.")

            # Create a DataFrame for the transformed data
            transformed_df = pd.DataFrame(vectorized_data, columns=cv.get_feature_names_out())
            transformed_df['title'] = df['title'].values  # Ensure the title is included

            return transformed_df  # Return the transformed DataFrame

        except Exception as e:
            logging.error('Exception occurred in get_data_transformation_object method')
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path: str):
        try:
            # Load the training dataset
            train_df = pd.read_csv(train_path)  # Ensure train_path is a string
            
            # Log the shape of the dataset
            logging.info(f"Training data shape: {train_df.shape}")

            # Transform the 'tags' column in the training dataset
            transformed_train_df = self.get_data_transformation_object(train_df, column_name='tags')

            # Log the columns of the transformed DataFrame
            logging.info(f"Transformed DataFrame columns: {transformed_train_df.columns.tolist()}")

            return transformed_train_df  # Return the transformed training DataFrame

        except Exception as e:
            logging.error('Exception occurred in initiate_data_transformation method')
            raise CustomException(e, sys)
