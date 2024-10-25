import os
import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_tranier import ModelTrainer

if __name__ == '__main__':
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    try:
        # Step 1: Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path = data_ingestion.initiate_data_ingestion()

        # Step 2: Data Transformation
        data_transformation = DataTransformation()
        transformed_data = data_transformation.initiate_data_transformation(train_data_path)

        # Step 3: Model Training
        model_trainer = ModelTrainer()
        model_trainer.train_model(transformed_data)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
