import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""
    data = np.array(data, dtype = np.float64)
    weights = np.array(weights, dtype = np.float64)
    print(np.diag(weights)) # - other way of doing this is to convert it as a diagonal and then multiply
    return weights*data
    
    pass