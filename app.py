from src.Students_Score_Project.logger import logging
from src.Students_Score_Project.exception import CustomException
from src.Students_Score_Project.components.data_ingestion import DataIngestion
from src.Students_Score_Project.components.data_ingestion import DataIngestionConfig
import sys



if __name__=="__main__":
    logging.info("Students Score Prediction Project Started")
    # from src.Students_Score_Project.pipeline import main
    
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
        
    except Exception as e: # Capture error message
        logging.info("Custom Exception")
        raise CustomException(e,sys)
