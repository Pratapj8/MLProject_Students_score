# utils.py is used to get the data from the URL,Database,local folder and save it in the folder(artifacts)
# 

import os
import sys
from src.Students_Score_Project.exception import CustomException
from src.Students_Score_Project.logger import logging
import pandas as pd

import pickle # to save the model
import numpy as np # for numerical operations

from dotenv import load_dotenv # to load environment variables from .env file
import pymysql # to connect to MySQL database




load_dotenv() # Read environment variables from .env file

host =os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


def read_sql_data():
    logging.info("Reading data from SQL database started")
    try:
        mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="",  # No password set
        db="college",
        port=3306
        )
        
        
        
        logging.info(f"Connection Established: {mydb}")
        df=pd.read_sql_query("SELECT * FROM students", mydb)
        print(df.head())
        
        return df
        
        
    except Exception as ex:
        raise CustomException(ex, sys)
    
# Saving the pickle file 
def save_object(file_path, obj):
    """
    This function saves the object as a pickle file
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
            
            
    except Exception as e:
        raise CustomException(e, sys)

