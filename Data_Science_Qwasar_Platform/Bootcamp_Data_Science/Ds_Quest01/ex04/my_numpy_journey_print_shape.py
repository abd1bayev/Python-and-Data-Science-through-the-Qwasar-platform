import numpy as np

def my_numpy_journey_print_shape(param_1):
    a = np.array(param_1)
    b = a.shape
    print(b)

my_numpy_journey_print_shape([[1, 2, 3, 4], [0, 1, 1, 1]])