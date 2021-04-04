# Preprocessing data and feature engineering 
# save it in data/processed folder
import os
import argparse
import pandas as pd
from get_data import read_params, get_data

def preprocessing(config_path):
    config = read_params(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    preprocessed_data_path = config["preprocess"]["processed_dataset_csv"] 
    curr_year = config["preprocess"]["current_year"] 
    
 
    ### This function is used to get CSV data as dataframe 
    df = get_data(config_path)
    update_df = df[['Year', 'Selling_Price', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
    
    ### As we see that year is appearing in year format but it is not tuthfull, so it need to fit as no of years from current year.
    update_df['No_Years'] = int(curr_year) - update_df['Year']
    update_df.drop(['Year'], axis=1, inplace=True)
    update_df = pd.get_dummies(update_df, drop_first=True)
    update_df.to_csv(preprocessed_data_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    preprocessing(config_path=parsed_args.config)

