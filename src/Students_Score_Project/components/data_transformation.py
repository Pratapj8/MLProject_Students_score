# data_transformation.py is used to transform the data
# # like scaling, encoding, etc
# It is all about Feature engineering(Feature selection, Feature extraction, Feature scaling)
#

# we read /take the data from the artifacts folder (raw.csv , train.csv, test.csv)


# This file is linked to Model_Training.py (need to change both files)
# Saving the Best Model

import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.Students_Score_Project.utils import save_object


# Students_Score_Project
from src.Students_Score_Project.exception import CustomException
from src.Students_Score_Project.logger import logging
import os #To store pkl file (picklle file)


# Input for data transformation

@dataclass
class DataTransformationConfig: # artifacts
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl") #Saving the best model into artifacts folder
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        '''
        This fucntion is used to transform the data
        like scaling, encoding, etc
        '''
        try:
            # Define the numerical and categorical columns
            numerical_columns = ['reading_score', 'writing_score']
            categorical_columns = [
                "gender", 
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            
            # When we get new data we need to handle that data too , handlle missing values
            # Create the numerical transformer
            # Handling numerical columns
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')), # repalace outlier with median
                ('scaler', StandardScaler()) # scale the data
            ])
            
            # Create the categorical transformer
            # Handlling categorical columns
            # I have already found out what i will use for categorical columns in EDA and Feature Engineering
            # 
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')), # replace missing values with most frequent
                ('one_hot_encoder', OneHotEncoder(handle_unknown='ignore')), # one hot encoding
                ('scaler', StandardScaler(with_mean=False)) # scale the data even it is in 0 & 1
            ])

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
            
            # Combine the pipeline
            Perprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipeline', cat_pipeline, categorical_columns)
                ]
            )
            return Perprocessor
        
        
        
        
        except Exception as e:
            raise CustomException(e, sys)
        
    # This function is used to transform the data ,train and test data
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path) # reading train data
            test_df = pd.read_csv(test_path) # reading test data
            
            logging.info("Reading train and test data completed")
            
            preprocessing_obj = self.get_data_transformer_object() # get the preprocessor object
            
            target_column_name = 'math_score' # target column name, output column
            numerical_columns = ['reading_score', 'writing_score'] # numerical columns
            
            # Divide the data into input and target features
            
            # input feature train data and target feature train data
            
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1) # input feature train data
            target_feature_train_df = train_df[target_column_name] # target feature train data
    
            # input feature test data and target feature train data
            
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1) # input feature train data
            target_feature_test_df = test_df[target_column_name] # target feature train data
            
            logging.info("Applying preprocessing on training and testing dataframe")
            
            
            # We Transform the data because data may get leaked
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df) # fit the preprocessor object on input feature train data
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df) # fit the preprocessor object on input feature train data

            # Creating train and test arry
            # c_ is used to concatenate the two arrays
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)] # combine the input feature train data and target feature train data
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)] # combine the input feature train data and target feature train data
            logging.info(f"Saved Preprocessing object")
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            ) # save the preprocessor object
            
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path # path of the preprocessor object
            )
            
            
        except Exception as e:
            raise CustomException(e, sys)