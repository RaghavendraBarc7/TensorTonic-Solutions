import numpy as np

def pairwise_diff(a):
    """Returns: np.ndarray of shape (n, n) where out[i,j] = a[i] - a[j]"""
    diff1 = np.array(a, dtype = np.float64)
    diff1 = diff1[:, np.newaxis]
    diff2 = np.array(a, dtype = np.float64)
    diff2 = diff2[np.newaxis, :]
    return diff1 - diff2
    pass