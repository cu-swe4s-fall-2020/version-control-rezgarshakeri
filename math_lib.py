import numpy as np

def div(a, b):
    if b == 0:
        print("denominator iz zero!!!")
        return np.inf
    else:
        return a/b