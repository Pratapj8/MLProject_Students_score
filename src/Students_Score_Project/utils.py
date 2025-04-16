# utils.py is used to get the data from the URL,Database,local folder and save it in the folder(artifacts)


# Remove comment if you want to import data from sql then comment it again

# Step 1

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



# Step 2
# Use this once you done importing data from sql , comment the above code

import os
import sys

import numpy as np 
import pandas as pd
#import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.Students_Score_Project.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            # Training completed
            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)