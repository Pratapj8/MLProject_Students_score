# utils.py is used to get the data from the URL,Database,local folder and save it in the data folder(artifacts)
# 

import os
import sys
from src.Students_Score_Project.exception import CustomException
from src.Students_Score_Project.logger import logging
import pandas as pd



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
        raise CustomeException(ex, sys)

