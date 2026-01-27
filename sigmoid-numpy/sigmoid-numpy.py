import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    return np.reciprocal(1 + np.exp(-np.array(x)), dtype =float)
