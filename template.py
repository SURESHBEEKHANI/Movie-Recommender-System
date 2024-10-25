import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Specify the project name
project_name = "Movie_Recommender_System_Content_Based_Filtering"

# List of files to create
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",  # Fixed typo: model_tranier -> model_trainer
    f"src/{project_name}/components/model_monitoring.py",  # Fixed typo: model_monitering -> model_monitoring
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create empty file if it doesn't exist or is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w'):
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists.")
