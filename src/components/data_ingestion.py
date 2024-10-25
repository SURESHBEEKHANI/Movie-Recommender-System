import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.exception import CustomException  
from src.logger import logging  
#from src.components.model_tranier import ModelTrainer

# Configuration for data ingestion
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')

# Data Ingestion Class
class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Starting the data ingestion process.')
        try:
            # Load dataset
            df = pd.read_csv('notebooks/data/data_preprocessing.csv')
            logging.info('Dataset loaded successfully into a pandas DataFrame.')

            # Create directories for data storage if they don't exist
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)

            # Save the raw dataset
            df.to_csv(self.config.train_data_path, index=False)
            logging.info('Raw dataset saved successfully.')

            return self.config.train_data_path  # Only return train data path for now

        except Exception as e:
            logging.error('An error occurred during data ingestion.')
            raise CustomException(e, sys)

if __name__ == '__main__':
    # Perform data ingestion
    data_ingestion = DataIngestion()
    train_data_path = data_ingestion.initiate_data_ingestion()

    # Call the data transformation step
    data_transformer = DataTransformation()
    transformed_data = data_transformer.initiate_data_transformation(train_data_path)
  