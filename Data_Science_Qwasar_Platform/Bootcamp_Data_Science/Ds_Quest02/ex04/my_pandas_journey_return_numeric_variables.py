import numpy as np
import pandas as pd

def my_pandas_journey_return_numeric_variables(param_1):
    return param_1.select_dtypes(include=np.number)