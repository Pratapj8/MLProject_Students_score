# app.py typically acts as the main script that launches your application.
# app.py initializes the web server and handles incoming HTTP requests. 
# You define routes like /predict, /home, etc. inside it.
# app.py might load your trained model, accept user input, and return predictions.
# It's useful if you're creating a simple UI (with tools like Streamlit or Flask) for your project.


from src.Students_Score_Project.logger import logging
from src.Students_Score_Project.exception import CustomException
from src.Students_Score_Project.components.data_ingestion import DataIngestion
# from src.Students_Score_Project.components.data_ingestion import DataIngestionConfig
from src.Students_Score_Project.components.data_transformation import DataTransformationConfig,DataTransformation



import sys



if __name__=="__main__": # Project entry point
    logging.info("Students Score Prediction Project Started")
    # from src.Students_Score_Project.pipeline import main
    
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path ,test_data_path = data_ingestion.initiate_data_ingestion()
        
        data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path ,test_data_path)
        
    except Exception as e: # Capture error message
        logging.info("Custom Exception")
        raise CustomException(e,sys)
