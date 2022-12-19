import numpy as np


def my_numpy_journey_print_datatype(param_1):
    a = np.array(param_1)
    a = a.dtype
    print(a)

my_numpy_journey_print_datatype([[1, 2, 3, 4], [0, 1, 1, 1], [7, 7, 7, 7]])