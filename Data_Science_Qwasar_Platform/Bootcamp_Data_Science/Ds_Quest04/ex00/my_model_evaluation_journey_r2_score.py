from sklearn.metrics import r2_score
import numpy as np
import pandas as pd

def my_model_evaluation_journey_r2_score(param_1, param_2):
    a = pd.read_csv(param_1)
    b = pd.read_csv(param_2)
    a = a.iloc[[0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1, 2,3,4]]
    b = b.iloc[[0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1, 2,3,4]]
    return r2_score(a, b)


a = "data_1.csv"
b = "data_2.csv"

print(my_model_evaluation_journey_r2_score(a,b))
