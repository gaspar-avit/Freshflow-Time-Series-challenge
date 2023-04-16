# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 19:44:12 2023

@author: gaspa
"""

import pickle
import xgboost as xgb
import pandas as pd
import numpy as np


def make_prediction(features):

    item = int(features['item_number'].values[0])
    xgb_model_loaded = pickle.load(
        open('./saved_models/' + str(item) + '.pkl', "rb"))

    dtest = xgb.DMatrix(features)
    prediction = xgb_model_loaded.predict(dtest)

    return int(prediction[0])


if __name__ == "__main__":

    input_data = np.array([80028349,
                  0.674927536231884,
                  1.055314009661836,
                  0,
                  0.0,
                  0.38,
                  2022,
                  1,
                  1,
                  9,
                  1,
                  9,
                  6,
                  True]).reshape(1,-1)

    input_data = pd.DataFrame(input_data, columns=['item_number',
                                                   'purchase_price',
                                                   'suggested_retail_price',
                                                   'orders_quantity',
                                                   'revenue',
                                                   'item_profit',
                                                   'year',
                                                   'month',
                                                   'week',
                                                   'day',
                                                   'quarter',
                                                   'day_of_year',
                                                   'day_of_week',
                                                   'weekend'])
    prediction = make_prediction(input_data)
    print("\nPrediction: ", prediction, "units")
