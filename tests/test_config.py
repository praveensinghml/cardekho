import json
import logging
import os
import joblib
import pytest

from prediction import form_response, api_response, predict
import prediction

input_data = {
    "incorrect_range": 
    {"Year": 2010, 
    "Present_Price": 5.59, 
    "Kms_Driven": 27000, 
    "Fuel_Type": "Petrol", 
    "Seller_Type": "Dealer", 
    "Transmission": "Manual", 
    "Owner": 0, 
    }
}


def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"]
