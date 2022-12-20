from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

def my_model_evaluation_journey_confusion_matrix(param_1, param_2):
    return confusion_matrix(param_1, param_2)

print(my_model_evaluation_journey_confusion_matrix([2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2], [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]))