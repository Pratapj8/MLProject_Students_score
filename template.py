# Creating multiple files or folder
# This script creates a directory structure and empty files for a Python project.

'''
template.py is a starter file that contains common code structure like imports, 
functions, and main() setup — so you don’t have to rewrite it every time you start a new script.
'''

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

# Project name 
project_name = "Students_Score_Project"

# List of files to be created
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Loop through each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to a Path object for better path handling
    filedir, filename = os.path.split(filepath)  # Split into directory and file name
    
    # If the directory part is not empty, create it (if it doesn't exist)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directory if needed
        logging.info(f"Creating directory: {filedir} for the file {filename}")
        
    # If file doesn't exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create an empty file
            logging.info(f"Creating empty file: {filename}")
    
    # If file already exists and is not empty, log that information
    else:
        logging.info(f"File {filename} already exists in the directory {filedir}")
    # Check if the file is empty