# data_ingestion.py is used to get the data from the URL,Database,local folder and save it in the data folder(artifacts)
# Automatically it will create a folder name with - artifacts
# mysql ---- > Train test split ---- > dataset


import os
import sys
from src.Students_Score_Project.exception import CustomException # Students_Score_Project
from src.Students_Score_Project.logger import logging            # Students_Score_Project
import pandas as pd

# Students_Score_Project
from src.Students_Score_Project.utils import read_sql_data # reading code from mysql

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass  # artifacts
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts", "train.csv")
    test_data_path:str=os.path.join("artifacts", "test.csv")
    raw_data_path:str=os.path.join("artifacts", "raw.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            #df=read_sql_data() ##reading code from mysql database(raw data,sql) # comment once you read the data
            df=pd.read_csv(os.path.join("notebook/data", "raw.csv")) # reading the data from artifacts folder
            
            
            
            logging.info("Reading completed mysql database")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) # creating artifacts folder
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set,test_set=train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            
            logging.info("Data Ingestion is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
            
        except Exception as e:
            raise CustomException(e, sys)